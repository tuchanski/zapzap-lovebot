from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from groq import Groq

app = Flask(__name__)
CORS(app)

tags = [
    "fofo", "apaixonado", "saudade",
      "reconfortar", "bom-dia", "boa-noite",
        "aleatorio", "emoji"]

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def generate_response(tags: list[str] = None) -> str:

    tags_text = ""

    if tags:
         tags_text = " ".join([f"[{tag}]" for tag in tags])

    prompt = (
        f"Você está respondendo sua namorada. "
        f"Seja o mais genérico possível. Envie uma mensagem fofa. "
        f"{tags_text}"
    )

    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
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
    tags_param = request.args.get("tags")
    tags_list = tags_param.split(",") if tags_param else []
    print(tags_list)
    valid_tags = [tag for tag in tags_list if tag in tags]
    return jsonify({"response": generate_response(valid_tags)})

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    number = data.get("numberTarget")
    message = data.get("aiResponse")
    send_whatsapp_message(number, message)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
