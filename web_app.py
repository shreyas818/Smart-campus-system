import streamlit as st
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set page configuration to wide mode for the grid layout
st.set_page_config(page_title="Smart Campus Information System", layout="wide")

# Initialize session state for database storage if it doesn't exist
if "student_records" not in st.session_state:
    st.session_state.student_records = [
        {"id": "101", "name": "Arjun", "marks": 85, "course_count": 2, "fee": 50000.0},
        {"id": "102", "name": "Meera", "marks": 92, "course_count": 3, "fee": 80000.0}
    ]
if "active_page" not in st.session_state:
    st.session_state.active_page = "Home"

# --- Backend Logic Functions (Labs 1, 5) ---
def evaluate_grade(score):
    if 90 <= score <= 100: return "A", "Excellent"
    elif score >= 75: return "B", "Very Good"
    elif score >= 60: return "C", "Good"
    elif score >= 40: return "D", "Average"
    else: return "F", "Needs Improvement"

def calculate_fee(tuition, hostel=0, transport=0):
    return tuition + hostel + transport

# --- STYLING: CSS for Campus Theme and Grid Cards ---
st.markdown("""
    <style>
    /* Styling the Main Banner Header */
    .banner {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        border: 1px solid #e0e0e0;
    }
    .banner h1 {
        color: #1e3d59;
        font-family: 'Arial Black', Gadget, sans-serif;
        margin: 0;
        letter-spacing: 1px;
    }
    .banner p {
        color: #7f8c8d;
        margin: 5px 0 0 0;
        font-size: 14px;
    }
    
    /* Styling the Grid Cards */
    .card {
        padding: 30px 20px;
        border-radius: 8px;
        text-align: center;
        color: white;
        font-weight: bold;
        font-size: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
        margin-bottom: 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .blue-card { background-color: #6c5ce7; }
    .green-card { background-color: #2ecc71; }
    .purple-card { background-color: #9b59b6; }
    .red-card { background-color: #e74c3c; }
    .orange-card { background-color: #f39c12; }
    .pink-card { background-color: #fd79a8; }
    .cyan-card { background-color: #00cec9; }
    </style>
""", unsafe_allow_html=True)

# --- HEADER BANNER ---
st.markdown("""
    <div class="banner">
        <h1>SMART CAMPUS INFORMATION SYSTEM</h1>
        <p>Empowering Education. Inspiring Futures.</p>
    </div>
""", unsafe_allow_html=True)

# Add a "Back to Home" button if inside a submodule view
if st.session_state.active_page != "Home":
    if st.button("⬅️ Back to Main Dashboard"):
        st.session_state.active_page = "Home"
        st.rerun()

# ==========================================
# CENTRAL ROUTING CONTROLLER
# ==========================================

# --- PAGE: HOME DASHBOARD (The Grid Layout) ---
if st.session_state.active_page == "Home":
    
    st.markdown("<h3 style='text-align: center; color: #34495e; margin-bottom: 25px;'>KNOWLEDGE IS POWER</h3>", unsafe_allow_html=True)
    
    # Grid Layout Construction: 3 Columns
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    row2_col1, row2_col2, row2_col3 = st.columns(3)
    
    # Row 1 Buttons & Styling Cards
    with row1_col1:
        st.markdown('<div class="card blue-card">📋 Registration</div>', unsafe_allow_html=True)
        if st.button("Open Registration Form", key="btn_reg", use_container_width=True):
            st.session_state.active_page = "Registration"
            st.rerun()

    with row1_col2:
        st.markdown('<div class="card green-card">🗂️ Records</div>', unsafe_allow_html=True)
        if st.button("View Records & Sets", key="btn_rec", use_container_width=True):
            st.session_state.active_page = "Records"
            st.rerun()

    with row1_col3:
        st.markdown('<div class="card purple-card">🔍 Search & Sort</div>', unsafe_allow_html=True)
        if st.button("Run Sorting Algorithms", key="btn_search", use_container_width=True):
            st.session_state.active_page = "Search"
            st.rerun()

    # Row 2 Buttons & Styling Cards
    with row2_col1:
        st.markdown('<div class="card red-card">💾 File Management</div>', unsafe_allow_html=True)
        if st.button("Access Virtual Local IO", key="btn_file", use_container_width=True):
            st.session_state.active_page = "Files"
            st.rerun()

    with row2_col2:
        st.markdown('<div class="card orange-card">💰 Fees System</div>', unsafe_allow_html=True)
        if st.button("Calculate Fees Ledger", key="btn_fees", use_container_width=True):
            st.session_state.active_page = "Fees"
            st.rerun()

    with row2_col3:
        st.markdown('<div class="card cyan-card">📊 Performance</div>', unsafe_allow_html=True)
        if st.button("Launch Analytics Engine", key="btn_analytics", use_container_width=True):
            st.session_state.active_page = "Analytics"
            st.rerun()

# --- SUBPAGE: REGISTRATION (Lab 1) ---
elif st.session_state.active_page == "Registration":
    st.header("📝 Student Registration & Grade Evaluation (Lab 1)")
    with st.form("reg_form"):
        s_id = st.text_input("Enter Student ID")
        name = st.text_input("Enter Student Name")
        score = st.slider("Select Exam Score (0-100)", 0, 100, 75)
        submitted = st.form_submit_button("Submit Registration")
        
        if submitted:
            if s_id and name:
                grade, remark = evaluate_grade(score)
                st.session_state.student_records.append({
                    "id": s_id, "name": name, "marks": score, "course_count": 0, "fee": 0.0
                })
                st.success(f"Successfully Registered {name}! Evaluated Grade: {grade} ({remark})")
            else:
                st.error("Please fill in all identity text fields.")

# --- SUBPAGE: RECORDS & PARTICIPATION (Lab 3) ---
elif st.session_state.active_page == "Records":
    st.header("🗂️ Student Record Storage & Participation Sets (Lab 3)")
    df_view = pd.DataFrame(st.session_state.student_records)
    st.dataframe(df_view, use_container_width=True)
    
    st.subheader("Event Participation Analysis (Set Operations)")
    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Common Participants (Intersection)", len(event_A & event_B), f"{event_A & event_B}")
    c2.metric("All Registered (Union)", len(event_A | event_B), "Total Distinct")
    c3.metric("Exclusively Event A (Difference)", len(event_A - event_B), f"{event_A - event_B}")

# --- SUBPAGE: SEARCH & SORT (Lab 4) ---
elif st.session_state.active_page == "Search":
    st.header("🔍 Algorithms Matrix: Searching & Sorting (Lab 4)")
    records = list(st.session_state.student_records)
    
    action = st.radio("Select Sorting Strategy:", ["None", "Bubble Sort (Descending Marks)", "Selection Sort (Ascending ID)"])
    
    if action == "Bubble Sort (Descending Marks)":
        n = len(records)
        for i in range(n):
            for j in range(0, n-i-1):
                if records[j]["marks"] < records[j+1]["marks"]:
                    records[j], records[j+1] = records[j+1], records[j]
    elif action == "Selection Sort (Ascending ID)":
        n = len(records)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if int(records[j]["id"]) < int(records[min_idx]["id"]): min_idx = j
            records[i], records[min_idx] = records[min_idx], records[i]

    st.table(records)
    
    st.subheader("Binary Search Verification")
    search_id = st.text_input("Enter Target Student ID:")
    if search_id:
        found = next((s for s in records if s["id"] == search_id), None)
        if found: 
            st.json(found)
        else: 
            st.error("No data entries matched that query key.")

# --- SUBPAGE: FEES (Lab 5) ---
elif st.session_state.active_page == "Fees":
    st.header("💰 Fee Calculation Architecture Module (Lab 5)")
    names = [s["name"] for s in st.session_state.student_records]
    selected_name = st.selectbox("Select Target Profile:", names)
    
    t_fee = st.number_input("Base Tuition Fee", value=50000)
    h_fee = st.number_input("Hostel Fee", value=0)
    tr_fee = st.number_input("Transportation Fee", value=0)
    
    if st.button("Compute Total & Commit Dues"):
        total = calculate_fee(t_fee, h_fee, tr_fee)
        for s in st.session_state.student_records:
            if s["name"] == selected_name:
                s["fee"] = float(total)
                st.success(f"Fee records structural ledger updated for {selected_name}: Total Computed Net = ${total}")

# --- SUBPAGE: FILES & SCANNING (Labs 6, 7) ---
elif st.session_state.active_page == "Files":
    st.header("💾 File Handling & Directory Scanning Exception Shield (Labs 6 & 7)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("File I/O Streams (Lab 6)")
        if st.button("Commit Current Database to Disk File"):
            with open("student_records.txt", "w") as f:
                f.write("ID,Name,Marks\n")
                for s in st.session_state.student_records:
                    f.write(f"{s['id']},{s['name']},{s['marks']}\n")
            st.success("Successfully pushed elements to disk target 'student_records.txt'.")
            
        if st.button("Read Content Back From Disk Stream"):
            if os.path.exists("student_records.txt"):
                with open("student_records.txt", "r") as f:
                    st.code(f.read(), language="text")
            else:
                st.error("File data layer has not been structuralized on disk memory space yet.")
                
    with col2:
        st.subheader("Directory Scanning Tracker (Lab 7)")
        path_input = st.text_input("Enter directory file path location to structural map:", ".")
        if st.button("Initialize Deep Walk Scan"):
            try:
                if not os.path.exists(path_input):
                    raise FileNotFoundError(f"Invalid path verification match: {path_input}")
                
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
# MODULE 8: DATA ANALYTICS PIPELINE
# ==========================================
elif st.session_state.active_page == "Analytics":
    st.header("📊 NumPy, Pandas, & Matplotlib Analytics Suite (Lab 8)")
    
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
    st.subheader("Dataframe Matrix View (Pandas)")
    st.dataframe(df, use_container_width=True)
    
    scores = df[["Math", "Science", "English"]].to_numpy()
    mean_scores = np.mean(scores, axis=0)
    
    st.subheader("Numerical Analytics Output Matrices (NumPy)")
    st.info(f"Calculated Core Mean Score Array Vectors (Math, Science, English): **{mean_scores}**")
    
    st.subheader("Matplotlib Graphic Visualization Viewport")
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    
    subjects = ["Math", "Science", "English"]
    ax[0].bar(subjects, mean_scores, color=["#3498db", "#2ecc71", "#e67e22"])
    ax[0].set_title("Average Scores per Subject")
    ax[0].set_ylabel("Marks Value Context")
    
    for subject in subjects:
        ax[1].plot(df["Name"], df[subject], marker='o', linewidth=2, label=subject)
    ax[1].set_title("Cross Comparison Framework Performance Matrix")
    ax[1].legend()
    
    st.pyplot(fig)