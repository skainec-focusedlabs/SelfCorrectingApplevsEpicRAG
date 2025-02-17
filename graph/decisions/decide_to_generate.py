

def decide_to_generate(state: dict) -> str:
    num_original_docs = state["num_original_docs"]
    filtered_docs = state["documents"]
    num_times_retrieved_docs = state["num_times_retrieved_docs"]

    print(f'Percentage of relevant docs {(len(filtered_docs) / num_original_docs)*100}%\n')

    if len(filtered_docs)/num_original_docs >= .5:
        return "generate_answer"
    elif num_times_retrieved_docs > 1:
        return "internet_question_rewriter"
    else:
        return "question_rewriter"
