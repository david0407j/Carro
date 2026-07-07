import os
from google import genai

client = genai.Client(api_key="AQ.Ab8RN6LYHTHtf0d6WgT9sXGETJ6D1zdwu9qzozErmsp8-9zFjg")


def get_car_bio(model, brand, year):
    prompt = f"""
    ME Mostrando informações sobre um veículo, gere uma descrição detalhada e envolvente do carro com base nos seguintes dados:
Dados do Veículo:
 {brand}
{model}
{year}
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
