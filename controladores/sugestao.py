from controladores import sistema
from editaveis import textos

"""Essa função tem com objetivo imprimir as informações 
    de acordo com o imc e a idade do usuário em questão"""


def sugerir(imc, idade):
    if imc < 18.5:  # magro
        if idade <= 12:  # Criança
            sistema.divisorias()
            textos.crianca_muito_magra()
            sistema.divisorias()
        elif 12 < idade <= 20:  # adolescente
            sistema.divisorias()
            textos.adolescente_muito_magro()
            sistema.divisorias()
        elif 20 < idade <= 65:  # adulto
            sistema.divisorias()
            textos.adulto_muito_magro()
            sistema.divisorias()
        else:  # idoso
            sistema.divisorias()
            textos.idoso_muito_magro()
            sistema.divisorias()

    elif 18.5 < imc < 30:  # no peso
        if idade <= 12:  # criança
            sistema.divisorias()
            textos.crianca_nopeso()
            sistema.divisorias()
        elif 12 < idade <= 20:  # adolescente
            sistema.divisorias()
            textos.adolecente_nopeso()
            sistema.divisorias()
        elif 20 < idade <= 65:  # adulto
            sistema.divisorias()
            textos.adulto_nopeso()
            sistema.divisorias()
        else:  # idoso
            sistema.divisorias()
            textos.idoso_nopeso()
            sistema.divisorias()
    else:  # Acima do peso
        if idade <= 12:  # criança
            sistema.divisorias()
            textos.crianca_acimapeso()
            sistema.divisorias()
        elif 12 < idade <= 20:  # adolecente
            sistema.divisorias()
            textos.adolecente_acimapeso()
            sistema.divisorias()
        elif 20 < idade <= 65:  # adulto
            sistema.divisorias()
            textos.adulto_acimapeso()
            sistema.divisorias()
        else:  # idoso
            sistema.divisorias()
            textos.idoso_acimapeso()
            sistema.divisorias()
