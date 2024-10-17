# from typing import Any, Dict
# from state_file import GraphState
# from ingestion import retriever # Change Accordingly this one is not the same as in the tutorial

# # Should change to generation of response instead

# def retrieve(state: GraphState) -> Dict[str, Any]:
#     print("---- RETRIEVING ----")

#     question = state['question']
    
#     documents = retriever.invoke(question) # Do semantic search and return relevant documents

#     return {"documents": documents, "question": question}