import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




def main():
    st.sidebar.image(
    "https://cdn-images-1.medium.com/max/1200/1*OPrCFbKQFOeL0QKCuDeR1g.png", width=300
    )

    st.title("Data APP Case Técnico -  David Gabriel")

    data= pd.read_json("result_products.json", orient='records')

    st.write("Data overview:")
    range_overview = st.slider("Select size", 5, len(data))
    st.write(data.head(range_overview))

    new_df = {}
    for column in data.columns.values:
        new_df[column] = data[column].count() 
    data_values = pd.DataFrame.from_dict(new_df,orient='index')
    st.write("Data Columns overview:")
    range_columns = st.slider("Select size", 5, len(data_values))
    st.write(data_values.head(range_columns))
    st.sidebar.header("Filters")



    category = st.sidebar.multiselect("Select Category", data["category"].values)
    st.write("Scatter plot:")



    range_filter_category = st.slider("Select size", 5, data["category"].count())
    fig= px.bar(
    data[:range_filter_category],
    x="category",
    text_auto=True)
    fig.update_traces( textposition="outside", cliponaxis=False,        overwrite=False)
    fig.update_layout(uniformtext_minsize=8,uniformtext_mode='hide')
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


    if category:
        fig= px.bar(
        data[data["category"].isin(category)],
        x="subcategory",
        text_auto=True)
        fig.update_traces( textposition="outside", cliponaxis=False,        overwrite=False)
        fig.update_layout(uniformtext_minsize=8,uniformtext_mode='hide')
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

if __name__ == "__main__":
    main()
