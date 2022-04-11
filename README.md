[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

# Overview

Use PTT (bulletin board system (BBS) in Taiwan) and Chinese Wiki corpora to build count-based and prediction-based word embeddings.  
The [evaluations](https://github.com/play0137/Traditional_Chinese_word_embedding/tree/master/evaluation) in similarity/relatedness tasks are better than the other pre-trained word embeddings.  

## Chinese Word Embeddings
Download
- [Chinese_word_embedding_count_based](https://mega.nz/file/OZJAwCSS#AjAg4wSNlJYZ7RrIJWvTdN8KAHGWpYC3TtnuyUDfR8A)
- [Chinese_word_embedding_CBOW](https://mega.nz/file/WBg22arI#CXf8WuIacWWBJGON8qpR-YKBYfTmRPaMONx5wj3t_Wg)

## Hyperparameter
Chinese_word_embedding_count_based  
Hyperparameter              | Setting
:--------------------------:|:----------:
Frequency weighting         | SPPMI_k10
Window size                 | 3
Dimensions                  | 700
Remove first k dimensions   | 6
Weighting exponent          | 0.5
Discover new words          | no

Chinese_word_embedding_CBOW  
Hyperparameter       | Setting
:-------------------:|:----------:
Window size          | 2
Dimensions           | 500
Model                | CBOW
Learning rate        | 0.025
Sampling rate        | 0.00001
Negative samples     | 2
Discover new words   | no

# References

If you use the Chinese word embedding in your works, please cite this paper:
> Ying-Ren Chen (2021). [Generate coherent text using semantic embedding, common sense templates and Monte-Carlo tree search methods](https://etd.lib.nctu.edu.tw/cgi-bin/gs32/hugsweb.cgi?o=dnthucdr&s=id=%22G021040625840%22.&searchmode=basic) (Master's thesis, National Tsing Hua University, Hsinchu, Taiwan).  

# License

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].  
[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
