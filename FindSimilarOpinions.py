import gensim.models.keyedvectors as word2vec
from textblob import TextBlob, Word, Blobber


class FindSimilarOpinions:
    extracted_opinions = {}
    word2VecObject = []
    cosine_sim = 0.3

    def __init__(self, input_cosine_sim, input_extracted_ops):
        self.cosine_sim = input_cosine_sim
        self.extracted_opinions = input_extracted_ops
        word2vec_add = "data//assign4_word2vec_for_python.bin"
        self.word2VecObject = word2vec.KeyedVectors.load_word2vec_format(word2vec_add, binary=True)
        return

    def get_word_sim(self, word_1, word_2):
        return self.word2VecObject.similarity(word_1, word_2)

    def findSimilarOpinions(self, query_opinion):
        # example data, which you will need to remove in your real code. Only for demo.

        '''
        example_similarity = self.get_word_sim("service", "waiter")
        print("Similarity of 'service' and 'server' is " + str(example_similarity))
        '''
        similar_opinions = {}
        query_attribute = query_opinion.split(', ')[0]
        query_value = query_opinion.split(', ')[1]
        for ext_opinion in self.extracted_opinions.keys():
            extracted_attribute = ext_opinion.split(', ')[0]
            extracted_value = ext_opinion.split(', ')[1]
            if(extracted_attribute not in self.word2VecObject.vocab):
                continue
            if (extracted_value not in self.word2VecObject.vocab):
                continue

            #checking if the sentiment of the assessments are the same
            #if (TextBlob(query_attribute).sentiment.polarity >= 0 and TextBlob(extracted_attribute).sentiment.polarity >= 0) or (TextBlob(query_attribute).sentiment.polarity <= 0 and TextBlob(extracted_attribute).sentiment.polarity <=0):
            if (TextBlob(query_value).sentiment.polarity >= 0 and TextBlob(
                        extracted_value).sentiment.polarity >= 0) or (
                        TextBlob(query_value).sentiment.polarity < 0 and TextBlob(
                        extracted_value).sentiment.polarity < 0):

                attribute_similarity = self.get_word_sim(query_attribute, extracted_attribute)
                value_similarity = self.get_word_sim(query_value, extracted_value)
                if attribute_similarity >= self.cosine_sim and value_similarity >= self.cosine_sim:
                    similar_opinions[ext_opinion] = self.extracted_opinions[ext_opinion]
        return similar_opinions
