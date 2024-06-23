import PyPDF2 as pdf
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

print(input_pdf_text('/Users/tirthshah/Desktop/Applications./Resumes/trial.pdf'))