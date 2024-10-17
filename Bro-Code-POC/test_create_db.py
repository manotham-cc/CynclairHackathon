from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
# from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import streamlit as st

def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
  """
    Initialize Database for demo purpose
  """
  
  db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
  return SQLDatabase.from_uri(db_uri)

# This should be our generation node
def get_sql_chain(db):

  """
    Get a chain of SQL expert LLM
    
    Return: An object with chained process for SQL retrieval.
  """

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
    
  prompt = ChatPromptTemplate.from_template(template)
  
  # llm = ChatOpenAI(model="gpt-4-0125-preview")
  llm = ChatGroq(model="llama-3.1-8b-instant", 
                 temperature=0)
  
  def get_schema(_):
    return db.get_table_info()
  
  return ( RunnablePassthrough.assign(schema=get_schema) | prompt | llm | StrOutputParser() )