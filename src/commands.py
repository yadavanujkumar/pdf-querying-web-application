import click
from icecream import ic
from src import db
from src import run_bot

@click.group()
def commands():
    pass

@commands.command()
@click.option("--name", help="Database name")
def create_db(name=None):
    ic("Creating a new database...")
    db.create(name)


@commands.command()
@click.option("--id", help="Document id")
@click.option("--file-path",help="Path to the PDF file")
@click.option("--db-name", help="Database name")
@click.option("--embedding-type", default='langchain', help="Document type")
def store_pdf(db_name, id, file_path,  embedding_type):
    collection = db.connect(db_name)
    ic(collection)
    id  = db.store(db_name, collection, id, file_path, embedding_type)

@commands.command()
@click.option("--db-name", help="Database name")
@click.option("--persona", default="employee", help="Role of person quering")
def run(db_name, persona):
    print("Started command")
    run_bot.run(db_name, persona)

# Initialise the commands
if __name__ == '__main__':
    commands()