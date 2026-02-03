from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents):
    """ Splits Sanskrit documents into chunks for retrieval. """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=390,
        chunk_overlap=50
    )

    chunks = []
    for doc in documents:
        chunks.extend(splitter.split_text(doc))

    return chunks


if __name__ == "__main__":
    sample = ["धर्मः नाम कर्तव्यपालनं नैतिकजीवनं च।"]
    print(chunk_documents(sample))
