import sys

sys.path.append('principal')
sys.path.append('constantes')
sys.path.append('objetos')

from jogo import jogo

try:
    jogo()
except:
    print(sys.exc_info())
        