import re

# Valida se a URL do MongoDB está no formato correto
def uri_valida(uri):
    padrao = r"^mongodb\+srv:\/\/.*"
    return bool(re.match(padrao, uri))
