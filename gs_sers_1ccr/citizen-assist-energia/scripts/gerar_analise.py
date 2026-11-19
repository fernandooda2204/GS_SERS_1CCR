"""Gera docs/analise_gerada.md a partir de data/parametros.json (cenário de referência)."""
from pathlib import Path
import sys

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

from energia import carregar_parametros, comparar  # noqa: E402
from respostas import brl, num, recomendacao, _tempo  # noqa: E402

p = carregar_parametros()
a = comparar(p)
s, l = a['a2_solar'], a['a3_led']
c = a['consumo_kwh_mes']

texto = f"""# Análise gerada — cenário de referência

Gerado por `scripts/gerar_analise.py` a partir de `data/parametros.json`. Residência de referência em São Paulo
(Enel SP, ligação monofásica) com consumo de {num(c, 0)} kWh/mês. Período comum de comparação: **1 mês**.

## Premissas principais
- Tarifa Enel SP B1 sem tributos: {brl(p['tarifa_energia_brl_kwh'])}/kWh (dado público).
- Consumo: {num(c, 0)} kWh/mês (estimativa próxima da média residencial da EPE).
- Solar: {num(p['potencia_solar_kwp'], 1)} kWp × {num(p['horas_sol_pleno_dia'], 1)} h de sol pleno × 30 dias × {num(p['fator_desempenho_solar'])} de desempenho; custo de {brl(p['custo_solar_brl_por_wp'])}/Wp (Greener).
- Iluminação atual: {num(p['luminarias_qtd'], 0)} lâmpadas fluorescentes compactas de {num(p['potencia_antiga_w'], 0)} W, {num(p['horas_luz_dia'], 0)} h/dia → LED de {num(p['potencia_led_w'], 0)} W a {brl(p['preco_lampada_led_brl'])}.

## Resultados

| Alternativa | Custo da energia/mês | Economia/mês | Investimento | Retorno simples | CO₂ evitado |
|---|---:|---:|---:|---|---:|
| A1 — Sem mudanças | {brl(a['a1_conta_brl'])} | — | — | — | — |
| A2 — Solar {num(p['potencia_solar_kwp'], 1)} kWp | {brl(s['depois_brl'])} | {brl(s['economia_brl_mes'])} | {brl(s['investimento_brl'])} | {_tempo(s['payback_meses'])} | {num(s['co2_evitado_kg_mes'], 1)} kg/mês |
| A3 — LED | {brl(l['depois_brl'])} | {brl(l['economia_brl_mes'])} | {brl(l['investimento_brl'])} | {_tempo(l['payback_meses'])} | {num(l['co2_evitado_kg_mes'], 1)} kg/mês |

Geração solar estimada: {num(s['geracao_kwh_mes'], 1)} kWh/mês, toda compensada (é menor que o consumo).
Economia da LED: {num(l['economia_kwh_mes'], 1)} kWh/mês.

## Recomendação (a mesma que o assistente mostra na opção 5)

```
{recomendacao(p, c)}
```

## Limitações
Não modela tributos, bandeiras, CIP, sazonalidade, curva horária, manutenção, degradação dos painéis, juros ou
custo de oportunidade. A parcela Fio B é uma aproximação didática. O custo por Wp é média de mercado e pode
subestimar sistemas pequenos. A viabilidade real depende da distribuidora, do telhado, do enquadramento na
Lei 14.300/2022 e de orçamentos locais.
"""

RAIZ.joinpath('docs/analise_gerada.md').write_text(texto, encoding='utf-8')
print(texto)
