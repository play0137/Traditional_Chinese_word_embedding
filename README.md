[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

# Overview

Use PTT (bulletin board system (BBS) in Taiwan) and Chinese Wiki corpora to build count-based and prediction-based word embeddings.  
The [evaluation](https://github.com/play0137/Traditional_Chinese_word_embedding/tree/master/evaluation) in similarity/relatedness tasks is better than the other pre-trained word embeddings.  

## Chinese Word Embeddings
- [Chinese_word_embedding_count_based](https://mega.nz/file/2RowDQrC#WiZ6z-HdeB7ysN97C_0GIQeXuS7JsX1TDhZOcttPsfg)
- [Chinese_word_embedding_CBOW](https://mega.nz/file/ScxjgZAA#mhZyzQfRTZWcRatIPiI8e-9Frf4DqV9AGm5gUBf2TgQ)

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

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
