import os

import paramiko

# Configurações do servidor SFTP
host = 'rodoparanaimplementos120531.protheus.cloudtotvs.com.br'
port = 2323
usuario = 'ftp_CRC3TS_production'
senha = 'KQW8Az2I'
pasta_remota = 'dev/system/nfse'

# Pasta local para salvar os arquivos
pasta_local = 'c:\\temp'

# Conectar ao servidor SFTP
with paramiko.Transport((host, port)) as transport:
    transport.connect(username=usuario, password=senha)
    sftp = paramiko.SFTPClient.from_transport(transport)

    # Mudar para a pasta remota
    try:
        sftp.chdir(pasta_remota)
    except IOError:
        print("Diretório destino não encontrado")

    # Listar os arquivos na pasta remota
    arquivos_remotos = sftp.listdir()

    # Criar a pasta local se não existir
    if not os.path.exists(pasta_local):
        os.makedirs(pasta_local)

    # Loop para baixar os arquivos PDF
    for arquivo_remoto in arquivos_remotos:
        if arquivo_remoto.lower().endswith('.pdf'):
            caminho_local = os.path.join(pasta_local, arquivo_remoto)

            # Baixar o arquivo
            sftp.get(arquivo_remoto, caminho_local)
            print(f"Download do arquivo {arquivo_remoto} realizado com sucesso!") # noqa E501

            # Excluir o arquivo remoto após o download
            sftp.remove(arquivo_remoto)

print("Download e exclusão concluídos.")

# pyinstaller --onefile monitor_data.py