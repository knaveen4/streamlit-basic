# basic streamlit application 
'''
        hii i'm naveen reddy and i recently started working on Data Applications 
        here to some basic app/code
'''
import streamlit as st 
import time
from streamlit_option_menu import option_menu





st.set_page_config(
    page_title="Reddy App",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="auto",
    
)

        

contact_form="""
          <form action="https://formsubmit.co/kothakapunaveenreddy2003@gmail.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="your name" required>
             <input type="email" name="email" placeholder="your email" required>
             <textarea id="w3review" name="message" rows="4" cols="50" placeholder="Send message.........." required>
             
             </textarea>
             <button type="submit">Send</button>
          </form>
          """

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

pass_list=['naveenreddy']
st.sidebar.title('Data Insights')
st.sidebar.write('your decision our responsible')
password=st.sidebar.text_input('Password',type='password')
login=st.sidebar.button('Login')
is_true= (len(password)>7 and len(password)<14)
is_found= password in pass_list


if login:
   if is_true and is_found:
      st.title("nvr")
   else:
      st.sidebar.write('Incorrect Password')
else:
  st.sidebar.write('Password between 7-14 letters')


st.sidebar.write('or')
signup=st.sidebar.button('Send message')


if signup:
        st.header('Get In Touch with Me ☑️')
        st.markdown(contact_form, unsafe_allow_html=True)      
        local_css("./style.css")

selected=option_menu(
        menu_title=None,
        options=["Home","About","Github"],
        icons=["house","phone","github"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    
    )
if selected=="Home":
   st.title(f"Welcome to AI World")
if selected=="About":
   st.title(f"We are in {selected}")
if selected=="Github":
   st.title(f"We era in {selected}")
   







   
