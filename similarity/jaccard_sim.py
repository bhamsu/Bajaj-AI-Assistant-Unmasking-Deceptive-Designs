
class JaccardSimilarity:

    def __init__(self):
        self.set1 = None
        self.set2 = None

    def score(self, string1, string2):
        self.set1 = set(string1)
        self.set2 = set(string2)

        intersection = len(self.set1.intersection(self.set2))
        union = len(self.set1) + len(self.set2) - intersection

        sim_score = intersection / union
        return sim_score * 100

    def __call__(self, *args, **kwargs):
        pass

    def __del__(self):
        pass
