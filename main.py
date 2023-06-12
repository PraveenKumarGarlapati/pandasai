import pandas as pd
import numpy as np
from pandasai import PandasAI
# from pandasai.llm.openai import OpenAI
from settings import API
import streamlit as st


path = 'Sample_NMReport.xlsx'
df = pd.read_excel(f'data/{path}')

#Check

prompt = 'What is this about?'

def main():
    st.title("Generate Insights")
    
    # Prompt input field
    prompt = st.text_input("Enter a text:")
    print(prompt)
    
    # OpenAI
    from pandasai.llm.openai import OpenAI
    llm = OpenAI(api_token=API)

    pandas_ai = PandasAI(llm)
    prompt_here = prompt
    # print(pandas_ai.run(df, prompt=prompt_here))

    if st.button("Show Insights"):
      st.write(pandas_ai.run(df, prompt=prompt))


if __name__ == "__main__":
    main()