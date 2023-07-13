# app.py
import streamlit as st
import matplotlib.pyplot as plt
import analysis  # This is the module you created

# Load and preprocess the data
filename = './Data/mlops_2022.csv'
data = analysis.read_data(filename)
data['project_title'] = data['project_title'].astype(str)
data['processed_titles'] = data['project_title'].apply(analysis.preprocess_text)

word_freq = analysis.calculate_word_frequency(data['processed_titles'])

# Streamlit code starts here
st.title('Project Title Analysis')

st.header('Top 10 Most Frequent Project Titles')
top_titles = data['project_title'].value_counts()[:10]
fig, ax = plt.subplots()
top_titles.plot(kind='barh', ax=ax, color='darkseagreen', edgecolor='black')
ax.set_title('Top 10 Most Frequent Project Titles')
ax.set_xlabel('Frequency')
ax.set_ylabel('Project Titles')
ax.invert_yaxis()
st.pyplot(fig)

st.header('Top 20 Most Frequent Words')
top_words = word_freq[:20]
fig, ax = plt.subplots()
top_words.plot(kind='bar', ax=ax, color='darkseagreen', edgecolor='black')
ax.set_title('Top 20 Most Frequent Words in Project Titles')
ax.set_xlabel('Words')
ax.set_ylabel('Frequency')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

st.header('Word Cloud')
wordcloud = analysis.generate_wordcloud(data['processed_titles'])
st.image(wordcloud.to_array())
