from pymongo import MongoClient
import os

# Responsável por acessar o banco de dados
class TransacoesCartoesRepositorio:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.cliente = None
        self.colecao = None
        self.modo_teste = os.getenv('MODO_TESTE', 'false').lower() == 'true'
        
        if not self.modo_teste:
            try:
                # Tentativa de conexão simples primeiro
                self.cliente = MongoClient(mongo_uri, serverSelectionTimeoutMS=10000)
                self.colecao = self.cliente[mongo_db]["transacoes_cartoes"]
                # Teste de conexão
                self.cliente.admin.command('ping')
                print("✅ Conexão com MongoDB estabelecida com sucesso!")
            except Exception as e:
                print(f"❌ Erro ao conectar com MongoDB: {e}")
                print("🔄 Tentando modo de teste...")
                self.modo_teste = True
    
    def inserir(self, transacao_cartao):
        if self.modo_teste:
            # Modo de teste - apenas imprime os dados
            print(f"📊 [MODO TESTE] Dados que seriam inseridos: {transacao_cartao.to_dict()}")
            return True
        else:
            # Insere um documento/moeda na coleção
            self.colecao.insert_one(transacao_cartao.to_dict())
            return True
        