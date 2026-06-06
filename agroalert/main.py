import requests
import gradio as gr
from groq import Groq

cliente = Groq(api_key="CHAVE-API")

CIDADES = {
    "Ribeirão Preto - SP": (-21.17, -47.81),
    "Sorriso - MT":        (-12.54, -55.72),
    "Passo Fundo - RS":    (-28.26, -52.41),
    "Barreiras - BA":      (-12.15, -44.99),
    "Unaí - MG":           (-16.36, -46.90),
    "Cascavel - PR":       (-24.96, -53.46),
    "Dourados - MS":       (-22.22, -54.81),
    "Petrolina - PE":      (-9.39,  -40.50),
}

def buscar_clima(lat, lon):
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        "&daily=precipitation_sum,temperature_2m_max,"
        "temperature_2m_min,windspeed_10m_max"
        "&timezone=America/Sao_Paulo&forecast_days=3"
    )
    d = requests.get(url, timeout=10).json()["daily"]
    return d

def gerar_alerta(cidade, pergunta_extra=""):
    lat, lon = CIDADES[cidade]
    c = buscar_clima(lat, lon)

    contexto_extra = (
        f"\nPergunta específica do agricultor: {pergunta_extra}\nResponda essa pergunta diretamente no início da resposta, antes do alerta geral."
        if pergunta_extra.strip() else ""
    )

    prompt = f"""
Você é o AgroAlert, assistente climático para pequenos agricultores brasileiros.
Analise os dados climáticos abaixo e responda de forma clara e direta.

Localidade: {cidade}
Previsão para os próximos 3 dias (dados de satélite via Open-Meteo):
- {c['time'][0]}: chuva {c['precipitation_sum'][0]}mm | máx {c['temperature_2m_max'][0]}°C | vento {c['windspeed_10m_max'][0]}km/h
- {c['time'][1]}: chuva {c['precipitation_sum'][1]}mm | máx {c['temperature_2m_max'][1]}°C | vento {c['windspeed_10m_max'][1]}km/h
- {c['time'][2]}: chuva {c['precipitation_sum'][2]}mm | máx {c['temperature_2m_max'][2]}°C | vento {c['windspeed_10m_max'][2]}km/h
{contexto_extra}

Responda com essa estrutura exata:

💬 RESPOSTA: [responda diretamente a pergunta do agricultor com base nos dados climáticos, ou escreva "Nenhuma dúvida enviada" se não houver pergunta]

🔴🟡🟢 RISCO: [ALTO / MÉDIO / BAIXO] — [motivo em uma frase]

⚠️ ATENÇÃO: [principal risco climático nos próximos dias]

✅ AÇÕES:
1. [ação prática 1]
2. [ação prática 2]
3. [ação prática 3]

🌱 MELHOR DIA: [indique o melhor dia dos 3 para plantar ou colher e por quê]

Use linguagem simples, direta e rural brasileira.
"""

    resposta = cliente.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    return resposta.choices[0].message.content

def interface(cidade, pergunta):
    try:
        return gerar_alerta(cidade, pergunta)
    except Exception as e:
        return f"Erro ao gerar alerta: {e}"

app = gr.Interface(
    fn=interface,
    inputs=[
        gr.Dropdown(
            choices=list(CIDADES.keys()),
            label="Sua cidade",
            value="Ribeirão Preto - SP"
        ),
        gr.Textbox(
            label="Dúvida extra (opcional)",
            placeholder="Ex: posso plantar milho amanhã?",
            lines=2
        ),
    ],
    outputs=gr.Textbox(
        label="Alerta AgroAlert — gerado por IA",
        lines=20
    ),
    title="🌦️ AgroAlert — Alertas Climáticos para Agricultores",
    description="Dados reais de satélites meteorológicos analisados por IA generativa.",
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    app.launch()