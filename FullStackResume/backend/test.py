import openai

resume_temp = r'''
%----------RESUME START----------
\documentclass[letterpaper,11pt]{article}
\nonstopmode

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\input{glyphtounicode}

%----------FONT OPTIONS----------
% Uncomment the font you'd like to use
% \usepackage[sfdefault]{FiraSans} % sans-serif
% \usepackage[default]{sourcesanspro} % sans-serif
% \usepackage{CormorantGaramond} % serif

\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-0.5in}
\addtolength{\textheight}{1in}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Ensure that generated PDFs are machine-readable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\renewcommand\labelitemii{$\bullet$} % Ensures bullets are consistent

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.15in, label=\textbullet]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%

\begin{document}

%----------HEADING----------
\begin{center}
    \textbf{\LARGE \scshape Name -- Job Title} \\ \vspace{1pt}
    \small phone number $|$ \href{email}{\underline{email}} $|$ 
    \href{linkedin}{\underline{linkedin}} $|$
    \href{github}{\underline{github}}
\end{center}

%-----------EDUCATION-----------
\section{Education}
\resumeSubHeadingListStart
  \resumeSubheading
    {School}{City, State}
    {Degrees, minors}{Start Date -- End Date}
    \resumeItemListStart
      \resumeItem{\textbf{GPA:} }
      \resumeItem{\textbf{Relevant Courses:} }
      \resumeItem{\textbf{Future Plans:} }
    \resumeItemListEnd
\resumeSubHeadingListEnd

%-----------EXPERIENCE-----------
\section{Experience}
\resumeSubHeadingListStart
  \resumeSubheading
    {Role}{City, State}
    {Company}{Start Date -- End Date}
    \resumeItemListStart
      \resumeItem{Description}
      \resumeItem{Description}
    \resumeItemListEnd
    
  \resumeSubheading
    {Role}{City, State}
    {Company}{Start Date -- End Date}
    \resumeItemListStart
      \resumeItem{Description}
      \resumeItem{Description}
    \resumeItemListEnd
\resumeSubHeadingListEnd

%-----------PROJECTS-----------
\section{Projects}
\resumeSubHeadingListStart
    
  \resumeProjectHeading
    {\textbf{Project} $|$ \emph{Skills, Tools}}{}
    \resumeItemListStart
      \resumeItem{Description}
      \resumeItem{Description}
      \resumeItem{Description}
    \resumeItemListEnd
    
  \resumeProjectHeading
    {\textbf{Project} $|$ \emph{Skills, Tools}}{}
    \resumeItemListStart
      \resumeItem{Description}
      \resumeItem{Description}
    \resumeItemListEnd
    
  \resumeProjectHeading
    {\textbf{Project} $|$ \emph{Skills, Tools}}{}
    \resumeItemListStart
      \resumeItem{Description}
      \resumeItem{Description}
      \resumeItem{Description}
    \resumeItemListEnd
    
\resumeSubHeadingListEnd

%-----------TECHNICAL SKILLS-----------
\section{Technical Skills}
\resumeSubHeadingListStart
    \resumeItemListStart
      \resumeItem{\textbf{Category:} }
      \resumeItem{\textbf{Category:} }
      \resumeItem{\textbf{Category:} }
      \resumeItem{\textbf{Category:} }
      \resumeItem{\textbf{Category:}}
    \resumeItemListEnd
\resumeSubHeadingListEnd

\end{document}

'''

resume = '''
Andrew Ebert
(720)627-9163 | andrew.ebert12@yahoo.com | linkedin.com/in/andrew-e-ebert | github.com/aebes5
Education
University of Colorado, Denver Denver, CO
Bachelor of Arts in Computer Science, Bachelor of Science in Mathematics Jan 2022 - May 2025
• GPA: 3.73/4
• Relevant Courses: Fundamentals of Computing, Data Structures, Algorithms, Database Concepts, Fundamentals of
Unix, Introduction to Optimization, NLP & LLM, Software Engineering, Numerical Analysis, Statistical Theory,
Calculus, Linear Algebra, Differential Equations, Math Clinic, Data Science, Machine Learning, Graph Theory
• Future Plans: Actively applying to CU Denver's 4+1 Data Science MS program.
Experience
Student Researcher Denver, CO
University of Colorado, Denver - Physics June 2023 - July 2024
• Automated the execution of 18 jobs on supercomputers using JSON.
• Compiled code, primarily using Intel compilers and Intel MKL, to run high-performance computing jobs and optimize
performance.
• Developed machine learning models (Random Forest and Binary Classification) using Python to classify 4 classes of
electronic/atomic transitions.
• Analyzed and visualized complex datasets, collaborating with a team to create scripts using Matplotlib and Pandas.
• Participated in a group research presentation on high-performance computing at CU Denver's 2023 Research and
Creative Activities Symposium (RaCAS Presentation).
Construction Laborer Aurora, CO
Accell Construction Aug 2021 - May 2023
• Applied a strong attention to detail and effective time management to efficiently complete tasks while ensuring the
client's specifications were met.
• Collaborated with a team, balancing individual tasks with collective goals of ensuring projects were completed on
time.
Projects
Fitness Tracker App | Java, Git
• Led a team of three individuals on a class project to develop an Android application using Java.
• Managed version control using Git to ensure consistency across contributions.
• Facilitated communication between team members to ensure all project deadlines were met on time.
Apartment Database | SQL, MySQL
• Designed and implemented a relational database to simulate operations within an apartment complex.
• Created and executed SQL queries using MySQL to manage tenants, apartments, and maintenance records for efficient
retrieval and data management with over 1000 manual entries.
Portfolio Optimization | Python, Python API, Gurobi
• Utilized Python APIs to web scrape companies listed in the S&P 500.
• Formulated an optimization problem to maximize portfolio returns, ensuring the selection of at least 25 stocks, each
contributing to no more than 20% of the total, to reduce volatility.
• Employed Gurobi to solve the problem with a maximum allowable variance of 7%.
Technical Skills
• Programming Languages: Python, C++, C, Java, R, SQL
• Tools & Technologies: Git, Linux, Unix, MySQL
• Data Visualization: Pandas, Matplotlib
• Optimization: NumPy, SciPy, Pyomo
• Machine & Deep Learning: Scikit-learn, PyTorch

'''

job_desc = '''
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

final_response = ""

prompt = f"""
        You are an expert resume writer. Tailor only the education/header section of the following resume text based on a resume template and job description.
        The resume template will be in LaTeX code. Do not alter the formatting or styles in the output resume. Simply fill in the section using:
        - The provided resume
        - The job description

        Additionally:
        - Order entries (e.g., projects, skills) based on relevance to the job description.
        - Use synonyms where appropriate to align with the job description (e.g., replacing "Machine Learning" with "ML" if needed).
        - Retain consistency with the formatting and "visual appeal" of the resume template.

        Resume Template:
        {resume_temp}

        Resume:
        {resume}

        Job Description:
        {job_desc}

        """
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
        )
    final_response += response["choices"][0]["message"]["content"].strip()
except Exception as e:
    print(f"Error generating section 'education': {e}")

prompt = f"""
        You are an expert resume writer. Tailor only the experience section of the following resume text based on a resume template and job description.
        The resume template will be in LaTeX code. Do not alter the formatting or styles in the output resume. Simply fill in the section using:
        - The provided resume
        - The job description

        Additionally:
        - Order entries (e.g., projects, skills) based on relevance to the job description.
        - Use synonyms where appropriate to align with the job description (e.g., replacing "Machine Learning" with "ML" if needed).
        - Retain consistency with the formatting and "visual appeal" of the resume template.

        Resume Template:
        {resume_temp}

        Resume:
        {resume}

        Job Description:
        {job_desc}

        """
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
        )
    final_response += response["choices"][0]["message"]["content"].strip()
except Exception as e:
    print(f"Error generating section 'education': {e}")


prompt = f"""
        You are an expert resume writer. Tailor only the projects section of the following resume text based on a resume template and job description.
        The resume template will be in LaTeX code. Do not alter the formatting or styles in the output resume. Simply fill in the section using:
        - The provided resume
        - The job description

        Additionally:
        - Order entries (e.g., projects, skills) based on relevance to the job description.
        - Use synonyms where appropriate to align with the job description (e.g., replacing "Machine Learning" with "ML" if needed).
        - Retain consistency with the formatting and "visual appeal" of the resume template.

        Resume Template:
        {resume_temp}

        Resume:
        {resume}

        Job Description:
        {job_desc}

        """
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
        )
    final_response += response["choices"][0]["message"]["content"].strip()
except Exception as e:
    print(f"Error generating section 'education': {e}")

prompt = f"""
        You are an expert resume writer. Tailor only the skills section of the following resume text based on a resume template and job description.
        The resume template will be in LaTeX code. Do not alter the formatting or styles in the output resume. Simply fill in the section using:
        - The provided resume
        - The job description

        Additionally:
        - Order entries (e.g., projects, skills) based on relevance to the job description.
        - Use synonyms where appropriate to align with the job description (e.g., replacing "Machine Learning" with "ML" if needed).
        - Retain consistency with the formatting and "visual appeal" of the resume template.

        Resume Template:
        {resume_temp}

        Resume:
        {resume}

        Job Description:
        {job_desc}

        """
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
        )
    final_response += response["choices"][0]["message"]["content"].strip()
except Exception as e:
    print(f"Error generating section 'education': {e}")


prompt = f"""
        You are an expert resume writer. You are ouputing a final resume that will be used to apply for a job.
        Here is what you'll be given:
        - A resume draft in latex code
        - A resume template in latex code

        What you'll do:
        - Proofread the resume draft and make sure there aren't typos or LaTeX issues.
        - Make sure the styling at the beginning of the template is present in your final resume.
        - Make sure there aren't repeated sections in the final resume.

        Resume Draft:
        {final_response}

        Resume Template:
        {resume_temp}

        """
try:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
        )
    print(response["choices"][0]["message"]["content"].strip())
except Exception as e:
    print(f"Error generating section 'education': {e}")