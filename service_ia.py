import requests


class ia_google:

    def __init__(self, api_key):
        self.api_key = api_key

    def generate_story(self, text, history=[]):
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": 'quero que todas as suas respostas passem por isso aqui     replacements = {        "**": "*",  # Negrito        "__": "*",  # Itálico        "\n\n": "\n",  # Remover linhas em branco extras    }'
                        }
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        {
                            "text": 'Ok, a partir de agora, todas as minhas respostas passarão pelas regras de substituição que você definiu. \n replacements = {        "**": "*",  # Negrito        "__": "*",  # Itálico        "\n\n": "\n",  # Remover linhas em branco extras    }\n\nComo posso te ajudar?'
                        }
                    ],
                },
            ]
            + history
            + [
                {
                    "role": "user",
                    "parts": [
                        {"text": text},
                    ],
                }
            ],
            "generationConfig": {
                "temperature": 1,
                "topK": 0,
                "topP": 0.95,
                "maxOutputTokens": 8192,
                "stopSequences": [],
            },
            "safetySettings": [
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
                },
            ],
        }
        params = {"key": self.api_key}

        response = requests.post(url, headers=headers, json=payload, params=params)

        if response.status_code == 200:
            temp = response.json()
            return temp["candidates"][0]["content"]["parts"][0]["text"]
        else:
            print("Error:", response.status_code)
            return None
