# Pantik-AI AGENT-example


AGI AGENT works by creating a good schema for the llm which description, function, arguments etc

the way this script works is it initially classifies the users questions based on choices provided. in this example we have ( employees, departments, employee_and_departments, other)

other was added to block irrelevant questions. 

Next we python functions for calling sql querries alongside tools schema which describes the functions that the agent can use.



# HOW TO EXTRACT:

The logic to extract data was simple. I create a good pydantic model which signifies exactly what i want to extract.
Then i used type checkers/validation through pydantic to make sure I can only get the exact schema returned from the function.


Here is the function: def question_category(system_prompt:str,prompt:str) -> QuestionCategory             (QuestionCategory Schema was used)
EXTRACT JSON SCHEMA FROM LLM MESSAGE GUIDE: https://api-docs.deepseek.com/guides/json_mode

# How to use tools:

I then created tools schema for all the python functions that i have written which can be found in the agent_tools.py file.
TOOLS GUIDE : https://api-docs.deepseek.com/guides/function_calling




# PROGRAM FILES:

agent_tools.py = has the schema of the tools + system_prompt

database.sqlite = the sqlite database

employee_queries.py = here we have functions for queries that can work with employee table

schema.py = here we have the pydantic schema which is used to extract which type of question or microservice is the user asking about (e.g is the user asking about Employees, Departments, Others)

main.py = main file
