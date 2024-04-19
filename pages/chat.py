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
    layout="wide",
    initial_sidebar_state="collapsed",
)

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
    response = chat.send_message(dson+" "+query)
    st.write(response.text)
