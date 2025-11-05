tools = [
    {
        "type": "function",
        "function": {
            "name": "get_employee_details",
            "description": "Retrieves all available data for a specific employee by their exact name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "employee_name": {
                        "type": "string",
                        "description": "search for the name, lastname and full name."
                    }
                },
                "required": ["employee_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_reports_by_manager_id",
            "description": "Finds all direct reports given a manager's unique numerical Employee ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "manager_id": {
                        "type": "integer",
                        "description": "The unique numerical ID of the manager (e.g., 1 for CEO, 2 for COO)."
                    }
                },
                "required": ["manager_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_employees_by_department",
            "description": "Retrieves the list of employees belonging to a specified department.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dept_name": {
                        "type": "string",
                        "description": "The full name of the department (e.g., 'IT Department', 'Finance Department')."
                    }
                },
                "required": ["dept_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_employees_by_job_title",
            "description": "Finds all employees who have a specific job title.",
            "parameters": {
                "type": "object",
                "properties": {
                    "job_title": {
                        "type": "string",
                        "description": "The exact job title to search for (e.g., 'Systems Administrator', 'Sales Manager')."
                    }
                },
                "required": ["job_title"]
            }
        }
    }
]


system_prompt = """
You are a Bot that assists in answering clients questions based on the database.
answer in a natural way as a human not a computer, donot mention the id under any circumstances.
Please answer which category type is the question that the user is asking.
<categories>
Employee : here we have a table of all our employees, use this table when we need to get some information out of only the employee table
Department: here we have a table of all our departments, use this table when we need to answer a question based only on department table
Employee_Department: here we will have a joined table of Employee and Department, use this table for information that may require information from both the employee table and the department table
Here is the schema of the final answer for our question
<SCHEMA>
class QuestionCategory(BaseModel):

    question_category: Literal['Employees','Department','Employee_Department','Other']
</SCHEMA>
<Examples>
EXAMPLE INPUT: 
1- how many employees are are present
EXAMPLE JSON OUTPUT:
{
    question_category:'Employees'
    question:'how many employees are are present'
}
EXAMPLE INPUT: 
2- does maria still work ?
EXAMPLE JSON OUTPUT:
{
    question_category:'Employees'
    question:'does maria still work ?'
}
3- which department does maria work in 
EXAMPLE JSON OUTPUT:
{
    question_category:'Employee_Department'
    question:'which department does maria work in '
}
EXAMPLE INPUT: 
How many employees in each department are above 40 years old?
EXAMPLE JSON OUTPUT:
{
    question_category:'Employee_Department'
    question:'which department does maria work in?'
}
EXAMPLE INPUT: 
How many total departments are present?
EXAMPLE JSON OUTPUT:
{
    question_category:'Department'
    question:'How many total departments are present?'
}
EXAMPLE INPUT: 
How are you?
EXAMPLE JSON OUTPUT:
{
    question_category:'Other'
    question:'How are you?'
}
EXAMPLE INPUT: 
what is the largest contry in the world?
EXAMPLE JSON OUTPUT:
{
    question_category:'Other'
    question:'what is the largest contry in the world?'
}
</Examples>
"""