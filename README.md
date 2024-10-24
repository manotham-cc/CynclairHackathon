# InvesTech Agent

InvesTech Agent is an LLM-powered chat-based solution. It allows you to interact with MySQL database using natural langauge queries. The solution is capable of generating an SQL query, self-reasoning and query correction, and translate an SQL prompt to natural language response that user can easily understand. Moreover, the solution enable users to track and understand an LLM reasoning and work process. This project is built using LangChain, LangGraph, Groq APIs, along with Streamlit for the user interface.

## Features

- **AI-Driven Insights**: Utilizes AI models to analyze data and deliver intelligent responses based on user queries.
- **Natural Language to SQL**: Translates natural language inputs into SQL queries for seamless database interaction.
- **Transparent Responses**: Provides natural language explanations for queries, along with the raw SQL code for clarity.
- **User-Friendly Interface**: Features a Streamlit-based web interface for easy interaction with the database.
- **Reasoning for Query Selection**: Explains the rationale behind the chosen SQL queries to enhance understanding and transparency.


## Requirements

- Python 3.8+
- MySQL database
- `.env` file to store sensitive environment variables
- Requirements.txt
## Installation

1. Clone the repository:
    ```bash
    https://github.com/Cynclair-Mahidol-Hackathon-2024/Bro-Code.git
    cd Brocode
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file and add your environment variables You Groq api key (Optional) :
    ```bash
     .env
    ```
    follow this site 
    https://console.groq.com/docs/quickstart

4. Run the application:
    ```bash
    streamlit run main.py
    ```

## How to Use

1. **Database Connection**: 
    - In the sidebar, provide the MySQL database connection details (host, port, user, password, and database name(schema)).
    - Click "Connect" to establish a connection with the database.

2. **Chat**: 
    - Enter your natural language queries in the chat box.
    - The AI will generate a SQL query based on your input and return the query's result in a human-readable format.

## Future Improvements

- **Fine-tune with Cybersecurity Datasets**: Improve the model's reasoning abilities by training it with cybersecurity-specific datasets, enabling it to identify and query the most relevant data in investigative scenarios.
- **Enhance RAG Techniques**: Implement more advanced Retrieval-Augmented Generation (RAG) techniques to enable the system to retrieve relevant information from the internet, improving the depth of responses.
- **Improve Conversational History Management**: Develop a more sophisticated system for handling conversation history, ensuring better context retention and more coherent long-term interactions.
  
## License

This project is licensed under the MIT License.
## Acknowledgements

We would like to express our gratitude to **Cynclair** and **Mahidol University International College** for providing us with the opportunity to participate in the Cynclair Mahidol Hackathon 2024. Their support and platform have been instrumental in driving this project forward.
- [LangChain](https://github.com/langchain-ai/langchain) for their excellent library.
- [Streamlit](https://streamlit.io/) for their easy-to-use framework.
  
---

Happy querying with InvesTech Agent!
