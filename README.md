# Citizen Assist AI — Módulo de Energia e Sustentabilidade

**Status: protótipo funcional / pesquisa documental parcialmente concluída em 19/11/2026 / testes com pessoas pendentes.**

## Contribuição da disciplina
Soluções em Energias Renováveis e Sustentáveis — Global Solution 2026.2, turmas 1CC. O módulo fornece estimativas de consumo residencial, compara a situação atual (A1), energia solar (A2) e troca de lâmpadas por LED (A3), além de comunicar impactos ambientais, fontes e limitações.

## Público e necessidade
Público proposto: moradores que desejam compreender o consumo da própria residência, economizar energia e avaliar opções sustentáveis. Necessidade: transformar potência e hábitos de uso em estimativas explicadas, sem prometer economias garantidas.

## Executar
Requer Python 3.10+; não precisa instalar dependências externas.

```bash
python run_assistente.py
python scripts/gerar_analise.py
python scripts/gerar_exemplos.py
python -m unittest discover -s tests -v
```

O menu oferece dez opções numeradas (incluindo Sair). Aparelhos cadastrados ficam em `data/aparelhos_local.json` (arquivo ignorado pelo Git). A geladeira aceita o kWh/mês de etiqueta; demais aparelhos usam potência e tempo de uso. Não há integração com IA online: este é um módulo determinístico de terminal; a ligação a um assistente central depende de sua interface.

## Modelo e resultados
- Fórmula de uso: `kWh = W × horas/dia × dias × quantidade / 1000`.
- Solar: produção mensal estimada via kWp × horas de sol pleno × 30 × desempenho. Compensação limitada ao consumo do mês.
- Custo pós-solar: aproximação de cobrança residual e piso tarifário; **não é uma simulação regulatória ou fatura oficial**.
- LED: diferença de consumo e economia com tarifa Enel SP B1 sem tributos.
- Impacto: kWh economizado/compensado × fator médio histórico do SIN 2025 (validar a aplicação metodológica).
- Investimento e retorno: payback simples, sem juros nem manutenção.

Confira `docs/analise_gerada.md` e `docs/03_comparacao_alternativas.md`.

## Dados, referências e limitações
Em `data/parametros.json`, alguns valores possuem fontes verificadas e outros seguem hipóteses. Veja `docs/10_auditoria_fontes_2026.md` e não confunda tarifa sem impostos com o valor da fatura. Fontes e checklist: `docs/02_dados_e_premissas.md`. A pesquisa preliminar de 6 preços consta em CSV; os CSVs de contas, aparelhos e validação contêm somente cabeçalhos porque não houve medições reais. A análise não substitui orçamento ou estudo técnico.

## Testes com usuários
**Nenhum teste real com usuários foi realizado.** Foram incluídos cinco **cenários fictícios de demonstração** (Gustavo, Ariane, Thalles, Felipe e Rogerio), com tempos, tarefas e pontuações SUS inventados apenas para mostrar como documentar resultados. Eles não contam como evidência acadêmica. Consulte `testes_usuarios/resumo_demonstracao.md` e `testes_usuarios/resultados_simulados.csv`. Para resultados válidos, aplicar os formulários em sessões reais, obter consentimento e anonimizar os registros.

## Equipe e entrega — preencher
- Integrante / RM: **[PENDENTE]**
- Repositório GitHub: **[PENDENTE]**
- Vídeo técnico no YouTube (não listado, até 3 minutos): **[PENDENTE]**
- Data e resultados dos testes: **[PENDENTE]**

O Portal recebe apenas `entrega_modelo.txt`, preenchido, após a publicação e verificação dos links.
