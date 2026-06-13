import streamlit as st
import tempfile
from agent import run_query
from ingest import ingest
from ingest import vector_db
import hashlib
import retrieve

st.title("Research Paper Assistant")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#upload pdf
uploaded_file = st.file_uploader("Upload Your Paper", type="pdf")
if uploaded_file is not None:
    st.success(f"File Uploaded: {uploaded_file.name}")
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        bytes_data = uploaded_file.getvalue()
        temp.write(bytes_data)
        file_path = temp.name
    hash_value = hashlib.sha256(bytes_data).hexdigest()
    retrieve.current_hash = hash_value
    result = vector_db.get(where={'source_hash': hash_value})
    if result['ids']:
        pass
    else:
        ingest(file_path, hash_value)


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