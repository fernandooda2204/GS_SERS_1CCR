from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from energia import carregar_parametros,comparar
p=carregar_parametros();a=comparar(p)
f=lambda x:f'{x:.2f}'
s=a['a2_solar'];l=a['a3_led']
t=f"""# Análise gerada — cenário SIMULADO\n\n**Cenário de consumo simulado.** Tarifa e preço de LED foram pesquisados, mas dados solares e custo do sistema continuam hipóteses. Não representa fatura ou orçamento real.\n\n- Referência: {f(a['consumo_kwh_mes'])} kWh/mês; tarifa B1 Enel SP (sem tributos e bandeiras) R$ {f(p['tarifa_energia_brl_kwh'])}/kWh.\n- A1 — Sem mudanças: R$ {f(a['a1_conta_brl'])}/mês.\n- A2 — Solar: geração {f(s['geracao_kwh_mes'])} kWh/mês; conta estimada R$ {f(s['depois_brl'])}/mês; economia R$ {f(s['economia_brl_mes'])}/mês; payback simples {f(s['payback_anos']) if s['payback_anos'] else 'não aplicável'} anos.\n- A3 — LED: economia {f(l['economia_kwh_mes'])} kWh/mês, R$ {f(l['economia_brl_mes'])}/mês, payback simples {f(l['payback_meses']) if l['payback_meses'] else 'não aplicável'} meses.\n- CO₂ evitado solar: {f(s['co2_evitado_kg_mes'])} kg/mês. CO₂ evitado LED: {f(l['co2_evitado_kg_mes'])} kg/mês.\n\n## Limitações\nNão modela integralmente tributos, bandeiras, compensação de créditos, sazonalidade, curva horária, manutenção, degradação, juros ou custo de oportunidade. A parcela Fio B é apenas uma aproximação didática; o custo de disponibilidade foi simplificado. A viabilidade depende do consumo, da distribuidora, do contrato, do município e de cotações reais.\n"""
Path(__file__).resolve().parents[1].joinpath('docs/analise_gerada.md').write_text(t,encoding='utf-8')
print(t)
