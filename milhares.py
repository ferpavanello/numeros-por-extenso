from unidades import pega_unidade
from dezenas import pega_dezena
from centenas import pega_centena


def pega_milhar(req):
    ret_milhar = ""

    if len(req) == 4:
        if req[1:3] == "000":
            ret_milhar = especifico_cem()

        else:
            ret_milhar += especifico_cem()
            ret_milhar += f" ${pega_centena(req[1:3])}"
    else:
        if req[1:4] == "0000":
            ret_milhar = f"${pega_dezena(req[0])} mil"

        else:
            ret_milhar += f"${pega_dezena(req[0])} mil "
            ret_milhar += pega_centena(req[1:3])


def especifico_cem(param):
    ret_especifico = ""
    if req[0] == "1":
        ret_especifico = "mil"
    else:
        ret_especifico += pega_unidade(req[0])
        ret_especifico += " mil"

    return ret_especifico
