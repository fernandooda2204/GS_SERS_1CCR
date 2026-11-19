"""Cálculos de energia do Citizen Assist AI (módulo de Energias Renováveis e Sustentáveis).

Funções puras: recebem parâmetros e devolvem números/dicionários, sem entrada nem saída de texto.
As respostas em linguagem simples ficam em `respostas.py`.
"""
import json
from pathlib import Path

ARQUIVO_PARAMETROS = Path(__file__).resolve().parent / 'data' / 'parametros.json'
DIAS_MES = 30


def carregar_parametros(arquivo=ARQUIVO_PARAMETROS):
    """Lê `parametros.json` e devolve {nome: valor}."""
    dados = json.loads(Path(arquivo).read_text(encoding='utf-8'))
    return {k: v['valor'] for k, v in dados.items()}


def carregar_fontes(arquivo=ARQUIVO_PARAMETROS):
    """Lê `parametros.json` completo (valor, unidade, fonte, verificação)."""
    return json.loads(Path(arquivo).read_text(encoding='utf-8'))


def _nao_negativo(*valores):
    if min(valores) < 0:
        raise ValueError('Valores não podem ser negativos')


def consumo_kwh(potencia_w, horas_dia, dias=DIAS_MES, quantidade=1):
    """E (kWh) = P (W) × horas/dia × dias × quantidade / 1000."""
    _nao_negativo(potencia_w, horas_dia, dias, quantidade)
    return potencia_w * horas_dia * dias * quantidade / 1000


def consumo_geladeira_etiqueta(kwh_mes):
    """Geladeira: usa o kWh/mês da etiqueta (o compressor liga e desliga, então W × h superestima)."""
    _nao_negativo(kwh_mes)
    return kwh_mes


def conta_base(consumo, tarifa):
    """Custo da energia sem impostos, bandeiras e CIP (não é o valor final da fatura)."""
    _nao_negativo(consumo, tarifa)
    return consumo * tarifa


def conta_sem_mudancas(p, consumo):
    """A1 — custo mensal sem mudanças: consumo × tarifa, respeitando o custo mínimo (disponibilidade)."""
    return max(conta_base(consumo, p['tarifa_energia_brl_kwh']), p['custo_disponibilidade_brl'])


def _payback(investimento, economia_mes):
    if economia_mes <= 0:
        return None, None
    meses = investimento / economia_mes
    return meses, meses / 12


def solar(p, consumo=None):
    """A2 — Solar fotovoltaica on-grid (modelo didático mensal)."""
    c = p['consumo_referencia_kwh_mes'] if consumo is None else consumo
    _nao_negativo(c)
    tarifa = p['tarifa_energia_brl_kwh']
    geracao = p['potencia_solar_kwp'] * p['horas_sol_pleno_dia'] * DIAS_MES * p['fator_desempenho_solar']
    compensavel = min(c, geracao)
    # Energia compensada abate a tarifa, mas parte do Fio B continua sendo cobrada (Lei 14.300/2022)
    # e a conta nunca fica abaixo do custo de disponibilidade.
    abatimento = compensavel * tarifa
    fio_b = compensavel * tarifa * p['parcela_tarifa_fio_b'] * p['fracao_fio_b_cobrada']
    antes = conta_sem_mudancas(p, c)
    depois = max(p['custo_disponibilidade_brl'], conta_base(c, tarifa) - abatimento + fio_b)
    economia = max(0.0, antes - depois)
    investimento = p['potencia_solar_kwp'] * 1000 * p['custo_solar_brl_por_wp']
    meses, anos = _payback(investimento, economia)
    return dict(
        geracao_kwh_mes=geracao,
        energia_compensada_kwh_mes=compensavel,
        antes_brl=antes,
        depois_brl=depois,
        economia_brl_mes=economia,
        investimento_brl=investimento,
        payback_meses=meses,
        payback_anos=anos,
        co2_evitado_kg_mes=compensavel * p['fator_emissao_kg_co2_kwh'],
    )


def led(p, consumo=None, potencia_atual_w=None, quantidade=None, horas_dia=None):
    """A3 — Troca das lâmpadas atuais por LED com a mesma quantidade e horas de uso."""
    c = p['consumo_referencia_kwh_mes'] if consumo is None else consumo
    pot = p['potencia_antiga_w'] if potencia_atual_w is None else potencia_atual_w
    qtd = p['luminarias_qtd'] if quantidade is None else quantidade
    horas = p['horas_luz_dia'] if horas_dia is None else horas_dia
    _nao_negativo(c, pot, qtd, horas)
    antes = consumo_kwh(pot, horas, quantidade=qtd)
    depois = consumo_kwh(p['potencia_led_w'], horas, quantidade=qtd)
    # A economia não pode ser maior que o consumo total informado.
    economia_kwh = min(c, max(0.0, antes - depois))
    conta_antes = conta_sem_mudancas(p, c)
    conta_depois = conta_sem_mudancas(p, c - economia_kwh)  # nunca abaixo do custo mínimo
    economia = conta_antes - conta_depois
    investimento = qtd * p['preco_lampada_led_brl'] if economia_kwh > 0 else 0.0
    meses, anos = _payback(investimento, economia)
    return dict(
        potencia_atual_w=pot,
        lampadas_qtd=qtd,
        antes_iluminacao_kwh_mes=antes,
        depois_iluminacao_kwh_mes=depois,
        economia_kwh_mes=economia_kwh,
        antes_brl=conta_antes,
        depois_brl=conta_depois,
        economia_brl_mes=economia,
        investimento_brl=investimento,
        payback_meses=meses,
        payback_anos=anos,
        co2_evitado_kg_mes=economia_kwh * p['fator_emissao_kg_co2_kwh'],
        iluminacao_maior_que_consumo=antes > c,
    )


def comparar(p, consumo=None, **led_kwargs):
    """A1 × A2 × A3 para o mesmo consumo e o mesmo período (1 mês)."""
    c = p['consumo_referencia_kwh_mes'] if consumo is None else consumo
    return dict(
        consumo_kwh_mes=c,
        a1_conta_brl=conta_sem_mudancas(p, c),
        a2_solar=solar(p, c),
        a3_led=led(p, c, **led_kwargs),
    )
