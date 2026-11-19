"""Calcula o SUS de respostas reais (escala 1 a 5)."""
import sys
def sus(respostas):
    if len(respostas) != 10 or any((not isinstance(n,int)) or n not in range(1,6) for n in respostas):
        raise ValueError('Informe exatamente 10 notas inteiras de 1 a 5.')
    return sum((n - 1 if i%2==0 else 5 - n) for i,n in enumerate(respostas))*2.5
if __name__=='__main__':
    try:
        print('SUS:',sus([int(x) for x in sys.argv[1:]]))
    except ValueError as e:
        print('Erro:',e);sys.exit(1)
