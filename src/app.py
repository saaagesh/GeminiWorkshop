##
## Web app that uses streamlit and the gemini api
##
## The user can enter a prompt and the gemini model will
## return a response (then output it to the screen)
##

##
## Run the app:
##  streamlit run /Users/skewalramani/Desktop/geminiworkshop/src/app.py
##
## Install Libraries:
##  pip install -q -U google-generativeai streamlit IPython
##

##
## Create a Gemini API Key
##  https://aistudio.google.com/app/apikey
##
## Tune the model:
##  https://aistudio.google.com/app/tuned_models/new_tuned_model
##

##
## Adjust to relative path
##
if __name__ == "__main__":
    import sys

    sys.path.append("src")

##
## Import the libraries
##
import streamlit as st
import google.generativeai as genai
import json

##
## We'll import our custom "to_markdown" function
##
from utils.to_markdown import to_markdown


##
## Set the page title (This shows at the top)
##
st.title("Gemini API")

##
## Get the api key from the config.json
##
config = json.load(open("./config.json"))
api_key: str = config["gemini"]["api_key"]

##
## Set the gemini api key and intialize the model
##
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

##
## Get the prompt input from the user
##
prompt = st.text_input("Enter a prompt")

##
## A button to get a response from the gemini model
##
## If it's clicked, it will run the model and write the response
## to the screen.
##
if st.button("Generate response"):
    ##
    ## Generate a response from the model
    ##
    response = model.generate_content(prompt)
    response.resolve()

    ##
    ## Get the first response from the model and then convert
    ## it to markdown using our custom function.
    ##
    ## The Gemini API Docs are different for this section. This
    ## line (below: text = ...) might change in the future.
    ##
    text = response._result.candidates[0].content.parts[0].text
    md = to_markdown(text)

    ## Write the response to the screen
    st.write(md.data)

