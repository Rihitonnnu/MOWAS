import pke
import ginza
import nltk
from spacy.lang import ja


pke.base.stopwords['ja_ginza_electra'] = 'japanese'
# ↓は以前のバージョンの書き方でうまく動かない
# pke.base.ISO_to_language['ja_ginza']

stopwords = list(ja.STOP_WORDS)
nltk.corpus.stopwords.words_org = nltk.corpus.stopwords.words
nltk.corpus.stopwords.words = lambda lang: stopwords if lang == 'japanese' else nltk.corpus.stopwords.words_olg(
    lang)


def key_extraction(text):
    extractor = pke.unsupervised.MultipartiteRank()
    # normalization=None を指定しないと，デフォルトの Stemming 処理が走りそれが日本語未対応のためエラーになる
    extractor.load_document(input=text, language='ja', normalization=None)

    extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ', 'NUM'})
    extractor.candidate_weighting()

    keyphrases = extractor.get_n_best(n=10)

    print(keyphrases)
