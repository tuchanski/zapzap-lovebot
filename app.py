import pywhatkit
import ollama

def get_topic_behavior():
    behavior = "Você está respondendo sua namorada. Seja o mais genérico possível. Envie uma mensagem fofa." # Mude conforme necessidade
    return behavior

def generate_response(prompt: str, model="llama3.1:8b") -> str:
    response = ollama.chat(model="llama3.1:8b", messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content'].replace("\"", "")

def send_whatsapp_message(number_target: str, message: str):
    pywhatkit.sendwhatmsg_instantly(number_target, message)

target = "" # +55(DDD)9XXXXXXXX 

prompt = get_topic_behavior()
response = generate_response(prompt)

print("Enviando: " + response)

send_whatsapp_message(target, response)