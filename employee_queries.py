import sqlite3


def questions_company(employee_name):
    """Finds all employees with the specified by name ."""

    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()

    sql_query_1 = "SELECT * FROM Employees WHERE name = ?;"
    cursor.execute(sql_query_1, (employee_name,))

    results = cursor.fetchall()
    if len(results) <= 0:
        return 'unfortunately we can not find that employee'
    else:
        return f"Results for {employee_name}: {results}"
    
def questions_manager(manager_id):
    """Finds all employees managed by the given ManagerID."""
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()

    sql_query = "SELECT * FROM Employees WHERE id = ?;"

    cursor.execute(sql_query, (manager_id,))

    results = cursor.fetchall()
    print(results)

    if len(results) <= 0:
        return f'Unfortunately, no employees are currently reporting to Manager ID {manager_id}.'
    else:
        return f"Employees reporting to Manager ID {manager_id}: {results}"
    
def questions_department(dept_name):
    """Finds all employees in the specified department."""
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()

    sql_query = "SELECT * FROM Employees LEFT JOIN Departments ON Employees.department_id = Departments.manager_id  WHERE department_id = ?;"

    cursor.execute(sql_query, (dept_name,))

    results = cursor.fetchall()
    print(results)

    if len(results) <= 0:
        return f'Unfortunately, the department "{dept_name}" could not be found.'
    else:
        return f"Employees in the {dept_name}: {results}"
    
def questions_title(job_title):
    """Finds all employees with the specified job title."""
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()

    sql_query = "SELECT * FROM Employees WHERE role = ?;"

    cursor.execute(sql_query, (job_title,))

    results = cursor.fetchall()
    print(results)

    if len(results) <= 0:
        return f'Unfortunately, no employees were found with the title "{job_title}".'
    else:
        return f"Employees with the title '{job_title}': {results}"

