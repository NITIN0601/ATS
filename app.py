from dotenv import load_dotenv

load_dotenv()
import base64
import streamlit as st
import os
import io
from PIL import Image
import pdf2image
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    """
    Input
    Output
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




## Streamlit APP

st.set_page_config(page_title="ATS Resume")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ",key="input")
uploaded_file = st.file_uploader("Upload your resume into PDF ", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Sucessfully")

submit_1 = st.button("Tell Me About the Resume")
#submit_2 = st.button("How Can I improvise my skills")
submit_3 = st.button("Percentage Match")

input_prompt_1 = """
                You are an experienced HR with Tech Experience in the field of any one job role of Data Scientist or Data Analyst or Data Engineer,
                Your taks is to review the provided resume against the job description for these profiles.
                Please share your professional evalluation on whether the candidate's profile aligns with the role.
                Highlight the strengths and weakness of the applicant in relation to the specified job requirements.
                """

input_prompt_3 = """
                You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of any one job role Data Science, Data Analyst, Data Engineer and ATS functionality, 
                Your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
                the job description. First the output should come as percentage and then list me out keywords missing and last final thoughts.
                """

if submit_1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt_1,pdf_content,input_text)
        st.subheader("The Response is : ")
        st.write(response)
    else:
        st.write("Please Upload the Resume file")

elif submit_3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt_3,pdf_content,input_text)
        st.subheader("The Response is : ")
        st.write(response)
    else:
        st.write("Please Upload the Resume file")