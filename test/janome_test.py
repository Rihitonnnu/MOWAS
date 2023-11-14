from janome.tokenizer import Tokenizer

t = Tokenizer()
for token in t.tokenize(u'こんにちは、私の名前は涼です'):
    print(token)
