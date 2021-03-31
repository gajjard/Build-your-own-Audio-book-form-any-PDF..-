# import PyPDF2 and pyttsx3
import PyPDF2
import pyttsx3

# Open PDF
# where mode='rb' is used for open the file in binary format for reading.
pdf_file = open('demo.pdf', 'rb')

# PDF file reader
pdf_read = PyPDF2.PdfFileReader(pdf_file)

# gives number of Pages in PDF file
num_pages = pdf_read.numPages

engine = pyttsx3.init()
print('Read PDF')

# loop for read out all pages one by one
for n in range(0, num_pages):
    # Retrieves a page by number from this PDF file.
    page = pdf_read.getPage(n)

    # Extract text from page.
    text = page.extractText()

    x = n + 1
    print(f"Reading page {x}/{num_pages}.")

    # read text from page.
    engine.say(text)
    engine.runAndWait()


