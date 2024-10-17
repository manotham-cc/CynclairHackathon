# Original: Question --> Get Doc --> Rate Doc --> Is Good or not
# Ours: Question --> Query --> Rate Query --> Is Good or not

from constants import *
from langchain_core.prompts import ChatPromptTemplate
from langchain.pydantic_v1 import BaseModel, Field
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

class GradeQueryResponse(BaseModel):
    """Binary Score to check on the generated query"""

    # Write a Clear description is a Good practice. LLM will leverage that in grading the query
    binary_score: str = Field(
        description="The generate query is useful for further investigation, 'yes' or 'no'")

# with_structured_output --> LLM must support function calling
structured_llm_grader = llm.with_structured_output(GradeQueryResponse)

system = """You are a grader, with specialty in cybersecurity, assessing the usefulness of the generated response. \n
If the response is useful for further investigation, grade it as useful. \n
Give a binary score 'yes' or 'no' score to indicate the usefulness of the generated response.
"""
grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Generated Response: \n\n {response} \n\n User Question: {question}")
    ]
)

system_reasoning = """You are a grader, with specialty in cybersecurity, assessing the usefulness of the generated response. \n
If the response is useful for further investigation, grade it as useful. Provide your reasoning.
"""

reason_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_reasoning),
        ("human", "Generated Response: \n\n {response} \n\n User Question: {question}")
    ]
)

response_grader = grade_prompt | structured_llm_grader
response_reasoning = reason_prompt | llm