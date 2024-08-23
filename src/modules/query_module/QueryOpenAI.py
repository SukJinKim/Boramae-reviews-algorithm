import ast
import re
from openai import OpenAI
from .QueryInterface import QueryInterface

class QueryOpenAI(QueryInterface):
    def extract_problem_components(self, problem_description):
        prompt = f"""
        The following input is a description of a programming problem. Please return a Python dictionary with the following keys:
        - 'PROBLEM_DESCRIPTION'
        - 'INPUT_DESCRIPTION'
        - 'OUTPUT_DESCRIPTION'
        - 'INPUT_EXAMPLE'
        - 'OUTPUT_EXAMPLE'

        INPUT:
        \"\"\"{problem_description}\"\"\"

        
        EXAMPLE:
        - INPUT:
            \"\"\"
            You are given an array of integers. Write a function to return the sum of the integers.Input: An array of integers.Output: A single integer, the sum of the integers.
            Example:Input: [1, 2, 3, 4]Output: 10
            \"\"\"
        - OUTPUT:
            {{
                'PROBLEM_DESCRIPTION': 'You are given an array of integers. Write a function to return the sum of the integers.',
                'INPUT_DESCRIPTION': 'An array of integers.',
                'OUTPUT_DESCRIPTION': 'A single integer, the sum of the integers.',
                'INPUT_EXAMPLE': '[1, 2, 3, 4]',
                'OUTPUT_EXAMPLE': '10'
            }}
        """
        try:
            client = OpenAI(api_key=self.api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            problem_components_str = response.choices[0].message.content
            dict_pattern = re.compile(r'\{.*\}', re.DOTALL)
            problem_components_str = dict_pattern.search(problem_components_str).group()
            
            problem_components = ast.literal_eval(problem_components_str)

            if not isinstance(problem_components, dict):
                raise TypeError("ERR_CONVERTING_DICT")

            return problem_components
        
        except Exception as e:
            raise ValueError(f"""
                             ERR_EXTRACTING_OPENAI: EXTACTING 과정에서 문제가 발생했습니다.
                             details : {e}
                             """)
    
    def optimize_after_review(self, submitted_code, problem_components, few_shot_learning, root_path):

        with open(f"{root_path}/src/modules/query_module/prompts/prompt_template.txt", "r") as f:
            prompt_template = f.read()
        with open(f"{root_path}/src/modules/query_module/prompts/few_shot_learning_prompt.txt", "r") as f:
            few_shot_learning_prompt = f.read()
        
        prompt = prompt_template.replace("{CODE}", submitted_code)\
                                .replace("{PROBLEM_DESCRIPTION}", problem_components['PROBLEM_DESCRIPTION'])\
                                .replace("{INPUT_DESCRIPTION}", problem_components['INPUT_DESCRIPTION'])\
                                .replace("{OUTPUT_DESCRIPTION}", problem_components['OUTPUT_DESCRIPTION'])\
                                .replace("{INPUT_EXAMPLE}", problem_components['INPUT_EXAMPLE'])\
                                .replace("{OUTPUT_EXAMPLE}", problem_components['OUTPUT_EXAMPLE'])\

        if few_shot_learning:
            prompt = prompt.replace("{FEW_SHOT_LEARNING}", few_shot_learning_prompt)
        
        try:
            client = OpenAI(api_key=self.api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=1.0
            )
            review_message = response.choices[0].message.content
            return review_message
        
        except Exception as e:
            raise ValueError(f"""
                                ERR_REVIEWING_OPENAI: REVIEWING 과정에서 문제가 발생했습니다.
                                details : {e}
                                """)