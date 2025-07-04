import streamlit as st
from weasyprint import HTML, CSS
from base64 import b64encode
from jinja2 import Environment, FileSystemLoader
from streamlit_pdf_viewer import pdf_viewer

def gen_pdf():
    environment = Environment(loader=FileSystemLoader("templates"))
    report = environment.get_template("cover.html")
    html = HTML(string=report.render(subject=subjectName,faculty=faculty,name=name,semester=semester,branch=branch,rollno=rollno))
    css = CSS('templates/styles.css')
    return html.write_pdf(stylesheets=[css])


st.title("Assignment Cover Generator")
with st.form("form"):
    name = st.text_input("Enter Your Name")
    rollno = st.text_input("Enter Your Register Number/Roll No:")
    branch = st.text_input("Enter branch:",placeholder="Eg. CS/EC/EEE")
    semester = st.number_input("Enter your current Sem:",min_value=1,max_value=10,step=1)
    subjectCode = st.text_input("Enter Subject Code",placeholder="Eg. CST-201")
    subjectName = st.text_input("Enter Subject Name",placeholder="Eg. Operating Systems")
    faculty = st.text_input("Enter faculty name:",placeholder='Mr. Rajesh P.')
    submitted = st.form_submit_button("Submit")

if submitted:
    if not name:
        st.error("Name is required")
    st.success("Success!. Press Download to save the pdf!")
    pdf_bytes = gen_pdf()
    st.download_button(label="Download PDF",data=pdf_bytes,mime="application/pdf")
    pdf_viewer(input=pdf_bytes, width=700, height=800)

