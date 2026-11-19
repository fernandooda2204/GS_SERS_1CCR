# 06 — Integração ao Citizen Assist AI

## 6.1 Situação atual
`run_assistente.py` é o protótipo independente e funcional de terminal. Não existe integração comprovada com um assistente central de outras disciplinas neste pacote.

## 6.2 Interface de integração
O arquivo `energia.py` expõe `carregar_parametros()`, `consumo_kwh()`, `consumo_geladeira_etiqueta()`, `solar()`, `led()` e `comparar()`, retornando valores e dicionários, sem dependências de I/O (exceto carga dos parâmetros).

## 6.3 Exemplo de chamada
```python
from energia import carregar_parametros, comparar
resposta = comparar(carregar_parametros(), consumo=180)
print(resposta['a3_led']['economia_brl_mes'])
```

## 6.4 Encaminhamento de consultas
No assistente central, classifique dúvidas sobre consumo, lâmpadas ou energia solar como intenção de energia. Obtenha o consumo do usuário e chame `comparar`; ao responder inclua a natureza hipotética das premissas, as referências e as limitações. **Não** apresente como módulo integrado antes de demonstrar isso em funcionamento no sistema principal.
