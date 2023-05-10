import openai

# Define a chave de API do OpenAI
openai.api_key = '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'

def generate_response(prompt):
    model_engine = "text-davinci-003"
    prompt = (f"{prompt}")

    # Cria uma solicitação de conclusão de texto usando a biblioteca openai
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Obtém a resposta gerada pela IA
    message = completions.choices[0].text
    return message.strip()

# Solicita ao usuário para fornecer uma pergunta
prompt = input("Coloque sua pergunta aqui: ")

# Gera uma resposta com base na pergunta fornecida
response = generate_response(prompt)

# Imprime a resposta gerada
print(response)
