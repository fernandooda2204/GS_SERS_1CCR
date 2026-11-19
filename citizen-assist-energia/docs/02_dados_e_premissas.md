# 02 — Dados, premissas e checklist de verificação

## 2.1 Contexto e grandezas
Potência em W, tempo em horas/dia, consumo em kWh/mês, tarifa em R$/kWh, investimento em R$, retorno simples em meses ou anos e emissão em kgCO₂e.

## 2.2 Cálculo de consumo
`E(kWh/mês) = P(W) × horas/dia × dias × quantidade / 1000`. Na geladeira, prefira kWh/mês da etiqueta oficial por causa dos ciclos do compressor.

## 2.3 Solar
`G = kWp × HSP × 30 × fator_de_desempenho`. HSP real depende da localização, orientação e inclinação. Não usar geração estimada como garantida.

## 2.4 Tarifa e compensação
A estimativa de solar é uma simplificação: não representa integralmente a Lei 14.300/2022, as regras para grupos diferentes, componentes tarifários e demais tributos. O valor mínimo de faturamento e a cobrança sobre a rede podem persistir. Conferir distribuidora, enquadramento, ano e fatura.

## 2.5 Custos
Orçamentos, preços e valores da fatura variam; as cifras iniciais do JSON são **cenários fictícios**.

## 2.6 Ambiental
Emissões evitadas são estimativas dependentes do fator do sistema elétrico no período e da metodologia aplicada. Não atribuir benefício como medido.

## 2.7 Registros
Usar `data/contas_reais_anonimizadas.csv` e `data/precos_pesquisa.csv` sem nome completo, endereço, CPF ou número de instalação.

## 2.8 Atualização
Alterar os valores e a propriedade `verificacao` em `data/parametros.json`, executar os dois scripts geradores e os testes; rever textos manuais.

## 2.9 Checklist de fontes — ver detalhes e ressalvas em docs/10_auditoria_fontes_2026.md
- [ ] [CRESESB — SunData](https://cresesb.cepel.br/index.php?section=sundata): pesquisar coordenadas e média de irradiação apropriada.
- [x] [ANEEL — tarifas e resoluções](https://www.gov.br/aneel/pt-br): localizar REH 3.596/2026 e componente TUSD Fio B pertinente, se aplicável.
- [x] [Lei 14.300/2022 — Planalto](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/l14300.htm): confirmar regras conforme o caso.
- [x] [INMETRO — PBE](https://www.gov.br/inmetro/pt-br/assuntos/avaliacao-da-conformidade/programa-brasileiro-de-etiquetagem): consumo real da etiqueta do refrigerador.
- [x] [MCTI — fatores de emissão](https://www.gov.br/mcti/pt-br): fator oficial e período para a conta ambiental.
- [ ] Conta de luz do grupo: tarifa aplicada, impostos, PIS/COFINS e custo mínimo.
- [x] Cotação de LED: 3 ofertas identificadas e datadas.
- [ ] Cotação de geladeira: 3 ofertas + etiqueta e consumo mensal.
- [ ] Cotação solar: 1–2 orçamentos/simuladores com condições explícitas.

Apenas parâmetros efetivamente conferidos foram alterados. **Checklist marcado significa verificação parcial da referência**, não comprovação de todos os valores do modelo; consultar docs/10.
