Markdown

# 🤖 SQL AI Agent with FastAPI

## 🌟 Overview

This project implements an intelligent SQL AI Agent exposed via a FastAPI web API. It allows users to interact with a SQL database using natural language queries, eliminating the need for direct SQL knowledge. Powered by Large Language Models (LLMs) like Google Gemini via LangChain, it translates natural language questions into executable SQL queries, fetches results, and provides answers in a human-readable format.

This agent is ideal for business intelligence, data exploration, and creating intuitive interfaces for non-technical users to access database insights.

## ✨ Features

* **Natural Language to SQL:** Converts plain English questions into precise SQL queries.
* **FastAPI Backend:** Provides a high-performance, asynchronous web API for seamless integration.
* **LLM Powered:** Leverages powerful LLMs (e.g., Google Gemini, OpenAI GPT) through LangChain for robust language understanding and SQL generation.
* **Database Agnostic:** Configurable to connect to various SQL databases (SQLite, PostgreSQL, MySQL, etc.) via SQLAlchemy.
* **Structured Project Layout:** Follows best practices for Python project organization, ensuring maintainability and scalability.
* **Interactive API Documentation:** Automatically generated OpenAPI (Swagger UI) documentation for easy testing and integration.
* **Containerization Ready:** Designed for easy Dockerization and deployment.

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)
* A terminal or command prompt

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone [https://github.com/gghantasal/sql-ai-agent-fastapi.git]
cd sql-ai-agent-fastapi

2. Set Up a Virtual Environment
It's highly recommended to use a virtual environment to manage dependencies.

Bash

python -m venv .venv
Activate the virtual environment:

macOS/Linux:

Bash

source .venv/bin/activate
Windows (Command Prompt):

Bash

.venv\Scripts\activate.bat
Windows (PowerShell):

PowerShell

.venv\Scripts\Activate.ps1
Your terminal prompt should now show (.venv) at the beginning.

3. Install Dependencies
Install all the required Python packages:

Bash

pip install -r requirements.txt
4. Database Setup
This project uses a simple SQLite database for demonstration.

Bash

python db/db_setup.py
This script will create a company.db file in the db/ directory and populate it with sample data (employees, departments, projects).

5. Configure Environment Variables
Create a .env file in the root of your project (sql-ai-agent-fastapi/) and add your API keys and database connection string:

Code snippet

# .env
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"
# Or if using OpenAI: OPENAI_API_KEY="YOUR_OPENAI_API_KEY_HERE"

DATABASE_URL="sqlite:///db/company.db"
# Example for PostgreSQL: DATABASE_URL="postgresql://user:password@host:port/database_name"
# Example for MySQL: DATABASE_URL="mysql+mysqlconnector://user:password@host:port/database_name"

LOG_LEVEL="INFO" # DEBUG, INFO, WARNING, ERROR, CRITICAL
Important: Replace "YOUR_GEMINI_API_KEY_HERE" with your actual API key.

6. Run the FastAPI Application
Start the Uvicorn server:

Bash

uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
The application will start, and you should see logs indicating successful database connection and agent initialization.

💡 Usage
Once the server is running, you can interact with the API:

API Documentation
Open your web browser and navigate to:

Swagger UI (Interactive API Docs): http://localhost:8000/docs

ReDoc (Alternative Docs): http://localhost:8000/redoc

You can use the Swagger UI to send requests to your API and test the agent.

Example Query (using Swagger UI or curl)
Navigate to http://localhost:8000/docs, find the /api/v1/sql-agent/ask endpoint, click "Try it out", and enter a question.

Example curl command:

Bash

curl -X POST "http://localhost:8000/api/v1/sql-agent/ask" \
     -H "Content-Type: application/json" \
     -d '{ "question": "What is the average salary of employees in the Engineering department?" }'
Expected Response (example):

JSON

{
  "answer": "The average salary of employees in the Engineering department is 82500.0."
}
Observe your terminal where Uvicorn is running to see the agent's detailed thought process, generated SQL, and query results (due to verbose=True).

📁 Project Structure
sql-ai-agent-fastapi/
├── .env                 # Environment variables
├── README.md            # Project overview and instructions
├── requirements.txt     # Python dependencies
├── db/                  # Database-related files
│   └── company.db       # SQLite database file
│   └── db_setup.py      # Script to create/populate DB
└── src/                 # Main source code
    ├── core/            # Core AI agent logic
    │   ├── agent.py     # Encapsulates LangChain SQL agent
    │   └── prompts.py   # LLM prompt templates
    ├── database/        # DB connection and schema handling
    │   ├── connection.py# DB connection function
    ├── models/          # Pydantic models for API request/response
    │   └── chat.py      # ChatRequest, ChatResponse models
    ├── api/             # FastAPI endpoints
    │   └── v1/          # API versioning
    │       ├── endpoints/
    │           ├── sql_chat.py # Endpoint for SQL agent interaction
    │           └── health.py   # Health check endpoint
    │       └── api.py   # Combines API routers
    ├── utils/           # Utility functions
    │   ├── logger.py    # Logging setup
    │   └── constants.py # Global constants
    └── main.py          # FastAPI application entry point
🛠 Technologies Used
Python 3.8+

FastAPI: High-performance web framework for building APIs.

LangChain: Framework for developing applications powered by LLMs.

Google Gemini API: (or OpenAI API) The underlying Large Language Model for natural language understanding and SQL generation.

SQLAlchemy: Python SQL Toolkit and Object Relational Mapper for database interaction.

Uvicorn: ASGI server to run FastAPI applications.

Pydantic: Data validation and settings management (used by FastAPI).

python-dotenv: For loading environment variables.

SQLite: (or PostgreSQL, MySQL etc.) The database used.

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Create a Pull Request.