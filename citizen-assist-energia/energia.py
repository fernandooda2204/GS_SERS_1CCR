"""Cálculos didáticos para o Citizen Assist AI; cenários sujeitos à validação."""
import json
from pathlib import Path
P=Path(__file__).resolve().parent/'data'/'parametros.json'
def carregar_parametros(arquivo=P):
    return {k: v['valor'] for k,v in json.loads(Path(arquivo).read_text(encoding='utf-8')).items()}
def consumo_kwh(potencia_w, horas_dia, dias=30, quantidade=1):
    if min(potencia_w,horas_dia,dias,quantidade)<0: raise ValueError('Valores não podem ser negativos')
    return potencia_w*horas_dia*dias*quantidade/1000
def consumo_geladeira_etiqueta(kwh_mes):
    if kwh_mes<0: raise ValueError('Valor inválido')
    return kwh_mes # ciclos do compressor tornam potência instantânea inadequada

def conta_base(consumo,tarifa):
    if consumo<0 or tarifa<0: raise ValueError('Valor inválido')
    return consumo*tarifa

def solar(p,consumo=None):
    c=p['consumo_referencia_kwh_mes'] if consumo is None else consumo
    if c<0: raise ValueError('Valor inválido')
    geracao=p['potencia_solar_kwp']*p['horas_sol_pleno_dia']*30*p['fator_desempenho_solar']
    compensavel=min(c,geracao)
    # Proxy ilustrativa: limita a economia pelo consumo, incorpora parcela Fio B e piso de custo.
    abatimento_bruto=compensavel*p['tarifa_energia_brl_kwh']
    fio_b=compensavel*p['tarifa_energia_brl_kwh']*p['parcela_tarifa_fio_b']*p['fracao_fio_b_cobrada']
    anterior=conta_base(c,p['tarifa_energia_brl_kwh'])
    posterior=max(p['custo_disponibilidade_brl'], anterior-abatimento_bruto+fio_b)
    poupanca=max(0,anterior-posterior)
    retorno=p['custo_sistema_solar_brl']/poupanca/12 if poupanca>0 else None
    return dict(geracao_kwh_mes=geracao,energia_compensada_kwh_mes=compensavel,antes_brl=anterior,depois_brl=posterior,economia_brl_mes=poupanca,investimento_brl=p['custo_sistema_solar_brl'],payback_anos=retorno,co2_evitado_kg_mes=compensavel*p['fator_emissao_kg_co2_kwh'])
def led(p,consumo=None):
    c=p['consumo_referencia_kwh_mes'] if consumo is None else consumo
    antigo=consumo_kwh(p['potencia_antiga_w'],p['horas_luz_dia'],quantidade=p['luminarias_qtd'])
    novo=consumo_kwh(p['potencia_led_w'],p['horas_luz_dia'],quantidade=p['luminarias_qtd'])
    poupanca_kwh=min(c,max(0,antigo-novo))
    poupanca=poupanca_kwh*p['tarifa_energia_brl_kwh']
    inv=p['luminarias_qtd']*p['preco_lampada_led_brl']
    return dict(antes_iluminacao_kwh_mes=antigo,depois_iluminacao_kwh_mes=novo,economia_kwh_mes=poupanca_kwh,economia_brl_mes=poupanca,investimento_brl=inv,payback_meses=inv/poupanca if poupanca>0 else None,co2_evitado_kg_mes=poupanca_kwh*p['fator_emissao_kg_co2_kwh'])
def comparar(p,consumo=None):
    c=p['consumo_referencia_kwh_mes'] if consumo is None else consumo
    return dict(consumo_kwh_mes=c,a1_conta_brl=conta_base(c,p['tarifa_energia_brl_kwh']),a2_solar=solar(p,c),a3_led=led(p,c))
