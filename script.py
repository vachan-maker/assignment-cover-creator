import streamlit as st
from weasyprint import HTML, CSS
from base64 import b64encode
from jinja2 import Environment, FileSystemLoader

def gen_pdf():
    environment = Environment(loader=FileSystemLoader("templates"))
    report = environment.get_template("cover.html")
    html = HTML(string=report.render())
    html.write_pdf('cover.pdf')

with st.form("form"):
    name = st.text_input("Enter Your Name")
    registerNumber = st.text_input("Enter Your Register Number")
    subjectCode = st.text_input("Enter Subject Code")
    subjectName = st.text_input("Enter Subject Name")
    assignmentTopic = st.text_input("Assignment Topic")
    submitted = st.form_submit_button("Submit")

if submitted:
    gen_pdf()

