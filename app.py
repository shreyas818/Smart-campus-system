import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# LAB 7: User-defined Exception
# ==========================================
class MissingFileOrFolderError(Exception):
    """Raised when a required file or folder is missing in the directory."""
    pass

# ==========================================
# CORE MODULE FUNCTIONS (Labs 1, 2, 4, 5, 6, 7, 8)
# ==========================================

# Lab 1: Grade Evaluation
def evaluate_grade(score):
    if 90 <= score <= 100:
        return "A", "Excellent"
    elif score >= 75:
        return "B", "Very Good"
    elif score >= 60:
        return "C", "Good"
    elif score >= 40:
        return "D", "Average"
    else:
        return "F", "Needs Improvement"

# Lab 5: Fee Calculation
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    return tuition_fee + hostel_fee + transportation_fee

# Lab 4: Sorting Implementations
def bubble_sort_records(records):
    # Sorts copies of records descending by marks
    sorted_records = list(records)
    n = len(sorted_records)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_records[j]["marks"] < sorted_records[j + 1]["marks"]:
                sorted_records[j], sorted_records[j + 1] = sorted_records[j + 1], sorted_records[j]
    return sorted_records

def selection_sort_records(records):
    # Sorts copies of records ascending by ID
    sorted_records = list(records)
    n = len(sorted_records)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if int(sorted_records[j]["id"]) < int(sorted_records[min_idx]["id"]):
                min_idx = j
        sorted_records[i], sorted_records[min_idx] = sorted_records[min_idx], sorted_records[i]
    return sorted_records

# Lab 7: Directory Scanning Logic
def scan_directory(path):
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: {path}")
        
        print(f"\nScanning directory: {path}\n")
        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            sub_indent = " " * 4 * (level + 1)
            for f in files:
                print(f"{sub_indent}{f}")
                
            if not files and not dirs:
                raise MissingFileOrFolderError(f"Empty folder detected: {root}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except MissingFileOrFolderError as e:
        print(f"Custom Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# Lab 8: Analytics Engine using NumPy, Pandas & Matplotlib
def run_analytics_dashboard():
    csv_file = "student_performance.csv"
    
    # Auto-generate sample CSV file if it does not exist yet to prevent crashes
    if not os.path.exists(csv_file):
        sample_data = {
            "Name": ["Priya", "Rahul", "Anita", "Arjun", "Meera"],
            "Math": [85, 72, 95, 64, 92],
            "Science": [90, 88, 89, 78, 81],
            "English": [78, 91, 92, 85, 76]
        }
        pd.DataFrame(sample_data).to_csv(csv_file, index=False)
        print(f"[*] Generated baseline performance asset file: '{csv_file}'")

    try:
        df = pd.read_csv(csv_file)
        print("\n--- Pandas: Raw Performance Matrix View ---")
        print(df.head())
        
        print("\n--- Pandas: Statistical Summary Matrix ---")
        print(df.describe())
        
        # NumPy conversion & array execution
        scores = df[["Math", "Science", "English"]].to_numpy()
        mean_scores = np.mean(scores, axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev_scores = np.std(scores, axis=0)
        
        print("\n--- NumPy Matrix Analysis Array Outputs ---")
        print(f"Mean Scores (Math, Science, English): {mean_scores}")
        print(f"Median Scores (Math, Science, English): {median_scores}")
        print(f"Standard Deviation (Math, Science, English): {std_dev_scores}")
        
        print("\n--- Top Performers ---")
        print(f"Math: {df.loc[df['Math'].idxmax(), 'Name']}")
        print(f"Science: {df.loc[df['Science'].idxmax(), 'Name']}")
        print(f"English: {df.loc[df['English'].idxmax(), 'Name']}")
        
        # Visual charts using Matplotlib
        subjects = ["Math", "Science", "English"]
        plt.figure(figsize=(10, 4))
        
        plt.subplot(1, 2, 1)
        plt.bar(subjects, mean_scores, color=["blue", "green", "orange"])
        plt.title("Average Scores per Subject")
        plt.ylabel("Average Score")
        
        plt.subplot(1, 2, 2)
        # Dynamic pandas plot alternative configuration compatible with subplots
        for subject in subjects:
            plt.plot(df["Name"], df[subject], marker='o', label=subject)
        plt.title("Student Performance Comparison")
        plt.ylabel("Scores")
        plt.legend()
        
        plt.tight_layout()
        print("\n[*] Displaying chart visualizations...")
        plt.show()
        
    except FileNotFoundError:
        print("Error: The performance data CSV file was not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# ==========================================
# MAIN APPLICATION MANAGEMENT LOOP
# ==========================================
def main():
    # Lab 3: Central Database Storage State (List of Dictionaries)
    student_records = [
        {"id": "101", "name": "Arjun", "marks": 85, "course_count": 0, "fee": 50000.0},
        {"id": "102", "name": "Meera", "marks": 92, "course_count": 0, "fee": 80000.0}
    ]
    
    # Lab 3: Participation sets
    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}

    while True:
        print("\n" + "="*50)
        print("     SMART CAMPUS INFORMATION SYSTEM (INTEGRATED)     ")
        print("="*50)
        print("1. Student Registration & Grade Evaluation (Lab 1)")
        print("2. Course Enrollment Management (Lab 2)")
        print("3. View Records & Participation Analysis (Lab 3)")
        print("4. Search & Sort Student Data (Lab 4)")
        print("5. Fee Calculation Module (Lab 5)")
        print("6. File-Based Academic Record Generator (Lab 6)")
        print("7. Directory Scanner with Exception Shield (Lab 7)")
        print("8. Run Performance Analytics Engine (Lab 8)")
        print("9. Exit Application")
        print("-"*50)
        
        choice = input("Select an option (1-9): ").strip()
        
        if choice == "1":
            print("\n--- [Lab 1] Registration & Grade Evaluation ---")
            s_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            score = float(input("Enter Exam Score (0-100): "))
            
            grade, remark = evaluate_grade(score)
            
            # Store into database
            student_records.append({
                "id": s_id, "name": name, "marks": score, "course_count": 0, "fee": 0.0
            })
            
            print("\n--- Evaluation Report Generated ---")
            print(f"Registered: {name} (ID: {s_id}) | Score: {score} | Grade: {grade} | [{remark}]")

        elif choice == "2":
            print("\n--- [Lab 2] Course Enrollment Management ---")
            name_query = input("Enter student name for enrollment processing: ")
            found_student = next((s for s in student_records if s["name"].lower() == name_query.lower()), None)
            
            if not found_student:
                print("Student not found in active operational record context.")
                continue
                
            enrolled_courses = []
            max_courses = 5
            while len(enrolled_courses) < max_courses:
                c_name = input(f"Enter course name (or 'done' to finish updates) [{len(enrolled_courses)}/{max_courses}]: ").strip()
                if c_name.lower() == 'done':
                    break
                credits = input("Enter credit value: ").strip()
                
                if not credits.isdigit() or int(credits) <= 0:
                    print("Invalid operational credit data. Skipping entry item processing...")
                    continue
                    
                enrolled_courses.append((c_name, int(credits)))
                print(f"Course '{c_name}' successfully parsed.")
            
            found_student["course_count"] = len(enrolled_courses)
            print(f"\nEnrollment Completed. Total Enrolled Courses: {len(enrolled_courses)}")

        elif choice == "3":
            print("\n--- [Lab 3] Student Record Storage Management ---")
            for s in student_records:
                print(f"ID: {s['id']} | Name: {s['name']:<10} | Score Marks: {s['marks']:<4} | Active Courses: {s['course_count']}")
            
            print("\n--- Event Participation Set Matrix Analysis ---")
            print("Common Participants (Intersection):", event_A & event_B)
            print("All Registered Participants (Union):", event_A | event_B)
            print("Exclusively Event A Matrix (Difference):", event_A - event_B)

        elif choice == "4":
            print("\n--- [Lab 4] Searching and Sorting Data ---")
            if not student_records:
                print("Database cache empty.")
                continue
            
            print("1. Sort by Marks Descending (Bubble Sort)")
            print("2. Sort by Student ID Ascending (Selection Sort)")
            print("3. Search Record by ID (Linear/Binary Search Execution)")
            sub_choice = input("Selection: ")
            
            if sub_choice == "1":
                res = bubble_sort_records(student_records)
                print("\nSorted Matrix Results (Bubble Sort):")
                for s in res: print(f"Marks: {s['marks']} -> ID: {s['id']}, Name: {s['name']}")
            elif sub_choice == "2":
                res = selection_sort_records(student_records)
                print("\nSorted Matrix Results (Selection Sort):")
                for s in res: print(f"ID: {s['id']} -> Name: {s['name']}, Marks: {s['marks']}")
            elif sub_choice == "3":
                target_id = input("Enter Target Student ID to lookup: ").strip()
                # Run binary search over an ID sorted workspace sequence array natively
                workspace = selection_sort_records(student_records)
                low, high, found_idx = 0, len(workspace) - 1, -1
                
                while low <= high:
                    mid = (low + high) // 2
                    if workspace[mid]["id"] == target_id:
                        found_idx = mid
                        break
                    elif int(workspace[mid]["id"]) < int(target_id):
                        low = mid + 1
                    else:
                        high = mid - 1
                
                if found_idx != -1:
                    match = workspace[found_idx]
                    print(f"Success! Found via Binary Search at index sequence target position [{found_idx}]. Data:")
                    print(f"-> Name: {match['name']} | Marks: {match['marks']} | Fee State: ${match['fee']}")
                else:
                    print("Record target ID key profile target not recovered.")

        elif choice == "5":
            print("\n--- [Lab 5] Fee Calculation System Function ---")
            name_query = input("Enter student name: ")
            found_student = next((s for s in student_records if s["name"].lower() == name_query.lower()), None)
            
            if found_student:
                t_fee = float(input("Enter Base Tuition Fee: "))
                h_fee = float(input("Enter Hostel Fee (Enter 0 if None): ") or 0)
                tr_fee = float(input("Enter Transportation Fee (Enter 0 if None): ") or 0)
                
                computed = calculate_fee(t_fee, h_fee, tr_fee)
                found_student["fee"] = computed
                print(f"Fee ledger context written successfully. Total Computed Net: ${computed}")
            else:
                print("Student identity lookup key missing from current tracking register context.")

        elif choice == "6":
            print("\n--- [Lab 6] File-Based Record Management Pipeline ---")
            filename = "student_records.txt"
            with open(filename, "w") as f:
                f.write("ID,Name,Marks\n")
                for s in student_records:
                    f.write(f"{s['id']},{s['name']},{s['marks']}\n")
            print(f"Records committed to disk output stream target: '{filename}'")
            
            print("\nVerifying File IO Integrity (Reading back written content):")
            with open(filename, "r") as f:
                for line in f:
                    print(line.strip())

        elif choice == "7":
            print("\n--- [Lab 7] Directory Structural Scanner Engine ---")
            target_dir = input("Enter workspace directory path value (e.g. '.'): ").strip()
            scan_directory(target_dir)

        elif choice == "8":
            print("\n--- [Lab 8] Science Stack Analytics Processing Dashboard ---")
            run_analytics_dashboard()

        elif choice == "9":
            print("\nShutting down Smart Campus Infrastructure Engine context layer safely. Goodbye!")
            break
        else:
            print("Invalid input code. Selection out of structural menu operational bounds index.")

if __name__ == "__main__":
    main()