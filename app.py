import streamlit as st
from openai import OpenAI
import chromadb
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

chroma_client = chromadb.PersistentClient(path = "./gita_db")

collection = chroma_client.get_collection("krishna_collection_2")

def create_embeddings(text):
    emb = client.embeddings.create(
        model = "text-embedding-3-small",
        input = text
    )

    return emb.data[0].embedding

def query(user_query):
    input_conversion = create_embeddings(user_query)
    final_result = collection.query(
        query_embeddings = [input_conversion],
        n_results = 10
    )

    final = final_result['documents']

    context = ""

    for i in range(10):
        verse_text = final[0][i]
        context += verse_text + '\n\n'

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": f""" 
            You are krishna, the writer of Bhagwat Gita and the user has asked you a query: {user_query}.
            
            We have selected a bunch of verses for you in {context}

            This is your job:
            1. Go through all the verses one by one in {context}
            2. Define a probability of verse which matches with the {user_query} of the verse
            3. Choose the verse with the highest probability score
            4. Next you are supposed to empathetically respond to the user {user_query} starting with: Hey Vats

            Remember the following: 
            1. You are supposed to respond in FIRST PERSON.
            2. Never say reflecting on the verses, instead start with the verse itself and tell the user that you told this to Arjun as well
            """}
        ], temperature = 0.7, seed = 1
    )

    
    return response.choices[0].message.content



st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }

    .krishna-title {
        font-size: 48px;
        font-weight: 700;
        text-align: center;
        color: #3b5998;
        margin-bottom: -10px;
        font-family: 'Georgia', serif;
    }
    
    .krishna-subtitle {
        font-size: 20px;
        text-align: center;
        color: #555;
        margin-bottom: 30px;
        font-family: 'Georgia', serif;
    }

    .response-box {
        background: #e8f5e9;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #4caf50;
        font-size: 18px;
        line-height: 1.6;
        color: #1b5e20;
        font-family: 'Georgia', serif;
    }

    .user-input-box {
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div class="krishna-title">Talk to Krishna</div>', unsafe_allow_html=True)
st.markdown('<div class="krishna-subtitle">Ask Krishna anything that you want answers to</div>', unsafe_allow_html=True)

user_input = st.text_input("Please ask your question")

if user_input:
    with st.spinner("Seeking guidance from krishna"):
        reply = query(user_input)

    st.markdown(f'<div class="response-box">{reply}</div>', unsafe_allow_html=True)
