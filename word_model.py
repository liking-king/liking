from langchain_core.pydantic_v1 import BaseModel,Field

class WordMemory(BaseModel):
    word:str = Field(description='要记忆的单词')
    content:str = Field(description='生成记忆单词的内容')