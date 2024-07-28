import streamlit as st
import todo_functions

todos = todo_functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'].strip()
    if len(todo) > 0:
        todo_functions.write_todos(todo + "\n")

    st.session_state['new_todo'] = ''

st.title("Todo App")



for idx, todo in enumerate(todos):
    if len(todo.strip()) > 0:
        st.checkbox(todo, key=idx)

st.text_input(label=" ", placeholder="Add a new to do...",
              on_change=add_todo, key='new_todo')

