import PyPDF2

def pdf_to_text_chunks(pdf_path, chunk_size=500):
    """
    Converts a PDF file to a list of text chunks.

    :param pdf_path: Path to the PDF file.
    :param chunk_size: Number of characters in each chunk.
    :return: List of text chunks.
    """
    # Read the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + ' '

    # Chunk the text
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

if __name__ == '__main__':
    # Example usage
    pdf_path = '/export/work/yusx/sadegh/test/sam.pdf'
    chunks = pdf_to_text_chunks(pdf_path)
    for chunk in chunks:
        print(chunk)
        print('---')
