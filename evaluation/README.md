## Run the evaluation
Ensure you have installed [Gensim](https://radimrehurek.com/gensim/) >= 4.0.0 library already.  
Change the input_word_embedding_path in Spearman.py to your own path, and run it.

## Compare to other pre-trained word embeddings
Calculate the cosine similarity between two word vectors to get their distance in low dimension vector space.  
After that, we adopt Spearman's rank correlation coefficient as evaluation function.  
It calculates the rank difference of two sequences in descending order.  
Two sequences are highly correlated if the value is close to 1, and less correlated if it is close to -1.  
Then we compare spearman scores with [gold standards](https://github.com/play0137/Traditional_Chinese_word_embedding/tree/master/evaluation/testsets) (human judgement).

<p align="left">
  <img width="700" height="300" src="./relatedness_compare_to_other_pre_trained_word_embeddings.png">
</p>

Table 4.9 shows comparison of our word embeddings and other pre-trained ones in relatedness tasks.  
Our count-based model outperforms other models in the similarity/relatedness tasks,  
and our prediction-based model and Numberbatch are the second.  
Even if the same dimensions (300d), our model still outperforms other pre-trained ones.  

---

<p align="left">
  <img width="700" height="300" src="./similarity_compare_to_other_pre_trained_word_embeddings.png">
</p>

Table A.4 shows the comparison in similarity tasks. Our prediction model has the highest spearman score.
