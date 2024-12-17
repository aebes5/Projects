class Validate_And_Feedback:
    def __init__(self, tailored_resume, job_desc):
        self.tailored_resume = tailored_resume
        self.job_desc = job_desc
        self.generated_feedback = None
        self.cos_sim = None
        self.properly_compiled = False

    def _validateResume(self):
        return
    
    def _generateFeedback(self):
        return
    
    def _generateSimilarity(self):
        return
    
    def methodDriver(self):
        self._validateResume()
        self._generateFeedback()
        
        if not self.properly_compiled:
            self.cos_sim = 0
        else:
            self._generateSimilarity()