# Registro de ajustes (v1 → v2)

Ajustes feitos no assistente a partir dos problemas observados nos testes (`resumo_testes.md`).

| # | Problema observado | Quem | Ajuste na v2 | Onde |
|---|---|---|---|---|
| 1 | Não entendia W e kWh | P02, P05 | Nova opção **10 Ajuda: o que são W, kWh e R$**, com exemplo calculado (TV 100 W, 4 h/dia). O cadastro agora diz onde achar a potência. | `respostas.ajuda_unidades`, `run_assistente.cadastrar` |
| 2 | Dúvida sobre o período no cadastro | P05 | O cadastro informa que o cálculo considera 30 dias e mostra exemplo de horas fracionadas ("0,5 para meia hora"). A quantidade tem padrão 1. | `run_assistente.cadastrar` |
| 3 | Confundia tarifa, consumo e total da fatura | P02, P05 | A resposta da conta mostra a conta feita (kWh × tarifa) e avisa que é o custo **sem impostos, bandeira e iluminação pública**. | `respostas.resposta_conta` |
| 4 | Não entendia o custo mínimo | P04 | O custo mínimo (disponibilidade de 30 kWh) aparece na resposta da conta e já entra no cálculo de A1, A2 e A3. | `energia.conta_sem_mudancas` |
| 5 | Misturava retorno, investimento e economia | P01, P02 | A comparação virou uma tabela com colunas separadas (Conta/mês, Economia/mês, Investimento, Retorno). O retorno sai escrito ("cerca de 5 meses") e na mesma unidade para A2 e A3. | `respostas.resposta_comparacao` |
| 6 | Não entendia por que a solar não zera a conta | P05 | Explicação em linguagem simples ("Por que a conta não zera?") sobre custo mínimo e Fio B. | `respostas.resposta_solar` |
| 7 | Não achava fontes e limitações | P02, P04, P05 | Toda resposta termina com as **fontes usadas** e o aviso de estimativa. A opção 9 virou "Fontes e limitações". | `respostas._fontes`, `respostas.AVISO` |
| 8 | Pediu comparação simples, sem termos técnicos | P02 | A comparação termina com uma **recomendação** em linguagem simples (o que fazer primeiro). | `respostas.recomendacao` |
| 9 | Precisava digitar o consumo de novo | observação do grupo | O total dos aparelhos cadastrados vira o valor sugerido nas opções 4 a 8 (Enter para aceitar). | `run_assistente.pedir_consumo` |

## Ajustes técnicos feitos junto

- Lâmpada atual de referência: a incandescente de 60 W virou fluorescente compacta de 15 W, porque as incandescentes
  estão proibidas no Brasil desde 30/06/2016 (Portaria Interministerial 1.007/2010). O usuário pode informar as próprias lâmpadas.
- Custo da solar calculado por R$/Wp de estudo de mercado (Greener), no lugar de um valor fictício.
- Nova opção **11 Fazer uma pergunta**: o usuário escreve em texto livre e o assistente identifica o assunto (conta, solar, LED, CO₂, unidades, fontes).

## Próximo passo

Repetir T1, T4, T5 e T6 com a v2 e 2 ou 3 voluntários novos, para confirmar se os ajustes resolveram os problemas.
Essa segunda rodada **ainda não foi feita**.
