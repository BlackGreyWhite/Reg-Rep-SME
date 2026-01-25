import streamlit as st
from chat_with_knowledge import chat_with_rag

st.title("📚 RAG Knowledge Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_with_rag(prompt, show_sources=False)
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})