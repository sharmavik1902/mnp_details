import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)

prompt = PromptTemplate(
    input_variables=["query"],
    template="""
You are an intelligent assistant that converts user queries into SQL-style filters...

Query: {query}
Output:
"""
)

chain = LLMChain(llm=llm, prompt=prompt)

def get_filters(query: str):
    return chain.run(query).strip()