import PyPDF2
from requests.utils import DEFAULT_ACCEPT_ENCODING

# Keep Tracking of Assignments Retrieved
listOfAssignments = []

# Extracting Assignments from PDF
def extractPDFContents(pdfPath):
    
    # Identifying Which Month to Look At
    selectedMonth = input('What month are you looking at? ')
    
    # Open the PDF File in Read
    with open(pdfPath, "rb") as file:
        
        # Create a PDF Reader
        pdf_reader = PyPDF2.PdfReader(file)

        # Iterate Over Each PDF Page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            
            # Extract Text from PDF Page
            text = page.extract_text()

            # Processing the Extracted Text
            lines = text.split('\n')
            for line in lines:
                if ":" in line:

                    # Delimiter for Next Slip
                    if 'Note to student' in line:
                        if selectedMonth in date:
                            assignmentDict = {'Name:': name, 'Assistant:': assistant, 'Date:': date, 'Part No:': partNo, 'Given In:': input(f'Where is {name} giving their talk on {date}? ')}
                            listOfAssignments.append(assignmentDict)
                        else:
                            pass
                    if line.startswith('Name:'):
                        name = line.replace('Name: ', '')
                    if line.startswith('Assistant:'):
                        assistant = line.replace('Assistant: ', '')
                    if line.startswith('Date:'):
                        date = line.replace('Date: ', '')
                    if line.startswith('Part no.:'):
                        partNo = line.replace('Part no.: ', '')
                    if line.startswith('To be given in:'):
                        pass
                    
# Inputting Assignment Slips
pdf_path = "AssignmentSlips.pdf"  # Replace Location of your Assignment Slips
extractPDFContents(pdf_path)
