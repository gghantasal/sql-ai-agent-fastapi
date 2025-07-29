# src/core/agent.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.agent_toolkits.sql.base import create_sql_agent # <--- This should be correct now
from langchain_core.runnables import Runnable
from langchain_core.prompts import PromptTemplate
from src.database.connection import get_db_connection, get_db_schema_info
from src.core.prompts import SYSTEM_PROMPT
from src.utils.logger import logger # <--- This import is fine here

_sql_agent_executor = None # Singleton agent executor

def initialize_sql_agent() -> Runnable:
    # ... (rest of the initialize_sql_agent function, remains as previously modified)
    global _sql_agent_executor
    if _sql_agent_executor is None:
        logger.info("Initializing SQL Agent...")
        try:
            llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0, google_api_key=os.getenv("GOOGLE_API_KEY"))
            db = get_db_connection()
            toolkit = SQLDatabaseToolkit(db=db, llm=llm)

            _sql_agent_executor = create_sql_agent(
                llm=llm,
                toolkit=toolkit,
                verbose=True,
                agent_type="openai-tools",
            )
            logger.info("SQL Agent initialized successfully.")
        except Exception as e:
            logger.exception("Failed to initialize SQL Agent.")
            raise
    return _sql_agent_executor


async def query_sql_agent(question: str) -> str:
    """
    Asynchronously queries the SQL agent with a natural language question.
    """
    # This ensures the agent is initialized when first called, or retrieves the existing one.
    agent_executor = initialize_sql_agent()
    logger.info(f"Received query for SQL Agent: '{question}'")
    try:
        response = await agent_executor.ainvoke({"input": question})
        output = response.get("output", "No direct output from agent.")
        logger.info(f"Agent response for '{question}': {output}")
        return output
    except Exception as e:
        logger.error(f"Error querying SQL Agent for '{question}': {e}")
        return f"An error occurred while processing your request: {e}"