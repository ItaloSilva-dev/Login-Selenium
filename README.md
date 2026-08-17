#  Automação de Login com Selenium e Python

Projeto desenvolvido para automatizar o processo de autenticação (login) em uma plataforma web, utilizando **Python** e **Selenium WebDriver**. O objetivo principal é demonstrar boas práticas de automação de testes, organização de código e configuração de ambiente profissional.

##  Tecnologias e Ferramentas Utilizadas

* **Python 3** (Linguagem base)
* **Selenium WebDriver** (Automação do navegador)
* **Virtualenv (venv)** (Isolamento do ambiente)
* **Git & GitHub** (Controle de versão e documentação)

##  Boas Práticas Aplicadas

* **Ambiente Isolado (`.venv`):** Todas as dependências do projeto ficam restritas a este diretório, evitando conflitos com o sistema global.
* **Segurança de Arquivos (`.gitignore`):** Configurado para não expor os arquivos da `venv` e dados sensíveis.
* **Lista de Dependências (`requirements.txt`):** Gerada automaticamente para facilitar a instalação correta do projeto em outras máquinas.

##  Como Instalar e Rodar o Projeto

Siga os passos abaixo para executar a automação no seu computador:

### 1. Clonar o Repositório
```bash
git clone https://github.com
cd Login-Selenium
```

### 2. Criar e Ativar o Ambiente Virtual
* **Windows (PowerShell):**
  ```powershell
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
* **Linux/Mac:**
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```

### 3. Instalar as Dependências
Com a venv ativa, instale o Selenium usando o arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Executar a Automação
```bash
python login.py
```

---
Feito com 💻 por [Seu Nome](https://github.com)
