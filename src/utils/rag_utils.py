from pymilvus import AnnSearchRequest
from sentence_transformers import SentenceTransformer
import pandas as pd
from pymilvus import MilvusClient, RRFRanker
from transformers import AutoTokenizer, AutoModelForCausalLM


client = MilvusClient("models/milvus_demo.db")
embedding_model = SentenceTransformer("Snowflake/snowflake-arctic-embed-s")
tokenizer = AutoTokenizer.from_pretrained("HuggingFaceTB/SmolLM2-135M-Instruct")
model = AutoModelForCausalLM.from_pretrained("HuggingFaceTB/SmolLM2-135M-Instruct")


def retrieve_chunks(query_text: str):
    query_dense_vector = embedding_model.encode(query_text).tolist()

    search_param_1 = {
        "data": [query_dense_vector],
        "anns_field": "dense_vector",
        "param": {"nprobe": 10},
        "limit": 2,
    }
    request_1 = AnnSearchRequest(**search_param_1)

    search_param_2 = {
        "data": [query_text],
        "anns_field": "sparse_vector",
        "param": {"drop_ratio_search": 0.2},
        "limit": 2,
    }
    request_2 = AnnSearchRequest(**search_param_2)

    reqs = [request_1, request_2]

    chunks = client.hybrid_search(
        collection_name="products_collection",
        reqs=reqs,
        limit=10,
        ranker=RRFRanker(),
        output_fields=["text"],
    )
    return chunks


def generate_answers(contexts, prompt):

    messages = [
        {
            "role": "system",
            "content": "/no_think You are expert in answering questions based on provided context. Make sure to answer only using the context. If the context does not contain the answer, respond with 'I don't know.' /end_no_think",
        },
        {"role": "user", "content": f"Context: {contexts}\n\nQuestion: {prompt}"},
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    generated_ids = model.generate(**model_inputs, max_new_tokens=32768)

    output_ids = generated_ids[0][len(model_inputs.input_ids[0]) :]

    return tokenizer.decode(output_ids, skip_special_tokens=True)
