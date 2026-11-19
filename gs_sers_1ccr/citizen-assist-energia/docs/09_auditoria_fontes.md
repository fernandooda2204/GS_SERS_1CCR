# 09 — Auditoria de fontes (19/11/2026)

## Conferido

| Item | Resultado | Fonte |
|---|---|---|
| Tarifa Enel SP B1 convencional | TUSD R$ 0,47242/kWh + TE R$ 0,31696/kWh = **R$ 0,78938/kWh**, sem tributos, bandeiras e CIP; vigência desde 04/07/2026 | https://www.enel.com.br/pt-saopaulo/Para_Voce/tarifa-energia-eletrica.html |
| Consumo residencial médio | Cerca de 182 kWh/mês por unidade consumidora (recorde de 181,8 kWh/mês na série da EPE) | EPE, Resenha Mensal do Mercado de Energia Elétrica: https://www.epe.gov.br/pt/publicacoes-dados-abertos/publicacoes/resenha-mensal-do-mercado-de-energia-eletrica |
| Fio B em 2026 | **60%** das componentes do art. 27 para sistemas na regra de transição | Lei 14.300/2022: https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm |
| Custo de disponibilidade | 30/50/100 kWh para mono/bi/trifásico; R$ 23,68 = 30 kWh sem tributos | https://www.gov.br/aneel/pt-br/assuntos/geracao/geracao-distribuida |
| Fim das incandescentes | Venda proibida desde 30/06/2016 (cronograma da Portaria Interministerial 1.007/2010) | Portaria Interministerial MME/MCTI/MDIC 1.007/2010 |
| Custo de sistema solar | R$ 2,84/Wp (4 kWp, jun/2025, Greener); média nacional de R$ 2,45/Wp no 1º tri/2026 (Solfácil) | Greener, Estudo Estratégico Geração Distribuída 2025; Solfácil Radar |
| Fator de emissão do SIN | 0,0461 kgCO₂/kWh (2025), fator médio | MCTI/SIRENE, via Inventário de Emissões 2025 da B3: https://www.b3.com.br/data/files/16/36/19/60/DDE3D9101BEEB2D9AC094EA8/Inventario_de_Emissoes_de_Gases_do_Efeito_Estufa_2025.pdf |
| Etiqueta de refrigeradores | kWh/mês por modelo no PBE do Inmetro | https://www.gov.br/inmetro/pt-br/assuntos/regulamentacao/avaliacao-da-conformidade/programa-brasileiro-de-etiquetagem/tabelas-de-eficiencia-energetica/refrigeradores-frigobares-combinados-combinados-frost-free |
| Preço de LED 9 W | 3 ofertas de 19/11/2026, mediana R$ 3,63 | `data/precos_pesquisa.csv` |

## Estimativas assumidas pelo grupo (com justificativa)

- **Sol pleno de 4,2 h/dia:** abaixo dos 4,5–4,8 kWh/m²·dia citados para a capital paulista, para não superestimar a geração. Para um endereço real, consultar o CRESESB SunData: https://cresesb.cepel.br/index.php?section=sundata
- **Fator de desempenho de 0,78:** dentro da faixa usual de 0,75 a 0,85.
- **Peso do Fio B na tarifa (25%):** hipótese didática. O valor exato está na resolução tarifária da ANEEL para a Enel SP.
- **8 lâmpadas, 5 h/dia:** residência de referência; o usuário informa os próprios valores.

## Fora do modelo
PIS/COFINS, ICMS, bandeiras e CIP (dependem da fatura de cada pessoa); orçamento local de instalação solar;
validação contra faturas reais.
