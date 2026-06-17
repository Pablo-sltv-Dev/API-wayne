# API-wayne

---
# links do postmans
 "https://solotv-3391511.postman.co/workspace/Final-Project-Infinity~9360ac56-9360-4842-b265-15c6250018a6/request/47017727-31766f6b-7b18-4299-863f-2130fa482d06?action=share&creator=47017727", 
 "https://solotv-3391511.postman.co/workspace/Final-Project-Infinity~9360ac56-9360-4842-b265-15c6250018a6/request/47017727-ccd91219-97ca-4fbb-8933-6b521be7358b?action=share&creator=47017727",


## Resumo: 
A verificação de senha e criação de hash está ok
a verificação de hash e criação de tokens está ok
a verificação de tokens e acesso a rota com token obrigatória está ok
Agr preciso limitar o acesso antes e dps da criação/verificaçãoi de token
O limite de requisição está ok


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
| Rota | Função |
| --- | --- |
| `/rta/test` | teste de conexão |
| `/rts/teste_info` | teste de recebimento de informação | 
| `/rta/login` | verificação de informações e criação de token | 
| `/rta/tk_verificacao` | verificação de token |
|  |  | 

---


---
## Mapa atual

```Bash
.
│
│
│
├── src/
    │   
    ├── __init__.py
    │
    ├── routes/
            │
            ├── __init__.py
            │
            ├── public.py
            │
            ├── private.py

│
├── DB/




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