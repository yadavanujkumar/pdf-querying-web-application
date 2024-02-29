import os
from icecream import ic
from dotenv import load_dotenv, find_dotenv

# Load .env file
load_dotenv(find_dotenv())

# Configure IC prefix
ic.configureOutput(prefix='PDF-Query -> ')

VECTOR_STORE = os.getenv('VECTOR_STORE')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")