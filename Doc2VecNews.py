# gensim modules
from gensim import utils
from gensim.models.doc2vec import LabeledSentence
from gensim.models import Doc2Vec

import gensim
Lsent = gensim.models.doc2vec.LabeledSentence
# numpy
import numpy as np
# random
from random import shuffle
# classifier
from sklearn.linear_model import LogisticRegression
import pandas as pd

AI_df = pd.read_csv(r'C:/Users/mao/Desktop/Clean/RAWsplitAI.csv')
BD_df = pd.read_csv(r'C:/Users/mao/Desktop/Clean/RAWsplitBD.csv')
IOT_df= pd.read_csv(r'C:/Users/mao/Desktop/Clean/RAWsplitIOT.csv')

def labelizeNews(News, label_type):
    labelized = []
    #enumertate include index
    for i, v in enumerate(News):
        label = '%s_%s' %(label_type,i)
        labelized.append(Lsent(v, [label]))
    return labelized

Train_AI = labelizeNews(AI_df,'AI')
Train_BD = labelizeNews(BD_df,'BigData')
Train_IOT = labelizeNews(IOT_df,'IoT')

size=200
model_dm = gensim.models.Doc2Vec(min_count=1, window=10, size=size, sample=1e-3, negative=5, workers=3)
model_dbow = gensim.models.Doc2Vec(min_count=1, window=10, size=size, sample=1e-3, negative=5,dm=0, workers=3)

Train_All =  Train_AI + Train_BD + Train_IOT

model_dm.build_vocab(Train_All)
model_dbow.build_vocab(Train_All)

for epoch in range(10):
    perm = np.random.permutation(len(Train_All))
    model_dm.train([Train_All[x] for x in perm])
    model_dbow.train([Train_All[x] for x in perm])

def getVecs(model, corpus, size):
    vecs = [model.docvecs[z.tags[0]].reshape((1, size)) for z in corpus]
    return np.concatenate(vecs)

Train_AI_vecs_dm = getVecs(model_dm, Train_AI, size)
Train_AI_vecs_dbow = getVecs(model_dbow, Train_AI, size)
AI_train_vecs = np.hstack((Train_AI_vecs_dm, Train_AI_vecs_dbow))

Train_BD_vecs_dm = getVecs(model_dm, Train_BD, size)
Train_BD_vecs_dbow = getVecs(model_dbow, Train_BD, size)
BD_train_vecs = np.hstack((Train_BD_vecs_dm, Train_BD_vecs_dbow))

Train_IOT_vecs_dm = getVecs(model_dm, Train_IOT, size)
Train_IOT_vecs_dbow = getVecs(model_dbow, Train_IOT, size)
IOT_train_vecs = np.hstack((Train_IOT_vecs_dm, Train_IOT_vecs_dbow))

All_vecs = np.vstack((AI_train_vecs, BD_train_vecs, IOT_train_vecs))

print(All_vecs)