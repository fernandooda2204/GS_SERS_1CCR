# Resultados dos testes com usuários

Testes presenciais realizados em 10/11/2026 e 12/11/2026 com 5 pessoas externas ao grupo, com consentimento.
Versão testada: **v1** do protótipo (menu de 10 opções). Registros individuais em `registros/`.
Só o primeiro nome dos participantes foi registrado.

## Resultados por participante

| Participante | Familiaridade digital | Tarefas sem ajuda (de 6) | Tempo total | SUS |
|---|---|---:|---:|---:|
| P01 Gustavo | avançada | 5/6 | 222 s | 75,0 |
| P02 Ariane | básica | 3/6 | 445 s | 57,5 |
| P03 Thalles | avançada | 6/6 | 134 s | 97,5 |
| P04 Felipe | avançada | 5/6 | 263 s | 72,5 |
| P05 Rogerio | avançada | 1/6 | 529 s | 50,0 |

- **Média SUS:** 70,5/100.
- **Tarefas concluídas sem ajuda:** 20 de 30 (66,7%).
- **Soma dos tempos:** 1.593 s.

## Resultados por tarefa

| Tarefa | Sem ajuda | Dificuldade observada |
|---|---:|---|
| T1 Cadastrar aparelho | 4/5 | P02 hesitou sobre potência em W; P05 precisou de orientação sobre o período (dias/mês). |
| T2 Listar aparelhos | 5/5 | — |
| T3 Consultar consumo | 3/5 | P02 e P05 não entenderam kWh sem explicação. |
| T4 Simular conta | 4/5 | P02 confundiu tarifa e total; P05 confundiu consumo (kWh) com gasto (R$); P04 pediu explicação sobre custo mínimo. |
| T5 Comparar A1/A2/A3 | 2/5 | P01 e P02 confundiram retorno, investimento e economia mensal; P05 não soube explicar por que a solar não zera a conta. |
| T6 Achar fontes e limitações | 2/5 | P02, P04 e P05 não encontraram as fontes ou ressalvas rapidamente. |

## Principais problemas

1. A diferença entre W, kWh e R$ não estava clara (P02, P05).
2. A tarifa sem impostos era confundida com o valor da fatura (P02, P05).
3. Na comparação, retorno, investimento e economia mensal se misturavam (P01, P02).
4. Custo mínimo e Fio B na energia solar precisavam de explicação mais simples (P04, P05).
5. As fontes e limitações ficavam só no fim do menu e eram difíceis de achar (P02, P04, P05).

Na entrevista inicial, 4 de 5 participantes disseram acompanhar só o valor em reais da conta, e P02 pediu
"uma comparação simples, sem termos técnicos".

Os ajustes feitos a partir desses problemas estão em `registro_ajustes.md`.
