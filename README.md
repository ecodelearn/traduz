# traduz
script python que cria legendas .SRT automáticamente


# Script de Tradução Automática

Este é um script Python chamado "traduz.py" que permite automatizar a tradução de legendas de vídeos usando o [Legen](https://github.com/legnaleurc/legen) como base. O script utiliza os códigos de língua fornecidos pelo Legen para gerar legendas em várias línguas automaticamente.

## Pré-requisitos

Antes de usar este script, você precisará ter o Legen instalado em seu ambiente. Você pode encontrar mais informações sobre como instalá-lo no [repositório do Legen](https://github.com/legnaleurc/legen).

## Como Usar

1. Clone este repositório para o seu ambiente local:

git clone https://github.com/ecodelearn/traduz.git


## IMPORTANTE !!!

copie o arquivo traduz.py para dentro do diretório do legen



2. Navegue até o diretório do projeto:

cd legen


3. Edite o script `traduz.py` para especificar o diretório de entrada do vídeo desejado. Você pode fazer isso alterando a variável `input_directory` no script para o caminho do diretório desejado.

4. Execute o script:

python traduz.py


O script irá percorrer todos os códigos de língua disponíveis e gerar legendas automaticamente para cada língua no diretório especificado.

## Códigos de Língua Disponíveis

Aqui estão os códigos de língua disponíveis para uso com o Legen:

| Língua            | Código ISO-639 |
|-------------------|----------------|
| Afrikaans         | af             |
| Albanian          | sq             |
| Amharic           | am             |
| Arabic            | ar             |
| Armenian          | hy             |
| ...               | ...            |

Certifique-se de ajustar o diretório de entrada (`input_directory`) no script para o local desejado dos seus vídeos antes de executar o script.

**Nota:** Este script é fornecido como está e não há garantias de suporte ou funcionamento em todos os cenários. Certifique-se de que você está em conformidade com as políticas de uso do YouTube ao legendar vídeos automaticamente.

## Contribuição

Contribuições são bem-vindas! Se você encontrar problemas ou quiser melhorar este script, sinta-se à vontade para criar um pull request ou abrir uma issue no repositório.

## Licença

Este projeto está licenciado sob a licença [MIT](LICENSE).
