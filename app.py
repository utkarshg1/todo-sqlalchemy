import streamlit as st 
from models import add_task, get_tasks, modify_task, delete_task, create_db

# Initialize db
create_db()

# Application header and title
st.set_page_config(page_title="To Do App", page_icon="😎")
st.title("To Do App - Utkarsh Gaikwad")

# Add new task
new_task = st.text_input("Add a new task")
if st.button("Add Task"):
    if new_task:
        add_task(new_task)
        st.success(f"Task {new_task} added successfully")
    else:
        st.error("Task cannot be empty")

# Show existing tasks 
st.subheader("To-do List")
tasks = get_tasks()

if tasks:
    for task in tasks:
        task_text = st.text_input(f"Task ID {task.id}", task.task, key=f"task_{task.id}")
        complete_status = st.checkbox(f"Complete Task ID {task.id}", value=task.complete, key=f"complete_{task.id}")
        modify_col, delete_col = st.columns(2)

        # Modify task
        if modify_col.button(f"Modify Task {task.id}"):
            if task_text:
                modify_task(task.id, task_text, complete_status)
                st.success(f"Task {task.id} modified to '{task_text}' with completion status {'Complete' if complete_status else 'Incomplete'}")
            else:
                st.error("Task cannot be empty")

        # Delete task
        if delete_col.button(f"Delete Task {task.id}"):
            delete_task(task.id)
            st.success(f"Task {task.id} deleted")
else:
    st.info("No tasks added yet.")