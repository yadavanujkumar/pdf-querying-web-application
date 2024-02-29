import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from ask import ask

# Load the environment file
load_dotenv()
PROMPT = None

def initialize_prompt(vectordb):
    context = '''
    As the ai aissistant, you possess complete mastery over our policy documents and wield the expertise
     to formulate responses. You must grasp the nuances of each query and tailor your replies accordingly. When a
      student seeks assistance , respond with a helpful demeanour and personal perspective.
    In the event that a question falls beyond the scope of the provided documents, respond with courtesy,
     stating that you do not possess the requisite information.
    '''

    global PROMPT

    template = """
        {context}
        Question: {question}
        Answer:
    """
    PROMPT = PromptTemplate(
        template=template, input_variables=["context", "question"]
    )
    return PROMPT


# The main function can be invoked by poetry
def __main__():
    global PROMPT
        
    while True:
        user_input = input("Enter a query: ") 
        if user_input == "exit": 
            break
        query = f"###Prompt {user_input}"
        try:
            llm_response = ask("pdf-query", PROMPT,query)
            print(llm_response["result"])
        except Exception as err:
            print('Exception occurred. Please try again', str(err))

if __name__ == '__main__':
    __main__()