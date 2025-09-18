
# 🚀 Step by Step Flask

Este repositório contém uma coleção de exercícios práticos em **Flask**, desenvolvidos passo a passo para aprender os conceitos fundamentais de rotas, templates e formulários em aplicações web com Python.

## 📂 Estrutura do Projeto

Os exercícios estão organizados por etapas (1 a 4), cada uma cobrindo novos conceitos:

### 🔹 Etapa 1 — Rotas Básicas
- **`1.3_flask.py`** → Rotas dinâmicas com parâmetros (`/saudacao/<nome>`):contentReference[oaicite:2]{index=2}  
- **`1.4_flask.py`** → Rota com tipagem de número e cálculo do dobro (`/dobro/<int:numero>`):contentReference[oaicite:3]{index=3}

### 🔹 Etapa 2 — Introdução a Templates HTML
- **`2.1_flask.py`** → Renderização de HTML com `render_template`:contentReference[oaicite:4]{index=4}  
- **`2.2_flask.py`** → Links de navegação entre rotas usando `url_for`:contentReference[oaicite:5]{index=5}

### 🔹 Etapa 3 — Variáveis e Estruturas de Controle no Jinja
- **`3.1_flask.py`** → Passagem de variáveis para templates (`{{ nome }}`):contentReference[oaicite:6]{index=6}  
- **`3.2_flask.py`** → Listas e loops em templates (`for` em `<ul>`):contentReference[oaicite:7]{index=7}  
- **`3.3_flask.py`** → Condicionais (`if`) em templates para verificar idade:contentReference[oaicite:8]{index=8}

### 🔹 Etapa 4 — Formulários e Validações
- **`4.1_flask.py`** → Formulário simples que recebe o nome e retorna uma saudação:contentReference[oaicite:9]{index=9}  
- **`4.2_flask.py`** → Formulário que soma dois números:contentReference[oaicite:10]{index=10}  
- **`4.3_flask.py`** → Validação de entrada: garante que os campos sejam números válidos:contentReference[oaicite:11]{index=11}

---

## 🛠️ Tecnologias Utilizadas
- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- HTML + Jinja2

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/step_by_step_flask.git
   cd step_by_step_flask


2. Crie um ambiente virtual e instale o Flask:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / Mac
   venv\Scripts\activate      # Windows
   pip install flask


3. Execute qualquer arquivo de exemplo:

   ```bash
   python 3.2_flask.py


4. Abra no navegador:

   ```
   http://127.0.0.1:5000/


## 🎯 Objetivo

Este repositório serve como um **guia prático de aprendizado** para quem deseja começar com Flask, construindo aplicações web passo a passo — do **"Hello World"** até **formulários com validação**.

✨ Desenvolvido com dedicação por [Johnny]([https://github.com/TJfiles]).


