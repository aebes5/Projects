from sentence_transformers import SentenceTransformer, util
from PyPDF2 import PdfReader
from docx import Document
import spacy
import pdfx
import re

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
    def __init__(self, resume_path, job_desc, sections, other_section):
        self.resume_path = resume_path
        self.job_desc = job_desc
        self.section_sims = {}
        self.sections = sections
        self.resume_text = None
        self.nlp_resume = None
        self.resume_emb = None
        self.overall_sim = None
        self.urls = []


    def _scanResume(self):
        text = ""

        if self.resume_path.lower().endswith('.pdf'): # use PyPDF2 for .pdf
            reader = PdfReader(self.resume_path)
            for page in reader.pages:
                text += page.extract_text()
        
        elif self.resume_path.lower().endswith('.docx'): # use docx for .docx
            document = Document(self.resume_path)
            for paragraph in document.paragraphs:
                text += paragraph.text
        
        else: # file type error
            raise ValueError("File extension not accepted, make sure you're using .pdf or .docx.")
        
        text = re.sub(r'[:/|•–-]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        self.resume_text = text

        self.job_desc = ' '.join(self.job_desc.split())

        refs = pdfx.PDFx(self.resume_path).get_references_as_dict()
        self.urls = refs['url']

        # print(self.urls)
        # print(self.resume_text)

    # spaCy based symbol cleaning for resume, more in depth features in other classes
    def _preProcessing(self):
        nlp = spacy.load("en_core_web_sm")
        self.nlp_resume = nlp(self.resume_text)


    # bert sentence transforming for paragraph embeddings
    def _sentenceTransformer(self):
        model = SentenceTransformer('paraphrase-MPNet-base-v2')

        self.resume_emb = model.encode(self.resume_text, convert_to_tensor=True)
        self.job_emb = model.encode(self.job_desc, convert_to_tensor=True)

    # separate sections and append text from each section to sections dict
    def _processSections(self):
        curr_section = None

        for sent in self.nlp_resume.sents:
            text = sent.text.strip()

            if any(section in text for section in self.sections):
                for section in self.sections:
                    if section in text:
                        curr_section = section
                        self.section_sims[curr_section] = []

            if curr_section:
                self.section_sims[curr_section].append(text)
        
        # print(self.sections)

    '''
    cosine similarity function for each section to determine
    most and least effective sections, using max for sections
    including multiple tensors/sentences which then takes into
    less relevant experience which shouldn't be weighed down
    with a mean
    '''
    def _getRelevance(self):
        model = SentenceTransformer('paraphrase-MPNet-base-v2')

        for key in self.section_sims.keys():
            section_embedding = model.encode(self.section_sims[key], convert_to_tensor=True)
            cos_sim = util.cos_sim(section_embedding, self.job_emb)
            
            # print(f"Similarity scores for each section {key}:")

            # for i, sim in enumerate(cos_sim):
                # print(f"Sentence{i + 1}: {sim.item()}")
        
        self.overall_sim = util.cos_sim(self.resume_emb, self.job_emb).item()
        print(self.overall_sim)

    def methodDriver(self):
        self._scanResume()
        self._preProcessing()
        self._sentenceTransformer()
        self._processSections()
        self._getRelevance()
