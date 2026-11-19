import argparse
from console import ConsoleChat

if __name__ == '__main__':
    arguments = argparse.ArgumentParser(prog="Ollama REST API chat",
                                        description="Chat with Large Language Model in Ollana")
    arguments.add_argument("-l", "--language", help="Define a language model. Must run on server", type=str)
    arguments.add_argument("-U", "--URI", help="The uri of the Ollama server", type=str)

    args = vars(arguments.parse_args())

    if not args.get("language") or not args.get("URI"):
        raise argparse.ArgumentError(None, "Please specify a language model and URI")
    elif len(args) < 1:
        raise argparse.ArgumentError(None, "No arguments entered! Call --help.")

    model = args.get("language")
    uri = args.get("URI")

    chat = ConsoleChat(uri=uri, model=model)
    chat.start_conversation()
