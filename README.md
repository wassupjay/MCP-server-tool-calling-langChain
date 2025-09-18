# MCP Server Tool Calling with LangChain

A demonstration of using MCP (Model Control Protocol) servers with LangChain to create and manage custom tools for language models.

This project consists of three main components:

1.  **Client (`client.py`):** The main application that uses LangChain and a Groq model to answer questions. It connects to the MCP servers to get a list of available tools.
2.  **Math Server (`mathserver.py`):** An MCP server that provides basic arithmetic operations (`add` and `multiply`). It communicates over standard input/output.
3.  **Weather Server (`weather.py`):** An MCP server that provides a simple weather lookup service. It communicates over HTTP.

## Project Structure

-   `client.py`: Main client application that connects to MCP servers and uses LangChain for tool calling.
-   `mathserver.py`: MCP server providing math operations (add, multiply).
-   `weather.py`: MCP server providing weather information.
-   `main.py`: Simple entry point for the application.
-   `.env`: For storing environment variables (e.g., `GROQ_API_KEY`).
-   `requirment.txt`: Python dependencies.

## Features

-   **Math Server:** Provides two basic arithmetic tools:
    -   `add(a, b)`: Adds two numbers.
    -   `multiply(a, b)`: Multiplies two numbers.
-   **Weather Server:** Provides a tool to get weather information:
    -   `get_weather(location)`: Returns a mock weather forecast for a given location.
-   **LangChain Integration:** The client uses LangChain to create a ReAct agent that can intelligently use the tools provided by the MCP servers to answer questions.
-   **Multi-Protocol Communication:** Demonstrates two different MCP transport protocols: `stdio` for the math server and `streamable_http` for the weather server.

## Prerequisites

-   Python 3.8+
-   A Groq API key.

## Setup and Running the Application

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd MCP-server-tool-calling-langChain
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirment.txt
    ```

3.  **Set up environment variables:**
    Create a file named `.env` in the project root and add your Groq API key:
    ```
    GROQ_API_KEY="your-groq-api-key"
    ```

4.  **Run the Weather Server:**
    In a terminal, run the weather server:
    ```bash
    python weather.py
    ```
    This will start an HTTP server on `localhost:8000`.

5.  **Run the Client:**
    In a separate terminal, run the client application:
    ```bash
    python client.py
    ```
    The client will automatically start the `mathserver.py` as a subprocess and then connect to both the math and weather servers. It will then proceed to ask two questions to the LangChain agent to demonstrate the tool-calling capabilities.
You should see output in the client's terminal showing the available tools, the response to the math question, and the response to the weather question.
