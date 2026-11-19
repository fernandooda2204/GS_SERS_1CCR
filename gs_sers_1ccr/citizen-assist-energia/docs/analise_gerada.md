# Análise gerada — cenário de referência

Gerado por `scripts/gerar_analise.py` a partir de `data/parametros.json`. Residência de referência em São Paulo
(Enel SP, ligação monofásica) com consumo de 200 kWh/mês. Período comum de comparação: **1 mês**.

## Premissas principais
- Tarifa Enel SP B1 sem tributos: R$ 0,79/kWh (dado público).
- Consumo: 200 kWh/mês (estimativa próxima da média residencial da EPE).
- Solar: 1,5 kWp × 4,2 h de sol pleno × 30 dias × 0,78 de desempenho; custo de R$ 2,84/Wp (Greener).
- Iluminação atual: 8 lâmpadas fluorescentes compactas de 15 W, 5 h/dia → LED de 9 W a R$ 3,63.

## Resultados

| Alternativa | Custo da energia/mês | Economia/mês | Investimento | Retorno simples | CO₂ evitado |
|---|---:|---:|---:|---|---:|
| A1 — Sem mudanças | R$ 157,88 | — | — | — | — |
| A2 — Solar 1,5 kWp | R$ 58,96 | R$ 98,91 | R$ 4.260,00 | cerca de 3,6 anos | 6,8 kg/mês |
| A3 — LED | R$ 152,19 | R$ 5,68 | R$ 29,04 | cerca de 5 meses | 0,3 kg/mês |

Geração solar estimada: 147,4 kWh/mês, toda compensada (é menor que o consumo).
Economia da LED: 7,2 kWh/mês.

## Recomendação (a mesma que o assistente mostra na opção 5)

```
RECOMENDAÇÃO
1. Comece pelo LED: custa R$ 29,04 e se paga em cerca de 5 meses.
2. Solar pode valer a pena: economia de R$ 98,91/mês, retorno em cerca de 3,6 anos. Exige investimento maior (R$ 4.260,00) e orçamento real.
3. Em qualquer caso: confira na fatura o consumo em kWh dos últimos 12 meses antes de investir.
```

## Limitações
Não modela tributos, bandeiras, CIP, sazonalidade, curva horária, manutenção, degradação dos painéis, juros ou
custo de oportunidade. A parcela Fio B é uma aproximação didática. O custo por Wp é média de mercado e pode
subestimar sistemas pequenos. A viabilidade real depende da distribuidora, do telhado, do enquadramento na
Lei 14.300/2022 e de orçamentos locais.
