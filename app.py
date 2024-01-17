from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai
import prompt_techinque as pt


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_model_response(input, pdf_content, prompt):
    """
    Input: PDF
    Output: Text response
    """
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0],prompt])
    return response.text

def input_pdf_setup(upload_file):
    """
    Convert the pdf to image
    """
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        #converting the data into bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr,format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode() #encoding to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


def logic_code(prompt_value):
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_model_response(prompt_value,pdf_content,input_text)
        st.subheader("The Response is : ")
        st.write(response)
    else:
        st.write("Please Upload the Resume file")




## Streamlit APP

st.set_page_config(page_title="ATS Resume")
st.header("ATS Tracking System")
input_job_text = st.text_input("Enter the Job Role",key="input_job_role") 
input_text = st.text_area("Job Description: ",key="input_job_desc")
uploaded_file = st.file_uploader("Upload your resume into PDF ", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Sucessfully")

submit_1 = st.button("Tell Me About the Resume")
submit_2 = st.button("Percentage Match")

if submit_1:
    logic_code(pt.prompt1(input_job_text))
elif submit_2:
    logic_code(pt.prompt2(input_job_text))
    