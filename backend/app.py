from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

import os

app = Flask(__name__)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

CORS(app) # Libera rotas pro front se comunicar com o back

# Core do Programa

def generate_response(tags: list[str] = None) -> str:
    tags_text = ""

    if tags:
         tags_text = " ".join([f"[{tag}]" for tag in tags])

    prompt = (
        f"Máximo 60 palavras."
        f"Você mandará uma mensagem fofa para sua namorada."
        f"Seja o mais genérico possível."
        f"{tags_text}"
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ], model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content.replace("\"", "")

def send_whatsapp_message(number_target: str, message: str):
    import pywhatkit

    number_target_filtered = ""
    response_filtered = ""

    for key, value in number_target.items():
        number_target_filtered = value

    for key, value in message.items():
        response_filtered = value
    
    try:
        pywhatkit.sendwhatmsg_instantly(number_target_filtered, response_filtered)
        print("Mensagem enviada com sucesso. <3")

    except Exception as e:
        print("Erro ao enviar mensagem: ", e)

# Rotas

@app.route("/generate", methods=["GET"])
def generate():
    tags_param = request.args.get("tags")
    tags_list = tags_param.split(",") if tags_param else []
    print(tags_list)
    return jsonify({"response": generate_response(tags_list)})

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    number = data.get("numberTarget")
    message = data.get("aiResponse")
    send_whatsapp_message(number, message)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
