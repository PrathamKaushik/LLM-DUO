from dotenv import load_dotenv
load_dotenv()

import streamlit as st 
import os 
import google.generativeai as genai 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Now we will load Gemini Pro model and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response 

# Now we will build  our streamlit app
st.set_page_config(page_title="Q&A with LLM")

# st.set_page_config(
#     page_title="Q&A with LLM",
#     page_icon=":shark:",
#     layout="centered",  # Can be "wide" or "centered"
#     initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
#     background_image="./Q&A.avif",  # URL or local file path
# )


st.header("LLM-based Q&A Application")

# Initializing the session state for chat history if it does not exist
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [] 
    
    
input = st.text_input("Input:", key="input")
submit = st.button("Ask me your Question!")

if submit and input:
    response = get_gemini_response(input)
    # Adding user query and Bot response to session chat history
    st.session_state["chat_history"].append(("You", input)) 
    st.subheader("Here is your Response:")
    for part in response:
        st.write(part.text)
        st.session_state["chat_history"].append(("Bot", part.text)) 
        
st.subheader("The Chat History is: ")

for role, text in st.session_state["chat_history"]:
    st.write(f"{role}:{text}")
    

         