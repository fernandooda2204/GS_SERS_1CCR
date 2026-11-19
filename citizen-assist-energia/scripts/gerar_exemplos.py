"""Gera data/exemplos_gerados.json: comparação A1 × A2 × A3 para 100, 200 e 300 kWh/mês."""
from pathlib import Path
import json
import sys

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

from energia import carregar_parametros, comparar  # noqa: E402


def arredondar(obj):
    if isinstance(obj, dict):
        return {k: arredondar(v) for k, v in obj.items()}
    if isinstance(obj, float):
        return round(obj, 2)
    return obj


p = carregar_parametros()
destino = RAIZ / 'data' / 'exemplos_gerados.json'
dados = {f'{c}_kwh_mes': arredondar(comparar(p, c)) for c in (100, 200, 300)}
destino.write_text(json.dumps(dados, indent=2, ensure_ascii=False), encoding='utf-8')
print('Exemplos gerados:', destino)
