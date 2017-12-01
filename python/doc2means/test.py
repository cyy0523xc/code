# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2017年12月01日 星期五 22时14分24秒
import jieba
import logging
import gensim
from sklearn.cluster import KMeans
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO)


# get input file,text format
source_filename = 'source.txt'
seq_filename = 'output.seq'
if False:
    with open(source_filename, 'r') as f, open(seq_filename, 'w') as output:
        input_lines = f.readlines()
        count = len(input_lines)
        print('源文件行数为：' + str(count))

        # read file and seperate words
        for line in input_lines:
            line = line.strip('\n')
            seg_list = jieba.cut(line)
            output.write(' '.join(seg_list)+'\n')

# 训练并保存模型
model_filename = "output.model"
sentences = gensim.models.doc2vec.TaggedLineDocument(seq_filename)
model = gensim.models.Doc2Vec(sentences, size=100, window=3)
model.train(sentences)
model.save(model_filename)

# k-means预测
num_clusters = 20    # 设定聚类个数
km = KMeans(n_clusters=num_clusters)  # 设置模型参数
result = km.fit_predict(model.docvecs)  # 用doc2vec训练的模型产生的句向量作为k-means的输入

# 将聚类预测结果和具体文档处理对应上
output_filename = 'output.txt'
with open(source_filename, 'r') as fr, open(output_filename, 'w') as fw:
    for i in range(0, num_clusters-1):
        for linenumber, eachline in enumerate(fr.readlines()):
            if linenumber >= len(result):
                break
            if result[linenumber] == i:
                fw.write(eachline+'\n')

        fw.write('------------------ %d -----------------------\n' % i)
