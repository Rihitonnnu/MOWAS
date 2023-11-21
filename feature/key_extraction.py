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
    # extractor = pke.unsupervised.TopicRank()
    extractor = pke.unsupervised.MultipartiteRank()
    # normalization=None を指定しないと，デフォルトの Stemming 処理が走りそれが日本語未対応のためエラーになる
    extractor.load_document(input=text, language='ja', normalization=None)

    extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ', 'NUM'})
    extractor.candidate_weighting(threshold=0.74, method='average', alpha=1.1)

    keyphrases = extractor.get_n_best(n=10)

    print(keyphrases)


key_extraction("""人工知能という名前は1956年にダートマス会議でジョン・マッカーシーにより命名された。
現在では、記号処理を用いた知能の記述を主体とする情報処理や研究でのアプローチという意味あいでも使われている。
日常語としての「人工知能」という呼び名は非常に曖昧なものになっており、多少気の利いた家庭用電気機械器具の制御システムやゲームソフトの思考ルーチンなどがこう呼ばれることもある。""")
# key_extraction("投資はしたい。つみたてNISAはどのようなものなのか。節約もしてて自炊もよくしているんですよ。")
