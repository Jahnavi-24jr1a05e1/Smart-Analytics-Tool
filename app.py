import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Smart Analytics Tool")
uploaded_file = st.file_uploader(
    "Upload a CSV File",
    type=["csv"]
)
if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)
    st.header("Dataset Preview")

    st.dataframe(df.head())
    st.header("Dataset Information")

    st.write("Rows and Columns:")

    st.write(df.shape)

    st.write("Columns:")

    st.write(df.columns)
    st.header("Missing Value Analysis")

    st.write(df.isnull().sum())
    st.header("Statistical Summary")

    st.write(df.describe())
    st.header("Visualization 1")

    numeric_columns = df.select_dtypes(
        include='number'
    ).columns
    x_col = st.selectbox(
        "Select X Column",
        numeric_columns
    )
    fig1 = px.histogram(
        df,
        x=x_col,
        title=f"Distribution of {x_col}"
    )

    st.plotly_chart(fig1)
    st.header("Visualization 2")
    y_col = st.selectbox(
        "Select Y Column",
        numeric_columns
    )
    fig2 = px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"{x_col} vs {y_col}"
    )

    st.plotly_chart(fig2)
    st.header("Visualization 3")
    fig3 = px.box(
        df,
        y=y_col,
        title=f"Box Plot of {y_col}"
    )

    st.plotly_chart(fig3)
    st.header("Insights")

    st.write("""
    This tool automatically analyzes uploaded datasets and provides:
    
    • Dataset preview
    
    • Missing value analysis
    
    • Statistical summary
    
    • Interactive visualizations
    """)                