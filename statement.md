# Problem Statement & Project Scope

## 1. Problem Statement
Educational institutions frequently encounter challenges when manually handling student demographic records and academic evaluations. Maintaining records across disparate spreadsheets or paper forms leads to data inconsistency, slow retrieval times, and increased vulnerability to calculation errors when determining student totals, percentages, and pass/fail statuses. There is a need for a centralized, modular, and lightweight command-line system that allows academic staff to perform quick record searches, register new student profiles, update subject marks, and compute performance results automatically.

## 2. Project Scope
The **Student Record Management System** provides an in-memory, CLI-based solution designed to streamline student administration. 

### In-Scope:
* **Student Record Creation:** Registering student profiles with metadata including ID, Name, Age, Status (Hosteller/Day Scholar), State, Course, and Semester.
* **Academic Calculation Engine:** Accepting subject-wise marks, automatically calculating total aggregate marks, overall percentages, and evaluating pass/fail status based on institutional criteria.
* **Search & Display:** Fetching individual records by Student ID or listing all enrolled students in a structured summary table.
* **Marks Management:** Updating subject marks dynamically for existing student profiles.
* **System Testing:** Unit validation suite to verify calculation accuracy.

### Out-of-Scope:
* Graphical User Interface (GUI) or Web Interface.
* External relational database management systems (RDBMS).

## 3. Target Users
* **Academic Administrators:** Staff responsible for enrolling new students and updating official demographic records.
* **Faculty / Course Coordinators:** Instructors who enter subject marks and generate performance results.
* **Department Evaluators:** Personnel needing rapid lookups of student registration details and academic standings.

## 4. High-Level Features
1. **Interactive CLI Navigation:** Menu-driven interface supporting direct Student ID lookups and structured sub-menus.
2. **Student Profile Management:** Add and store multi-attribute student records.
3. **Academic Evaluation:** Automatic total, percentage, and pass/fail result generation upon mark entry.
4. **Marks Update Functionality:** Modify academic records without re-entering demographic profile data.
5. **System Validation:** Integrated testing script to ensure mathematical correctness of academic performance evaluations.