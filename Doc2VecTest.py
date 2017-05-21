# gensim modules
from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec
# numpy
import numpy
# random
from random import shuffle
# classifier
from sklearn.linear_model import LogisticRegression
class LabeledLineSentence(object):
    def __init__(self, sources):
        self.sources = sources

        flipped = {}

        # make sure that keys are unique
        for key, value in sources.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                raise Exception('Non-unique prefix encountered')

    def __iter__(self):
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    yield LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no])

    def to_array(self):
        self.sentences = []
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    self.sentences.append(LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no]))
        return self.sentences

    def sentences_perm(self):
        shuffle(self.sentences)
        return self.sentences
sources = {'C:/Users/mao/Desktop/TestTrain/test_ai.txt':'TEST_AI', 'C:/Users/mao/Desktop/TestTrain/test_avr.txt':'TEST_AVR', 'C:/Users/mao/Desktop/TestTrain/test_bd.txt':'TEST_BD', 'C:/Users/mao/Desktop/TestTrain/test_iot.txt':'TEST_IOT', 'C:/Users/mao/Desktop/TestTrain/train_ai.txt':'TRAIN_AI','C:/Users/mao/Desktop/TestTrain/train_avr.txt':'TRAIN_AVR','C:/Users/mao/Desktop/TestTrain/train_bd.txt':'TRAIN_BD','C:/Users/mao/Desktop/TestTrain/train_iot.txt':'TRAIN_IOT'
}

sentences = LabeledLineSentence(sources)
# for i in sentences:
#     print(i)
model = Doc2Vec(min_count=1, window=10, size=300, sample=1e-4, negative=5, workers=8)

model.build_vocab(sentences.to_array())
for epoch in range(20):
    model.train(sentences.sentences_perm())
model.save('C:/Users/mao/Desktop/TestTrain/model/tech.d2v')
model = Doc2Vec.load('C:/Users/mao/Desktop/TestTrain/model/tech.d2v')
model.most_similar('Apple')
model.docvecs['TEST_AI_0']
