import json

import requests

class OllamaRestApi:
    _headers = {"Content-Type": "application/json"}

    def __init__(self, uri: str, model: str):
        self.uri = f"{uri}/api/chat"
        self.model = model

    def send_message(self, message: str):
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": message}],
            "stream": True
        }

        response = requests.post(
            url=self.uri,
            headers=self._headers,
            data=json.dumps(payload),
            stream=True
        )

        if response.status_code != 200:
            yield f"[Fehler vom Server: {response.status_code}] {response.text}"
            return

        for line in response.iter_lines():
            if not line:
                continue
            try:
                chunk = json.loads(line.decode("utf-8"))
                if chunk.get("done"):
                    break
                content = chunk.get("message", {}).get("content", "")
                if content:
                    yield content
            except json.JSONDecodeError as e:
                yield f"\n[JSON Fehler]: {e}"


if __name__ == '__main__':
    chat = OllamaRestApi(uri="http://localhost:11434", model="llama3.2:1b")
    print(chat.send_message("Hello World!"))