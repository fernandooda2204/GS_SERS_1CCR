# 03 — Comparação das alternativas

**Mesmo cenário e período:** residência simulada com 200 kWh/mês; avaliações mensais. Os números específicos são gerados em `docs/analise_gerada.md` e **não representam uma residência real**.

| Alternativa | Benefício esperado | Custos e limitações |
|---|---|---|
| A1 — Manter a situação | referência para comparação | consumo e tarifa atuais |
| A2 — Solar fotovoltaica | possível abatimento da fatura e geração renovável | investimento alto, dependência de insolação, cobrança residual, regras de compensação, telhado e manutenção |
| A3 — LED | redução de potência para iluminação de uso equivalente | investimento por lâmpada; economia depende do uso; não reduzir a qualidade da iluminação |

Usar o payback **simples** somente como comparação preliminar. No cenário inicial A3 pode retornar antes de A2 pelo investimento proporcionalmente menor. Isso depende de uso, potência existente, orçamento e tarifa; não é regra universal.

## Fórmulas
A1 = consumo × tarifa. A2 = geração estimada (kWp × HSP × 30 × desempenho); energia compensada até consumo; estimativa financeira aproximada com parcela tarifária residual. A3 = (potência antiga – LED) × horas × 30 × quantidade / 1000. Retorno simples = investimento / economia por período.
