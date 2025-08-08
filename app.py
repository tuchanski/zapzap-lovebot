from flask import Flask, render_template, request
import ollama

app = Flask(__name__)

def generate_response(prompt: str, model="llama3.1:8b") -> str:
    response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content'].replace("\"", "")

def send_whatsapp_message(number_target: str, message: str):
    import pywhatkit
    pywhatkit.sendwhatmsg_instantly(number_target, message)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    prompt = "Você está respondendo sua namorada. Seja o mais genérico possível. Envie uma mensagem fofa."
    numero = ""

    if request.method == "POST":
        action = request.form["action"]
        numero = request.form.get("numero")

        if action == "generate":
            response = generate_response(prompt)
        elif action == "send":
            response = request.form.get("response")
            send_whatsapp_message(numero, response)

    return render_template("index.html", response=response, numero=numero)

if __name__ == "__main__":
    app.run()