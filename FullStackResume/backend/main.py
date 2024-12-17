from FileProcessing import File_Processing
from KeywordExtraction import Keyword_Extraction
from TailoringResume import Tailoring_Resume

job = '''
Ibotta is seeking a Machine Learning Intern to join our innovative team and contribute to our mission to Make Every Purchase Rewarding. As a participant in our 2025 Summer Internship, you will have the opportunity to fully integrate with your team to directly contribute to ongoing Ibotta business initiatives. In addition to the daily time with your team, you will participate in ongoing teach outs curated to help build skills essential to transitioning into the workforce and building your career. We are looking for candidates who are eager to learn, excited to work on real-world business challenges, and want to be part of a mission-driven company.

 

This will be a full-time, 12 week, internship during the summer of 2025. This is a hybrid position located in Denver, Colorado and requires 3 days in-office per week. Required in-office hybrid days are Tuesday, Wednesday, and Thursday. Candidates must live in the United States.

 

What you will be doing:

Work with the mentor on understanding our models, users and clients.

Build, train, and validate deep learning, recommender, and reinforcement learning

Run statistical analysis and create predictive models based on past user purchases and behavior

Develop recommender systems and machine learning algorithms for user targeting and personalization

Build well tested, maintainable, and extendable code

Report and understand system performance in detail, and identify ideas for improvement

Embrace and uphold Ibotta's Core Values: Integrity, Boldness, Ownership, Teamwork, Transparency & A good idea can come from anywhere

 

What we are looking for:

Juniors working towards a bachelor's degree with a focus in Computer Science, Engineering, Data Analytics or a related field

Proven ability to think creatively and implement ideas from start to finish

Good written and verbal communication skills

Hunger to learn and collaborate with your teammates

Good understanding of the key concepts of Recommender Systems and Machine Learning

Proven expertise with data handling, processing, statistical and analytical skills

Python experience is required, as well as experience with either Tensorflow or PyTorch

Spark/PySpark experience is an additional plus

Ability to develop and maintain ML models, in addition to being able to visualize, analyze, and communicate results

Experience with SQL required

Good understanding of A/B testing and control group concepts
'''

# driver
def main(resume, job_desc, sections, other_section, resume_temp):
    # scan resume/job description and get embeddings

    file_processing = File_Processing(resume_path=resume, job_desc=job_desc, sections=sections, other_section=other_section)
    file_processing.methodDriver()

    keyword_extraction = Keyword_Extraction(resume=file_processing.resume_text, job_desc=file_processing.job_desc)
    keyword_extraction.methodDriver()

    tailoring_resume = Tailoring_Resume(resume_temp=resume_temp, resume=file_processing.resume_text, job_keywords=keyword_extraction.job_keywords, 
                                        missing_keywords=keyword_extraction.missing_keywords, job_desc=job_desc, other=other_section)
    tailoring_resume.methodDriver()

    print(tailoring_resume.final_resume)

    return file_processing.overall_sim, resume_temp# tailored_resume, feedback

""" 

    validate_and_feedback = ValidateAndFeedback(tailoring_resume.resume_temp, keyword_extraction.missing_keywords)
    validate_and_feedback.validateResume()
    validate_and_feedback.generateFeedback()
"""

main('Ebert_Andrew_Resume.pdf', job, ['Education', 'Experience', 'Projects', 'Technical Skills'], None, 'template.tex')
