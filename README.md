# Simple LangChain Agent Exploration

This project is a personal exploration of the [LangChain](https://python.langchain.com/) framework. It demonstrates how to build a simple local AI agent that can interact with external tools (in this case, fetching stock prices) using a locally running Large Language Model (LLM).

## Overview

The agent is designed to answer questions about financial data. It uses:
*   **LangChain**: For orchestration and agent construction.
*   **Ollama**: To run the LLM locally.
*   **yfinance**: A tool to fetch real-time market data.

## Prerequisites

*   **Python 3.10+** (tested on 3.13)
*   **Ollama**: You need to have Ollama installed and running on your machine. [Download Ollama here](https://ollama.com/).

## Setup Instructions

### 1. Install Dependencies

Install the required Python packages:

```bash
pip install langchain langchain-ollama yfinance python-dotenv
```

### 2. Setup Ollama

This project uses the `mistral:latest` model. You need the Ollama server running and the model pulled.

1.  **Pull the Model**:
    Open a terminal and run:
    ```bash
    ollama pull mistral:latest
    ```

2.  **Start the Ollama Server**:
    Run the following command to start the API server (required for the agent to connect):
    ```bash
    ollama serve
    ```
    *Keep this terminal window open.*

### 3. Environment Variables (Optional)

If you have specific API keys or other environment configurations, create a `.env` file in the root directory.

```bash
touch .env
```

*(Note: The current agent relies on local Ollama and public `yfinance` data, so no external API keys are strictly required for the basic functionality).*

## Usage

Run the main script:

```bash
python main.py
```

The agent is currently hardcoded to ask for the price of Google, but you can modify the `invoke` call in `main.py` to ask about other stocks (e.g., "What is the price of Bitcoin?").

## Project Structure

*   `main.py`: The core script that initializes the model, tools, and runs the agent.
*   `.gitignore`: Specifies files to be ignored by git (e.g., `.env`, `__pycache__`).
