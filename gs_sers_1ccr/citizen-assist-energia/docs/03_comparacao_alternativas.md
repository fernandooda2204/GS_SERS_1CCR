# 03 — Comparação das alternativas

**Mesma necessidade e mesmo período:** residência de referência com 200 kWh/mês, comparação mensal.
Os números são gerados por `scripts/gerar_analise.py` (ver `docs/analise_gerada.md`).

## Fórmulas
- **A1 — Sem mudanças:** consumo × tarifa, com mínimo de 30 kWh × tarifa.
- **A2 — Solar:** geração = kWp × sol pleno × 30 × desempenho; energia compensada = mín(consumo, geração);
  conta = máx(mínimo, consumo × tarifa − compensada × tarifa + Fio B cobrado); investimento = Wp × R$/Wp.
- **A3 — LED:** economia (kWh) = (W atual − W LED) × horas × 30 × quantidade / 1000; conta = A1 recalculada com o consumo menor.
- **Retorno simples** = investimento ÷ economia mensal (sem juros).
- **CO₂ evitado** = kWh economizado ou compensado × fator de emissão.

## Resultado (cenário de referência)

| | A1 Sem mudanças | A2 Solar 1,5 kWp | A3 LED |
|---|---:|---:|---:|
| Conta/mês | R$ 157,88 | R$ 58,96 | R$ 152,19 |
| Economia/mês | — | R$ 98,91 | R$ 5,68 |
| Investimento | — | R$ 4.260,00 | R$ 29,04 |
| Retorno simples | — | cerca de 3,6 anos | cerca de 5 meses |
| CO₂ evitado | — | 6,8 kg/mês | 0,3 kg/mês |

## Comparação qualitativa

| | Benefícios | Custos e limitações |
|---|---|---|
| A1 | referência; nenhum investimento | custo continua igual |
| A2 | maior economia em reais; fonte renovável | investimento alto; depende de telhado, sombra e insolação; não zera a conta (custo mínimo e Fio B); regras da Lei 14.300/2022 |
| A3 | investimento muito baixo; retorno rápido; sem obra | economia pequena se a casa já usa lâmpadas eficientes; nenhuma se já usa LED |

## Conclusão
A3 tem o menor risco e o retorno mais rápido, por isso é a primeira recomendação. A2 economiza muito mais por mês,
mas exige investimento cerca de 150 vezes maior e só deve ser decidida com orçamento real. O grupo usa como critério
um retorno de até 6 anos para dizer que a solar "pode valer a pena", bem abaixo da vida útil típica dos painéis (25 anos).
Com consumo baixo (perto do mínimo de 30 kWh), a solar não compensa.
