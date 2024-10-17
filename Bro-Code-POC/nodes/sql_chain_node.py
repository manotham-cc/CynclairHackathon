from typing import Any, Dict
from chains.sql_chain import sql_chain
from state_file import GraphState
from langchain_core.runnables import RunnablePassthrough


def get_sql_chain(state: GraphState) -> Dict[str, Any]:
    print("---- GETTING SQL QUERY BASE ON QUESTION ----")
    question = state['question']
    schema = state['database_schema']
    database = state['database']
    chat_history = state['chat_history']
    
    sql_response = sql_chain.invoke({"schema":schema, "question":question, "chat_history": chat_history})

    def get_schema():
        return database.get_table_info()

    # state['logging_string'] = state['logging_string'] + "\n\n" + "---- GETTING SQL QUERY BASE ON QUESTION ----" + "\n\n" + \
    # str(question) + "\n\n" + str(sql_response) + "\n\n"

    return {"question": question, 
            "generation": sql_response,
            "logging_string": state['logging_string'] + "\n\n" + "---- SQL CHAIN ----" + "\n\n" + "---- GETTING SQL QUERY BASE ON QUESTION ----" \
            + "\n\n" + str(question) + "\n\n" + str(sql_response) + "\n\n",
            "sql_runnable": ( RunnablePassthrough.assign(schema=get_schema) | sql_chain )}