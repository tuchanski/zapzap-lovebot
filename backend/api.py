from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from groq import Groq

app = Flask(__name__)
CORS(app)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def generate_response() -> str:
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Você está respondendo sua namorada. Seja o mais genérico possível. Envie uma mensagem fofa.",
        }
    ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content.replace("\"", "")

def send_whatsapp_message(number_target: str, message: str):
    import pywhatkit
    number_target_dict = ""
    response_dict = ""

    for key, value in number_target.items():
        number_target_dict = value

    for key, value in message.items():
        response_dict = value
    
    try:
        pywhatkit.sendwhatmsg_instantly(number_target_dict, response_dict)
    except Exception as e:
        print(e)

@app.route("/generate", methods=["GET"])
def generate():
    return jsonify({"response": generate_response()})

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    number = data.get("numberTarget")
    message = data.get("aiResponse")
    send_whatsapp_message(number, message)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
