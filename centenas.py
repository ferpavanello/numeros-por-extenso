from unidades import pega_unidade
from dezenas import pega_dezena


def pega_centena(req):
    ret_centena = ""

    if req[1:3] == "00":
        ret_centena = pontuais(req[0])

    elif req[:2] == "00":
        ret_centena = f" e {pega_unidade(req[2])}"

    else:
        if req[0] == "1":
            ret_centena += "cento"
        elif req[0] != "0":
            ret_centena += pontuais(req[0])

        ret_centena += " e "
        ret_centena += pega_dezena(req[1:3])

    return ret_centena


def pontuais(param):
    if param[0] == "1":
        return "cem"
    elif param[0] == "2":
        return "duzentos"
    elif param[0] == "3":
        return "trezentos"
    elif param[0] == "4":
        return "quatrossentos"
    elif param[0] == "5":
        return "quinhentos"
    elif param[0] == "6":
        return "seissentos"
    elif param[0] == "7":
        return "setessentos"
    elif param[0] == "8":
        return "oitossentos"
    elif param[0] == "9":
        return "novessentos"
