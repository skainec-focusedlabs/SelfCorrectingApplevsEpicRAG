import os
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, UnstructuredPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import PGVector
from langchain_experimental.text_splitter import SemanticChunker

from app.config import EMBEDDING_MODEL, PG_COLLECTION_NAME

load_dotenv()

loader = DirectoryLoader(
    os.path.abspath("../source_docs"),
    glob="**/*.pdf",
    use_multithreading=True,
    show_progress=True,
    max_concurrency=50,
    loader_cls=UnstructuredPDFLoader,
)

docs = loader.load()

embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

text_splitter = SemanticChunker(embeddings=embeddings)
chunks = text_splitter.split_documents(docs)

PGVector.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name=PG_COLLECTION_NAME,
    connection_string=os.getenv("POSTGRES_URL"),
    pre_delete_collection=True,
    use_jsonb=True,
)
