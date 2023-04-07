import openai

API_KEY = open("API_KEY", "r").read()
openai.api_key = API_KEY

chat_log = []

while(True):
    user_message = input()
    if user_message.lower() == "quit":
        break
    else:
        chat_log.append({"role" : "user", "content" : user_message})
        responce = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = chat_log
        )
    ass_responce = responce['choices'][0]['message']['content']
    print("chatgpt:", ass_responce.strip("\n").strip())
    chat_log.append({"role" : "assistant", "content" : ass_responce.strip("\n").strip()})