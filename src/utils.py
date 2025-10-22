import requests


API_KEY = "AIzaSyA3Vwmdu5hwncVkn8r_lwxGyWAG_Qu4Rhg"


API_URL ="https://generativelanguage.googleapis.com/v1beta/models/gemini-1.0-flash:generateContent"

def send_to_gemini(mensaje):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": mensaje}
                ]
            }
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        resultado = response.json()
        print("Respuesta de Gemini:")
        print(resultado["candidates"][0]["content"]["parts"][0]["text"])
    except requests.exceptions.HTTPError as err:
        print(f" Error HTTP: {err.response.status_code}")
        print(err.response.json())
    except Exception as e:
        print(f"Error inesperado: {e}")