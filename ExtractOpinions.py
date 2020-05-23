#import StringDouble
#import ExtractGraph
from stanfordcorenlp import StanfordCoreNLP
import json


class ExtractOpinions:
    # Extracted opinions and corresponding review id is saved in extracted_pairs, where KEY is the opinion and VALUE
    # is the set of review_ids where the opinion is extracted from.
    # Opinion should in form of "attribute, assessment", such as "service, good".
    extracted_opinions = {}

    def __init__(self):
        self.nlp = StanfordCoreNLP('http://localhost', port=9000, timeout=30000)  # , quiet=False, logging_level=logging.DEBUG)
        self.props = {'annotators': 'tokenize, ssplit, lemma, parse, depparse',
                   'outputFormat': 'json'}

        #stanfordnlp.download('en')  # This downloads the English models for the neural pipeline
        #self.nlp = stanfordnlp.Pipeline()  # This sets up a default neural pipeline in English

        return

    def extract_pairs(self, review_id, review_content):
        pos_list = ['NN', 'NNS', 'JJ', 'JJR', 'JJS']
        ann = json.loads(self.nlp.annotate(review_content.lower()))

        sentences = ann['sentences']
        for sentence in sentences:
            dp = sentence['enhancedPlusPlusDependencies']
            tokens = sentence['tokens']
            for i_dict in dp:
                if (i_dict['dep'] == 'nsubj'):

                    attribute_idx = i_dict['dependent']
                    attribute_token = tokens[attribute_idx - 1]
                    attribute_pos = attribute_token['pos']

                    value_idx = i_dict['governor']
                    value_token = tokens[value_idx - 1]
                    value_pos = value_token['pos']

                    if value_pos not in pos_list or attribute_pos not in pos_list:
                        continue
                    else:
                        attribute_lemma = attribute_token['lemma']
                        value_lemma = value_token['lemma']

                    opinion = attribute_lemma + ", " + value_lemma
                    if opinion in self.extracted_opinions.keys():
                        doc_list = self.extracted_opinions[opinion]
                        doc_list.append(review_id)
                        self.extracted_opinions[opinion] = doc_list
                    else:
                        self.extracted_opinions[opinion] = [review_id]

                elif i_dict['dep'] == 'amod':
                    attribute_idx = i_dict['governor']
                    attribute_token = tokens[attribute_idx - 1]
                    attribute_pos = attribute_token['pos']

                    value_idx = i_dict['dependent']
                    value_token = tokens[value_idx - 1]
                    value_pos = value_token['pos']

                    if value_pos not in pos_list or attribute_pos not in pos_list:
                        continue
                    else:
                        attribute_lemma = attribute_token['lemma']
                        value_lemma = value_token['lemma']

                    opinion = attribute_lemma + ", " + value_lemma
                    if opinion in self.extracted_opinions.keys():
                        doc_list = self.extracted_opinions[opinion]
                        doc_list.append(review_id)
                        self.extracted_opinions[opinion] = doc_list
                    else:
                        self.extracted_opinions[opinion] = [review_id]

        return


