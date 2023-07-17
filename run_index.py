import os
import sys
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
print(OPENAI_API_KEY)

from llama_index import VectorStoreIndex, SimpleDirectoryReader


documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)
# print(index)

def run_index(content):
    query_engine = index.as_query_engine()
    print(query_engine)
    response = query_engine.query("What is the most relevant category for the following news article (in exactly 1 word)??? " + f"{content}")

    stripped = str(response).strip().replace('\n', '')
    # print(stripped)
    return stripped