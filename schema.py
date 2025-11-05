from pydantic import BaseModel,field_validator
from typing import Literal

class QuestionCategory(BaseModel):

    question_category: Literal['Employees','Department','Employee_Department','Other']
    question : str
    @field_validator('question_category')
    @classmethod
    def forbid_other_category(cls, v) -> str:
        """Raises a validation error if the category is 'Other'."""
        
        if v == 'Other':
            raise ValueError(
                f"We are sorry, our bot can only assist you in questions regarding our Employees and staff"
            )
        if v == 'Department':
            raise ValueError(
                f"WE ARE ONLY TESTING EMPLOYEE TABLE NOW, IF WE GOT THIS ERROR MEANS WE GOT DEPARTMENT"
            )
        
        if v == 'Employee_Department':
            raise ValueError(
                f"WE ARE ONLY TESTING EMPLOYEE TABLE NOW, IF WE GOT THIS ERROR MEANS WE GOT DEPARTMENT"
            )
        
        return v

