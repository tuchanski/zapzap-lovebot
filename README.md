# 💌 WhatsApp LoveBot

Um bot simples, fofo e automatizado que usa inteligência artificial para gerar mensagens carinhosas e enviá-las pelo WhatsApp. Ideal para impressionar sua namorada.

---

## ✨ O que ele faz?

1. Gera uma mensagem fofa usando o modelo **LLaMA 3** local via **Ollama**
2. Exibe a mensagem gerada na interface web com Flask
3. Permite enviar a mensagem instantaneamente via **WhatsApp Web** com **pywhatkit**

---

## 🛠️ Tecnologias usadas

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Ollama](https://ollama.com) (executando o modelo `llama3.1:8b` localmente)
- [pywhatkit](https://pypi.org/project/pywhatkit/) para automação do WhatsApp
- HTML + CSS (Jinja2 template)

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/tuchanski/whatsapp-lovebot
cd whatsapp-lovebot
```

2. Instale as dependências:

```bash
pip install flask pywhatkit
```

3. Certifique-se de que o Ollama está instalado e rodando:

```bash
ollama run llama3.1:8b
```

> ⚠️ Use o modelo `llama3.1:8b` corretamente nomeado conforme seu Ollama local.

---

## 🚀 Executando

Execute a aplicação:

```bash
python app.py
```

Abra no navegador:

```
http://127.0.0.1:5000/
```

O bot irá:
- Gerar uma mensagem fofa com IA
- Mostrar a mensagem na interface web
- Permitir o envio instantâneo para o número informado

---

## 📸 Exemplo de uso

<img src="img\whatsapp_lovebot.png" alt="Exemplo de Uso">

---

## ⚠️ Avisos

- O `pywhatkit` abre o WhatsApp Web automaticamente no navegador.
- Você precisa estar logado no WhatsApp Web para que funcione.
- Use com responsabilidade e carinho.

---

## 📄 Autor

Feito com amor por [Tuchanski](https://github.com/tuchanski) 💕
