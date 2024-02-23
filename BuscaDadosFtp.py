import os
from ftplib import FTP

# Configurações do servidor FTP
host = 'ftp.b3gestaoetecnolo1.hospedagemdesites.ws'
usuario = 'b3gestaoetecnolo1'
senha = 'B3gestao_Senh@'
pasta_remota = 'teste'

# Pasta local para salvar os arquivos
pasta_local = 'c:\\temp'

# Conectar ao servidor FTP
with FTP(host) as ftp:
    # Fazer login
    ftp.login(usuario, senha)

    # Mudar para a pasta remota
    try:
        ftp.cwd(pasta_remota)
    except Exception:
        print("Diretório destino não encontrado")

    # Listar os arquivos na pasta remota
    arquivos_remotos = ftp.nlst()

    # Criar a pasta local se não existir
    if not os.path.exists(pasta_local):
        os.makedirs(pasta_local)

    # Loop para baixar os arquivos PDF
    for arquivo_remoto in arquivos_remotos:
        if arquivo_remoto.lower().endswith('.pdf'):
            caminho_local = os.path.join(pasta_local, arquivo_remoto)

            # Baixa o Arquivo
            with open(caminho_local, 'wb') as arquivo_local:
                ftp.retrbinary(f"RETR {arquivo_remoto}", arquivo_local.write)
                print(f"Download do arquivo {arquivo_remoto} realizado com sucesso!") # noqa eE501
          
            # Excluir o arquivo remoto após o download
            ftp.delete(arquivo_remoto)
        else:
            print("Não existem arquivos para download")

# pyinstaller --onefile BuscaDadosFtp.py