---

# Smart Campus Information System

A comprehensive, interactive web dashboard built with **Streamlit** that integrates various academic operations, data analytics, and data-structure algorithms into a unified **8-Lab Academic Framework**.

---

## 🚀 Features Matrix

The application is structured as a multi-page dashboard managed via a centralized layout router, covering the following core technical modules:

| Module / Lab | Feature | Technical Stack / Components |
| --- | --- | --- |
| **Lab 1 & 5** | **Registration & Fees** | Dynamic Streamlit forms, conditional logic, and conditional tuition fee ledger computation. |
| **Lab 3** | **Records & Sets** | Pandas DataFrame viewports mixed with Python Mathematical Set operations (`Union`, `Intersection`, `Difference`) for event analytics. |
| **Lab 4** | **Search & Sort Matrix** | Low-level execution of **Bubble Sort** (by Marks) and **Selection Sort** (by ID), accompanied by search lookups. |
| **Lab 6 & 7** | **File IO & Exception Shield** | Local system disk streaming (`.txt` writing/parsing) paired with a robust `try-except` directory tree mapper (`os.walk`). |
| **Lab 8** | **Data Analytics Pipeline** | Matrix manipulation via **NumPy**, tabular ingestion with **Pandas**, and vector visualization plots using **Matplotlib**. |

---

## 🛠️ Tech Stack & Dependencies

* **UI Framework:** Streamlit (Wide-mode custom grid layout)
* **Styling Engine:** Embedded HTML5 & CSS3 injection
* **Data Science Suite:** NumPy, Pandas, Matplotlib
* **System Engine:** Native Python OS filesystem libraries

---

## 💻 Installation & Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-campus-system.git
cd smart-campus-system

```

### 2. Install Dependencies

Ensure you have Python 3.8+ installed, then run:

```bash
pip install streamlit numpy pandas matplotlib

```

### 3. Run the Application

Execute the Streamlit server deployment command:

```bash
streamlit run app.py

```

---

## 📂 Project Architecture

```text
smart-campus-system/
│
├── app.py                      # Main application monolithic script
├── student_records.txt         # Lab 6: Local Disk I/O Target File (Generated)
└── student_performance.csv     # Lab 8: Analytics Pipeline Seed File (Generated)

```

---

## 🧠 Core Backend Core Logic Snippet Examples

### Custom Grade Evaluation Engine

$$\text{Grade} = \begin{cases} 
A & \text{if } 90 \le \text{score} \le 100 \\ 
B & \text{if } 75 \le \text{score} < 90 \\ 
C & \text{if } 60 \le \text{score} < 75 \\ 
D & \text{if } 40 \le \text{score} < 60 \\ 
F & \text{if } \text{score} < 40 
\end{cases}$$

### Fee Ledger Accumulation Formula

$$\text{Total Fee} = \text{Tuition} + \text{Hostel} + \text{Transport}$$

---

> 💡 **Session State Notice:** This system leverages Streamlit's global `st.session_state` cache runtime buffer to maintain structural state and record memory consistency across subpage routing loops without needing an external heavy database instance.
