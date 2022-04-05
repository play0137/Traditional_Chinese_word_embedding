""" 用來評估word embedding的方法 """
import os
import sys
import numpy as np
from scipy import stats
from gensim.models import Word2Vec, KeyedVectors
import pdb

skipped_dims = 0  # skip the first k columns of SVD matrix

# read files
def getInputFilesName(dirPath):
    file_list = list()
    for dir_path, dir_names, file_names in os.walk(dirPath):
        for file in file_names:
            file_list.append(os.path.join(dir_path, file))
    return file_list

def readVocabList(vocab_list_path):
    vocab_list = list()
    with open(vocab_list_path, 'r', encoding="UTF-8") as f:
        for line in f:
            line = line.replace(' ', '')
            line = line.split(':')

            #看詞頻要大於多少才計算, noHMM > 29, with_HMM > 79
            if int(line[1]) > 29:
                vocab_list.append(line[0])
    vocab_list.sort()
    return vocab_list

def Spearman(test_rank, my_rank):
    total = 0
    pair_num = len(test_rank)

    for i in range(pair_num):
        total += (test_rank[i]-my_rank[i])**2
    spearman = 1 - 6 * total / (pair_num * (pair_num**2 - 1))
    return spearman

def main():
    # ptt_wiki_noHMM
    vocab_list_path = r"D:\Andy\研究所\research\workspace\word_frequency\ptt_wiki\ptt_wiki_frequency_noHMM.txt"
    # input_word_embedding = r"D:\Andy\研究所\research\model\word_embedding\pre_trained_word_embedding\wiki.zh.align.vec"
    input_word_embedding = r'D:\Andy\研究所\research\model\word_embedding\ptt_wiki\count_based\best_model\SVD_700d_ws3_p0.5_SPPMI_k10_skip6_321.npy'
    # input_word_embedding = r"D:\Andy\研究所\research\model\word_embedding\ptt_wiki\prediction_based\unused\window_2_noHMM\skip_gram\word2vec_300d_skip_alpha005_sample000001_neg2_iter5.model"
    
    # ptt_wiki_chinatimes_ltn
    # vocab_list_path = r"D:\Andy\研究所\research\workspace\word_frequency\ptt_wiki_chinatimes_ltn\frequency_noHMM.txt"
    # input_word_embedding = r"D:\Andy\研究所\research\model\word_embedding\ptt_wiki_chinatimes_ltn\count_based\SVD\normalization\window_3\find_optimal_caron_p\SVD_1200d_ws3_p0.5_SPPMI_k10_321.npy"

    input_testset = r"D:\Andy\研究所\research\workspace\datasets\similarity_relatedness"
    file_list = getInputFilesName(input_testset)
    testset_list = list()
    # 排檔案順序
    testset_list.append(file_list[1])
    testset_list.append(file_list[3])
    testset_list.append(file_list[6])
    testset_list.append(file_list[0])
    testset_list.append(file_list[2])
    testset_list.append(file_list[5])
    testset_list.append(file_list[7])
    testset_list.append(file_list[4])
    
    file_extension = input_word_embedding.split('.')[-1]
    if file_extension == 'vec' or file_extension == 'model':
        if file_extension == 'vec':
            """ pre_trained_word_embedding """
            m = KeyedVectors.load_word2vec_format(input_word_embedding, binary=True)
        elif file_extension == 'model':
            """ prediction-based """
            m = Word2Vec.load(input_word_embedding)

        for i in range(len(testset_list)):
            print(testset_list[i].split('\\')[-1])
            print(m.wv.evaluate_word_pairs(testset_list[i], delimiter=" ")[1])
        sys.exit(0)

    elif file_extension == 'npy':
        """ count-based """
        vocab_list = readVocabList(vocab_list_path)
        words_vec_array = np.load(input_word_embedding)
        (row, col) = words_vec_array.shape
        print("shape:", words_vec_array.shape)

        # create words vector dict
        words_vec = dict()
        for r in range(row):
            words_vec[vocab_list[r]] = words_vec_array[r][skipped_dims:]

        score_list = list()
        print("Spearman rank-order(count):")
        for i in range(len(testset_list)):
            with open(testset_list[i], 'r', encoding="UTF-8") as file_r:
                testset = file_r.readlines()

            test_score = list()
            my_score = list()
            words_pair = list()
            OOV_pairs = 0
            total_pairs = 0
            # create score list of test set and my data
            for test_line in testset:
                total_pairs += 1
                test_line = test_line.strip("\n")
                test_w1, test_w2, t_score = test_line.split(" ")
                if test_w1 in vocab_list and test_w2 in vocab_list:
                    test_score.append(float(t_score))

                    #cosine similarity
                    #my_score.append(np.dot(words_vec[test_w1], words_vec[test_w2]) / (np.linalg.norm(words_vec[test_w1])*np.linalg.norm(words_vec[test_w2])) )
                    '''因為embedding有做過normalization了，所以不用除於長度'''
                    my_score.append(np.dot(words_vec[test_w1], words_vec[test_w2]))
                    words_pair.append(test_w1+" "+test_w2)

                elif test_w1 not in vocab_list:
                    # print("OOV w1:", test_w1)
                    OOV_pairs += 1
                elif test_w2 not in vocab_list:
                    # print("OOV w2:", test_w2)
                    OOV_pairs += 1

            # sort the data in descending order
            test_rank = len(test_score) - stats.rankdata(test_score).astype("int64")
            my_rank = len(my_score) - stats.rankdata(my_score).astype("int64")

            # calculate Spearman rank-order
            spearman_score = Spearman(test_rank, my_rank)
            score_list.append(spearman_score)

            file = testset_list[i].split("\\")
            print(file[len(file)-1]+':')
            print(f"{round(spearman_score, 3)}, OOV:{OOV_pairs}/{total_pairs}({round((OOV_pairs/total_pairs)*100, 1)}%)\n")
            
            if i == 2:
                avg_score = 0
                for score in score_list[:3]:
                    avg_score += score
                print(f"avg_similar_score:\n{round(avg_score/3, 3)}\n")
            elif i == 6:
                avg_score = 0
                for score in score_list[3:7]:
                    avg_score += score
                print(f"avg_relatedness_score:\n{round(avg_score/4, 3)}\n")

        avg_score = 0
        for score in score_list:
            avg_score += score
        print(f"total_avg:\n{round(avg_score/8, 3)}")


if __name__ == "__main__":
    main()