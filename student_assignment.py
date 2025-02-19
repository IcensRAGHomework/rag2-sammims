from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    print(f"pages: {len(docs)}")

    spiltter = CharacterTextSplitter(chunk_overlap = 0)
    chunks = spiltter.split_documents(docs)
    # negative indices where -1 refers to the last element,
    # -2 to the second-last, and so on
    last_chunk = chunks[-1]
    print(f"last chunk: {last_chunk.metadata}")

    return last_chunk

def hw02_2(q2_pdf):
    pass

hw02_1(q1_pdf)
hw02_2(q2_pdf)