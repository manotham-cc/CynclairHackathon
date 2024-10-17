from typing import Any, Dict
from chains.generation import generation_chain
from chains.sql_chain import sql_chain
from langchain_core.runnables import RunnablePassthrough
from state_file import GraphState


def generate(state: GraphState) -> Dict[str, Any]:
    """
        From the corresponding code generate response to return to the user
    """
    print("---- GENERATING ----")
    question = state['question']
    response = state['generation']
    chat_history = state['chat_history']
    db = state['database']

    true_generation_chain = (
        RunnablePassthrough.assign(query= RunnablePassthrough.assign(schema= lambda _: db.get_table_info()) | sql_chain ).assign(
            schema=lambda _: db.get_table_info(),
            response=lambda vars: db.run(vars["query"]),
        ) | generation_chain
        )

    generation = true_generation_chain.invoke({"context":response, "question":question, "chat_history": chat_history})

    # state['logging_string'] = state['logging_string'] + "\n\n" + "---- GENERATING ----" + "\n\n" + str(question) + "\n\n" + str(generation) + "\n\n"

    return {"question": question, 
            "generation": generation,
            "logging_string": state['logging_string'] + "\n\n" + "---- GENERATING RESPONSE ----" + "\n\n" + str(question) + "\n\n" + str(generation) + "\n\n"}