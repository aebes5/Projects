import spacy
from spacy.tokens import DocBin

'''
Keyword Extraction Class

Order of function called methods includes:
-   Using spaCy's Named Entity Recognition to extract keywords in job description while removing
    irrelevant NER types (!could be further improved by training domain specific data!)
-   Determine matching/missing keywords in the resume
-   Classify missing keywords as Tools, Technologies, Softskills to determine where improvements
    can be made; for example, using different keywords to touch on Softskills and give user feedback
    on missing Tools/Technologies

Purpose:
Determine missing keywords from resume to job_desc which will be used in tailoring
'''

class Keyword_Extraction:
    def __init__(self, resume, job_desc):
        self.resume = resume
        self.job_desc = job_desc
        self.job_keywords = []
        self.missing_keywords = []


    def _getJobDescKeywords(self):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(self.job_desc)


        print(f"Extracted entities (before filtering): {[ent.text for ent in doc.ents]}")
        exclude_types = {"DATE", "EVENT", "GPE", "NORP"}

        for ent in doc.ents:
            if ent.label_ not in exclude_types: 
                self.job_keywords.append(ent)
                # print(f"Keyword added: {ent.text}, Label: {ent.label_}")

        # if not self.job_keywords:
            # print("No keywords extracted after filtering.")


    def _matchingKeywords(self):
        for keyword in self.job_keywords:
            if keyword.text not in self.resume:
                self.missing_keywords.append(keyword)
            
        print(self.missing_keywords)

    def methodDriver(self):
        self._getJobDescKeywords()
        self._matchingKeywords()
    