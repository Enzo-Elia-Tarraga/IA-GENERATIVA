# 🌦️ AgroAlert — Sistema de Alertas Climáticos para Agricultores

> Sistema de alertas climáticos inteligentes para pequenos agricultores brasileiros, utilizando dados reais de satélites meteorológicos analisados por IA Generativa.

---

## 📋 Sobre o Projeto

O **AgroAlert** é uma solução desenvolvida para a disciplina **Disruptive Architectures: IoT, IOB & Generative IA** da FIAP, como parte da Global Solution 2026-1.

O sistema coleta dados climáticos em tempo real por meio da Open-Meteo API e utiliza Inteligência Artificial Generativa para transformar informações meteorológicas em alertas claros e acessíveis para pequenos agricultores brasileiros.

### 💡 Problema que Resolve

Pequenos agricultores frequentemente não possuem acesso rápido a informações climáticas precisas e personalizadas para sua região. O AgroAlert busca democratizar esse acesso, convertendo dados técnicos em recomendações simples e práticas para auxiliar na tomada de decisões relacionadas ao plantio, irrigação e colheita.

---

## 🏗️ Arquitetura da Solução

```text
Satélites Meteorológicos
        ↓
   Open-Meteo API
        ↓
   Backend Python
        ↓
IA Generativa (LLaMA 3.3 via Groq)
        ↓
 Interface Gradio
        ↓
     Agricultor
```

### 📝 Explicação da Arquitetura

O AgroAlert utiliza dados climáticos reais provenientes de satélites meteorológicos, disponibilizados através da Open-Meteo API. Essas informações são processadas pelo backend desenvolvido em Python, que organiza os dados e monta um contexto para análise.

Em seguida, os dados são enviados para o modelo de Inteligência Artificial Generativa LLaMA 3.3, acessado através da Groq API. A IA interpreta as condições climáticas e gera alertas personalizados em linguagem natural.

Por fim, os resultados são exibidos na interface web desenvolvida com Gradio, permitindo que o agricultor visualize o nível de risco climático, os principais riscos identificados, recomendações práticas e orientações para plantio ou colheita.

## OS PRINTS DO PROJETO ESTÃO NA PASTA IMAGE


## 🚀 Como Executar o Projeto

### Pré-requisitos

* Python 3.11 ou superior

### 1. Clonar o Repositório

```bash
git clone https://github.com/SEU_USUARIO/agroalert.git
cd agroalert
```

### 2. Criar e Ativar o Ambiente Virtual

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

```bash
python main.py
```

A interface ficará disponível no navegador:

```text
http://127.0.0.1:7860
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia     | Função                  |
| -------------- | ----------------------- |
| Python 3.11    | Linguagem principal     |
| Gradio         | Interface web           |
| Open-Meteo API | Dados climáticos        |
| Groq API       | Inferência de IA        |
| LLaMA 3.3 70B  | Modelo de IA Generativa |
| GitHub         | Versionamento           |

---

## 🌍 Cidades Suportadas

| Cidade         | Estado | Região Agrícola          |
| -------------- | ------ | ------------------------ |
| Ribeirão Preto | SP     | Cana-de-açúcar e Laranja |
| Sorriso        | MT     | Soja e Milho             |
| Passo Fundo    | RS     | Trigo e Soja             |
| Barreiras      | BA     | Soja e Algodão           |
| Unaí           | MG     | Soja e Milho             |
| Cascavel       | PR     | Soja e Trigo             |
| Dourados       | MS     | Soja e Milho             |
| Petrolina      | PE     | Fruticultura Irrigada    |

---

## 📁 Estrutura do Projeto

```text
agroalert/
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🎯 Conexão com Tecnologia Espacial

Os dados climáticos utilizados pelo AgroAlert são provenientes de satélites meteorológicos que monitoram continuamente a atmosfera terrestre. A Open-Meteo API disponibiliza essas informações de forma gratuita, permitindo que sejam utilizadas em aplicações de impacto social.

Dessa forma, o AgroAlert transforma dados espaciais em conhecimento prático para agricultores, conectando tecnologia, sustentabilidade e inovação.

---

## 🤖 Inteligência Artificial Generativa

O AgroAlert utiliza o modelo LLaMA 3.3 70B, acessado através da Groq API.

A Inteligência Artificial recebe dados meteorológicos reais e uma pergunta opcional do agricultor. Com base nessas informações, gera respostas personalizadas contendo:

* Nível de risco climático;
* Principal ameaça identificada;
* Recomendações práticas;
* Orientações para plantio e colheita.

As respostas são produzidas em linguagem natural, facilitando a compreensão por usuários sem conhecimento técnico.

---

## 📽️ Vídeo de Demonstração

🎬 https://youtu.be/pyl7Oz2sV9M

---

## 👥 Integrantes

| Nome                    | RM     |
| ----------------------- | ------ |
| Enzo Elia Tarraga       | 560901 |
| Rafael Terra Teodoro    | 560955 |
| Otoniel Arantes Barbado | 560112 |
| Ranaldo Jose da Silva   | 559210 |
| Fabricio Jose da Silva  | 560694 |

**Turma:** 2TDSZ

---

## 📄 Licença

Este projeto foi desenvolvido exclusivamente para fins acadêmicos na disciplina **Disruptive Architectures: IoT, IOB & Generative IA**, da FIAP, como parte da Global Solution 2026-1.
