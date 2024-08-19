from langchain_community.document_loaders import PyPDFLoader

import os
def load_documents(file_paths):
    documents = []
    for file_path in file_paths:
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        documents.extend(docs)
    return documents

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

syllabus_pdf_path = os.path.join(BASE_DIR, 'static', 'English-Language-Syllabus-min.pdf')
summary_pdf_path = os.path.join(BASE_DIR, 'static', 'Zimsec Exam Summary Section RAG Document.pdf')

COMMON_DOCUMENTS = [syllabus_pdf_path]
SUMMARY_DOCUMENTS = [summary_pdf_path]
READING_DOCUMENTS = []
WRITING_DOCUMENTS = []

def get_combined_documents(task_type):
    if task_type == "reading":
        return load_documents(COMMON_DOCUMENTS + READING_DOCUMENTS)
    elif task_type == "writing":
        return load_documents(COMMON_DOCUMENTS + WRITING_DOCUMENTS)
    elif task_type == "summary":
        return load_documents(COMMON_DOCUMENTS + SUMMARY_DOCUMENTS)
    else:
        raise ValueError("Invalid task type. Must be 'reading' or 'writing' or 'summary'.")