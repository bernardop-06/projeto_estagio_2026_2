# Chamados Helpdesk

Sistema de chamados helpdesk e suporte de TI;

Um sistema com página pública onde qualquer um pode abrir um chamado, categorizando-o e detalhando o problema;
Página de painel protegido com login onde é possível visualizar todos os chamados e alterar o seu estado(Pendente, Concluído e Cancelado);

---

## Pré-requisitos

- Python 3.10 ou superior (desenvolvido e testado com 3.11.9)
- Git

Nenhum banco de dados precisa ser instalado. O projeto usa SQLite, que é um arquivo
criado automaticamente dentro da pasta do projeto.

---

## Como rodar

### 1. Clonar o repositório

```bash
git clone https://github.com/bernardop-06/projeto_estagio_2026_2
cd <projeto_estagio_2026_2>
```

### 2. Criar e ativar o ambiente virtual

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (Prompt de Comando):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Se o PowerShell recusar a execução do script, libere apenas para esta janela:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Com o ambiente ativo, o início da linha do terminal passa a mostrar `(.venv)`.

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Criar o banco de dados

```bash
python manage.py migrate
```

Este comando cria o arquivo `db.sqlite3` com todas as tabelas. O banco não vem no
repositório de propósito — cada pessoa gera o seu, vazio.

### 5. Criar o usuário da equipe de suporte

```bash
python manage.py createsuperuser
```

Informe um nome de usuário e uma senha. O campo de e-mail pode ficar em branco.
É com esse usuário que se acessa o painel.

### 6. Rodar o servidor

```bash
python manage.py runserver
```

Acesse o link fornecido no terminal

---

## Como usar

| Página | Endereço | Acesso |
|---|---|---|
| Abertura de chamado | `/` | Público |
| Confirmação de envio | `/enviado/` | Público |
| Login da equipe | `/login/` | Público |
| Painel de chamados | `/painel/` | Exige login |

Para abrir um chamado, preencha o formulário na página inicial. Para acompanhar os
chamados, clique em **Acesso da equipe** no cabeçalho e entre com o usuário criado no
passo 5.

No painel é possível ver todos os chamados, ordenados do problema mais antigo para o
mais recente, e alterar o status de cada um.

---

## Estrutura dos dados

Cada chamado registra:

| Campo | Observação |
|---|---|
| Nome | Obrigatório |
| E-mail | Obrigatório, validado |
| Categoria | Quatro opções, incluindo "Não sei identificar" |
| Data de início do problema | Obrigatória, não pode ser futura |
| Hora aproximada de início | Opcional |
| Descrição | Obrigatória |
| Status | `pendente`, `confirmado` ou `cancelado` — nasce sempre como `pendente` |

O raciocínio por trás dessas escolhas está em [DECISOES.md](DECISOES.md).

---

## Tecnologias

- Python 3.11
- Django 5.2
- SQLite
- Tailwind CSS via CDN

