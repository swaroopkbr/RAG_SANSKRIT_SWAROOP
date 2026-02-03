import os
from pypdf import PdfReader


def load_documents(data_folder="data"):
    
    """Loads all the Sanskrit documents from txt and pdf files and return the list of raw text."""

    documents = []

    for file_name in os.listdir(data_folder):
        file_path = os.path.join(data_folder, file_name)

        # Load TXT file
        if file_name.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                documents.append(f.read())

        # Load PDF file
        elif file_name.endswith(".pdf"):
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            documents.append(text)

    return documents


if __name__ == "__main__":
    docs = load_documents()
    print("✅ Documents Loaded:", len(docs))
