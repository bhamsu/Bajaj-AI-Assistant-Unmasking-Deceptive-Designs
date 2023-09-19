
# Importing all the required modules
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CosineSimilarity:

    def __init__(self):
        self.vectorizer = None

    def score(self, attr1, attr2, img = False):

        similarity = 0
        if not img:
            # Tokenize the strings and create vectors
            self.vectorizer = CountVectorizer().fit_transform([attr1, attr2])
            vectors = self.vectorizer.toarray()

            # Calculate cosine similarity
            similarity = cosine_similarity(vectors[0].reshape(1, -1), vectors[1].reshape(1, -1))

        elif img:
            # similarity = cosine_similarity(attr1.reshape(1, -1), attr2.reshape(1, -1))
            similarity = cosine_similarity(attr1, attr2)
        try:
            # Convert similarity score to percentage
            similarity_percentage = similarity[0][0] * 100
            return similarity_percentage
        except TypeError as e:
            print("Something went wrong!!")
            print(e)

        return 0


    def __call__(self, *args, **kwargs):
        pass

    def __del__(self):
        pass


