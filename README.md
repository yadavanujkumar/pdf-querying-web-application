# PDF Querying Web Application

A web application for uploading PDF documents and querying their contents using AI-powered natural language processing. The system provides a conversational bot experience that can answer questions based on the contents of uploaded PDFs. It supports direct querying via the web UI and Slack integration.

## Features

- **Upload PDFs** via a modern Bootstrap-based web interface.
- **Automatic document parsing and embedding** using LangChain and OpenAI.
- **Query the PDF contents** using a conversational AI bot—either from the web UI or integrated with Slack.
- **Multi-persona support:** Customize response style for students, employees, managers, or HR.
- **Persistent vector database** for storing embeddings and fast retrieval.
- **Progress bar and feedback** in the web UI for uploads.
- **CLI commands** for advanced database and bot management.

## Technologies Used

- Python 3
- LangChain
- OpenAI API (for embeddings)
- ChromaDB (vector store)
- Flask (for web app)
- Slack Bolt (for Slack bot)
- Bootstrap (for UI)
- Click (for CLI)
- dotenv (for environment management)

## Setup Instructions

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Set environment variables:**
   - Create a `.env` file in the root directory with the following keys:
     ```
     VECTOR_STORE=path/to/vectorstore
     OPENAI_API_KEY=your_openai_api_key
     SLACK_APP_TOKEN=your_slack_app_token
     SLACK_BOT_TOKEN=your_slack_bot_token
     ```

3. **Run the web UI:**
   ```bash
   poetry run python ui.py
   ```
   - Open your browser and go to the provided address.
   - Select and upload a PDF file.

4. **Start the bot (CLI):**
   ```bash
   poetry run run-bot --db-name pdf-query
   ```
   - The bot will load your PDF and be ready to answer queries.

5. **Query your bot:**
   - Ask questions about the uploaded PDF in the web app or via Slack (if integrated).

## CLI Usage

- **Create a new database:**
  ```bash
  poetry run python src/commands.py create-db --name mydb
  ```
- **Store a PDF:**
  ```bash
  poetry run python src/commands.py store-pdf --db-name mydb --id doc1 --file-path /path/to/file.pdf --embedding-type langchain
  ```
- **Run the bot:**
  ```bash
  poetry run python src/commands.py run --db-name mydb --persona employee
  ```

## Slack Integration

- Configure your Slack app tokens in `.env`.
- The bot can respond to messages and commands (e.g., `/hello-socket-mode`).

## File Structure

- `src/`: Core Python modules (app, bot, database, config, CLI).
- `templates/`: HTML templates for the web UI.
- `README.md`: Project documentation.

## Example Workflow

1. Upload a PDF using the web UI.
2. The document is parsed and embedded into a vector database.
3. Start the bot and query: "What is the main topic of this document?"
4. Receive AI-generated answers based on PDF contents.

## License

MIT

---

**Developed by [yadavanujkumar](https://github.com/yadavanujkumar)**
