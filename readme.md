CasperAI is a simple and intelligent chatbot built with Streamlit and Google Gemini AI. It allows users to upload PDF documents and ask questions directly about their content. The system provides precise, context-based answers without generalizing beyond the uploaded file.

- PDF upload and text extraction
- Interactive chat-style interface
- Context-limited answers drawn only from the provided PDF
- Gemini AI integration for intelligent text understanding
- Minimal Streamlit-based user interface

How It Works

- Upload a PDF file.
- Ask a question using the chat input.
- CasperAI extracts the PDF text and queries the Gemini model for a context-based answer.
- The response is displayed in the chat interface.

Dependencies

- streamlit
- google-generativeai
- pypdf

Future Improvements

- Support for multiple PDFs
- Persistent chat history
- Additional document formats
- Improved UI with chat styling
- Enhanced file security

Author

Tariq
Creator of CasperAI

“CasperAI — A quiet assistant that reads what you upload.”