from unidades import pega_unidade
from dezenas import pega_dezena
from centenas import pega_centena


def controle(req):
    tamanho = len(req)
    escrita = ""

    if tamanho == 1:
        escrita = pega_unidade(req)
    elif tamanho == 2:
        escrita = pega_dezena(req)
    elif tamanho == 3:
        escrita = pega_centena(req)

    print(escrito)
