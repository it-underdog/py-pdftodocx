# PDF to Docx converter
### A simple script made with PyPDF2

You can install PyPDF2 via pip:

```py
pip install PyPDF2
```

replace 'loremipsum.pdf' with your file (don't forget to place the pdf you want to convert in the same folder as main.py) and 'loremipsum.docx'.

```py
import PyPDF2

#Open thhe PDF file
with open('loremipsum.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    #Open a new Word file
    with open('loremipsum.docx', 'w') as doc_file:
        for page in range(len(pdf_reader.pages)):
            text = pdf_reader.pages[page].extract_text()
            doc_file.write(text)
```

run
```py
python main.py
```
enjoy your converted file.