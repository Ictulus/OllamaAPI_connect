from api import OllamaRestApi


class ConsoleChat:
    _api : OllamaRestApi
    def __init__(self, uri: str, model: str):
        self._api = OllamaRestApi(uri=uri, model=model)

    def start_conversation(self):
        print("Chat with the Llama API. Type in /exit to end the conversation.")
        while True:
            user_input = input()
            if user_input.strip() == "/exit":
                break

            print("Llama:", end=" ", flush=True)
            for part in self._api.send_message(user_input):
                print(part, end="", flush=True)
            print()
