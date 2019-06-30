from unidades import pega_unidade
from dezenas import pega_dezena
from centenas import pega_centena


def pega_milhar(req):
    ret_milhar = ""

    if len(req) == 4:
        if req[1:4] == "000":
            ret_milhar = especifico_cem(req[0])

        else:
            ret_milhar += especifico_cem(req[0])
            ret_milhar += f" {pega_centena(req[1:4])}"
    else:
        if req[1:5] == "0000":
            ret_milhar = f"{pega_dezena(req[:2])} mil"

        else:
            ret_milhar += f"{pega_dezena(req[:2])} mil "
            ret_milhar += pega_centena(req[2:5])

    return ret_milhar


def especifico_cem(param):
    ret_especifico = ""
    if param == "1":
        ret_especifico = "mil"
    else:
        ret_especifico += pega_unidade(param)
        ret_especifico += " mil"

    return ret_especifico
