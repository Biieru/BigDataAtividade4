class TransacoesCartoes:

    def __init__(self, trimestre, nomeBandeira, nomeFuncao,
                 qtdTransacoesNacionais, valorTransacoesNacionais, qtdTransacoesInternacionais, valorTransacoesInternacionais):
        self.trimestre = trimestre
        self.nomeBandeira = nomeBandeira
        self.nomeFuncao = nomeFuncao
        self.qtdTransacoesNacionais = qtdTransacoesNacionais
        self.valorTransacoesNacionais = valorTransacoesNacionais
        self.qtdTransacoesInternacionais = qtdTransacoesInternacionais
        self.valorTransacoesInternacionais = valorTransacoesInternacionais

    def to_dict(self):
        return {
            "trimestre": self.trimestre,
            "nomeBandeira": self.nomeBandeira,
            "nomeFuncao": self.nomeFuncao,
            "qtdTransacoesNacionais": self.qtdTransacoesNacionais,
            "valorTransacoesNacionais": self.valorTransacoesNacionais,
            "qtdTransacoesInternacionais": self.qtdTransacoesInternacionais,
            "valorTransacoesInternacionais": self.valorTransacoesInternacionais
        }