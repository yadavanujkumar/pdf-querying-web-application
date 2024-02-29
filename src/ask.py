
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import icecream as ic
from src import db

def ask(db_name, context, query):
    vectordb = None
    vectordb = db.get_db(db_name)
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})
    llm = ChatOpenAI(model_name='gpt-4')
    qa = RetrievalQA.from_chain_type(
        llm=llm, 
        chain_type="stuff", 
        retriever=retriever, 
        return_source_documents=False,
        chain_type_kwargs={"prompt": context}
    )
    return qa(query)
