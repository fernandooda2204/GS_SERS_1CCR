# 06 — Integração ao Citizen Assist AI

O módulo de energia é a contribuição de Soluções em Energias Renováveis e Sustentáveis ao Citizen Assist AI.
Ele tem três camadas:

| Camada | Arquivo | Função |
|---|---|---|
| Cálculo | `energia.py` | Fórmulas de consumo, A1, A2 e A3. Funções puras, sem entrada ou saída de texto. |
| Respostas | `respostas.py` | Transforma os resultados em orientações em linguagem simples, com recomendação, fontes e limitações. |
| Interface | `run_assistente.py` | Menu de terminal e perguntas em texto livre (opção 11). |

## Como a análise vira resposta
A opção 5 e as perguntas do tipo "o que vale mais a pena?" chamam `comparar()`, que calcula A1, A2 e A3.
`recomendacao()` decide o texto a partir desses números. A recomendação mostrada ao usuário é, portanto, sempre a
mesma da análise em `docs/analise_gerada.md` para o mesmo consumo.

## Ponto de integração
Qualquer interface do assistente (terminal, chat ou web) pode usar a mesma função:

```python
from energia import carregar_parametros
from respostas import responder

p = carregar_parametros()
print(responder('vale a pena colocar placa solar?', p, consumo=180))
```

`responder()` identifica o assunto da pergunta (conta, solar, LED, CO₂, unidades, fontes) e devolve o texto da
resposta. Se a pergunta não for sobre energia, devolve `None`, para que o assistente encaminhe a outro módulo.
