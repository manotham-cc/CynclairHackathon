from dotenv import load_dotenv

from langgraph.graph import END, StateGraph
from constants import RETRIEVE, GRADE_RESPONSES, GENERATE, WEBSEARCH, SQL_CHAIN
from nodes import generate, grade_responses, get_sql_chain
from state_file import GraphState

load_dotenv()

def decide_to_generate(state):
    print("---- ASSESS GRADED RESPONSE")

    # If needed to regenerate the query
    if state["generation"] == "":
        print("DECISION: Query not useful, regenerate query.")
        return SQL_CHAIN
    else:
        print("DECISION: Query useful, generating natural langauge response.")
        return GENERATE


workflow = StateGraph(GraphState) # An object state graph with the user-defined object GraphState

workflow.add_node(SQL_CHAIN, get_sql_chain) # Entry Point
workflow.add_node(GRADE_RESPONSES, grade_responses)
workflow.add_node(GENERATE, generate)

workflow.set_entry_point(SQL_CHAIN) # Entry Point
workflow.add_edge(SQL_CHAIN, GRADE_RESPONSES)
workflow.add_conditional_edges(
    GRADE_RESPONSES,
    decide_to_generate,
    {
        SQL_CHAIN: SQL_CHAIN,
        GENERATE: GENERATE,
    }
)
workflow.add_edge(GENERATE, END)
app = workflow.compile()

# Entry Point ควรเป็น SQL Chain แล้ว