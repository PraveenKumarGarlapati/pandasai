import pandas as pd
import numpy as np
from pandasai import PandasAI
# from pandasai.llm.openai import OpenAI
# from settings import API
import streamlit as st
import matplotlib as plt
import tkinter



# path = 'Sample_NMReport.xlsx'
# df = pd.read_excel(f'data/{path}')
# prompt = 'Show a histogram please'

# #Check
# API = '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'

def main():
    st.title("Upload and Display DataFrame")

    # Upload option and button
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Top", 5, "rows of the dataframe:")
        st.dataframe(df.head(5))

    st.title("Generate Insights")
    
    # Prompt input field
    API = st.text_input("Provide your API Key here")
    prompt = st.text_input("Enter a text:")
    print(prompt)
    
    # OpenAI
    from pandasai.llm.openai import OpenAI


    if st.button("Show Insights"):
        llm = OpenAI(api_token=API)

        pandas_ai = PandasAI(llm, verbose= True)
        # prompt_here = prompt

        st.write(pandas_ai.run(df, prompt=prompt))


if __name__ == "__main__":
    main()