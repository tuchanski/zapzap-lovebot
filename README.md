# whatsapp-lovebot 💌🤖

Um bot simples, fofo e automatizado que usa inteligência artificial para gerar mensagens carinhosas e enviá-las pelo WhatsApp. Ideal para impressionar sua namorada.

## ✨ O que ele faz?

1. Gera uma mensagem fofa usando o modelo **LLaMA 3** local via **Ollama**
2. Envia a mensagem instantaneamente via **WhatsApp Web** usando a biblioteca **pywhatkit**

## 🛠️ Tecnologias usadas

- [Python 3.10+](https://www.python.org/)
- [Ollama](https://ollama.com) (executando o modelo `llama3.1:8b` localmente)
- [pywhatkit](https://pypi.org/project/pywhatkit/) para automação do WhatsApp

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/tuchanski/whatsapp-lovebot
cd whatsapp-lovebot
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Certifique-se de que o Ollama está instalado e rodando:

```bash
ollama run llama3.1:8b
```

4. Edite o número de destino no código:

```python
target = "+55DDD9XXXXXXXX"
```

> Use o formato internacional (com DDI `+55`, DDD, e número com 9 dígitos)

## 🚀 Executando

Execute o script:

```bash
python app.py
```

O bot irá:
- Gerar uma mensagem fofa via IA
- Mostrar o texto gerado no terminal
- Abrir o WhatsApp Web e enviar a mensagem instantaneamente

## 🧠 Exemplo de saída

```
Enviando: Você é a melhor parte dos meus dias. Te amo ❤️
```

## ⚠️ Aviso importante

- A automação usa o navegador para enviar a mensagem. Tenha o WhatsApp Web logado.
- Evite spam. Use com responsabilidade e carinho.
- As mensagens são **geradas automaticamente por IA**, revise se necessário.

## 📄 Autor

Feito com amor por [Tuchanski](https://github.com/tuchanski) 💕
