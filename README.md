# Tutorial: Criando um Aplicativo de Registro de Usuários com Flask e SQL Server Para Shaiya Server

Este tutorial mostrará como criar um aplicativo web de registro de usuários usando Flask, um micro-framework em Python, e o SQL Server como banco de dados. O aplicativo permite que os usuários se registrem fornecendo um nome de usuário, senha e e-mail, e os dados do registro são armazenados no banco de dados SQL Server.

## Pré-requisitos

- Python instalado (versão 3.6 ou superior)
- SQL Server instalado e configurado
- Conhecimento básico de Python e SQL

## Passo 1: Configurando o Ambiente

Certifique-se de ter o Python instalado. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

Instale o Flask executando o seguinte comando no terminal:

```bash
pip install Flask
```

## Passo 2: Criando o Banco de Dados SQL Server

Verifique seu banco de dados no SQL Server se está igual a abaixo para armazenar os dados do aplicativo. SQL Server Management Studio (SSMS)

```
TABLE Users_Master 
    UserUID INT IDENTITY(1,1) PRIMARY KEY,
    UserID VARCHAR(18) NOT NULL,
    Pw VARCHAR(18) NOT NULL,
    JoinDate SMALLDATETIME NOT NULL,
    Admin BIT NOT NULL,
    AdminLevel TINYINT NOT NULL,
    UseQueue BIT NOT NULL,
    Status SMALLINT NOT NULL,
    Leave TINYINT NOT NULL,
    LeaveDate SMALLDATETIME,
    UserType CHAR(1) NOT NULL,
    UserIp VARCHAR(15),
    Point INT NOT NULL,
    Enpassword CHAR(32),
    Birth VARCHAR(10),
    Email VARCHAR(50) NOT NULL,
    UserCargo INT NOT NULL,
    PwName VARCHAR(12) NOT NULL
```

## IMPORTANTE 

Esse projeto é uma adaptação do projeto de DanisFilth em Projeto de Shaiya, é apenas uma parte de seu projeto, tornando uma alternativa de não usar o PHP.