from typing import List, TypedDict, Any
from langchain_core.messages import AIMessage, HumanMessage

class GraphState(TypedDict):
    """
        Represent the state of our Graph

        Attributes:
            question: question
            generation: LLM generation
            is_useful: whether the response (SQL query) is useful for further investigation
            schema: Schema of the database ?

            web_search: whether to add search result from the website or not
            documents: list of documents --> Maybe not needed ???? (List of Content)
    """

    question: str
    generation: str
    sql_runnable: Any
    documents: List[str]
    logging_string: str

    database: Any
    database_schema: str # Should be SQL database object

    chat_history: List[Any]