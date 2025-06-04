import requests
import streamlit as st

def get_response(input_text,language="French"):
    json_body = {
        "input":{
            "language":language,
            "text": input_text
        },
        "config":{},
        "kwargs":{}
    }

    response = requests.post("http://127.0.0.1:8000/chain/invoke",json=json_body)

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return {"error":"Invalid response from API"}
    
st.title("Language Translation app")

input_text = st.text_input("Enter the text you want to convert")

language = st.selectbox("Select your language", options=['Yoruba','Igbo','Hausa','French'])

translate_button = st.button("Translate", disabled=not bool(input_text))

if translate_button:
    response = get_response(input_text,language)
    st.write("**Translated Text:**",response['output'])