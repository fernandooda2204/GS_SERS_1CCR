"""Protótipo de terminal: 10 escolhas numeradas, com persistência local dos aparelhos."""
import json
from pathlib import Path
from energia import carregar_parametros, consumo_kwh, consumo_geladeira_etiqueta, comparar
APARELHOS=Path(__file__).resolve().parent/'data'/'aparelhos_local.json'
def ler_numero(msg, minimo=0):
    while True:
        try:
            n=float(input(msg).strip().replace(',','.'))
            if n<minimo: raise ValueError()
            return n
        except ValueError: print('Informe um número válido não negativo.')
def aparelhos():
    try: return json.loads(APARELHOS.read_text(encoding='utf-8'))
    except (OSError,ValueError): return []
def salvar(items): APARELHOS.write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
def brl(v): return f'R$ {v:,.2f}'.replace(',','X').replace('.',',').replace('X','.')
def exibir(d):
    for k,v in d.items():
        if isinstance(v,dict):
            print('\n'+k+':');exibir(v)
        else: print(f'  {k.replace("_"," ")}: {round(v,2) if isinstance(v,float) else v}')
def main():
    p=carregar_parametros()
    print('\nCitizen Assist AI | Módulo Energia (protótipo ilustrativo)')
    while True:
        print("""\n1 Cadastrar aparelho  2 Listar aparelhos  3 Consumo dos aparelhos
4 Simular conta       5 Comparar alternativas  6 Energia solar
7 Troca por LED       8 Impacto ambiental     9 Premissas e fontes
10 Sair""")
        op=input('Escolha (1-10): ').strip()
        if op=='1':
            nome=input('Nome do aparelho: ').strip() or 'Aparelho'
            if 'geladeira' in nome.lower():
                c=consumo_geladeira_etiqueta(ler_numero('Consumo da etiqueta (kWh/mês): '))
            else:
                potencia=ler_numero('Potência (W): ')
                horas=ler_numero('Horas de uso por dia: ')
                qtd=ler_numero('Quantidade de aparelhos: ',1)
                c=consumo_kwh(potencia,horas,quantidade=qtd)
            itens=aparelhos();itens.append({'nome':nome,'kwh_mes':round(c,3)});salvar(itens)
            print(f'Adicionado: {c:.2f} kWh/mês')
        elif op=='2':
            itens=aparelhos()
            for a in itens: print(f"- {a['nome']}: {a['kwh_mes']} kWh/mês")
            if not itens: print('Nenhum aparelho cadastrado.')
        elif op=='3':
            total=sum(a['kwh_mes'] for a in aparelhos());print(f'Total cadastrado: {total:.2f} kWh/mês. Não inclui cargas não cadastradas.')
        elif op in ('4','5','6','7','8'):
            referencia=p['consumo_referencia_kwh_mes']
            c=ler_numero(f'Consumo mensal em kWh (exemplo: {referencia}): ')
            comp=comparar(p,c)
            if op=='4': print('Conta estimada sem solar:',brl(comp['a1_conta_brl']))
            elif op=='5': exibir(comp)
            elif op=='6': exibir(comp['a2_solar'])
            elif op=='7': exibir(comp['a3_led'])
            elif op=='8': print('CO₂ evitado estimado (solar):',round(comp['a2_solar']['co2_evitado_kg_mes'],2),'kg/mês\nCO₂ evitado estimado (LED):',round(comp['a3_led']['co2_evitado_kg_mes'],2),'kg/mês')
            print('Atenção: valores ilustrativos, sem garantia de economia. Confira tarifas, regras e equipamentos.')
        elif op=='9':
            raw=json.loads((Path(__file__).resolve().parent/'data'/'parametros.json').read_text(encoding='utf-8'))
            for k,v in raw.items(): print(f"{k}: {v['valor']} {v['unidade']} | {v['fonte']} | {v['verificacao']}")
        elif op=='10': print('Até mais!');break
        else: print('Opção inválida. Escolha de 1 a 10.')
if __name__=='__main__': main()
