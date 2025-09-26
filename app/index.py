from app.config import Configuracao
from app.repositories.transacao_cartoes_repositorio import TransacoesCartoesRepositorio
from app.services.transacao_cartoes_servicos import TransacoesCartoesServicos
from app.preprocessors.transacao_cartoes_preprocessador import TransacoesCartoesProcessador
from app.utils.segurança import uri_valida

def main():
    print("🚀 Iniciando aplicação Big Data - Transações de Cartões")
    print(f"📡 URI MongoDB: {Configuracao.MONGO_URI[:50]}...")
    print(f"🗄️ Banco: {Configuracao.MONGO_DB}")
    print(f"🌐 API BCB: {Configuracao.BCB_API_URI[:50]}...")
    
    # Validação da URI do banco
    if not uri_valida(Configuracao.MONGO_URI):
        raise ValueError("MONGO_URI inválida!")
    
    print("\n📊 Obtendo dados da API do Banco Central...")
    repositorio = TransacoesCartoesRepositorio(Configuracao.MONGO_URI, Configuracao.MONGO_DB)
    pre_processador = TransacoesCartoesProcessador()
    servico = TransacoesCartoesServicos(Configuracao.BCB_API_URI, pre_processador)
    
    try:
        transacoes_cartoes = servico.obter_e_preprocessar()
        print(f"✅ {len(transacoes_cartoes)} registros obtidos da API")
        
        print("\n💾 Inserindo dados no banco...")
        for i, registro in enumerate(transacoes_cartoes, 1):
            repositorio.inserir(registro)
            if i % 10 == 0:  # Mostra progresso a cada 10 registros
                print(f"📈 Processados {i}/{len(transacoes_cartoes)} registros")
        
        print(f"\n🎉 Processo concluído! {len(transacoes_cartoes)} registros processados com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro durante o processamento: {e}")
        raise

if __name__ == "__main__":
    main()