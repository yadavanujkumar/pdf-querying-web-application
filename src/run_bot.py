# Use the package we installed
from langchain.prompts import PromptTemplate
import logging
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_bolt import App
from src import config
from src import ask 

# Configure the logging settings
logging.basicConfig(level=logging.INFO,  # Set the logging level to DEBUG for detailed output
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a logger instance for your module
logger = logging.getLogger(__name__)

db_name = ""
query_person = ""
# hr = """
#         HR is seeking for assistance, respond in professional and polite tone.
#     """
# manager = """
#         A manager is seeking assistance for their team members, respond with a helpful demeanour.
#     """
employee = """
         An employee is making inquiry, please provide a personal perspective.
     """
ai_aisstiant = """
        A student is asking question, please provide a personal perspective and with a helpful demeanour.
    """


# Install the Slack app and get xoxb- token in advance
app = App(token=config.SLACK_BOT_TOKEN)

def get_prompt():
    global query_person
    # context = '''
    # As the Head of HR at Arrkgroup, you possess complete mastery over our policy documents and wield the expertise to formulate responses. You must grasp the nuances of each query and tailor your replies accordingly. When a manager seeks assistance for their team members, respond with a helpful demeanour. However, if an employee makes an inquiry, provide a personal perspective.
    # Do not reply to any messages that fall beyond the scope of the provided documents, respond with courtesy, stating that you do not possess the requisite information. If you don't know the answer, just say that you don't know, don't try to make up an answer
    # '''

    context=    '''
    As the Ai Aisstiant, you possess complete mastery over our 
    documents and wield the expertise to formulate responses.
    You must grasp the nuances of each query and tailor your replies accordingly.
    When a student seeks assistance , respond with a helpful demeanour and provide a personal perspective.
    Do not reply to any messages that fall beyond the scope of the provided documents,
    espond with courtesy, stating that you do not possess the requisite information.
    If you don't know the answer, just say that you don't know, don't try to make up an answer
    '''
    context = context + query_person

    template = """
        # You are an AI assistant for answering Human Resource (HR) policies related questions in Digital Solutions.
        # Follow these steps to answer the customer queries.
    
        You are an AI assistant for answering pdf related questions .
        Follow these steps to answer the student queries.

        The student query will be delimited with four hashtags, i.e. ####.
        Step 1:#### First identify if the query is related to pdf or not. Queries related to pdf. 
        If not, do not move to next step and politely inform that you are tuned to only answer questions about HR.

       # Please refer to leaves for holidays and vice versa

        Step 2:#### First decide whether the user is asking a question about hardware or software. 

        Step 3:#### Search answer related to the query in the vectorestore. Answer only if it related to the query.

        Step 4:#### If answer was not found in the vectorstore, 

        Step 5:#### If the answer is found, respond to user in a friendly tone and ask if any further help is required.
    
        Step 6:#### If the answer is not found, respond to user in a friendly tone and ask if do you don't know the answer.
    
        Make sure the answer is in Markdown and should be well formatted.
        
        {context}
        Question: {question}
        Answer:
    """
    PROMPT = PromptTemplate(
        template=template, input_variables=["context", "question"]
    )
    return PROMPT

@app.message("")
def handle_message(body, say):
    global db_name
    logger.info(db_name)
    context = get_prompt()
    query = body['event']['text']
    result = ask.ask(db_name, context, query)
    say(result['result'])

@app.command("/hello-socket-mode")
def hello_command(ack, body):
    user_id = body["user_id"]
    ack(f"Hi, <@{user_id}>!")

# The main function can be invoked by poetry
def run(db, query_persona):
    global db_name
    global query_person
    # global hr
    # global manager
    global employee
    global ai_aisstiant

    logger.info(f"db name {db}")
    db_name = db 

    if query_persona is None or query_persona.strip() == "":
        print("Input is null or empty.")
        query_person= ai_aisstiant
    else:
        # Compare query_persona with specific values
        if query_persona.upper() == "HR":
            query_person = student
        elif query_persona.upper() == "MANAGER":
            query_person = manager
        else:
            query_person = ai_aisstiant

    logger.info(f"Query person set to {query_person}")
    logger.info("Bot has started...")
    SocketModeHandler(app, config.SLACK_APP_TOKEN).start()