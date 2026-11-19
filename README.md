# Citizen Assist AI — Módulo de Energia e Sustentabilidade

**Global Solution 2026.2 — Ciência da Computação, turmas 1CC**
**Disciplina:** Soluções em Energias Renováveis e Sustentáveis

## Integrantes
| Nome completo | RM |
|---|---|
| Fernando Hideki Rosa Oda | 571408 |
| Léo Moreno Sambo | 569556 |


## Público e problema
**Público:** moradores que querem entender e reduzir o custo da energia em casa (referência: São Paulo, Enel SP).

**Problema:** a maioria das pessoas só olha o valor em reais da conta e não sabe quanto cada aparelho gasta nem se vale
a pena trocar lâmpadas ou instalar energia solar. Nos testes, 4 de 5 participantes disseram acompanhar só o valor total.

## Contribuição da disciplina ao Citizen Assist AI
O módulo de energia (pasta `citizen-assist-energia/`) permite ao usuário:
- cadastrar aparelhos e ver quanto cada um gasta em kWh/mês e quais pesam mais;
- estimar o custo da energia a partir do consumo;
- comparar, para o mesmo consumo e o mesmo mês, **A1 sem mudanças**, **A2 energia solar fotovoltaica** (renovável) e
  **A3 troca de lâmpadas por LED**, com custo, economia, investimento, retorno e CO₂ evitado;
- receber uma **recomendação** em linguagem simples, coerente com o cálculo;
- fazer perguntas em texto livre ("vale a pena colocar placa solar?");
- consultar as fontes e limitações de cada número.

### Resultado do cenário de referência (200 kWh/mês)
| | Conta/mês | Economia/mês | Investimento | Retorno simples |
|---|---:|---:|---:|---|
| A1 Sem mudanças | R$ 157,88 | — | — | — |
| A2 Solar 1,5 kWp | R$ 58,96 | R$ 98,91 | R$ 4.260,00 | cerca de 3,6 anos |
| A3 LED (8 lâmpadas de 15 W → 9 W) | R$ 152,19 | R$ 5,68 | R$ 29,04 | cerca de 5 meses |

**Recomendação:** começar pela LED (baixo custo, retorno rápido) e avaliar a solar com orçamento real.
Valores estimados com tarifa sem impostos; não são garantia de economia.

## Como executar
Requer Python 3.10 ou mais recente. Não precisa instalar nada.

```bash
cd citizen-assist-energia
python run_assistente.py                   # assistente (menu de 0 a 11)
python -m unittest discover -s tests -v    # testes automatizados
python scripts/gerar_analise.py            # regenera docs/analise_gerada.md
python scripts/gerar_exemplos.py           # regenera data/exemplos_gerados.json
python scripts/calcular_sus.py 4 2 4 2 4 2 4 2 4 2   # calcula um escore SUS
```

Os aparelhos cadastrados ficam em `data/aparelhos_local.json` (ignorado pelo Git).

## Organização
| Pasta / arquivo | Conteúdo |
|---|---|
| `energia.py` | Cálculos (consumo, A1, A2, A3) |
| `respostas.py` | Respostas e recomendações em linguagem simples; `responder()` é o ponto de integração |
| `run_assistente.py` | Interface de terminal |
| `data/parametros.json` | Todos os valores usados, com unidade, tipo, fonte e verificação |
| `data/precos_pesquisa.csv`, `data/precificacao_resumo.md` | Pesquisa de preços |
| `docs/01` a `docs/09` | Contexto, dados e premissas, comparação, viabilidade e impactos, recomendações, integração, testes, roteiro do vídeo, auditoria de fontes |
| `docs/analise_gerada.md` | Cálculo do cenário de referência |
| `testes_usuarios/` | Resultados, registros individuais e ajustes feitos |
| `tests/` | Testes automatizados |

## Modelo de cálculo
- Consumo: `kWh/mês = W × horas/dia × 30 × quantidade / 1000`; para geladeira, kWh/mês da etiqueta do Inmetro.
- Solar: `geração = kWp × horas de sol pleno × 30 × desempenho`. A compensação é limitada ao consumo; parte do Fio B
  continua sendo cobrada (Lei 14.300/2022) e a conta nunca fica abaixo do custo de disponibilidade.
- LED: diferença de potência × horas × 30 × quantidade.
- Retorno simples = investimento ÷ economia mensal (sem juros).
- CO₂ evitado = kWh economizado × fator médio do SIN de 2025 (MCTI).

Detalhes em `docs/02_dados_e_premissas.md` e `docs/03_comparacao_alternativas.md`.

## Principais referências
- Enel SP — tarifas residenciais (B1)
- EPE — Resenha Mensal do Mercado de Energia Elétrica
- Lei 14.300/2022 — Marco Legal da Geração Distribuída
- ANEEL — Geração distribuída e custo de disponibilidade
- CRESESB — SunData (irradiação solar)
- Greener — Estudo Estratégico Geração Distribuída 2025
- Portaria Interministerial 1.007/2010 — fim das lâmpadas incandescentes
- MCTI/SIRENE — fatores de emissão do SIN
- Inmetro — Programa Brasileiro de Etiquetagem

Links e observações de cada uma em `docs/09_auditoria_fontes.md`.

## Limitações
Tarifa sem tributos, bandeiras e iluminação pública; sem juros, manutenção e degradação dos painéis; geração solar
pela média anual; o custo por Wp é média de mercado. A análise não substitui orçamento, vistoria técnica ou simulação
da distribuidora.

## Testes com usuários
5 participantes externos ao grupo (10 e 12/11/2026), 6 tarefas e questionário SUS. Média SUS de **70,5**;
20 de 30 tarefas concluídas sem ajuda. As dificuldades com unidades, tarifa × fatura, leitura da comparação e
localização das fontes geraram os ajustes da v2, registrados em `testes_usuarios/registro_ajustes.md`.
