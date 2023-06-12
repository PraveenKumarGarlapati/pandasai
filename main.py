import pandas as pd
import numpy as np
from pandasai import PandasAI
# from pandasai.llm.openai import OpenAI
# from settings import API
import streamlit as st
import matplotlib as plt



path = 'Sample_NMReport.xlsx'
df = pd.read_excel(f'data/{path}')

#Check


def main():
    st.title("Generate Insights")
    
    # Prompt input field
    API = st.text_input("Provide your API Key here")
    prompt = st.text_input("Enter a text:")
    print(prompt)
    
    # OpenAI
    from pandasai.llm.openai import OpenAI
    # print(pandas_ai.run(df, prompt=prompt_here))

    if st.button("Show Insights"):
        llm = OpenAI(api_token=API)

        pandas_ai = PandasAI(llm, verbose= True)
        # prompt_here = prompt

        st.write(pandas_ai.run(df, prompt=prompt))


if __name__ == "__main__":
    main()