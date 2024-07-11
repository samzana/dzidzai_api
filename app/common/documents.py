from langchain_community.document_loaders import PyPDFLoader

def load_documents(file_paths):
    documents = []
    for file_path in file_paths:
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        documents.extend(docs)
    return documents

COMMON_DOCUMENTS = ["/Users/samuelzana/Desktop/dzidzai/dzidzai_api/app/common//English-Language-Syllabus-min.pdf"]
READING_DOCUMENTS = []
WRITING_DOCUMENTS = []

def get_combined_documents(task_type):
    if task_type == "reading":
        return load_documents(COMMON_DOCUMENTS + READING_DOCUMENTS)
    elif task_type == "writing":
        return load_documents(COMMON_DOCUMENTS + WRITING_DOCUMENTS)
    else:
        raise ValueError("Invalid task type. Must be 'reading' or 'writing'.")