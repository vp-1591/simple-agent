# pip install -qU langchain "langchain[anthropic]"
from langchain.agents import create_agent
import yfinance as yf
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.tools import tool

# 1. Define the Tool
@tool
def get_latest_price(ticker_symbol: str) -> str:
    """
    Fetches the latest trading price for a stock or crypto ticker symbol 
    (e.g., AAPL for Apple, BTC-USD for Bitcoin). Input must be the ticker symbol string.
    """
    try:
        ticker = yf.Ticker(ticker_symbol)
        # Get historical data for the last 1 day
        hist = ticker.history(period="1d")
        
        if not hist.empty:
            current_price = hist['Close'].iloc[-1]
            return f"The latest price for {ticker_symbol.upper()} is ${current_price:.2f}."
        else:
            return f"Error: Could not retrieve price data for {ticker_symbol.upper()}. Check the ticker symbol."
    except Exception as e:
        return f"Tool Execution Error: {e}"

load_dotenv()

# Using Ollama is recommended for local execution to save VRAM (avoids CUDA OOM)
# Ensure you have 'langchain-ollama' installed and Ollama running with 'phi3' pulled.
model = init_chat_model(
    "mistral:latest",
    model_provider="ollama",
    temperature=0.1,
)

agent = create_agent(
   model=model,
  tools=[get_latest_price],
   system_prompt='''
   You are a specialized Finance Price Agent.
   ''',
)

# Run the agent
print("Invoking agent...")
response = agent.invoke(
   {"messages": [{"role": "user", "content": "what is the price of Google right now?"}]}
)
# Extract and print the last message content for readability
last_message = response["messages"][-1]
print("\n--- Agent Response ---")
print(last_message.content)