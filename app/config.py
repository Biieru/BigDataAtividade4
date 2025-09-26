import os
from dotenv import load_dotenv

load_dotenv() # Carrega as variáveis do .env

class Configuracao:
    # Valores padrão para teste (substitua pelos seus dados reais do MongoDB Atlas)
    MONGO_URI = os.getenv('MONGO_URI') or "mongodb+srv://<USUARIO>:<SENHA>@cluster0.yjkvba7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    BCB_API_URI = os.getenv('BCB_API_URI') or "https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/Quantidadeetransacoesdecartoes(trimestre=@trimestre)?@trimestre='20251'&$top=200&$format=json&$select=trimestre,nomeBandeira,nomeFuncao,qtdTransacoesNacionais,valorTransacoesNacionais,qtdTransacoesInternacionais,valorTransacoesInternacionais"
    MONGO_DB = os.getenv('MONGO_DB') or "banco_central"
    