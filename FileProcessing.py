from sentence_transformers import SentenceTransformer, util
from PyPDF2 import PdfReader
from docx import Document
import spacy

'''
File Processing Class

Order of function called methods includes:
-   Scanning user's resume in .pdf or .docx format
-   Processing to spaCy model for cleaning and in depth features like Named Entity Recognition (NER)
-   Transforming text to sentence_transformers model, essentially a BERT model for longer texts
-   Process each section (education, experience, projects, skills), (!could be developed more later!)
-   Gain a cosine similarity for each section to determine strong/weak sections (!could add weights to sections later!)

Purpose:
Format the resumes into NLP text models (useful for NER in other sections) with embeddings and section scores
'''

class File_Processing:
    def __init__(self, resume_path, job_desc, job_count, project_count):
        self.resume_path = resume_path
        self.job_desc = job_desc
        self.job_count = job_count
        self.project_count = project_count
        self.resume_text = None
        self.nlp_resume = None
        self.sections = {}
        self.resume_emb = None
        self.job_emb = None


    def scanResume(self):
        text = ""

        if self.resume_path.lower().endswith('.pdf'): # use PyPDF2 for .pdf
            reader = PdfReader(self.resume_path)
            for page in reader.pages:
                text += page.extract_text() + '\n'
        
        elif self.resume_path.lower().endswith('.docx'): # use docx for .docx
            document = Document(self.resume_path)
            for paragraph in document.paragraphs:
                text += paragraph.text + '\n'
        
        else: # file type error
            raise ValueError("File extension not accepted, make sure you're using .pdf or .docx.")
        
        self.resume_text = text


    # spaCy based symbol cleaning for resume, more in depth features in other classes
    def preProcessing(self):
        nlp = spacy.load("en_core_web_sm")
        self.nlp_resume = nlp(self.resume_text)


    # bert sentence transforming for paragraph embeddings
    def sentenceTransformer(self):
        model = SentenceTransformer('all-MiniLM-L6-v2')

        self.resume_emb = model.encode(self.resume_text, convert_to_tensor=True)
        self.job_emb = model.encode(self.job_desc, convert_to_tensor=True)

    # separate sections and append text from each section to sections dict
    def processSections(self):
        section_splits = ["Education", "Experience", "Projects", "Skills"]
        curr_section = None

        for sent in self.nlp_resume.sents:
            text = sent.text.strip()

            if any(section in text for section in section_splits):
                for section in section_splits:
                    if section in text:
                        curr_section = section
                        self.sections[curr_section] = []

            if curr_section:
                self.sections[curr_section].append(text)
        
        # print(self.sections)

    '''
    cosine similarity function for each section to determine
    most and least effective sections, using max for sections
    including multiple tensors/sentences which then takes into
    less relevant experience which shouldn't be weighed down
    with a mean
    '''
    def getRelevance(self):
        model = SentenceTransformer('all-MiniLM-L6-v2')

        for key in self.sections.keys():
            section_embedding = model.encode(self.sections[key], convert_to_tensor=True)
            cos_sim = util.cos_sim(section_embedding, self.job_emb)
            
            print(f"Similarity scores for each section {key}:")

            for i, sim in enumerate(cos_sim):
                print(f"Sentence{i + 1}: {sim.item()}")


    '''
    First things first:
    Figure out the issue with projects/work not being broken up correctly
    Could possibly use something like NER for something like proper nouns
    Worth keeping in mind that something like keywords we have covered
    AKA Python should be the first language we see in the case of somebody
    visually inspecting the resume
    '''