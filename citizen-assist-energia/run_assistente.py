"""Citizen Assist AI — Módulo de Energia (interface de terminal).

Menu numerado + pergunta em texto livre. Aparelhos cadastrados ficam em data/aparelhos_local.json.
"""
import json
from pathlib import Path

from energia import carregar_parametros, consumo_geladeira_etiqueta, consumo_kwh
import respostas as r

APARELHOS = Path(__file__).resolve().parent / 'data' / 'aparelhos_local.json'

MENU = """
================ Citizen Assist AI | Energia ================
 1 Cadastrar aparelho         7 Troca por LED
 2 Listar aparelhos           8 Impacto ambiental (CO₂)
 3 Consumo dos aparelhos      9 Fontes e limitações
 4 Quanto vou pagar?         10 Ajuda: o que são W, kWh e R$
 5 Comparar alternativas     11 Fazer uma pergunta
 6 Energia solar              0 Sair
============================================================="""


def ler_numero(msg, minimo=0, padrao=None):
    """Lê um número (aceita vírgula). Enter vazio usa o valor padrão, se houver."""
    while True:
        texto = input(msg).strip().replace(',', '.')
        if texto == '' and padrao is not None:
            return padrao
        try:
            n = float(texto)
            if n < minimo:
                raise ValueError
            return n
        except ValueError:
            print(f'Digite um número maior ou igual a {r.num(minimo, 0)} (ex.: 100 ou 4,5).')


def aparelhos():
    try:
        return json.loads(APARELHOS.read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return []


def salvar(itens):
    APARELHOS.write_text(json.dumps(itens, ensure_ascii=False, indent=2), encoding='utf-8')


def pedir_consumo(p):
    """Usa o total dos aparelhos cadastrados como sugestão; o usuário pode digitar o kWh da fatura."""
    total = sum(a['kwh_mes'] for a in aparelhos())
    padrao = total if total > 0 else p['consumo_referencia_kwh_mes']
    origem = 'total dos seus aparelhos' if total > 0 else 'consumo médio de referência'
    print('Dica: o consumo em kWh está na sua conta de luz, perto do gráfico dos últimos meses.')
    return ler_numero(f'Consumo mensal em kWh [Enter = {r.num(padrao)} kWh, {origem}]: ', padrao=padrao)


def pedir_lampadas(p):
    print('Informe as lâmpadas que você usa hoje (Enter = valor de referência).')
    return dict(
        potencia_atual_w=ler_numero(f"  Potência de cada lâmpada (W) [{r.num(p['potencia_antiga_w'], 0)}]: ", padrao=p['potencia_antiga_w']),
        quantidade=ler_numero(f"  Quantas lâmpadas [{r.num(p['luminarias_qtd'], 0)}]: ", padrao=p['luminarias_qtd']),
        horas_dia=ler_numero(f"  Horas acesas por dia [{r.num(p['horas_luz_dia'], 0)}]: ", padrao=p['horas_luz_dia']),
    )


def cadastrar():
    nome = input('Nome do aparelho (ex.: TV, chuveiro, geladeira): ').strip() or 'Aparelho'
    if 'geladeira' in nome.lower() or 'freezer' in nome.lower():
        print('Para geladeira, use o consumo em kWh/mês da etiqueta amarela do Inmetro.')
        c = consumo_geladeira_etiqueta(ler_numero('Consumo da etiqueta (kWh/mês): '))
    else:
        print('A potência (W) fica na etiqueta, no manual ou embaixo do aparelho.')
        potencia = ler_numero('Potência (W): ')
        horas = ler_numero('Horas de uso por dia (ex.: 0,5 para meia hora): ')
        qtd = ler_numero('Quantidade de aparelhos iguais [1]: ', 1, padrao=1)
        c = consumo_kwh(potencia, horas, quantidade=qtd)
    itens = aparelhos()
    itens.append({'nome': nome, 'kwh_mes': round(c, 3)})
    salvar(itens)
    print(f'Adicionado: {nome} gasta cerca de {r.num(c)} kWh/mês (considerando 30 dias).')


def main():
    p = carregar_parametros()
    print('\nOlá! Eu ajudo você a entender o consumo de energia da sua casa e a comparar formas de economizar.')
    while True:
        print(MENU)
        op = input('Escolha uma opção (0-11): ').strip()
        print()
        if op == '1':
            cadastrar()
        elif op == '2':
            itens = aparelhos()
            for a in itens:
                print(f"- {a['nome']}: {r.num(a['kwh_mes'])} kWh/mês")
            if not itens:
                print('Nenhum aparelho cadastrado. Use a opção 1.')
        elif op == '3':
            print(r.resposta_aparelhos(aparelhos()))
        elif op == '4':
            print(r.resposta_conta(p, pedir_consumo(p)))
        elif op == '5':
            c = pedir_consumo(p)
            print(r.resposta_comparacao(p, c, **pedir_lampadas(p)))
        elif op == '6':
            print(r.resposta_solar(p, pedir_consumo(p)))
        elif op == '7':
            c = pedir_consumo(p)
            print(r.resposta_led(p, c, **pedir_lampadas(p)))
        elif op == '8':
            print(r.resposta_ambiental(p, pedir_consumo(p)))
        elif op == '9':
            print(r.resposta_fontes())
        elif op == '10':
            print(r.ajuda_unidades(p))
        elif op == '11':
            pergunta = input('Sua pergunta (ex.: "vale a pena colocar placa solar?"): ')
            resposta = r.responder(pergunta, p, pedir_consumo(p) if r.identificar_intencao(pergunta) not in (None, 'unidades', 'fontes') else None)
            print(resposta or 'Não entendi. Tente perguntar sobre conta, solar, LED, CO₂, unidades ou fontes.')
        elif op == '0':
            print('Até mais!')
            break
        else:
            print('Opção inválida. Digite um número de 0 a 11.')


if __name__ == '__main__':
    main()
