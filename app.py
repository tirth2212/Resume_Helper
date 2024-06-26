import streamlit as st
import openai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json


load_dotenv()


st.set_page_config(
    page_title="Smart ATS",
    page_icon="👨‍💼",
    layout="centered",
)

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    st.error("Please enter your OpenAI API Key.")
    st.stop()

openai.api_key = API_KEY

def get_gpt4_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1500,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message.content.strip()


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


input_prompt = """
You are a highly skilled ATS (Application Tracking System) with extensive experience in evaluating resumes in the tech field, including software engineering, machine learning, artificial intelligence, data science, data analysis, and big data engineering. Your task is to evaluate the provided resume against the given job description. Consider the competitive nature of the job market and aim to provide the best assistance for improving the resume. Assess the match percentage between the resume and the job description, identify missing keywords, and offer a profile summary. Provide the response in the following structured format:

{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}

Here are the details:

Resume: {text}
Job Description: {jd}
"""


st.title("Resume Matcher ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        print('done')
        response = get_gpt4_response(input_prompt.format(text=text, jd=jd))
        st.subheader("Response:")
        parsed_response = json.loads(response)
        for key, value in parsed_response.items():
            st.write(f"**{key}:** {value}")


