from unidades import pega_unidade
from dezenas import pega_dezena
from centenas import pega_centena


def controle(req):
    tamanho = len(req)
    retorno = ""

    if req[0] == "-":
        retorno += "menos "

    if tamanho == 1:
        retorno += pega_unidade(req)
    elif tamanho == 2:
        retorno += pega_dezena(req)
    elif tamanho == 3:
        retorno += pega_centena(req)
    else:
        retorno += pega_milhar(req)

    print(retorno)
