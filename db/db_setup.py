# db_setup.py
import sqlite3

def setup_database():
    conn = sqlite3.connect("company.db")
    cursor = conn.cursor()

    # Drop tables if they exist to start fresh
    cursor.execute("DROP TABLE IF EXISTS employees;")
    cursor.execute("DROP TABLE IF EXISTS departments;")
    cursor.execute("DROP TABLE IF EXISTS projects;")

    # Create tables
    cursor.execute("""
        CREATE TABLE departments (
            department_id INTEGER PRIMARY KEY,
            department_name TEXT NOT NULL UNIQUE
        );
    """)

    cursor.execute("""
        CREATE TABLE employees (
            employee_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone_number TEXT,
            hire_date DATE,
            job_id TEXT,
            salary REAL,
            department_id INTEGER,
            CONSTRAINT fk_department
                FOREIGN KEY (department_id)
                REFERENCES departments (department_id)
        );
    """)

    cursor.execute("""
        CREATE TABLE projects (
            project_id INTEGER PRIMARY KEY,
            project_name TEXT NOT NULL,
            start_date DATE,
            end_date DATE,
            budget REAL,
            department_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments(department_id)
        );
    """)

    # Insert data into departments
    departments_data = [
        (1, 'Sales'),
        (2, 'Marketing'),
        (3, 'Engineering'),
        (4, 'Human Resources'),
        (5, 'Finance')
    ]
    cursor.executemany("INSERT INTO departments VALUES (?, ?)", departments_data)

    # Insert data into employees
    employees_data = [
        (101, 'John', 'Doe', 'john.doe@example.com', '123-456-7890', '2020-01-15', 'SE_MGR', 90000.00, 3),
        (102, 'Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '2021-03-20', 'SALES_REP', 60000.00, 1),
        (103, 'Peter', 'Jones', 'peter.jones@example.com', '555-123-4567', '2019-07-01', 'DEV', 75000.00, 3),
        (104, 'Alice', 'Williams', 'alice.w@example.com', '111-222-3333', '2022-05-10', 'HR_REP', 55000.00, 4),
        (105, 'Bob', 'Johnson', 'bob.j@example.com', '444-555-6666', '2020-11-25', 'FIN_ANALYST', 80000.00, 5),
        (106, 'Charlie', 'Brown', 'charlie.b@example.com', '777-888-9999', '2023-01-01', 'SALES_MGR', 70000.00, 1)
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", employees_data)

    # Insert data into projects
    projects_data = [
        (1, 'Project Alpha', '2023-01-01', '2023-06-30', 150000.00, 3),
        (2, 'Project Beta', '2023-03-15', '2023-09-30', 200000.00, 3),
        (3, 'Marketing Campaign A', '2023-02-01', '2023-04-30', 50000.00, 2),
        (4, 'Sales Strategy 2024', '2023-10-01', '2024-03-31', 75000.00, 1)
    ]
    cursor.executemany("INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?)", projects_data)

    conn.commit()
    conn.close()
    print("Database 'company.db' created and populated successfully.")

if __name__ == "__main__":
    setup_database()