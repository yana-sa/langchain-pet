import os

from dotenv import load_dotenv

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
load_dotenv()


def main():
    print("Hello from langchain-pet!")

    prompt_template = "Create a short description what this text is about: {text}"
    prompt = PromptTemplate(
        input_variables=["text"],
        template=prompt_template
    )

    llm = ChatOllama(model="gemma3:latest", temperature=0)
    chain = prompt | llm

    response = chain.invoke({"text": "Are you a perfectionist who finds joy in refining architecture until it shines? Join Software Planet Group as a React/PHP/Laravel Developer! Shape a next-gen recruitment platform with clean, precise code. Your attention to detail belongs here — apply now!"})

    print(response)

if __name__ == "__main__":
    main()
