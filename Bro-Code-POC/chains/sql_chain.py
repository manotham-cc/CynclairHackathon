from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from dotenv import load_dotenv
load_dotenv()

template = """
You are an expert Detection Engineer. Given the threat intelligence database schema and the user's question,
generate an appropriate investigative query to retrieve the desired data.

<SCHEMA>{schema}</SCHEMA>

Conversation History: {chat_history}

Write only the investigative SQL query and nothing else. Do not wrap the query in any other text, not even backticks.

Question: {question}
Investigative Query:
if the question can't respone in sql code return nothing
"""

# template = """
# You are an expert Detection Engineer. Given the threat intelligence database schema and the user's question,
# generate an appropriate investigative query to retrieve the desired data.

# <SCHEMA>{schema}</SCHEMA>

# Write only the investigative SQL query and nothing else. Do not wrap the query in any other text, not even backticks.

# Question: {question}
# Investigative Query:
# if the question can't respone in sql code return nothing
# """

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)
sql_prompt = ChatPromptTemplate.from_template(template)
sql_chain = sql_prompt | llm | StrOutputParser()

# sql_runnable = ( RunnablePassthrough.assign(schema=get_schema) | sql_prompt | llm | StrOutputParser() )