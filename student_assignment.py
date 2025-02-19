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

def hw02_2(q2_pdCf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    print(f"pages: {len(docs)}")

    # merge all docs to one plain text
    plain_text = ""
    for doc in docs:
        plain_text = plain_text + doc.page_content + "\n"
    print(f"plain_text: \n{plain_text}\n")

    # step1: split to chpaters
    chapter_separator = [r"(?:\n|^|\s*)第\s+(?:[一二三四五六七八九十百千萬]+|零)\s+章.*\n"]
    chapter_splitter = RecursiveCharacterTextSplitter(
        separators = chapter_separator,
        chunk_size = 0,
        chunk_overlap = 0,
        is_separator_regex = True,
        keep_separator = True)
    chapters = chapter_splitter.split_text(plain_text)
    print(f"chapter count: {len(chapters)}")

    # step2: split chapters to article, and collect chapter and article in one chunk
    chapter_article_chunks = []
    article_separator = [r"(?:\n|^)第\s+[0-9]+(?:-[0-9]+)?\s+條.*\n"]
    article_splitter = RecursiveCharacterTextSplitter(
        separators = article_separator,
        chunk_size = 0,
        chunk_overlap = 0,
        is_separator_regex = True,
        keep_separator = True)
    for chapter in chapters:
        articles = article_splitter.split_text(chapter)
        chapter_article_chunks.extend(articles)

    print(f"result chunk count: {len(chapter_article_chunks)}")


hw02_1(q1_pdf)
hw02_2(q2_pdf)