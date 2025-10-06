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
    instructions = "Answer only the questions that are directly related to the content provided in the PDF text. Do not use or include any external or generalized knowledge beyond what is present in the document. If a user asks a question that is unrelated to the PDF, respond with “Sorry, I am not trained for this.” Avoid summarizing or restating the entire document—your responses should be concise, factual, and limited strictly to the context of the provided text."
    genai.configure(api_key = os.environ.get("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-2.5-flash")
    # prompt = instructions + "\n\nUser Question: " + user_prompts + "\n\nPDF Text: " + pdfFile
    # response = model.generate_content(prompt) #generating the response
    prompt = user_prompts + instructions
    response = model.generate_content([pdf_file_text, prompt])
    return response.text