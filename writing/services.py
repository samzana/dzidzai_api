from typing import List
from common.prompts import FREE_COMPOSITION_PROMPT, GUIDED_COMPOSITION_PROMPT
from common.rag import create_rag_chain


guided_composition_rag_chain = create_rag_chain("guided_compositions", GUIDED_COMPOSITION_PROMPT)
free_composition_rag_chain = create_rag_chain("free_compositions", FREE_COMPOSITION_PROMPT)

def grade_guided_composition_response(prompt: List[str], composition_type: str, response: str):
    combined_prompt = " ".join(prompt)
    input_context = f"prompt: {combined_prompt}\n\ntype: {composition_type}\n\nresponse: {response}"
    return guided_composition_rag_chain.invoke({"input": input_context})

def grade_free_composition_response(prompt: str, composition_type: str, response: str):
    input_context = f"prompt: {prompt}\n\ntype: {composition_type}\n\nresponse: {response}"
    return free_composition_rag_chain.invoke({"input": input_context})