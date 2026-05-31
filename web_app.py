import streamlit as st
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(page_title="Smart Campus System", layout="wide")

# Custom Error from Lab 7
class MissingFileOrFolderError(Exception):
    pass

# Initialize session state for database storage if it doesn't exist
if "student_records" not in st.session_state:
    st.session_state.student_records = [
        {"id": "101", "name": "Arjun", "marks": 85, "course_count": 2, "fee": 50000.0},
        {"id": "102", "name": "Meera", "marks": 92, "course_count": 3, "fee": 80000.0}
    ]

# --- Core Functions ---
def evaluate_grade(score):
    if 90 <= score <= 100: return "A", "Excellent"
    elif score >= 75: return "B", "Very Good"
    elif score >= 60: return "C", "Good"
    elif score >= 40: return "D", "Average"
    else: return "F", "Needs Improvement"

def calculate_fee(tuition, hostel=0, transport=0):
    return tuition + hostel + transport

# --- UI Layout ---
st.title("🏫 Smart Campus Information System")
st.markdown("### Integrated Mini-Project Dashboard (Labs 1–8)")
st.divider()

# Sidebar Navigation
menu = [
    "Student Registration & Grades", 
    "Course Enrollment", 
    "Records & Participation", 
    "Search & Sort Data", 
    "Fee Calculation", 
    "File Management", 
    "Directory Scanner", 
    "Performance Analytics"
]
choice = st.sidebar.selectbox("Navigate Modules", menu)

# ==========================================
# MODULE 1: Student Registration
# ==========================================
if choice == "Student Registration & Grades":
    st.header("Grading & Registration (Lab 1)")
    with st.form("reg_form"):
        s_id = st.text_input("Student ID")
        name = st.text_input("Student Name")
        score = st.slider("Exam Score", 0, 100, 75)
        submitted = st.form_submit_button("Register Student")
        
        if submitted:
            grade, remark = evaluate_grade(score)
            st.session_state.student_records.append({
                "id": s_id, "name": name, "marks": score, "course_count": 0, "fee": 0.0
            })
            st.success(f"Registered {name}! Grade: {grade} ({remark})")

# ==========================================
# MODULE 2: Course Enrollment
# ==========================================
elif choice == "Course Enrollment":
    st.header("Course Enrollment Management (Lab 2)")
    names = [s["name"] for s in st.session_state.student_records]
    selected_name = st.selectbox("Select Student", names)
    
    c_name = st.text_input("Course Name")
    credits = st.number_input("Credit Value", min_value=1, max_value=5, value=3)
    
    if st.button("Enroll in Course"):
        for s in st.session_state.student_records:
            if s["name"] == selected_name:
                s["course_count"] += 1
                st.success(f"Enrolled {selected_name} into '{c_name}' ({credits} Credits).")

# ==========================================
# MODULE 3: Records & Sets
# ==========================================
elif choice == "Records & Participation":
    st.header("Student Record Data & Sets (Lab 3)")
    df_view = pd.DataFrame(st.session_state.student_records)
    st.dataframe(df_view, use_container_width=True)
    
    st.subheader("Event Participation Analysis (Sets)")
    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Common Participants", len(event_A & event_B), f"{event_A & event_B}")
    col2.metric("All Participants", len(event_A | event_B), f"Total Union")
    col3.metric("Only Event A", len(event_A - event_B), f"{event_A - event_B}")

# ==========================================
# MODULE 4: Search & Sort
# ==========================================
elif choice == "Search & Sort Data":
    st.header("Searching and Sorting algorithms (Lab 4)")
    records = list(st.session_state.student_records)
    
    action = st.radio("Select Operation", ["Original List", "Sort by Marks (Bubble Sort)", "Sort by ID (Selection Sort)"])
    
    if action == "Sort by Marks (Bubble Sort)":
        n = len(records)
        for i in range(n):
            for j in range(0, n-i-1):
                if records[j]["marks"] < records[j+1]["marks"]:
                    records[j], records[j+1] = records[j+1], records[j]
                    
    elif action == "Sort by ID (Selection Sort)":
        n = len(records)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if int(records[j]["id"]) < int(records[min_idx]["id"]): min_idx = j
            records[i], records[min_idx] = records[min_idx], records[i]

    st.table(records)
    
    st.subheader("Linear / Binary Search")
    search_id = st.text_input("Enter Student ID to find:")
    if search_id:
        found = next((s for s in records if s["id"] == search_id), None)
        if found: st.json(found)
        else: st.error("Record ID match not discovered.")

# ==========================================
# MODULE 5: Fee Calculation
# ==========================================
elif choice == "Fee Calculation":
    st.header("Fee Ledger Architecture (Lab 5)")
    names = [s["name"] for s in st.session_state.student_records]
    selected_name = st.selectbox("Select Student", names)
    
    tuition = st.number_input("Tuition Fee", value=50000)
    hostel = st.number_input("Hostel Fee", value=0)
    transport = st.number_input("Transportation Fee", value=0)
    
    if st.button("Compute & Update Fee Record"):
        total = calculate_fee(tuition, hostel, transport)
        for s in st.session_state.student_records:
            if s["name"] == selected_name:
                s["fee"] = float(total)
                st.success(f"Updated total structural dues for {selected_name}: ${total}")

# ==========================================
# MODULE 6: File Management
# ==========================================
elif choice == "File Management":
    st.header("File-Based Academic Records (Lab 6)")
    
    if st.button("Write Storage Matrix to student_records.txt"):
        with open("student_records.txt", "w") as f:
            f.write("ID,Name,Marks\n")
            for s in st.session_state.student_records:
                f.write(f"{s['id']},{s['name']},{s['marks']}\n")
        st.success("File written successfully.")

    if st.button("Read Content Back From File"):
        if os.path.exists("student_records.txt"):
            with open("student_records.txt", "r") as f:
                st.code(f.read(), language="text")
        else:
            st.error("File resource path not built yet.")

# ==========================================
# MODULE 7: Directory Scanner
# ==========================================
elif choice == "Directory Scanner":
    st.header("Directory Scanning Engine with Shielding (Lab 7)")
    path_input = st.text_input("Enter path target directory to scan:", ".")
    
    if st.button("Execute Trace Scan"):
        try:
            if not os.path.exists(path_input):
                raise FileNotFoundError(f"Invalid pathway location: {path_input}")
            
            output_lines = []
            for root, dirs, files in os.walk(path_input):
                level = root.replace(path_input, "").count(os.sep)
                indent = " " * 4 * level
                output_lines.append(f"{indent}{os.path.basename(root)}/")
                for f in files:
                    output_lines.append(f"{" " * 4 * (level + 1)}{f}")
            
            st.code("\n".join(output_lines), language="text")
        except Exception as ex:
            st.exception(ex)

# ==========================================
# MODULE 8: Data Analytics Pipeline
# ==========================================
elif choice == "Performance Analytics":
    st.header("Analytics Environment Dashboard (Lab 8)")
    
    csv_file = "student_performance.csv"
    if not os.path.exists(csv_file):
        sample_data = {
            "Name": ["Priya", "Rahul", "Anita", "Arjun", "Meera"],
            "Math": [85, 72, 95, 64, 92],
            "Science": [90, 88, 89, 78, 81],
            "English": [78, 91, 92, 85, 76]
        }
        pd.DataFrame(sample_data).to_csv(csv_file, index=False)

    df = pd.read_csv(csv_file)
    st.subheader("Raw Data Matrix Dataframe")
    st.dataframe(df, use_container_width=True)
    
    scores = df[["Math", "Science", "English"]].to_numpy()
    mean_scores = np.mean(scores, axis=0)
    
    st.subheader("NumPy Array Output Vectors")
    st.write(f"Mean Core Scores per Subject (Math, Science, English): **{mean_scores}**")
    
    # Matplotlib plots rendered dynamically directly on page canvas frame bounds
    st.subheader("Matplotlib Visualization Pipeline Matrices")
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    
    subjects = ["Math", "Science", "English"]
    ax[0].bar(subjects, mean_scores, color=["blue", "green", "orange"])
    ax[0].set_title("Average Scores per Subject")
    
    for subject in subjects:
        ax[1].plot(df["Name"], df[subject], marker='o', label=subject)
    ax[1].set_title("Student Comparison Matrix")
    ax[1].legend()
    
    st.pyplot(fig)