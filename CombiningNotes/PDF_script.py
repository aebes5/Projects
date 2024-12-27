import os
from PyPDF2 import PdfMerger

directory = "path/to/your/pdfs"
# directory = "C:/Users/andre/Downloads"
output_file = "name.pdf"
# output_file = "LLM_notes.pdf"

merger = PdfMerger()

# sort files by name and append
for file in sorted(os.listdir(directory)):
    if file.endswith(".pdf"):
        pdf = os.path.join(directory, file)
        merger.append(pdf)

# write to output_file
merger.write(output_file)
merger.close()