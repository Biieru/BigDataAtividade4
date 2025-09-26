from app.models.transacao_cartoes import TransacoesCartoes

class TransacoesCartoesProcessador:
    def processar(self, data):
        # Valida e converte os campos conforme necessário
        trimestre = data.get("trimestre")
        nome_bandeira = data.get("nomeBandeira", "")
        nome_funcao = data.get("nomeFuncao", "")
        qtd_transacoes_nacionais = int(data.get("qtdTransacoesNacionais", 0))
        valor_transacoes_nacionais = float(data.get("valorTransacoesNacionais", 0))
        qtd_transacoes_internacionais = int(data.get("qtdTransacoesInternacionais", 0))
        valor_transacoes_internacionais = float(data.get("valorTransacoesInternacionais", 0))
        
        return TransacoesCartoes(
            trimestre, nome_bandeira, nome_funcao,
            qtd_transacoes_nacionais, valor_transacoes_nacionais,
            qtd_transacoes_internacionais, valor_transacoes_internacionais
        )