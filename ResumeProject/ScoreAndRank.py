class ScoreAndRank:
    def __init__(self, resume_emb, job_emb):
        self.resume_emb = resume_emb
        self.job_emb = job_emb

    def scoreRelevance(self):
        return 0

    def rankSections(self, section_type):
        return 0