import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

def main():
    load_dotenv()
    st.set_page_config(page_title="Article Question Answering")
    st.header("Ask any questions related to the uploaded article 📚")

    # File upload
    pdf = st.file_uploader("Upload your Article", type="pdf")

    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ''.join(page.extract_text() for page in pdf_reader.pages)

        # Splitting text into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1200,
            chunk_overlap=3000,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        st.write(chunks)

        # Creating embeddings
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # User input
        user_question = st.text_input("Ask any questions related to the uploaded article:")

        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            
            # Running the QA chain
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=user_question)
                print(cb)
                
            # Displaying the response
            st.write(response)

if __name__ == '__main__':
    main()
