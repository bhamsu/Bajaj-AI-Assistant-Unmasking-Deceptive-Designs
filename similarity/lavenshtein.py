
class LevenshteinDistance:

    def __init__(self):
        self.str1 = None
        self.str2 = None

    def distance(self, string1, string2):

        self.str1 = string1
        self.str2 = string2

        m, n = len(self.str1), len(self.str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if self.str1[i - 1] == self.str2[j - 1]:
                    cost = 0
                else:
                    cost = 1
                dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                               dp[i][j - 1] + 1,  # Insertion
                               dp[i - 1][j - 1] + cost)  # Substitution

        return dp[m][n]

    @staticmethod
    def score(distance):
        # Calculating the score/percentage from Levenshtein Distance
        sim_score = 1 / (1 + distance)
        return (1 - sim_score) * 100

    def __call__(self, *args, **kwargs):
        distance = self.distance(kwargs['string1'], kwargs['string2'])
        score = self.score(distance)
        return score

    def __del__(self):
        pass




