import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("World Happiness and Social Support Analysis")

# Load the dataset
st.header("1. Load Dataset")
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")
    st.write(df.head())

    # Create a new column based on social support level
    df['Support_Level'] = df['Social support'].apply(lambda x: 'High' if x > 1.2 else 'Low')

    # First Graph: Average Happiness Score by Support Level
    st.header("2. Average Happiness Score by Social Support Level")
    fig1, ax1 = plt.subplots()
    sns.barplot(data=df, x='Support_Level', y='Score', ci='sd', ax=ax1)
    ax1.set_title("Average Happiness Score by Social Support Level")
    ax1.set_ylabel("Average Happiness Score")
    ax1.set_xlabel("Social Support Level")
    st.pyplot(fig1)

    # Second Graph: Boxplot of Happiness Score by Support Level
    st.header("3. Boxplot of Happiness Score")
    fig2, ax2 = plt.subplots()
    sns.boxplot(data=df, x='Support_Level', y='Score', ax=ax2)
    ax2.set_title("Happiness Score by Social Support Level")
    ax2.set_ylabel("Happiness Score")
    st.pyplot(fig2)

    # Third Graph: Countplot of Support Level
    st.header("4. Count of Countries by Social Support Level")
    fig3, ax3 = plt.subplots()
    sns.countplot(data=df, x='Support_Level', ax=ax3)
    ax3.set_title("Count of Countries by Social Support Level")
    ax3.set_ylabel("Number of Countries")
    st.pyplot(fig3)

    # Fourth Graph: Trend - Social Support vs Happiness Rank
    st.header("5. Trend: Social Support vs. Overall Happiness Rank")
    fig4, ax4 = plt.subplots()
    sns.regplot(data=df, x='Overall rank', y='Social support', ax=ax4)
    ax4.set_title("Trend: Social Support vs. Overall Happiness Rank")
    ax4.set_xlabel("Overall Happiness Rank (lower is better)")
    ax4.set_ylabel("Social Support")
    st.pyplot(fig4)

else:
    st.warning("Please upload the CSV file to proceed.")
