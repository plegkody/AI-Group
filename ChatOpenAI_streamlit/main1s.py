import streamlit as st
import os
from datetime import datetime


st.header("Chatbot")

# st.write("This is a chatbot")

# chat_history = st.checkbox("Show chat history")

# if chat_history:
#     st.write("Chat history")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# React to user input
prompt = st.chat_input("User: ")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Assistant: {prompt}"

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])