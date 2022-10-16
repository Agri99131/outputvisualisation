# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st

import pandas as pd


def main():
    st.title('Oil Palm Yield Prediction in 2021')
    url='https://raw.githubusercontent.com/YH99131/outputvisualisation/main/selecteddnn_predictions.csv'
    df=pd.read_csv(url)
    st.dataframe(df.head(5))
    
    #line chart
    df2=df[['Block','Predicted','Actual']]
    df2=df2.set_index('Block')
    lang_list=df2.columns.tolist()
    lang_choices=st.multiselect('choose features', lang_list,default='Predicted')
    new_df=df2[lang_choices]
    st.line_chart(new_df)
    
if __name__=='__main__':
    main()


