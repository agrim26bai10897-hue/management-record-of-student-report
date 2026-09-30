# Student Record Management System - Comprehensive Project Report

**Course Evaluation:** Flipped Course Project (VITyarthi)  
**Student Name:** Agrim Pandey
**Program & Branch:** B.Tech CSE (ai-ml)  
**Institution:** VIT Bhopal University  
**Date:** September 2026  

---

## 1. Introduction
The **Student Record Management System** is a modular Python command-line application built to streamline student profile registration, grade calculation, dynamic scorecard updating, and batch analytics. Developed under structured modular programming principles, it offers fast ID-based lookups, dual-layer institutional pass/fail grading, and CSV report export.

---

## 2. Problem Statement
Manual student record administration using loose spreadsheets or paper registers leads to:
1. Clerical and calculation errors when calculating totals and percentages across large student batches.
2. Inconsistent enforcement of pass criteria (minimum 40 per subject AND 40% aggregate).
3. Slow student record lookups during departmental advising.
4. Tedious recalculation during mark updates and re-evaluations.

This project delivers a centralized, local terminal application that validates user inputs, computes metrics automatically, and exports structured reports.

---

## 3. Functional Requirements
- **FR-01 (Student Registration):** Register student profiles with ID, Name, Age (15-100), Status, State, Program, Semester, and 3-subject marks.
- **FR-02 (Academic Computation):** Automated total score, percentage calculation, and pass/fail evaluation (subject cutoff >= 40, aggregate >= 40%).
- **FR-03 (Record Lookup):** Instant search by Student ID displaying formatted profile cards.
- **FR-04 (Marks Management):** Dynamic scorecard updates with real-time recalculation of results.
- **FR-05 (Batch Summary):** Formatted terminal table view of all enrolled students.
- **FR-06 (Batch Analytics):** Computes class average, pass rate, top performer, and subject-wise averages.
- **FR-07 (CSV Data Export):** Generates `student_report.csv` for external use.
- **FR-08 (Automated Testing):** Built-in unit validation suite checking calculation boundaries and file output.

---

## 4. Non-Functional Requirements
- **Usability:** Menu-driven interface with clear input prompts and defensive error messages.
- **Performance:** $O(1)$ dictionary lookups ensuring sub-millisecond response times.
- **Reliability:** `try-except` boundary checks preventing program crashes on invalid inputs.
- **Modularity:** 6 clean modules separating presentation, business logic, storage, analytics, and testing.
- **Resource Efficiency:** Zero third-party packages; runs on standard Python 3.13 library.

---

## 5. System Architecture
```text
+--------------------------------------------------------------------------+
|                        PRESENTATION LAYER (CLI)                          |
|                       main.py (Menu Loop & Input)                        |
+------------------------------------+-------------------------------------+
                                     |
                                     v
+------------------------------------+-------------------------------------+
|                         APPLICATION LAYER                                |
|  +-------------------------------+   +--------------------------------+  |
|  |       student_manager.py      |   |       report_generator.py      |  |
|  |  (Search, Add, Update, Table) |   |    (Analytics & CSV Export)    |  |
|  +---------------+---------------+   +---------------+----------------+  |
+------------------|-----------------------------------|-------------------+
                   |                                   |
                   v                                   v
+--------------------------------------------------------------------------+
|                         BUSINESS LOGIC LAYER                             |
|               academic_engine.py (Formulas, Cutoffs, Rules)              |
+------------------------------------+-------------------------------------+
                                     |
                                     v
+--------------------------------------------------------------------------+
|                          DATA & STORAGE LAYER                            |
|             data_store.py (Dictionary Database) / student_report.csv     |
+--------------------------------------------------------------------------+
```

---

## 6. Design Diagrams

### 6.1 Use Case Diagram
```text
                  +----------------------------------------------+
                  |         Student Record Management            |
                  |                                              |
                  |   ( Search Student by ID ) <---------------+ |
                  |                                             \|
                  |   ( Register New Student ) <----------------( Faculty / )
                  |                                             ( Academic  )
                  |   ( Update Student Marks ) <----------------( Staff     )
                  |                                             /|
                  |   ( View Enrolled Summary ) <--------------+ |
                  |                                             \|
                  |   ( Generate Analytics & CSV ) <-----------+ |
                  |                                              |
                  |   ( Run Validation Test Suite ) <----------+ |
                  +----------------------------------------------+
```

### 6.2 Workflow Diagram
```text
 [ Start ] --> [ Main Screen ]
                     |
                     +---> [ ID ]   ---> [ Search & Display Profile ]
                     +---> [ NEW ]  ---> [ Register Profile & Marks ]
                     +---> [ MENU ] ---> [ Sub-Menu: 1 to 7 ]
                     |                       |-> (1) Search
                     |                       |-> (2) Add
                     |                       |-> (3) Update Marks
                     |                       |-> (4) Display Table
                     |                       |-> (5) Batch Analytics
                     |                       |-> (6) Export CSV
                     |                       |-> (7) Back
                     +---> [ EXIT ] ---> [ Terminate ]
```

### 6.3 Sequence Diagram (Marks Update)
```text
User           main.py         student_manager     academic_engine      data_store
 |                |                   |                   |                  |
 |-- Select (3) ->|                   |                   |                  |
 |                |-- update_marks() >|                   |                  |
 |                |                   |-- Query ID ------------------------->|
 |                |                   |<- Return data -----------------------|
 |                |<-- Prompt marks --|                   |                  |
 |-- Enter marks >|                   |                   |                  |
 |                |                   |-- calculate() --->|                  |
 |                |                   |<- new metrics ----|                  |
 |                |                   |-- Write updated dictionary --------->|
 |<-- Success ----|<------------------|                   |                  |
```

### 6.4 Schema Design
```text
STUDENT RECORD ENTITY
-----------------------------------------------------------------------------
Field         Type          Description
-----------------------------------------------------------------------------
StudentID     String (PK)   Unique student identifier (e.g., 'VIT001')
Name          String        Full legal name of the student
Age           Integer       Student age (15 <= Age <= 100)
Status        String        'Hosteller' or 'Day Scholar'
State         String        Home state of origin
Course        String        Degree program (e.g., 'B.Tech CSE')
Semester      Integer       Academic semester (1 <= Semester <= 12)
Marks         Dictionary    Keys: Math, Physics, CS (Scores: 0 to 100)
Total         Float         Sum of subject marks (out of 300)
Percentage    Float         Calculated aggregate percentage
Result        String        'Pass' (if all sub >= 40 and % >= 40) else 'Fail'
-----------------------------------------------------------------------------
```

---

## 7. Implementation & Code Structure
The system is divided into 6 modular Python files:
1. `data_store.py`: In-memory student records dictionary.
2. `academic_engine.py`: Academic calculation engine and pass/fail evaluation logic.
3. `student_manager.py`: Input validation, search, addition, updates, and tabular display.
4. `report_generator.py`: Aggregate batch statistics and CSV reporting.
5. `main.py`: Interactive CLI navigation and menu execution.
6. `test_system.py`: Comprehensive automated test assertions.

---

## 8. Testing Approach
Automated validation checks in `test_system.py`:
- **Test 1:** Normal passing marks calculation.
- **Test 2:** Cutoff boundary check (marks < 40 causing failure).
- **Test 3:** Empty marks fallback.
- **Test 4:** Statistical aggregations (mean, pass rate, top student).
- **Test 5:** CSV export and file integrity verification.

All tests execute and pass with 100% assertion success.

---

## 9. Challenges Faced & Learnings
- **Console Character Encoding:** Resolved encoding limitations on Windows terminals by replacing non-ASCII glyphs with standard bracket tags (`[OK]`).
- **Defensive Input Handling:** Utilized `while-try-except` loops to gracefully reject non-numeric inputs.
- **Modular Software Design:** Demonstrated separation of concerns and reusable software design.

---

## 10. References
- Python 3 Documentation (https://docs.python.org/3/)
- PEP 8 Python Style Guidelines (https://peps.python.org/pep-0008/)
- VIT Bhopal University Course Guidelines (VITyarthi)
