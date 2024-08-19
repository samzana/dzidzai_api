from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from common.documents import get_combined_documents
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

#openai_api_key = "sk-proj-797OmQPX4ti1RJl6OX6WT3BlbkFJG8v1zvaapmRvp6JKPUt3"

if not openai_api_key:
    raise ValueError("OpenAI API key not found. Please set it in the .env file or check the key.")

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = openai_api_key

model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)

def create_rag_chain(task_type, system_prompt: str):
    docs = get_combined_documents(task_type)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings(openai_api_key=openai_api_key))

    retriever = vectorstore.as_retriever()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    question_answer_chain = create_stuff_documents_chain(model, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    return rag_chain