

def decide_to_generate(state: dict) -> str:
    num_original_docs = state["num_original_docs"]
    filtered_docs = state["documents"]
    num_times_retrieved_docs = state["num_times_retrieved_docs"]

    print(f'Percent of docs which are relevant {(len(filtered_docs) / num_original_docs)*100}%\n')

    if len(filtered_docs)/num_original_docs >= .5:
        return "generate_answer"
    elif num_times_retrieved_docs > 1:
        return "ask_the_internet"
    else:
        return "transform_query"
