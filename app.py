import streamlit as st
from agent import run_query

st.title("Research Paper Assistant")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# chat input
if query := st.chat_input("Ask a question about the paper..."):
    # display user message
    with st.chat_message("user"):
        st.write(query)
    st.session_state.messages.append({"role": "user", "content": query})

    # get and display response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.write_stream(run_query(query))
    st.session_state.messages.append({"role": "assistant", "content": response})