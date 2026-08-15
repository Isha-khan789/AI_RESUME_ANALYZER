import pypdf as pdf
def extract_text_from_pdf(file_path):
    reader=pdf.PdfReader(file_path)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
    return text
if __name__=="__main__": 
    text=extract_text_from_pdf("resume.pdf")  
    print(text)
  
    
   