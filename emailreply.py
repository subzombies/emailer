import os
import streamlit as st

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

st. set_page_config(layout="wide",page_title="EmailGPT 📧",page_icon ="📧")

os.environ['OPENAI_API_KEY'] = "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"


st.markdown("<h1 style='text-align: center; color: black;'>Email Replier📧</h1>", unsafe_allow_html=True)

inp,oup = st.columns(2)

with inp:
    prompt = ""
    prompt = st.text_area(label = "Enter email to generate reply to",height = 400)
    context_in = st.text_area(label="Enter any additional context",height=200)
    butt = st.button("Generate")



#Prompt Tepmplate
context_template = PromptTemplate(
    input_variables = ['hello','mail'],
    template = "Write a reply to the email, Context: {hello} Email: {mail}"
    )


#Memory 
memory = ConversationBufferMemory(input_key='hello',memory_key='chat_history')
st.session_state.outp = ""
#Llms
llm = OpenAI(model_name = "gpt-4",temperature=0.532)
replier = LLMChain(llm=llm, prompt=context_template,memory=memory)


with oup:
    
    if butt:
        context = replier.run(hello=open("context.txt").read() + context_in ,mail=prompt)
        st.text_area(value=context,label="Result",height = 600) 
        
        
    

    

    

    
