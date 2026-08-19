# API-Wayne

Sistema de gerenciamento de segurança e recursos internos das Indústrias Wayne.

---

## 1. Visão geral

A **API-Wayne** é uma API desenvolvida para fornecer uma estrutura de gerenciamento de segurança, autenticação de usuários e controle de acesso aos recursos internos das Indústrias Wayne.

O sistema possui mecanismos de:

* Autenticação de usuários;
* Criação e verificação de hash de senhas;
* Criação de tokens de autenticação;
* Verificação de tokens;
* Controle de acesso a rotas protegidas;
* Limitação de requisições;
* Recebimento e processamento de informações.

---

# 2. Objetivos do projeto

## 2.1 Sistema de Gerenciamento de Segurança

Desenvolver um sistema de controle de acesso que permita apenas usuários autorizados a acessar áreas restritas das Indústrias Wayne.

O sistema deverá permitir diferentes níveis de acesso, como:

* Funcionários;
* Gerentes;
* Administradores de segurança.

Cada tipo de usuário poderá possuir diferentes permissões dentro da API.

---

## 2.2 Gestão de Recursos

Desenvolver uma interface para gerenciamento de recursos internos, incluindo:

* Inventário de equipamentos;
* Veículos;
* Dispositivos de segurança;
* Outros recursos pertencentes às Indústrias Wayne.

Administradores deverão possuir permissão para:

* Adicionar recursos;
* Remover recursos;
* Atualizar informações;
* Consultar recursos cadastrados.

---

## 2.3 Dashboard de Visualização

Desenvolver um dashboard para apresentar informações relevantes sobre:

* Segurança;
* Recursos;
* Atividades;
* Usuários;
* Eventos registrados no sistema.

O objetivo é fornecer uma visualização centralizada das informações da API.

---

# 3. Estrutura atual do projeto

A estrutura atual do projeto está organizada da seguinte forma:

```text
.
├── DB/
│
├── docu.md
├── README.md
├── requirements.txt
├── run.py
│
├── src/
│   ├── db/
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── public.py
│   │   └── private.py
│   │
│   ├── utils/
│   │
│   └── __init__.py
│
└── venv/
    ├── bin/
    ├── include/
    ├── lib/
    ├── lib64 -> lib
    └── pyvenv.cfg
```

> A pasta `venv` contém o ambiente virtual Python e normalmente não deve ser versionada no Git.

---

# 4. Rotas da API

As rotas atualmente previstas na API são:

| Rota                  | Função                                         | Acesso    |
| --------------------- | ---------------------------------------------- | --------- |
| `/rta/test`           | Teste de conexão com a API                     | Público   |
| `/rts/teste_info`     | Teste de recebimento de informações            | Público   |
| `/rta/login`          | Verificação das credenciais e criação do token | Público   |
| `/rta/tk_verificacao` | Verificação do token de autenticação           | Protegido |

---

## 4.1 `/rta/test`

### Objetivo

Realizar um teste simples para verificar se a API está funcionando corretamente.

### Função

Teste de conexão.

### Exemplo

```http
GET /rta/test
```

### Resposta esperada

```json
{
    "message": "API funcionando"
}
```

---

## 4.2 `/rts/teste_info`

### Objetivo

Testar o recebimento de informações enviadas para a API.

### Função

Recebimento e processamento de informações.

### Exemplo

```http
POST /rts/teste_info
```

### Dados

Os dados enviados dependem da implementação atual da rota.

---

## 4.3 `/rta/login`

### Objetivo

Realizar a autenticação do usuário.

A rota é responsável por:

1. Receber as informações de login;
2. Verificar as credenciais;
3. Comparar a senha recebida com o hash armazenado;
4. Criar um token caso a autenticação seja válida;
5. Retornar o token para o cliente.

### Exemplo

```http
POST /rta/login
```

### Fluxo

```text
Cliente
   │
   ▼
/rta/login
   │
   ▼
Verificação das credenciais
   │
   ├── Credenciais inválidas
   │       │
   │       ▼
   │    Acesso negado
   │
   └── Credenciais válidas
           │
           ▼
       Criação do token
           │
           ▼
       Token retornado
```

---

## 4.4 `/rta/tk_verificacao`

### Objetivo

Verificar se o token fornecido pelo usuário é válido.

Essa rota faz parte do mecanismo de proteção dos recursos da API.

### Exemplo

```http
GET /rta/tk_verificacao
Authorization: Bearer <TOKEN>
```

### Fluxo

```text
Cliente
   │
   ▼
Envia requisição + Token
   │
   ▼
Verificação do token
   │
   ├── Token inválido
   │       │
   │       ▼
   │    Acesso negado
   │
   └── Token válido
           │
           ▼
       Acesso permitido
```

---

# 5. Controle de requisições

A API utiliza o mecanismo `@app.before_request`.

Esse mecanismo permite executar uma função **antes do processamento de cada requisição**.

Dessa forma, cada rota acessada passa primeiro pelo controle definido no `before_request`.

Exemplo conceitual:

```python
@app.before_request
def before_request():
    # Verificações realizadas antes da rota
    pass
```

O objetivo é centralizar verificações de segurança que devem ocorrer antes do processamento das rotas.

Entre essas verificações podem estar:

* Limitação de requisições;
* Verificação de autenticação;
* Verificação de token;
* Controle de acesso;
* Bloqueio de requisições suspeitas.

---

# 6. Fluxo de autenticação

O fluxo de autenticação da API atualmente funciona da seguinte maneira:

```text
                 ┌───────────────┐
                 │    Cliente    │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │    /login     │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ Verificar     │
                 │ credenciais   │
                 └───────┬───────┘
                         │
                    ┌────┴────┐
                    │         │
                  Inválido   Válido
                    │         │
                    ▼         ▼
                 Bloqueia   Cria token
                              │
                              ▼
                         Cliente recebe
                            token
                              │
                              ▼
                      Requisição protegida
                              │
                              ▼
                      Verificação do token
                              │
                         ┌────┴────┐
                         │         │
                       Inválido   Válido
                         │         │
                         ▼         ▼
                      Bloqueia   Permite
                                  acesso
```

---

# 7. Segurança implementada

## 7.1 Hash de senha

A API possui implementação para criação de hash das senhas.

O objetivo é evitar o armazenamento das senhas em texto puro.

Fluxo:

```text
Senha do usuário
       │
       ▼
Criação do hash
       │
       ▼
Banco de dados
```

Durante o login:

```text
Senha informada
       │
       ▼
Comparação com hash armazenado
       │
       ▼
Credenciais válidas?
```

---

## 7.2 Tokens

Após a autenticação, a API cria um token para identificar e autorizar o usuário.

Esse token deverá ser enviado nas requisições que exigem autenticação.

Exemplo:

```http
Authorization: Bearer <TOKEN>
```

---

## 7.3 Verificação de token

As rotas protegidas deverão verificar o token antes de permitir o acesso.

```text
Requisição
    │
    ▼
Token existe?
    │
    ├── Não ──► Acesso negado
    │
    └── Sim
          │
          ▼
     Token válido?
          │
      ┌───┴───┐
      │       │
     Não     Sim
      │       │
      ▼       ▼
   Negado   Permitir
             acesso
```

---

# 8. Limitação de requisições

A API já possui um mecanismo de **limitação de requisições**.

O objetivo é impedir que um cliente envie uma quantidade excessiva de requisições em um determinado período.

Essa camada faz parte do sistema de segurança da API.

Status atual:

**Implementado e funcionando.**

---

# 9. Status atual do projeto

| Funcionalidade                                       | Status                |
| ---------------------------------------------------- | --------------------- |
| Criação de hash de senha                             | ✅ Funcionando         |
| Verificação de hash                                  | ✅ Funcionando         |
| Login                                                | ✅ Funcionando         |
| Criação de token                                     | ✅ Funcionando         |
| Verificação de token                                 | ✅ Funcionando         |
| Proteção de rotas com token                          | ✅ Funcionando         |
| Limitação de requisições                             | ✅ Funcionando         |
| Controle de acesso por tipo de usuário               | 🚧 Em desenvolvimento |
| Controle de acesso antes da criação do token         | 🚧 Em desenvolvimento |
| Controle de acesso após criação/verificação do token | 🚧 Em desenvolvimento |
| Gerenciamento de recursos                            | 🚧 Planejado          |
| Dashboard                                            | 🚧 Planejado          |

---

# 10. Próximos passos

## Segurança e autenticação

* [ ] Definir níveis de acesso dos usuários;
* [ ] Criar sistema de permissões;
* [ ] Diferenciar funcionários, gerentes e administradores;
* [ ] Limitar acesso às rotas de acordo com o nível do usuário;
* [ ] Definir quais verificações devem ocorrer antes do login;
* [ ] Definir quais verificações devem ocorrer depois da autenticação;
* [ ] Melhorar o controle de expiração dos tokens;
* [ ] Registrar tentativas de acesso.

## Gestão de recursos

* [ ] Criar CRUD de equipamentos;
* [ ] Criar CRUD de veículos;
* [ ] Criar CRUD de dispositivos de segurança;
* [ ] Implementar controle de permissões para alteração dos recursos;
* [ ] Criar sistema de consulta dos recursos.

## Dashboard

* [ ] Criar interface do dashboard;
* [ ] Exibir usuários ativos;
* [ ] Exibir recursos cadastrados;
* [ ] Exibir atividades recentes;
* [ ] Exibir eventos de segurança;
* [ ] Integrar dashboard com a API.

---

# 11. Testes no Postman

Os testes da API estão sendo realizados utilizando o Postman.

### Requisição 1

[Abrir requisição no Postman — teste 1](https://solotv-3391511.postman.co/workspace/Final-Project-Infinity~9360ac56-9360-4842-b265-15c6250018a6/request/47017727-31766f6b-7b18-4299-863f-2130fa482d06?action=share&creator=47017727&utm_source=chatgpt.com)

### Requisição 2

[Abrir requisição no Postman — teste 2](https://solotv-3391511.postman.co/workspace/Final-Project-Infinity~9360ac56-9360-4842-b265-15c6250018a6/request/47017727-ccd91219-97ca-4fbb-8933-6b521be7358b?action=share&creator=47017727&utm_source=chatgpt.com)

---

# 12. Resumo do desenvolvimento

Até o momento, os principais mecanismos de segurança da API foram implementados e testados.

### Funcionando

* Criação de hash;
* Verificação de senha através do hash;
* Autenticação;
* Criação de tokens;
* Verificação de tokens;
* Proteção de rotas;
* Limitação de requisições.

### Próximo foco

O próximo objetivo é aprimorar o **controle de acesso**, principalmente a definição de permissões antes e depois da autenticação.

A API deverá futuramente trabalhar com diferentes níveis de usuário e permissões específicas para cada recurso.

---

# 13. Autor

**Desenvolvido por Pablo.**















