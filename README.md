# 📊 Big Data - Análise de Transações de Cartões

## 🎯 Descrição do Projeto

Este projeto implementa uma solução de Big Data para análise de transações de cartões utilizando dados do Banco Central do Brasil (BCB). A aplicação coleta, processa e armazena dados de transações de cartões de crédito e débito para análise posterior.

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas bem estruturada:

```
app/
├── config.py                    # Configurações da aplicação
├── index.py                     # Ponto de entrada principal
├── models/                      # Modelos de dados
│   └── transacao_cartoes.py
├── preprocessors/               # Processamento de dados
│   └── transacao_cartoes_preprocessador.py
├── repositories/                # Acesso a dados
│   └── transacao_cartoes_repositorio.py
├── services/                    # Lógica de negócio
│   └── transacao_cartoes_servicos.py
└── utils/                       # Utilitários
    └── segurança.py
```

## 🚀 Funcionalidades

- **Coleta de Dados**: Integração com API do Banco Central do Brasil
- **Processamento**: Limpeza e transformação de dados
- **Armazenamento**: Persistência em MongoDB Atlas
- **Modo de Teste**: Funcionamento offline para desenvolvimento
- **Validação**: Verificação de integridade dos dados
- **Logs Detalhados**: Acompanhamento do processamento

## 📋 Pré-requisitos

- Python 3.8+
- MongoDB Atlas (ou MongoDB local)
- Conta no Banco Central do Brasil para acesso à API

## 🛠️ Instalação

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd BigDataAtividade4
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac
```

3. **Instale as dependências**
```bash
pip install -r app/requirements.txt
```

4. **Configure as variáveis de ambiente**
Crie um arquivo `.env` na raiz do projeto:
```env
MONGO_URI=mongodb+srv://usuario:senha@cluster.mongodb.net/
MONGO_DB=banco_central
BCB_API_URI=https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/Quantidadeetransacoesdecartoes(trimestre=@trimestre)?@trimestre='20251'&$top=200&$format=json&$select=trimestre,nomeBandeira,nomeFuncao,qtdTransacoesNacionais,valorTransacoesNacionais,qtdTransacoesInternacionais,valorTransacoesInternacionais
```

## 🎮 Como Usar

### Execução Normal
```bash
py -m app.index
```

### Modo de Teste (sem MongoDB)
```bash
set MODO_TESTE=true
py -m app.index
```

## 📊 Dados Processados

A aplicação processa dados de transações de cartões incluindo:

- **Trimestre**: Período de referência
- **Nome da Bandeira**: Visa, Mastercard, etc.
- **Função**: Crédito ou Débito
- **Transações Nacionais**: Quantidade e valor
- **Transações Internacionais**: Quantidade e valor

## 🔧 Configurações

### MongoDB Atlas
- Configure seu cluster no MongoDB Atlas
- Adicione seu IP à whitelist
- Use a string de conexão fornecida

### API Banco Central
- A API é pública e não requer autenticação
- Dados atualizados trimestralmente
- Suporte a filtros por período

## 🛡️ Segurança

- Validação de URIs MongoDB
- Tratamento de erros SSL/TLS
- Modo de teste para desenvolvimento seguro
- Logs sem exposição de credenciais

## 🐛 Solução de Problemas

### Erro de Conexão MongoDB
```
ServerSelectionTimeoutError: SSL handshake failed
```
**Solução**: A aplicação automaticamente entra em modo de teste. Para resolver:
1. Verifique se seu IP está na whitelist do MongoDB Atlas
2. Confirme as credenciais de acesso
3. Teste a conectividade de rede

### Erro de Módulo Não Encontrado
```
ModuleNotFoundError: No module named 'dotenv'
```
**Solução**: Instale as dependências:
```bash
pip install -r app/requirements.txt
```

## 📈 Monitoramento

A aplicação fornece logs detalhados:
- 🚀 Status de inicialização
- 📊 Progresso de coleta de dados
- 💾 Status de inserção no banco
- ❌ Tratamento de erros
- 🎉 Confirmação de conclusão

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- **Sassha Michaelis** - Desenvolvimento e implementação

## 📞 Suporte

Para suporte, abra uma issue no repositório ou entre em contato através do email.

---

## 🎯 Próximos Passos

- [ ] Implementar dashboard de visualização
- [ ] Adicionar testes unitários
- [ ] Implementar cache de dados
- [ ] Adicionar métricas de performance
- [ ] Criar documentação da API

---

**Desenvolvido com ❤️ para análise de Big Data**
