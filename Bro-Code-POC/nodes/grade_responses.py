# Node Implementation of retriever response

from typing import Any, Dict
from chains.response_grader import response_grader, response_reasoning
from state_file import GraphState


def grade_responses(state: GraphState) -> Dict[str, Any]:
    """
        Determine Whether the generated response is useful for further investigation
        (Or should I use the world make sense for a given situation)

        Args:
            state (dict): The current graph state
        
        Returns:
            state (dict): Regenerated and useful response ??
    """
    
    print("---- GRADING RESPONSE ----")
    question = state['question']
    response = state['generation']
    
    score = response_grader.invoke(
        {"question": question, "response": response}
    )

    reason = response_reasoning.invoke(
        {"question": question, "response": response}
    )

    grade = score.binary_score

    if grade.lower() == "yes":
        print("---- GRADE: RESPONSE USEFUL, RETURN RESPONSE ----")
        # state['logging_string'] = state['logging_string'] + "\n\n" + "---- GRADE: RESPONSE USEFUL, RETURN RESPONSE ----" + \
        #             "\n\n" + str(question) + "\n\n" + str(response) + "\n\n"
        
        return {"question": question, 
                "generation": response,
                "logging_string": state['logging_string'] + "\n\n" + "GRADING RESPONSE" + "\n\n" + "---- GRADE: RESPONSE USEFUL, RETURN RESPONSE ----" + \
                    "\n\n" + str(question) + "\n\n" + str(response) + "\n\n" + reason.content + "\n\n"}
    else:
        print("---- GRADE: RESPONSE NOT USEFUL, RETURN EMPTY RESPONSE ----") 
        # state['logging_string'] = state['logging_string'] + "\n\n" + "---- GRADE: RESPONSE NOT USEFUL, RETURN EMPTY RESPONSE----" + \
        #             "\n\n" + str(question) + "\n\n" + str(response) + "\n\n"
        
        return {"question": question, 
                "generation": "",
                "logging_string": state['logging_string'] + "\n\n" + "GRADING RESPONSE" + "\n\n" + "---- GRADE: RESPONSE NOT USEFUL, RETURN EMPTY RESPONSE----" + \
                    "\n\n" + str(question) + "\n\n" + str(response) + "\n\n" + reason.content + "\n\n"}

