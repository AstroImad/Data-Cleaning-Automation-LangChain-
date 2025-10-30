import pandas as pd
import pandas as pd
import re
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

data = pd.read_csv("[Imad] test data  - Form Responses 1.csv")

from langchain_core.prompts import ChatPromptTemplate, FewShotPromptTemplate, PromptTemplate

#Column Renaming Function

def rename_columns(data):
    column = data.columns.tolist()

    examples =[
        {"column": "Phone Number (Copy from ARIA)",
        "rename": "phonenum"},

        {"column": "I will list several stated objectives of the JS-SEZ. Please state on a scale of 1 (Very Negative) to 5 (Very Positive) how you feel about each of the objectives.",
        "rename": "How do you feel about the stated JS-SEZ objective?"},

        {"column": "On a scale of 1 (very negative) to 5 (very positive), what effect do you think the JS-SEZ will have on Malaysia in the long-term?",
         "rename": "What effect do you think the JS-SEZ will have on Malaysia in the long-term?"}
    ]

    example_prompt = PromptTemplate.from_template("Question: {column}\nAnswer: {rename}")

    prompt_template = FewShotPromptTemplate(
        examples = examples,
        example_prompt = example_prompt,

    )