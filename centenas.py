from unidades import pega_unidade
from dezenas import pega_dezena


def pega_centena(req):
    ret_centena = ""

    if req[1:2] == "00":
        return pontuais(req[0])

    elif req[2] == "0":
        if req[0] == "1":
            ret_centena += "cento"
        else:
            ret_centena += pontuais(req[0])
            ret_centena += " e "
            ret_centena += pega_unidade(req[2])

    elif req[2] == "0":
        if req[0] == "1":
            ret_centena += "cento"
        else:
            ret_centena += pontuais(req[0])

        ret_centena += " e "
        ret_centena += pega_dezena(req[1:2])
        return ret_centena


def pontuais(param):
    if req[0] == "1":
        return "cem"
    elif req[0] == "2":
        return "duzentos"
    elif req[0] == "3":
        return "trezentos"
    elif req[0] == "4":
        return "quatrossentos"
    elif req[0] == "5":
        return "quinhentos"
    elif req[0] == "6":
        return "seissentos"
    elif req[0] == "7":
        return "setessentos"
    elif req[0] == "8":
        return "oitossentos"
    elif req[0] == "9":
        return "novessentos"
