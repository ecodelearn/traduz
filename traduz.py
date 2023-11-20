import subprocess

# Lista de códigos de língua e seus respectivos nomes. Se quiser aumentar a gama de tradução procure os códigos em : https://cloud.google.com/translate/docs/languages
languages = {
    'Afrikans': 'af',
    'Albanian': 'sq',
    'Portugues': 'pt',
    'Inglês': 'en',
    'Espanhol': 'es',
    'Alemão': 'de',
    'Francês': 'fr',
    'Italiano': 'it',
    'Russo': 'ru',
    'Korean': 'ko',
    'Chinese': 'zh-CN',
    'Japones': 'ja',
    'Hindi': 'hi',

    # Adicione todos os outros códigos de língua aqui
}

# Caminho do diretório de entrada MUDAR PARA O DIRETÓRIO ONDE FICA O SEU MP4 (VÍDEO ORIGINAL).
input_directory = '/home/dds/sandeco/'

# Opções desabilitadas
disable_embed = '--disable_embed'
disable_burn = '--disable_burn'

# Loop pelos códigos de língua
for language_name, language_code in languages.items():
    # Comando para legendar o vídeo com o código de língua atual
    command = f"python legen.py -i {input_directory} {disable_embed} {disable_burn} --lang {language_code}"
    
    # Execute o comando
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Legenda para a língua {language_name} gerada com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar legenda para a língua {language_name}: {e}")
