from gensim.models import KeyedVectors

def main():
    # 加载 2 种不同格式的模型
    word_vector1 = KeyedVectors.load_word2vec_format(
        "./.models/GoogleNews-vectors-negative300.bin.gz", binary=True
    )
    word_vector2 = KeyedVectors.load('./.models/word2vec-google-news-300.model')

    # 词嵌入，获取向量
    word = "phone"
    vector1 = word_vector1[word]
    vector2 = word_vector2[word]
    print(type(vector1), vector1[:5])
    print(type(vector2), vector2[:5])
    print((vector1 == vector2).all())

    # Gensim 其他常用的方法
    word1 = "apple"
    word2 = "banana"
    word_list1 = ["i", "eat", "apple"]
    word_list2 = ["i", "eat", "banana"]

    # Compute cosine similarity between two sets of words.
    # 计算两列单词之间的余弦相似度——也可以用来评估文本之间的相似度
    print(word_vector2.n_similarity(word_list1, word_list2))

    # Compute cosine similarity between two words.
    # 计算2个词之间的余弦相似度
    print(word1, "vs", word, ":", word_vector2.similarity(word1, word))
    print(word1, "vs", word2, ":", word_vector2.similarity(word1, word2))

    # 找出前 3 个最相似的词
    print(word_vector2.similar_by_word(word, topn=3))


if __name__ == "__main__":
    main()