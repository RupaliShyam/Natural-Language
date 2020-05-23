# Natural-Language

Design and develop a reviewer opinion extraction using CoreNLP tool and querying system

(1) The system automatically extracts opinions from all the reviews. The extracted opinions from the reviews can be represented as a tuple with two elements: attribute and value. Opinions are extracted based on the coreNLP Enhanced Dependencies Annotation parsing results. 

(2) the user inputs an opinion as a query, and your system compares the input opinion with the extracted opinions and returns similar opinions. The semantic similarity between different words can be obtained by word embedding. Google pre-trained word embeddings with Skip-gram model are be used, and cosine similarity is used to measure the word semantic similarity. However, the Google pre-trained word embeddings is too large, 8G after decompression. Therefore, this code uses a custom word2vec bin which only contains words that appear in this corpus.  

(3) a set of reviews are returned as supporting evidence for this opinion. 
 
