# Project 9 : Python Website 
import streamlit as st
import pandas as pd
import random

# Function to generate random student data
def generate_student_data(num_students: int) -> pd.DataFrame:
    """
    Generates a DataFrame with random student data.

    Args:
    - num_students (int): The number of student records to generate.

    Returns:
    - pd.DataFrame: A DataFrame containing the student data.
    """
    # List of names to randomly assign
    names = ["Ali", "Kinza", "Ahmed", "Hamza", "Sana", "Farah", "Maria", "Zohaib", "Danish", "Safa", "Asad"]
    students = []
    
    # Generate student data
    for i in range(1, num_students + 1):
        student = {
            "ID": i,
            "Name": random.choice(names),
            "Age": random.randint(18, 25),
            "Grade": random.choice(["A", "B", "C", "D", "E", "F"]),
            "Marks": random.randint(40, 100)
        }
        students.append(student)
    
    return pd.DataFrame(students)

# Streamlit app configuration
st.set_page_config(page_title='Student Data Generator', layout='wide')
st.title("🎓 Student CSV File Generator 📊")

# Input for the number of students
num_students = st.number_input(
    "🔢 Enter the number of students to generate:", 
    min_value=1, 
    max_value=100, 
    value=15, 
    step=1,
    help="Enter a positive integer to specify the number of student records. 📈"
)

# Function to handle student data generation and display
def handle_generate_students(num_students: int):
    """
    Handles the logic for generating student data, displaying it, and providing the download button.

    Args:
    - num_students (int): The number of students to generate.
    """
    if num_students <= 0:
        st.error("❌ Please enter a valid number of students greater than 0.")
        return

    # Generate student data
    st.info(f"🧑‍🎓 Generating {num_students} student records...")
    df = generate_student_data(num_students)

    # Display the DataFrame
    st.subheader("📋 Generated Students Data")
    st.dataframe(df)

    # Provide download button for the CSV file
    csv_file = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="💾 Download CSV File",
        data=csv_file,
        file_name="students.csv",
        mime="text/csv",
        help="Click to download the generated student data as a CSV file. 🗂️"
    )

    # Success message
    st.success(f"✅ {num_students} student(s) record generated successfully! 🎉")

# Trigger the student generation on button click
if st.button("🖱️ Generate Students"):
    handle_generate_students(num_students)


