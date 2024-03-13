# import required libraries
from os import environ
import os.path
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from django.conf import settings

# OpenAI Key
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_KEY")


# A function check if a previous index in storage already exists
# and if not, rebuilds the storage context
# def prepareIndex():
#     # set the persist directory
#     PERSIST_DIR = os.path.join(settings.BASE_DIR, 'modelsx', 'storage')
#     print("PERSIST_DIRR: " + PERSIST_DIR)

#     if not os.path.exists(PERSIST_DIR):
#         # load the documents and create the index
#         print("Rebuilding index...")

#         documents = SimpleDirectoryReader("Corpus").load_data()
#         index = VectorStoreIndex.from_documents(documents)

#         # store it for later
#         index.storage_context.persist(persist_dir=PERSIST_DIR)
#     else:
#         # load the existing index
#         print("Using already existing index...")

#         storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
#         index = load_index_from_storage(storage_context)

#         queryEngine = index.as_queryEngine()

#     return queryEngine

def getInsights(query):
    # prepare the index
    # queryEngine = prepareIndex()

    # set the persist directory
    PERSIST_DIR = os.path.join(settings.BASE_DIR, 'modelsx', 'storage')

    if not os.path.exists(PERSIST_DIR):
        # load the documents and create the index
        print("Rebuilding index...")

        documents = SimpleDirectoryReader("Corpus").load_data()
        index = VectorStoreIndex.from_documents(documents)

        # store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # load the existing index
        print("Using already existing index...")

        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)

        # queryEngine = index.as_queryEngine()

    # query the index based on the query
    response = index.query(query)

    # return the response
    return response