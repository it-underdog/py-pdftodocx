import PyPDF2

#Open thhe PDF file
with open('loremipsum.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    #Open a new Word file
    with open('loremipsum.docx', 'w') as doc_file:
        for page in range(len(pdf_reader.pages)):
            text = pdf_reader.pages[page].extract_text()
            doc_file.write(text)