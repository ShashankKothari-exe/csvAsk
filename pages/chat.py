import pandas as pd
import streamlit as st
import json, csv
#from keys import myKey
myKey=st.secrets["myKey"]
import google.generativeai as genai 

import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))




genai.configure(api_key=myKey)
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(
    page_title="CSV Analysis APP",
    page_icon="〽️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

#To hide hamburger menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

df = pd.read_csv('tmpdataset.csv')

def csv_to_json(csv_file):
    data = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return json.dumps(data, indent=4)

try:
    for message in chat.history:
        display(to_markdown(f'**{message.role}**: {message.parts[0].text}'))
except:
    ""  

chatForm = st.form('chat_form')
query = chatForm.text_input('Enter your query:')
submit = chatForm.form_submit_button(f'Search')
  
if submit:
    dson=csv_to_json("tmpdataset.csv")
    chat = model.start_chat(history=[])
    try:
        response = chat.send_message(dson+" "+query)
        st.write(response.text)
    except:
        response = "Sorry I cannot respond to that.\nTry to upload a structured file"    
        st.write(response)
