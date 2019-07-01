from unidades import pega_unidade
from dezenas import pega_dezena
from centenas import pega_centena
from milhares import pega_milhar


def controle(req):
    retorno = ""

    if req[0] == "-":
        retorno += "menos "
        req = req[1:]

    tamanho = len(req)

    if tamanho == 1:
        retorno += pega_unidade(req)
    elif tamanho == 2:
        retorno += pega_dezena(req)
    elif tamanho == 3:
        retorno += pega_centena(req)
    else:
        retorno += pega_milhar(req)

    return retorno
