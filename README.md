# 🌊 Controle de Níveis de Água

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)

Sistema de monitoramento de reservatório desenvolvido para exibir alertas visuais no terminal utilizando cores para identificar o nível de água e possíveis riscos.

## 📝 Descrição do Projeto

Este projeto simula o monitoramento de um reservatório de água. O sistema processa diferentes níveis de preenchimento e utiliza a biblioteca **Colorama** para destacar mensagens de status com cores específicas (Vermelho, Amarelo, Verde, Ciano e Azul), facilitando a leitura rápida de situações críticas ou de alerta.

### 🚀 Funcionalidades

*   ✅ Armazenamento de mensagens em listas estruturadas.
*   ✅ Função dedicada para gestão de cores por nível.
*   ✅ Simulação visual de 5 níveis de alerta.
*   ✅ Limpeza de estilo (reset) após a execução para manter a integridade do terminal.

---

## 🛠️ Tecnologias Utilizadas

*   **Python 3.x**
*   **Colorama**: Biblioteca para estilização de texto no terminal.

---

## 🏗️ Tabela de Níveis e Cores

| Nível | Situação | Cor Sugerida |
| :--- | :--- | :--- |
| **Nível 1** | Muito baixo (crítico) | 🔴 Vermelho |
| **Nível 2** | Baixo | 🟡 Amarelo |
| **Nível 3** | Médio | 🟢 Verde |
| **Nível 4** | Alto | 🔵 Ciano |
| **Nível 5** | Muito alto (alerta) | 🔵 Azul |

---

## 🔧 Como Executar o Projeto

### 1. Clonagem e Execução
```bash
# Clone o repositório
git clone [https://github.com/hugoarcanjodev/controle-de-niveis-de-agua.git](https://github.com/hugoarcanjodev/controle-de-niveis-de-agua.git)

# Acesse a pasta
cd controle-de-niveis-de-agua

# Execute o sistema
python app.py
```

### 2. Em casos de erro do Python
Certifique-se de ter o Python instalado em sua máquina.

Criar e ativar o ambiente virtual (venv)
```bash
# Criar
python -m venv venv

# Ativar (Windows)
.\venv\Scripts\activate
```

### 3. Instalação da Biblioteca
No terminal, instale o `colorama` via pip:
```bash
pip install colorama
```

### 4. Erros de coloração
Importe o `init` do `colorama` no inicio do programa, chame o init logo abaixo e antes da lógica do programa:
```bash
from colorama import Fore, Style, init
init() # Isso garante que as cores funcionem em qualquer sistema operacional
```

---

## 📁 Estrutura de Arquivos

- `app.py`: Arquivo principal com a lógica do sistema.
- `.gitignore`: Define arquivos e pastas ignorados pelo Git (como __pycache__).
- `README.md`: Documentação completa do projeto.

## 👨‍💻 Desenvolvedor

[Hugo Arcanjo](https://github.com/hugoarcanjodev)

## ⚖️ Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT).