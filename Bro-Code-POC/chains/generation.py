from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

template ="""
You are a data analyst and expert cybersecurity at a company. You are interacting with a user who is asking you questions about the company's database
Based on the table below, question, sql query, and sql response, write a natural language response.
Conversation History: {chat_history}
SQL Query: <SQL>{query}</SQL>
User question: {question}
SQL Response: {response}
after response show your SQL query
"""

prompt = ChatPromptTemplate.from_template(template)
generation_chain = prompt | llm | StrOutputParser()

  