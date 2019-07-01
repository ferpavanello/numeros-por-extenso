from unidades import pega_unidade
from dezenas import pega_dezena
from centenas import pega_centena


def pega_milhar(req):
    ret_milhar = ""

    if len(req) == 4:
        if req[1:] == "000":
            ret_milhar = especifico_cem(req[0])

        elif req[2:] == "00":
            ret_milhar += especifico_cem(req[0])
            ret_milhar += f" e {pega_centena(req[1:])}"

        elif req[3:] == "0" or req[1:3] == "00":
            ret_milhar += especifico_cem(req[0])
            ret_milhar += f" {pega_centena(req[1:])}"

        else:
            ret_milhar += especifico_cem(req[0])
            ret_milhar += pega_centena(req[1:])
    else:
        if req[1:] == "0000":
            ret_milhar = f"{pega_dezena(req[:2])} mil"

        elif req[2:] == "000":
            ret_milhar += f"{pega_dezena(req[:2])} mil"

        elif req[3:] == "00":
            ret_milhar += f"{pega_dezena(req[:2])} mil e "
            ret_milhar += pega_centena(req[2:])

        else:
            ret_milhar += f"{pega_dezena(req[:2])} mil "
            ret_milhar += pega_centena(req[2:])

    return ret_milhar


def especifico_cem(param):
    ret_especifico = ""
    if param == "1":
        ret_especifico = "mil"
    else:
        ret_especifico += pega_unidade(param)
        ret_especifico += " mil"

    return ret_especifico
