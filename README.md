# API-wayne

---
## Resumo: 
A criação de tokenn está ok, mas a verificação do token já criado não está dando certo

verificação:
1. Rota '/rta/teste' | method - GET | -> **OK**
2. Rota '/rta/login' | method - POST |->
    A rota login deve conter as informações "email" e "senha" do usuario que quer conectar. Se as informações estiverem certas, então a rota irá retornar um token.
    informações usadas
    | informação | valor |
    |-----| ----|
    | Email | teste@gmail.com|
    | senha | senha1234 |
    | token | ' eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ0ZXN0ZUBnbWFpbC5jb20iLCJleHAiOjE3ODA2NTkxODl9.0_AMCvAIcT46P94d-M8WuQ32YA-X7bD9gjcT4fIJd0w '|

    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ0ZXN0ZUBnbWFpbC5jb20iLCJleHAiOjE3ODA2NTk1MjN9.OaOP4sgNPh7TFcVi4styA33QvMUX-VrCbdMXPcKegmM



---
## Objetivos:

1. Sistema de Gerenciamento de Segurança:
    * Desenvolva um sistema de controle de acesso que permita apenas
    usuários autorizados a acessar áreas restritas das instalações das Indústrias
    Wayne.
    * Implemente autenticação e autorização para diferentes tipos de usuários,
    como funcionários, gerentes e administradores de segurança.


2. Gestão de Recursos:
    * Desenvolva uma interface para gerenciar recursos internos, como 
    inventário de equipamentos, veículos e dispositivos de segurança.
    * Permita que os administradores possam adicionar, remover e atualizar 
    informações sobre esses recursos de forma eficiente.

3. Dashboard de Visualização:
    * Crie um painel de controle visualmente atraente que exiba dados relevantes 
    sobre segurança, recursos e atividades dentro das Indústrias Wayne.


---
## Rotas
Pra cada rota que for acessa ela terá uma intervenção do decorador `@app.before_request`
|Rota|Função|
|---|---|
|

---


---
## Mapa atual

```Bash
.
├── docu.md
├── README.md
├── requirements.txt
├── run.py
├── src
│   ├── db
│   ├── __init__.py
│   ├── __pycache__
│   ├── routes.py
│   └── utils
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── lib64 -> lib
    └── pyvenv.cfg

```


---
## Feito por Pablo