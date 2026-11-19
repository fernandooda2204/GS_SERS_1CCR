"""Respostas do Citizen Assist AI para dúvidas de energia, em linguagem simples.

Transforma os resultados de `energia.py` em orientações, sempre com fonte e limitação.
Ponto de integração com o assistente: `responder(pergunta, parametros, consumo)`.
"""
import unicodedata

from energia import carregar_fontes, comparar, consumo_kwh

AVISO = ('Atenção: são estimativas, não garantia de economia. Tarifa sem impostos, bandeira e '
         'iluminação pública; a sua fatura real é maior.')


def num(valor, casas=2):
    """Número no formato brasileiro: 1.234,56."""
    return f'{valor:,.{casas}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


def brl(valor):
    return f'R$ {num(valor)}'


def _tempo(meses):
    if meses is None:
        return 'não se paga (não há economia)'
    if meses < 1:
        return 'menos de 1 mês'
    if meses < 24:
        return f'cerca de {num(meses, 0)} meses'
    if meses > 25 * 12:
        return 'mais de 25 anos (mais que a vida útil típica dos painéis)'
    return f'cerca de {num(meses / 12, 1)} anos'


def _fontes(*chaves):
    fontes = carregar_fontes()
    linhas = ['Fontes:']
    for chave in chaves:
        linhas.append(f"  - {fontes[chave]['fonte']}")
    return '\n'.join(linhas)


def ajuda_unidades(p):
    tarifa = p['tarifa_energia_brl_kwh']
    exemplo_kwh = consumo_kwh(100, 4)
    return '\n'.join([
        'ENTENDENDO W, kWh e R$',
        '- W (watt) é a POTÊNCIA: quanto o aparelho "puxa" enquanto está ligado. Vem na etiqueta ou no manual.',
        '- kWh (quilowatt-hora) é a ENERGIA gasta: potência × tempo ligado. É o que aparece na conta de luz.',
        '- R$ é o CUSTO: kWh × tarifa.',
        '',
        f'Exemplo: TV de 100 W ligada 4 h por dia → 100 × 4 × 30 dias ÷ 1000 = {num(exemplo_kwh, 0)} kWh/mês'
        f' → {num(exemplo_kwh, 0)} × {brl(tarifa)} = {brl(exemplo_kwh * tarifa)} por mês.',
        '',
        f'A tarifa usada ({brl(tarifa)}/kWh) é da Enel SP SEM impostos, bandeira e iluminação pública.',
        'Por isso o valor total da sua fatura dividido pelos kWh dá um número maior.',
        '',
        'Geladeira: use o consumo em kWh/mês da etiqueta do Inmetro, porque o motor liga e desliga sozinho.',
    ])


def resposta_aparelhos(itens):
    if not itens:
        return 'Nenhum aparelho cadastrado. Use a opção 1.'
    total = sum(a['kwh_mes'] for a in itens)
    maiores = sorted(itens, key=lambda a: a['kwh_mes'], reverse=True)
    linhas = [f'Total dos aparelhos cadastrados: {num(total)} kWh/mês.']
    if total > 0:
        linhas.append('Os que mais pesam:')
        for a in maiores[:3]:
            linhas.append(f"  - {a['nome']}: {num(a['kwh_mes'])} kWh/mês ({num(100 * a['kwh_mes'] / total, 0)}% do total)")
        linhas.append('Dica: reduzir o tempo de uso dos primeiros da lista é o que mais diminui a conta.')
    linhas.append('Aparelhos que você não cadastrou não estão nessa soma.')
    return '\n'.join(linhas)


def resposta_conta(p, c):
    comp = comparar(p, c)
    return '\n'.join([
        f"Com {num(c, 0)} kWh/mês, o custo da energia fica em cerca de {brl(comp['a1_conta_brl'])} por mês.",
        f"Conta: {num(c, 0)} kWh × {brl(p['tarifa_energia_brl_kwh'])}/kWh (mínimo de {brl(p['custo_disponibilidade_brl'])}).",
        'Este é o custo da energia SEM impostos (ICMS, PIS/COFINS), bandeira e iluminação pública.',
        _fontes('tarifa_energia_brl_kwh'),
        AVISO,
    ])


def resposta_solar(p, c):
    s = comparar(p, c)['a2_solar']
    linhas = [
        f"ENERGIA SOLAR ({num(p['potencia_solar_kwp'], 1)} kWp)",
        f"- Geração estimada: {num(s['geracao_kwh_mes'], 0)} kWh/mês (média do ano).",
        f"- Conta hoje: {brl(s['antes_brl'])}/mês → com solar: {brl(s['depois_brl'])}/mês.",
        f"- Economia: {brl(s['economia_brl_mes'])}/mês.",
        f"- Investimento estimado: {brl(s['investimento_brl'])}. Retorno: {_tempo(s['payback_meses'])}.",
    ]
    if s['geracao_kwh_mes'] > c:
        linhas.append('- O sistema gera mais do que você consome: o excedente vira crédito e não reduz a conta deste mês.'
                      ' Um sistema menor (ou nenhum) seria mais adequado.')
    linhas += [
        '',
        'Por que a conta não zera? Você continua pagando o custo mínimo da ligação e parte do uso da rede',
        '(o "Fio B", que a Lei 14.300/2022 cobra de forma gradual: 60% em 2026).',
        '',
        'Antes de decidir: peça orçamentos, confira se o telhado recebe sol sem sombra e simule com a distribuidora.',
        _fontes('horas_sol_pleno_dia', 'custo_solar_brl_por_wp', 'fracao_fio_b_cobrada'),
        AVISO,
    ]
    return '\n'.join(linhas)


def resposta_led(p, c, **led_kwargs):
    l = comparar(p, c, **led_kwargs)['a3_led']
    if l['economia_kwh_mes'] <= 0:
        return '\n'.join([
            f"Suas lâmpadas de {num(l['potencia_atual_w'], 0)} W já gastam o mesmo ou menos que uma LED de "
            f"{num(p['potencia_led_w'], 0)} W. Não há economia em trocar.",
            AVISO,
        ])
    linhas = [
        f"TROCA POR LED ({num(l['lampadas_qtd'], 0)} lâmpadas de {num(l['potencia_atual_w'], 0)} W → {num(p['potencia_led_w'], 0)} W)",
        f"- Iluminação hoje: {num(l['antes_iluminacao_kwh_mes'], 1)} kWh/mês → com LED: {num(l['depois_iluminacao_kwh_mes'], 1)} kWh/mês.",
        f"- Economia: {num(l['economia_kwh_mes'], 1)} kWh/mês = {brl(l['economia_brl_mes'])}/mês.",
        f"- Investimento: {brl(l['investimento_brl'])}. Retorno: {_tempo(l['payback_meses'])}.",
    ]
    if l['iluminacao_maior_que_consumo']:
        linhas.append('Obs.: a iluminação informada passa do consumo total da casa. Confira os números.')
    linhas += [
        'Escolha uma LED com luminosidade (lúmens) parecida com a da lâmpada atual.',
        _fontes('potencia_antiga_w', 'preco_lampada_led_brl'),
        AVISO,
    ]
    return '\n'.join(linhas)


def resposta_ambiental(p, c, **led_kwargs):
    comp = comparar(p, c, **led_kwargs)
    s, l = comp['a2_solar'], comp['a3_led']
    return '\n'.join([
        'IMPACTO AMBIENTAL (CO₂ evitado)',
        f"- Solar: cerca de {num(s['co2_evitado_kg_mes'], 1)} kg/mês ({num(12 * s['co2_evitado_kg_mes'], 0)} kg/ano).",
        f"- LED: cerca de {num(l['co2_evitado_kg_mes'], 1)} kg/mês ({num(12 * l['co2_evitado_kg_mes'], 0)} kg/ano).",
        'A eletricidade brasileira já é majoritariamente renovável, então cada kWh economizado evita pouco CO₂.',
        'O ganho ambiental é real, mas pequeno; o principal benefício para a família é o financeiro.',
        _fontes('fator_emissao_kg_co2_kwh'),
        'Fator médio do sistema elétrico em 2025: indica ordem de grandeza, não emissão medida.',
    ])


def recomendacao(p, c, **led_kwargs):
    """Recomendação final, coerente com a comparação A1 × A2 × A3."""
    comp = comparar(p, c, **led_kwargs)
    s, l = comp['a2_solar'], comp['a3_led']
    linhas = ['RECOMENDAÇÃO']
    if l['economia_kwh_mes'] > 0:
        linhas.append(f"1. Comece pelo LED: custa {brl(l['investimento_brl'])} e se paga em {_tempo(l['payback_meses'])}.")
    else:
        linhas.append('1. Suas lâmpadas já são eficientes: a troca por LED não traz economia.')
    if s['economia_brl_mes'] <= 0 or s['geracao_kwh_mes'] > 2 * c:
        linhas.append('2. Solar não compensa com esse consumo: a conta já está perto do valor mínimo '
                      'e o sistema geraria bem mais do que você usa.')
    elif s['payback_anos'] and s['payback_anos'] <= 6:
        linhas.append(f"2. Solar pode valer a pena: economia de {brl(s['economia_brl_mes'])}/mês, retorno em "
                      f"{_tempo(s['payback_meses'])}. Exige investimento maior ({brl(s['investimento_brl'])}) e orçamento real.")
    else:
        linhas.append(f"2. Solar tem retorno longo ({_tempo(s['payback_meses'])}). Só considere com orçamento e financiamento favoráveis.")
    linhas.append('3. Em qualquer caso: confira na fatura o consumo em kWh dos últimos 12 meses antes de investir.')
    return '\n'.join(linhas)


def resposta_comparacao(p, c, **led_kwargs):
    comp = comparar(p, c, **led_kwargs)
    s, l = comp['a2_solar'], comp['a3_led']
    tabela = [
        f"COMPARAÇÃO PARA {num(c, 0)} kWh/mês (mesmo período: 1 mês)",
        f"{'':24}{'Conta/mês':>14}{'Economia/mês':>15}{'Investimento':>15}  Retorno",
        f"{'A1 Sem mudanças':24}{brl(comp['a1_conta_brl']):>14}{'-':>15}{'-':>15}  -",
        f"{'A2 Solar ' + num(p['potencia_solar_kwp'], 1) + ' kWp':24}{brl(s['depois_brl']):>14}"
        f"{brl(s['economia_brl_mes']):>15}{brl(s['investimento_brl']):>15}  {_tempo(s['payback_meses'])}",
        f"{'A3 LED':24}{brl(l['depois_brl']):>14}"
        f"{brl(l['economia_brl_mes']):>15}{brl(l['investimento_brl']):>15}  {_tempo(l['payback_meses'])}",
        f"CO₂ evitado: solar {num(s['co2_evitado_kg_mes'], 1)} kg/mês | LED {num(l['co2_evitado_kg_mes'], 1)} kg/mês",
        '',
        recomendacao(p, c, **led_kwargs),
        '',
        _fontes('tarifa_energia_brl_kwh', 'custo_solar_brl_por_wp', 'potencia_antiga_w'),
        AVISO,
    ]
    return '\n'.join(tabela)


def resposta_fontes():
    linhas = ['PREMISSAS, FONTES E LIMITAÇÕES']
    for chave, v in carregar_fontes().items():
        linhas.append(f"\n• {chave.replace('_', ' ')}: {str(v['valor']).replace('.', ',')} {v['unidade']} [{v['tipo']}]")
        linhas.append(f"  Fonte: {v['fonte']}")
        linhas.append(f"  Observação: {v['verificacao']}")
    linhas += [
        '',
        'LIMITAÇÕES GERAIS',
        '- Não inclui impostos, bandeiras, iluminação pública, juros, manutenção nem perda de eficiência dos painéis.',
        '- A geração solar varia ao longo do ano; o modelo usa a média mensal.',
        '- As regras de compensação (Lei 14.300/2022) dependem da data de instalação e da distribuidora.',
        '- Não substitui orçamento, vistoria técnica ou simulação da distribuidora.',
    ]
    return '\n'.join(linhas)


# ---------------- Integração com o assistente (perguntas em texto livre) ----------------

def _normalizar(texto):
    sem_acento = unicodedata.normalize('NFKD', texto.lower())
    return ''.join(ch for ch in sem_acento if not unicodedata.combining(ch))


INTENCOES = [
    ('ambiental', ('co2', 'carbono', 'ambiental', 'meio ambiente', 'emiss', 'poluic')),
    ('solar', ('solar', 'painel', 'placa', 'fotovolt', 'renovave')),
    ('led', ('led', 'lampada', 'iluminacao', 'luz da casa')),
    ('comparar', ('compar', 'melhor', 'vale a pena', 'economizar', 'qual escolher', 'o que fazer')),
    ('conta', ('conta', 'fatura', 'quanto pago', 'quanto vou pagar', 'tarifa', 'custo')),
    ('unidades', ('kwh', 'watt', ' w ', 'potencia', 'unidade', 'o que e')),
    ('fontes', ('fonte', 'premissa', 'limitac', 'referencia', 'de onde')),
]


def identificar_intencao(pergunta):
    texto = f' {_normalizar(pergunta)} '
    for intencao, palavras in INTENCOES:
        if any(palavra in texto for palavra in palavras):
            return intencao
    return None


def responder(pergunta, p, consumo=None):
    """Recebe a pergunta do usuário e devolve a resposta de energia (ou None se não for sobre energia)."""
    c = p['consumo_referencia_kwh_mes'] if consumo is None else consumo
    intencao = identificar_intencao(pergunta)
    if intencao is None:
        return None
    respostas = {
        'ambiental': lambda: resposta_ambiental(p, c),
        'solar': lambda: resposta_solar(p, c),
        'led': lambda: resposta_led(p, c),
        'comparar': lambda: resposta_comparacao(p, c),
        'conta': lambda: resposta_conta(p, c),
        'unidades': lambda: ajuda_unidades(p),
        'fontes': resposta_fontes,
    }
    return respostas[intencao]()
