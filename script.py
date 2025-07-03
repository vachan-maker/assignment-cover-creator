import streamlit as st
from weasyprint import HTML, CSS
from base64 import b64encode

def gen_pdf():
    html = HTML(string='''
    <h1>The title</h1>
    <p>Content goes here</p>
    ''')
    css = CSS(string='@page { size: A4; margin: 1cm }')
    html.write_pdf('example.pdf', stylesheets=[css])

st.title('Assignment Cover Generator')

with st.form("form"):
    name = st.text_input("Enter Your Name")
    registerNumber = st.text_input("Enter Your Register Number")
    subjectCode = st.text_input("Enter Subject Code")
    subjectName = st.text_input("Enter Subject Name")
    assignmentTopic = st.text_input("Assignment Topic")
    submitted = st.form_submit_button("Submit")

if submitted:
    gen_pdf()

