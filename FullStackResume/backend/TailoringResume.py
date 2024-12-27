import openai

class Tailoring_Resume:
    def __init__(self, resume_temp, resume, job_keywords, missing_keywords, job_desc, other):
        self.resume_temp = resume_temp
        self.resume = resume
        self.job_keywords = job_keywords
        self.missing_keywords = missing_keywords
        self.job_desc = job_desc
        self.other = other
        self.tailored_resume = ""
        self.final_resume = 'test.tex'
        self.example = 'example.txt'

    def _generate_prompt(self, section):
        """
        Generates a clear and concise prompt for OpenAI to tailor the specified resume section.
        
        :param section: The specific section of the resume to tailor (e.g., 'Experience', 'Education').
        :return: A string containing the generated prompt.
        """
        return f"""
        You are a professional resume writer specializing in LaTeX formatting. 
        Your task is to tailor the {section} section of a resume to match the given job description and keywords. 

        Follow these rules:
        - Do not modify LaTeX formatting, styles, or macros in the template.
        - Use the provided resume, job description, and keywords.
        - Ensure all missing keywords are naturally incorporated.
        - Prioritize relevance to the job description and order entries accordingly.
        - Avoid typos, repeated sections, or excessive changes to content already aligned with the job description.

        Inputs:
        Resume Template:
        {self.resume_temp}

        Resume:
        {self.resume}

        Missing Keywords:
        {self.missing_keywords}

        Job Keywords:
        {self.job_keywords}

        Job Description:
        {self.job_desc}

        Output:
        - Provide only the tailored LaTeX code for the {section} section.
        """

    def _generate_section(self, section_name):
        """Generates a tailored section based on the given section name."""
        prompt = self._generate_prompt(section_name)
        try:
            # OpenAI API call
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",  # Use gpt-4-turbo or the latest model for best results
                messages=[
                    {"role": "system", "content": "You are an expert in LaTeX resume formatting."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.2,  # Make output deterministic
                max_tokens=2000  # Adjust based on section size
            )
            return response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"Error generating section '{section_name}': {e}")
            return ""

    def _tailorEducation(self):
        """Tailors the Education section."""
        self.tailored_resume += self._generate_section("Education") + "\n\n"

    def _tailorExperience(self):
        """Tailors the Work Experience section."""
        self.tailored_resume += self._generate_section("Work Experience") + "\n\n"

    def _tailorProjects(self):
        """Tailors the Projects section."""
        self.tailored_resume += self._generate_section("Projects") + "\n\n"

    def _tailorSkills(self):
        """Tailors the Skills section."""
        self.tailored_resume += self._generate_section("Skills") + "\n\n"

    def _tailorOther(self):
        """Tailors the Other section (if any)."""
        if self.other:
            self.tailored_resume += self._generate_section(self.other) + "\n\n"

    def _finalizeResume(self):
        prompt = f"""
        You are an expert resume writer. You are ouputing a final resume that will be used to apply for a job.
        Here is what you'll be given:
        - A resume draft in latex code
        - A resume template in latex code

        What you'll do:
        - Proofread the resume draft and make sure there aren't typos, grammatical errors, or LaTeX issues.
        - Most importantly, make sure the styling at the beginning of the template is present in your final resume.
        - Make sure there aren't repeated sections in the final resume.

        Resume Draft:
        {self.tailored_resume}

        Resume Template:
        {self.resume_temp}

        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4-turbo",
                messages=[{"role": "system", "content": prompt}]
            )
            self.final_resume = response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"Error finalizing resume: {e}")

    def methodDriver(self):
        """Driver method to tailor the resume by section and perform a final review."""
        self._tailorEducation()
        self._tailorExperience()
        self._tailorProjects()
        self._tailorSkills()
        self._tailorOther()
        self._finalizeResume()

    def save_resume(self, filename):
        """Saves the final resume to a file."""
        if self.final_resume:
            with open(filename, "w") as file:
                file.write(self.final_resume)
                print(f"Resume saved to {filename}")
        else:
            print("No final resume to save.")
