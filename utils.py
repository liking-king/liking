from langchain.prompts import ChatPromptTemplate
from prompt_template import system_template_text, user_template_text
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from word_model import WordMemory


def generate_word(word, openai_api_key, creativity):
    prompt = ChatPromptTemplate([
        ('system', system_template_text),
        ('user', user_template_text)
    ])

    model = ChatOpenAI(
        model_name="deepseek-chat",
        base_url="https://api.deepseek.com/v1",
        openai_api_key=openai_api_key,
        temperature=creativity,
    )

    output_parser = PydanticOutputParser(pydantic_object=WordMemory)
    chain = prompt | model | output_parser

    result = chain.invoke({
        "parse_instruction": output_parser.get_format_instructions(),
        "word": word
    })
    return result