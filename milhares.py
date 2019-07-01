from unidades import pega_unidade
from dezenas import pega_dezena
from centenas import pega_centena


def pega_milhar(req):
    ret_milhar = ""

    if len(req) == 4:
        ret_milhar += especifico_cem(req[0])
        if req[1:] != "000":
            if req[2:] == "00":
                ret_milhar += " e"

            ret_milhar += f" {pega_centena(req[1:])}"

    else:
        ret_milhar += f"{pega_dezena(req[:2])} mil"

        if req[1:] != "0000" and req[2:] != "000":

            if req[3:] == "00":
                ret_milhar += " e"

            ret_milhar += f" {pega_centena(req[2:])}"

    return ret_milhar


def especifico_cem(param):
    ret_especifico = ""
    if param == "1":
        ret_especifico = "mil"
    else:
        ret_especifico += pega_unidade(param)
        ret_especifico += " mil"

    return ret_especifico
