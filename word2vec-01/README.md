# Word2vec 的预训练模型使用

学一点，积累一点，拿来就能用。

## Code

**Gensim:** 致力于将文本表达为向量的开源Python库
**KeyedVectors:** 不管预训练什么模型（Word2Vec、FastText等），最后都是为了通过 "键"（单词、短句等） 找到 "向量" 的映射。该模块就是应用于将 "键" 映射到 "向量" 。

## 参考资料

[加载使用谷歌的预训练模型googlenews-vectors-negative300.bin.gz](https://blog.csdn.net/fgg1234567890/article/details/112974650)
[Word2Vec模型保存与加载的两种方式](https://www.jianshu.com/p/8d03e3c5b9ec)
[Gesim官网](https://radimrehurek.com/gensim/intro.html)
[KeyedVectors 源代码](https://github.com/piskvorky/gensim/blob/develop/gensim/models/keyedvectors.py)
[Gensim之Word2vec介绍](https://blog.csdn.net/qq_27586341/article/details/90025288)

## 模型下载

[https://code.google.com/archive/p/word2vec/](https://code.google.com/archive/p/word2vec/)
[https://huggingface.co/fse/word2vec-google-news-300/tree/main](https://huggingface.co/fse/word2vec-google-news-300/tree/main)
