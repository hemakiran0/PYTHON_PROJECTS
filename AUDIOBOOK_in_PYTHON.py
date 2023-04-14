import pyttsx3
from PyPDF2 import PdfReader

book = open(r"D:\books\The Art of Thinking Clearly (Dobelli, Rolf Griffin, Nicky) (z-lib.org) (1).pdf", 'rb')
pdf_reader = PdfReader(book)
book_len = len(pdf_reader.pages)
print(book_len)
speaker = pyttsx3.init()
for num in range(12,book_len):
    page = pdf_reader.pages[num]
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()
