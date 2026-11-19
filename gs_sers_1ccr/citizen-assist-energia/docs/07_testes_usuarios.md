# 07 — Testes com usuários

## Método
- **Participantes:** 5 adultos externos ao grupo (4 com familiaridade digital avançada, 1 básica), em 10/11/2026 e 12/11/2026.
- **Consentimento:** obtido antes de cada teste. Só o primeiro nome foi registrado, sem endereço, CPF ou dados da conta de luz.
- **Versão testada:** v1 do protótipo (menu de 10 opções).
- **Roteiro:** 3 perguntas de descoberta, 6 tarefas cronometradas, questionário SUS. O avaliador não indicou respostas.

### Perguntas de descoberta
1. Você costuma olhar o valor em kWh na sua conta?
2. Como identifica os aparelhos que mais consomem?
3. O que precisaria entender para decidir trocar lâmpadas ou instalar solar?

### Tarefas
- T1: localizar o menu de cadastro e adicionar um aparelho.
- T2: listar os aparelhos cadastrados.
- T3: consultar o consumo dos aparelhos.
- T4: simular uma conta com o consumo indicado.
- T5: comparar A1, A2 e A3 e explicar o que é apenas estimativa.
- T6: localizar a origem e as limitações dos dados.

### SUS (System Usability Scale)
10 afirmações em escala de 1 a 5. Itens ímpares: resposta − 1; itens pares: 5 − resposta; soma × 2,5.
Cálculo em `scripts/calcular_sus.py`.

## Resultados
- Média SUS: **70,5/100**.
- Tarefas concluídas sem ajuda: **20 de 30 (66,7%)**.
- Tarefas mais difíceis: T5 (comparação) e T6 (fontes), com 2 de 5 sem ajuda cada.

Detalhes por participante e por tarefa: `testes_usuarios/resumo_testes.md` e `testes_usuarios/resultados_testes.csv`.
Registros individuais: `testes_usuarios/registros/`.

## Ajustes realizados
Os 8 problemas observados geraram ajustes na v2 do assistente: ajuda sobre unidades, tabela de comparação com colunas
separadas, explicação de por que a solar não zera a conta, fontes em todas as respostas e recomendação em linguagem
simples. Lista completa em `testes_usuarios/registro_ajustes.md`.

## Próximo passo
Repetir T1, T4, T5 e T6 com a v2 e 2 ou 3 voluntários novos (ainda não realizado).
