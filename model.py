from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import glob
import os
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

porter_stemmer = PorterStemmer()
def stemming_tokenizer(str_input):
#tokenizer for both my query and documents
	words = re.sub(r"[^A-Za-z]", " ", str_input).lower().split()
	words = [porter_stemmer.stem(word) for word in words]
	return words

folder_path = os.getcwd() + '/startup'
all_docs_contents=[]
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
	with open(filename, 'r') as f:
		text = f.read()
		all_docs_contents.append(str(text))

tfidf_vectorizer = TfidfVectorizer(stop_words='english', tokenizer=stemming_tokenizer, use_idf=True, norm='l1')
X = tfidf_vectorizer.fit_transform(all_docs_contents)
print (X.shape)

term_document = pd.DataFrame(X.toarray(), columns=tfidf_vectorizer.get_feature_names())
print (term_document)

query_1 = "CEO"
query_2 = "CFO"
query_3 = "CTO"
query_4 = "COO"
query_5 = "CIO"
queries = [query_1, query_2, query_3, query_4, query_5]
print (queries)

vector = tfidf_vectorizer.transform(queries)
print (vector)
query = pd.DataFrame(vector.toarray(), columns=tfidf_vectorizer.get_feature_names())
print(tfidf_vectorizer.vocabulary_)
print (query.shape)
print (query)

w=cosine_similarity(query, term_document)
print(w)

