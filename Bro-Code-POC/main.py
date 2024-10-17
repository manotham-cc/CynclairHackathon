from graph import app
import streamlit as st
from dotenv import load_dotenv
from test_create_db import init_database
from langchain_core.messages import AIMessage, HumanMessage
from graph import app

load_dotenv()
if __name__ == "__main__":
    # Change Question to be dynamically input of user ???
    # print(app.invoke(input={"question": "what is agent memory ?"}))

# =============================================================================================================== #
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
        AIMessage(content="Hello! I'm a SQL assistant. Ask me anything about your database."),
        ]

    st.set_page_config(page_title="Chat with MySQL", page_icon=":speech_balloon:")

    st.title("InvesTech Agent")

    with st.sidebar:
        st.subheader("Settings")
        st.write("This is a simple chat application using MySQL. Connect to the database and start chatting.")
        
        st.text_input("Host", value="localhost", key="Host")
        st.text_input("Port", value="3306", key="Port")
        st.text_input("User", value="root", key="User")
        st.text_input("Password", type="password", value="12345", key="Password")
        st.text_input("Database",value= "test",key="Database")
        
        if st.button("Connect"):
            with st.spinner("Connecting to database..."):
                db = init_database(
                    st.session_state["User"],
                    st.session_state["Password"],
                    st.session_state["Host"],
                    st.session_state["Port"],
                    st.session_state["Database"]
                )
                st.session_state.db = db
                st.success("Connected to database!")
        
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.markdown(message.content)

    user_query = st.chat_input("Type a message...")
    if user_query is not None and user_query.strip() != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        
        with st.chat_message("Human"):
            st.markdown(user_query)
            
        with st.chat_message("AI"):
            response = app.invoke(input={"question": user_query, 
                                         "database": st.session_state.db, 
                                         "database_schema": st.session_state.db.get_table_info(),
                                         "chat_history": st.session_state.chat_history,
                                         "logging_string": ""})
            # response = get_response(user_query, st.session_state.db, st.session_state.chat_history)
            st.markdown(response['generation'])
            
        st.session_state.chat_history.append(AIMessage(content=response['generation']))

        with st.sidebar:
            st.subheader("See the though of your LLM !")
            st.write(response["logging_string"])
    