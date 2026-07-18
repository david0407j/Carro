import os
from google import genai

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_car_bio(model, brand, year):
    prompt = f"""
Gere uma descrição detalhada e envolvente do carro com base nos dados:

Marca: {brand}
Modelo: {model}
Ano: {year}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
