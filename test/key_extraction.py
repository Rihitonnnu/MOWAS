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


# Wikipedia カエルより引用
# https://ja.wikipedia.org/wiki/%E3%82%AB%E3%82%A8%E3%83%AB
# text = ("カエル（蛙、英語: Frog）は、両生綱無尾目（むびもく、Anura）に分類される構成種の総称。古称としてかわず（旧かな表記では「かはづ」）などがある。英名は一般にはfrogであるが，ヒキガエルのような外観のものをtoadと呼ぶことが多い。"
#         "成体の頭は三角形で、目は上に飛び出している。一見すると頭部には種による差異がないようにも思えるが、実際には天敵対策のために毒液を流し込む鋭い棘を発達させた種や、大きめの獲物を飲み込めるように大きく裂けた顎を持つ種など、種ごとの違いが大きい。中には頭部をヘルメットのように活用して巣穴に蓋をする種もいる。極わずかの例外を除き、上顎にしか歯が生えていない。が歯が無い種類でも、牙状の突起を進化させたものが少なくない[3]。獲物を飲み込む際には、目玉を引っ込めて強制的に喉の奥へ押し込む。"
#         "胴体は丸っこく、尻尾は幼体にしか存在しない。ほとんどの種で肋骨がない。"
#         "後肢が特に発達しており、後肢でジャンプすることで、敵から逃げたり、エサを捕まえたりする。後肢の指の間に水掻きが発達するものが多く、これを使ってよく泳ぐ。"
#         "前肢は人間の腕に似た形状をしている。ジャンプからの着地の際に身体への衝撃を和らげるのが主な役目である。餌となる小動物に飛びついて両肢で押さえつけたり、冬眠などのために土砂を掘ったり、汚れ落としのために片肢で顔を拭いたりする動作も可能である。アオガエル科やアマガエル科などの樹上生活をする種の多くでは指先に吸盤が発達し、その補助で細い枝などに掴まることができる。人間や猿のように物を片肢ないし両肢で掴み取ることはできない。"
#         "幼生は四肢がなく、ひれのついた尾をもつ。成体とは違う姿をしていて、俗に「オタマジャクシ（お玉杓子）」と呼ばれる（食器のお玉杓子に似た形状から）。オタマジャクシはえら呼吸を行い、尾を使って泳ぐため、淡水中でないと生きることができない。オタマジャクシは変態することで、尾をもたず肺呼吸する、四肢をもった幼体（仔ガエル）となる。"
#         )

text = ("最近は色々なことに取り組んでいます。特に楽しいのはフットサルやサイクリング、音楽鑑賞が好きです。"
        "その中でもフットサルが一番好きです")

extractor = pke.unsupervised.MultipartiteRank()

# normalization=None を指定しないと，デフォルトの Stemming 処理が走りそれが日本語未対応のためエラーになる
extractor.load_document(input=text, language='ja', normalization=None)

extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ', 'NUM'})
extractor.candidate_weighting()

keyphrases = extractor.get_n_best(n=10)

print(keyphrases)
