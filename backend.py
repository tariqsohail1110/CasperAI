import google.generativeai as genai
import os
from pypdf import PdfReader

#function to extract text from PDF
def extractPdf(pdf_file):
    # file_obj = open(pdf_file, "rb")
    reader = PdfReader(pdf_file) 
    num_of_pages = len(reader.pages)
    text = "" #empty text string
    for pagenum in range(0, num_of_pages):
        page = reader.pages[pagenum]
        text +=  page.extract_text() 
    return text



# Function to get user prompt and generate response through the extracted text
def Q_and_A_Chatbot(pdf_file_text, user_prompts):
    instructions = "Answer the quetions the user asked, only form the topics in the text given to you, No Generalization, and if someone asks about anything other than that text, Say that Sorry I am not trained for this, and don't summarize the text also but, and don't say anything if the user's question is relevant"
    genai.configure(api_key = os.environ.get("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
    # prompt = instructions + "\n\nUser Question: " + user_prompts + "\n\nPDF Text: " + pdfFile
    # response = model.generate_content(prompt) #generating the response
    prompt = user_prompts + instructions
    response = model.generate_content([pdf_file_text, prompt])
    return response.text