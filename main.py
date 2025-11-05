import sqlite3
import json
from schema import QuestionCategory
from openai import OpenAI
from employee_queries import *
from agent_tools import tools,system_prompt

client = OpenAI(api_key="insert api key", base_url="https://api.deepseek.com/v1")

DB_PATH = "database.sqlite"
system_prompt = system_prompt
tool_function_map = {
    "get_employee_details": questions_company,
    "get_reports_by_manager_id": questions_manager,
    "get_employees_by_department": questions_department,
    "get_employees_by_job_title": questions_title,
}

test_prompts = [
    "How many employees are in the IT?",
    "who are the employees under manager id 1?",
    "Do you have an employee named Hannah Fuchs?",

]

#### we will only use tables Employees because i cant study the entire table.
def question_category(system_prompt:str,prompt:str) -> QuestionCategory:
    try:
        messages = [{"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}]

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            response_format={
                'type': 'json_object'
            }
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        ValueError()
    

## test of second prompt

def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools
    )
    return response.choices[0].message
def main():
    for prompt in test_prompts:

        messages = [{"role":"system", "content": "answer in a natural way like you are human, make the answer only 1 line"},
                    {"role": "user", "content": prompt}]
        message = send_messages(messages)
        messages.append(message)

        print(f"SYSTEM PROMPT>\t {messages[0]['content']}")
        print(f"User question>\t {messages[1]['content']}")

        tool_call = message.tool_calls[0]
        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments)
        print(f"LLM Requested Tool:\t **{tool_name}**")
        print(f"Arguments:\t\t {tool_args}")
        function_to_call = tool_function_map.get(tool_name)

        function_result = function_to_call(**tool_args)

        messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": function_result 
            })
            
        final_message = send_messages(messages)
        print(f"Model Final Answer:\t {final_message.content}")
        print("="*70)






