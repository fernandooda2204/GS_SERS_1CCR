from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from energia import carregar_parametros,comparar
p=carregar_parametros();dest=Path(__file__).resolve().parents[1]/'data'/'exemplos_gerados.json'
dest.write_text(json.dumps({str(c):comparar(p,c) for c in (100,200,300)},indent=2,ensure_ascii=False),encoding='utf-8')
print('Exemplos simulados gerados:',dest)
