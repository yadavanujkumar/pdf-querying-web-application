import os
import chromadb
from icecream import ic
from src import config
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
#from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction



def create(name):
    path = f"{config.VECTOR_STORE}/{name}"
    if os.path.exists(path):
        ic("Database is already exists with this name")
    else:
        os.makedirs(path)
        client = chromadb.PersistentClient(path=path)
        client.create_collection(name=name)
        ic("Database created successfully")

def connect(name):
    try:
        path = f"{config.VECTOR_STORE}/{name}"
        client = chromadb.PersistentClient(path=path)
        return client.get_collection(name=name)
    except Exception as e:
        ic(e)

def store(db_name, collection, id, file_path, embedding_type):
    if "langchain" in embedding_type.lower():
        store_langchain_openai_embedding(
            db_name, 
            collection,
            id, 
            file_path
        )
    else:
        ic("Invalid embedding type. Valid type is 'langchain'")
    
# Return available embeddings into the collection
def get_embedding(collection, id):
    pass

def get_embeddings(collection):
    pass

def get(collection, id):
    pass

def get_all(collection):
    pass

def store_langchain_openai_embedding(db_name, collection, id, file_path):
    try:
        file_loader = PyMuPDFLoader(file_path)
        print("Step 1")
        documents = file_loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=10)
        texts = text_splitter.split_documents(documents)
        print("Step 2")
        embeddings = OpenAIEmbeddings()
        path = f"{config.VECTOR_STORE}/{db_name}"
        print("Saving now into chroma")
        vectordb = Chroma.from_documents(
            documents=texts, 
            embedding=embeddings,
            persist_directory=path
        )
        print("Persisting now into chroma")
        vectordb.persist()
        ic("Document embedding using Langchain is successfull")
    except Exception as e:
        ic(e)
        print("Exception ...")

def get_db(db_name):
    embeddings = OpenAIEmbeddings()
    path = f"{config.VECTOR_STORE}/{db_name}"
    vectordb = None
    vectordb = Chroma(              
        embedding_function=embeddings,
        persist_directory=path
    )
    return vectordb 

