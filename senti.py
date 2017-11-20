#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def acc(filelocation):
    file = open(filelocation,'r')
    hit=0
    tot=0
    for line in file:
        if line=='\n':continue
        tokens = line.split()
        y=tokens[-1]
        tokens = tokens[0:-1]
        tot+=1
        if str(predict2(tokens))==y:hit+=1
    return hit/tot



good,bad = dict(),dict()
go,bo = 0,0
gl,bl = 0,0
graphx,graphy=[],[]

#def train(fileloc):
file = open('yelp_labelled.txt','r')
for line in file:
    tokens = line.split()
    if tokens[-1] == '1':
        go+=1
        for i in range(len(tokens)-1):
            gl+=1
            if tokens[i] not in good:good[tokens[i]]=1
            else:good[tokens[i]]+=1
    else:
        bo+=1
        for i in range(len(tokens)-1):
            bl+=1
            if tokens[i] not in bad:bad[tokens[i]]=1
            else:bad[tokens[i]]+=1
    if go%10==0:
        graphx.append(go)
        graphy.append(acc('run_results.txt')*100)
        
        
        
print(go)
file = open('amazon_cells_labelled.txt','r')
for line in file:
    tokens = line.split()
    if tokens[-1] == '1':
        go+=1
        for i in range(len(tokens)-1):
            gl+=1
            if tokens[i] not in good:good[tokens[i]]=1
            else:good[tokens[i]]+=1
    else:
        bo+=1
        for i in range(len(tokens)-1):
            bl+=1
            if tokens[i] not in bad:bad[tokens[i]]=1
            else:bad[tokens[i]]+=1
    if go%10==0:
        graphx.append(go)
        graphy.append(acc('run_results.txt')*100)


file = open('imdb_labelled.txt','r')
for line in file:
    tokens = line.split()
    if tokens[-1] == '1':
        go+=1
        for i in range(len(tokens)-1):
            gl+=1
            if tokens[i] not in good:good[tokens[i]]=1
            else:good[tokens[i]]+=1
    else:
        bo+=1
        for i in range(len(tokens)-1):
            bl+=1
            if tokens[i] not in bad:bad[tokens[i]]=1
            else:bad[tokens[i]]+=1
    if go%10==0:
        graphx.append(go)
        graphy.append(acc('run_results.txt')*100)

mng,mnb = 1,1
for key in good.keys():
    mng=min(mng,good[key]/gl)

for key in bad.keys():
    mnb=min(mnb,bad[key]/bl)
mng/=10
mnb/=10
def predict(sentence):
    words = sentence.split()
    pg,pb = 1,1
    for word in words:
        if word in good:pg *= good[word]/gl
        else:pg *= mng
        if word in bad:pb *= bad[word]/bl
        else:pb *= mnb
    #return (pg,pb)
    if pg>=pb:return 'positive'
    else:return 'negative'

def predict2(words):
    pg,pb = 1,1
    for word in words:
        if word in good:pg *= good[word]/gl
        else:pg *= mng
        if word in bad:pb *= bad[word]/bl
        else:pb *= mnb
    if pg>=pb:return 1
    else: return 0

import matplotlib.pyplot as plt
plt.plot(graphx,graphy)
plt.title('Accuracy graph')
plt.xlabel('iterations')
plt.ylabel('accuracy')
plt.show()


# check for queries

query = 'worst journey ever'
print(predict(query))




    