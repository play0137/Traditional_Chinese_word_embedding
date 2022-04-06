""" 用Spearman's rank correlation來評估word embedding """
import os
import pathlib
from gensim.models import Word2Vec, KeyedVectors

def main():
    here = pathlib.Path(__file__).parent.resolve()
    input_word_embedding = r'path_to_your_count_based_word_embedding\SVD_700d_ws3.vec' # count-based
    # input_word_embedding = r'path_to_your_CBOW_word_embedding\word2vec_500d_CBOW.model' # prediction-based

    input_testsets = str(here) + r"\testsets"
    file_list = getInputFilesName(input_testsets)
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
            m = KeyedVectors.load_word2vec_format(input_word_embedding, binary=True)
        elif file_extension == 'model':
            m = Word2Vec.load(input_word_embedding)

        for i in range(len(testset_list)):
            print(testset_list[i].split('\\')[-1])
            print(m.wv.evaluate_word_pairs(testset_list[i], delimiter=" ")[1])

        
# read files
def getInputFilesName(dirPath):
    file_list = list()
    for dir_path, dir_names, file_names in os.walk(dirPath):
        for file in file_names:
            if "txt" in file:
                file_list.append(os.path.join(dir_path, file))
    return file_list

if __name__ == "__main__":
    main()