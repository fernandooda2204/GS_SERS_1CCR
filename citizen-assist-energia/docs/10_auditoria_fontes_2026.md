# Auditoria de fontes e premissas — 19/11/2026

## Confirmado com fontes

| Item | Resultado | Fonte | Situação |
|---|---|---|---|
| Tarifa Enel SP B1 convencional | TUSD R$ 0,47242/kWh + TE R$ 0,31696/kWh = **R$ 0,78938/kWh** sem tributos/bandeiras/CIP; vigência desde 04/07/2026 | https://www.enel.com.br/pt-saopaulo/Para_Voce/tarifa-energia-eletrica.html | Verificado |
| Regra Fio B em 2026 | **60%** das componentes especificadas no art. 27 para sistemas enquadrados na regra de transição; outras situações podem ser distintas | https://www2.camara.leg.br/legin/fed/lei/2022/lei-14300-6-janeiro-2022-792217-normaatualizada-pl.html | Verificado com ressalva |
| Disponibilidade | Equivalente a 30/50/100 kWh conforme monofásico/bifásico/trifásico; R$ 23,6814 é proxy de 30 kWh sem tributos | https://www.gov.br/aneel/pt-br/assuntos/geracao/geracao-distribuida | Regra verificada, aplicação real pendente |
| Emissão média do SIN | **0,0461 kgCO₂/kWh (2025)**; histórico de 2025, não garantia nem fator marginal de deslocamento | https://www.b3.com.br/data/files/16/36/19/60/DDE3D9101BEEB2D9AC094EA8/Inventario_de_Emissoes_de_Gases_do_Efeito_Estufa_2025.pdf | Conferência indireta via inventário com referência MCTI |
| Etiqueta de refrigeradores | Conferir kWh/mês por modelo e versão no PBE; novos critérios em 2026 | https://www.gov.br/inmetro/pt-br/assuntos/regulamentacao/avaliacao-da-conformidade/programa-brasileiro-de-etiquetagem/tabelas-de-eficiencia-energetica/refrigeradores-frigobares-combinados-combinados-frost-free | Procedimento verificado, modelos pendentes |
| Preços LED e geladeiras | Seis anúncios identificados, com lojas e valores registrados | `data/precos_pesquisa.csv` | Pesquisa preliminar, conferir anúncios antes de entregar |

## Ainda NÃO verificado

- SunData: nenhuma extração documental da irradiação média no plano inclinado para coordenadas da residência foi realizada; **4,2 h/dia continua premissa hipotética**. Ferramenta: https://www.cresesb.cepel.br/index.php?section=sundata
- Componente TUSD **Fio B específico** da Enel SP: 0,25 é proxy, não valor oficial homologado. Não confundir TUSD total de 0,47242 com TUSD Fio B. A simulação solar segue didática.
- PIS/COFINS, ICMS, bandeira e CIP: exigem conta real e/ou normas tributárias pertinentes ao período. **R$ 0,78938/kWh não é tarifa final cobrada.**
- Orçamento instalado de sistema solar 1,5 kWp, com instalação, projeto, inversor e condições comerciais; **R$ 8.500 não é preço verificado**.
- Consumo e valor de 3–12 contas reais por domicílio, etiquetas de todos os equipamentos e validação do erro contra faturas.
- Entrevistas, tarefas cronometradas, SUS, correções e segunda rodada com participantes.

## Transparência metodológica

O programa usa modelo didático que considera a energia gerada em cada mês como compensável até o consumo mensal. O sistema brasileiro tem regras mais complexas de injeção, autoconsumo, créditos, impostos e faturamento. A simulação e o payback **não devem ser usados para tomar decisão de investimento** sem orçamento e análise técnica. Não foram realizados testes de campo nem coletados dados privados.
