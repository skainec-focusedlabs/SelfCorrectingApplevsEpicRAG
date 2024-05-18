from langgraph.graph import END, StateGraph

from decisions.decide_to_generate import decide_to_generate
from generate.generate import generate
from graph.graph_state import GraphState
from document_retrievers.get_relevant_docs import get_relevant_docs
from document_retrievers.retrieve_docs import retrieve
from query_transformer.query_transformer import query_transformer

workflow = StateGraph(GraphState)

workflow.add_node("retrieve", retrieve)
workflow.add_node("get_relevant_docs", get_relevant_docs)
workflow.add_node("transform_query", query_transformer)
workflow.add_node("generate", generate)

workflow.add_edge("retrieve", "get_relevant_docs")
workflow.add_conditional_edges(
    "get_relevant_docs",
    decide_to_generate,
    {
        "generate": "generate",
        "transform_query": "transform_query",
    }
)
workflow.add_edge("transform_query", END)
workflow.add_edge("generate", END)

workflow.set_entry_point("retrieve")
app_workflow = workflow.compile()
