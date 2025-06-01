import sys
from importlib.metadata import version

from openai import OpenAI

from program_settings import ProgramSettings

conversation_history = []


def chat_with_gpt(client, prompt):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        stream = True
    )

    for chunk in response:
        if chunk.choices[0].delta.content is not None:  # Check if content exists
            plain_text = chunk.choices[0].delta.content
            print(plain_text, end = "")  # Print without new lines
            conversation_history.append(plain_text)
    return


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_package_version(package_name: str) -> str:
    return version(package_name)


def main():
    secret_key = ProgramSettings.get_setting('SECRET_OPENAPI_KEY')
    client = OpenAI(api_key = secret_key)

    # question = "What do I need to know in order to read/write my Java POJO's from/to a MongoDB Atlas collection?"
    question = (
        "How do I use Jackson in Java to read/write POJO's to a MongoDB Atlas collection if I am not using Maven "
        "or Gradle?")
    chat_with_gpt(client, question)

    # Save the conversation history to a plain text file
    with open("chat_history.txt", "w") as file:
        file.writelines(conversation_history)


if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    print(f'openai version: {get_package_version("openai")}')



    main()

