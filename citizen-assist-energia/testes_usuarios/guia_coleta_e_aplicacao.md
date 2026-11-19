# Coleta real e aplicação de testes — pronto para executar

**Não há participantes entrevistados ou contas particulares acessíveis neste projeto. Todos os resultados observacionais continuam não coletados.**

## Consumo de 3 a 12 meses
1. Cada voluntário adulto que autorizar o uso da fatura identifica localmente os 3 a 12 meses, kWh e total pago. Não copiar nome, endereço, CPF, código de instalação ou código de barras.
2. Atribuir identificador aleatório D01, D02 etc.; preencher `data/contas_reais_anonimizadas.csv`. Não publicar foto integral de conta.
3. Registrar aparelhos, potências, horas e, no caso de geladeira, kWh/mês da etiqueta em `data/modelo_aparelhos_reais.csv`.
4. Calcular `erro_% = abs(kWh_estimado - kWh_fatura) / kWh_fatura * 100`, se kWh_fatura > 0; preencher `data/resumo_validacao.csv`. A estimativa não inclui todos os aparelhos e pode diferir bastante.
5. Da fatura real, calcular tarifa efetiva = valor total/kWh somente como indicador de desembolso, avisando que inclui CIP, tributos e outras parcelas; não é a tarifa homologada.

## Teste moderado com usuários adultos (5–8 pessoas)
1. Obter consentimento e registrar apenas P01–P08 (não vincular IDs a contas).
2. Perguntar as três questões de descoberta em `docs/07_testes_usuarios.md`.
3. Deixar a pessoa executar T1–T6 sem indicar caminho; cronometrar cada tarefa, registrar sem ajuda/com ajuda/não concluiu e comentário literal anonimizável.
4. Aplicar o SUS conforme questionário autorizado, 10 respostas de 1 a 5. Usar o script `scripts/calcular_sus.py` para escore.
5. Consolidar problemas em `testes_usuarios/registro_ajustes.md`; implementar correções e fazer nova rodada com 2–3 outras pessoas.
6. Relatar N total, taxa de conclusão independente e média SUS **somente depois de obter os dados**. Não preencher números fictícios.

## Segurança de dados
Não pedir fatura integral, números de instalação, nomes completos, telefones ou endereços; excluir identificadores acidentalmente coletados. Os resultados não são representativos estatisticamente da população.
