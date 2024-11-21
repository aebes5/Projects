from FileProcessing import File_Processing
from KeywordExtraction import Keyword_Extraction
import TailoringResume
import ScoreAndRank
import ValidateAndFeedback

# driver
def main(resume, job_desc, job_count, project_count, resume_temp):
    # scan resume/job description and get embeddings

    file_processing = File_Processing(resume, job_desc, job_count, project_count)
    file_processing.scanResume()
    file_processing.preProcessing()
    file_processing.sentenceTransformer()
    file_processing.processSections()
    file_processing.getRelevance()

    keyword_extraction = Keyword_Extraction(resume, job_desc)
    keyword_extraction.getJobDescKeywords()
    keyword_extraction.matchingKeywords()
"""
    keyword_extraction.classifyKeywords()

    tailoring_resume = TailoringResume(resume_temp, file_processing.resume_text, keyword_extraction.classified_keywords, 
                                       file_processing.project_section, project_count, file_processing.work_section, file_processing.job_count)
    tailoring_resume.tailorEducation()
    tailoring_resume.tailorWorkExperience()
    tailoring_resume.tailorProjects()
    tailoring_resume.tailorSkills()
    
    score_and_rank = ScoreAndRank(file_processing.resume_emb, file_processing.job_emb)
    score_and_rank.scoreRelevance()
    score_and_rank.rankSections("Education")
    score_and_rank.rankSections("Work")
    score_and_rank.rankSections("Projects")
    score_and_rank.rankSections("Skills")

    validate_and_feedback = ValidateAndFeedback(tailoring_resume.resume_temp, keyword_extraction.missing_keywords)
    validate_and_feedback.validateResume()
    validate_and_feedback.generateFeedback()

"""

def readFile(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()  # Reads the entire file into a string
    return file_contents

if __name__ == "__main__":
    job_desc = readFile('sample.txt')
    main('Ebert_Andrew_Resume.pdf', job_desc, 2, 2, 3) #template)

