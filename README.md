# Projeto Shaiya - Cadastro de Usuários com Flask e SQL Server
 
Este projeto consiste em um aplicativo web simples que permite aos usuários se registrarem fornecendo informações como nome de usuário, senha e e-mail. Os dados de registro são armazenados em um banco de dados SQL Server. Este README fornecerá instruções detalhadas sobre como configurar e executar o aplicativo.

Para saber sobre o projeto ao todo é necessário seguir o canal do [DanisFilth](https://www.youtube.com/@DanisFilth/videos), todos os arquivos podem ser modificados ao seu valor, mais está voltado ao tutorial do Youtuber Danis.

Incrementos internos: IP do usuário, data de registro, etc.

## Pré-requisitos

Antes de iniciar, certifique-se de que você tenha os seguintes requisitos instalados:

- Python (versão 3.6 ou superior): [Download Python](https://www.python.org/downloads/)
- SQL Server: Certifique-se de ter um servidor SQL Server instalado e configurado com uma tabela chamada `Users_Master` conforme definido no projeto.

## Instalação

1. Clone este repositório para o seu computador:

```Bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse o diretório do projeto:

```Bash
cd seu-repositorio
```

3. Instale as dependências necessárias usando o pip (gerenciador de pacotes do Python):

```Bash
pip install -r requirements.txt
```

4. Edite o arquivo `app.py` para configurar o acesso ao seu banco de dados SQL Server. Você precisará fornecer as informações corretas de conexão, incluindo o nome do servidor, nome do banco de dados, nome de usuário e senha.

## Executando o Aplicativo

Para executar o aplicativo, execute o seguinte comando no diretório raiz do projeto:

```Bash
python app.py
```

O aplicativo estará disponível em seu navegador em `http://127.0.0.1:5000/`, onde você poderá acessar o formulário de registro.

## Personalização

Este é um projeto básico que pode ser personalizado de acordo com suas necessidades. Você pode adicionar recursos adicionais, como autenticação de usuário, validação de formulário, criptografia de senhas, entre outros, para atender aos requisitos específicos do seu projeto.

Certifique-se de ajustar o projeto conforme necessário para torná-lo mais seguro e adequado às suas necessidades.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar problemas ou solicitar recursos no repositório. Se desejar contribuir com código, crie um fork do repositório, faça as alterações e envie uma solicitação pull.

Aproveite o uso deste projeto!

