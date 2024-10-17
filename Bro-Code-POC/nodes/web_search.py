from typing import Any, Dict

from langchain.schema import Document
from langchain_community.tools.tavily_search import TavilySearchResults # For Tabily Search Engine
from state_file import GraphState

from dotenv import load_dotenv

load_dotenv()

web_search_tool = TavilySearchResults(max_results=3)


def web_search(state: GraphState) -> Dict[str, Any]:
    print("---- SEARCHING THE WEB ----")
    question = state['question']
    documents = state['documents']

    tavily_results = web_search_tool.invoke({"query": question}) # Get the search result from tavily search engine

    joined_tavily_result = "\n".join(
        [tavily_results["content"] for tavily_result in tavily_results]
    ) # Joined into one larger single string

    web_results = Document(page_content=joined_tavily_result) # Create a Langchain documents from that large single string

    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
    
    return {"documents": documents, "question":question}

