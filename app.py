import streamlit as st

st.title("Smart Learning Assistant")

st.subheader("Ask your question")

question = st.text_input("Type your question here")

if question:
    st.write("You Asked:", question)

    if question.lower() == "what is ai?":
        st.write("AI Answer: Artificial Intelligence is technology that enables computers to think and learn like humans.")

    elif question.lower() == "what is python?":
        st.write("AI Answer: Python is a popular programming language used for AI, web development, and software projects.")

    else:
        st.write("AI Answer: Sorry, I am still learning 😊")
        