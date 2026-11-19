# 02 — Dados e premissas

Todos os valores usados nos cálculos estão em `data/parametros.json`, cada um com unidade, **tipo** (dado público,
estimativa justificada, hipótese didática, pesquisa de preços), fonte e observação. O assistente mostra essa lista na opção 9.

## 2.1 Unidades
Potência em W; tempo em h/dia; período de 30 dias; energia em kWh/mês; tarifa em R$/kWh; investimento em R$;
retorno simples em meses (e anos, quando passa de 2 anos); emissões em kgCO₂/mês.

## 2.2 Consumo de aparelhos
`E (kWh/mês) = P (W) × horas/dia × 30 × quantidade / 1000`.
Para geladeira e freezer, usa-se o kWh/mês da etiqueta do Inmetro (PBE), porque o compressor liga e desliga.

## 2.3 Energia solar
`Geração (kWh/mês) = kWp × horas de sol pleno × 30 × fator de desempenho`.
A energia compensada é limitada ao consumo do mês. A conta com solar desconta a energia compensada, soma a parte do
Fio B que continua sendo cobrada e nunca fica abaixo do custo de disponibilidade.

## 2.4 Tarifa e custo mínimo
Tarifa Enel SP B1 convencional **sem tributos**: TUSD + TE = R$ 0,78938/kWh (vigência desde 04/07/2026).
Custo mínimo: 30 kWh × tarifa (ligação monofásica) = R$ 23,68/mês, aplicado a A1, A2 e A3.

## 2.5 Resumo das premissas

| Parâmetro | Valor | Tipo | Fonte |
|---|---|---|---|
| Tarifa | R$ 0,78938/kWh | dado público | Enel SP |
| Consumo de referência | 200 kWh/mês | estimativa justificada | EPE: consumo residencial médio de cerca de 182 kWh/mês |
| Sol pleno | 4,2 h/dia | estimativa conservadora | CRESESB SunData; 4,5–4,8 em referências para a capital |
| Desempenho do sistema | 0,78 | estimativa justificada | faixa usual de 0,75 a 0,85 |
| Sistema solar | 1,5 kWp | premissa de projeto | gera menos que o consumo de referência |
| Custo solar | R$ 2,84/Wp | dado público | Greener (jun/2025) |
| Fio B cobrado | 60% | dado público | Lei 14.300/2022, art. 27 |
| Peso do Fio B na tarifa | 25% | hipótese didática | — |
| Lâmpada atual | 15 W (fluorescente compacta) | estimativa justificada | Portaria Interministerial 1.007/2010 (fim das incandescentes) |
| Lâmpada LED | 9 W, R$ 3,63 | pesquisa de preços | `data/precos_pesquisa.csv` |
| Lâmpadas e uso | 8 lâmpadas, 5 h/dia | estimativa | residência de referência |
| Fator de emissão | 0,0461 kgCO₂/kWh | dado público | MCTI/SIRENE (2025), via inventário B3 |

Os valores marcados como estimativa podem ser trocados pelo usuário no assistente: consumo (opções 4 a 8) e
lâmpadas (opções 5 e 7).

## 2.6 Como atualizar
Alterar `valor`, `fonte` e `verificacao` em `data/parametros.json`, rodar `scripts/gerar_analise.py`,
`scripts/gerar_exemplos.py` e os testes.
