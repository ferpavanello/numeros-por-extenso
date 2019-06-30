from unidades import pega_unidade


def pega_dezena(req):
    ret_dezena = ""

    if req[1] == "0":
        ret_dezena = pontuais(req[0])
    elif req[0] == "1":
        ret_dezena = especifico_dez(req[1])
    else:
        ret_dezena += pontuais(req[0])
        ret_dezena += " e "
        ret_dezena += pega_unidade(req[1])

    return ret_dezena


def pontuais(param):
    if param == "1":
        return "dez"
    elif param == "2":
        return "vinte"
    elif param == "3":
        return "trinta"
    elif param == "4":
        return "quarenta"
    elif param == "5":
        return "cinquenta"
    elif param == "6":
        return "sessenta"
    elif param == "7":
        return "setenta"
    elif param == "8":
        return "oitenta"
    elif param == "9":
        return "noventa"


def especifico_dez(param):
    if param == "1":
        return "onze"
    elif param == "2":
        return "doze"
    elif param == "3":
        return "treze"
    elif param == "4":
        return "quatorze"
    elif param == "5":
        return "quinze"
    elif param == "6":
        return "dezesseis"
    elif param == "7":
        return "dezessete"
    elif param == "8":
        return "dezoito"
    elif param == "9":
        return "dezenove"
