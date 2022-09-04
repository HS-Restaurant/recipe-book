from gensim.models import Word2Vec
wordmodel = Word2Vec.load('./word2vec/word2vec.model')

def similarity(word1, word2):
    return wordmodel.wv.similarity(word1, word2)
