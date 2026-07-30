import streamlit as st
import requests

BASE_URL = "https://course-manager-s5bk.onrender.com"  # Replace with your FastAPI backend URL
st.title("📚Course Management System")
#------------------------------------------------------------
menu=st.sidebar.selectbox(
    "Choose an operation",
    ["Select","View Courses", "Add Course", "Update Course", "Delete Course"]
)
#------------------------------------------------------------
if menu=="View Courses":
    st.header("Available Courses")
    response = requests.get(f"{BASE_URL}/courses")
    if response.status_code == 200:
        data = response.json()
        st.write(data["courses"])
    else:
        st.error("Failed to fetch courses.")
#------------------------------------------------------------
elif menu=="Add Course":
    st.header("Add a New Course")
    course = st.text_input("Enter course name")
    if st.button("Add Course"):
        response = requests.post(f"{BASE_URL}/add_course/{course}")
        if response.status_code == 200:
            data = response.json()
            st.success(data["message"])
        else:
            st.error("Failed to add course.")
#------------------------------------------------------------
elif menu=="Update Course":
    st.header("Update an Existing Course")
    old_course = st.text_input("Enter the old course name")
    new_course = st.text_input("Enter the new course name")
    if st.button("Update Course"):
        response = requests.put(f"{BASE_URL}/update_course/{old_course}/{new_course}")
        if response.status_code == 200:
            data = response.json()
            st.success(data["message"])
        else:
            st.error("Failed to update course.")
#------------------------------------------------------------
elif menu=="Delete Course":
    st.header("Delete a Course")
    course = st.text_input("Enter course name to delete")
    if st.button("Delete Course"):
        response = requests.delete(f"{BASE_URL}/delete_course/{course}")
        if response.status_code == 200:
            data = response.json()
            st.success(data["message"])
        else:
            st.error("Failed to delete course.")
#------------------------------------------------------------
