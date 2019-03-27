## An implementation of Syntax sql Models in Allennlp

This is a initial implementation of testing pretrained models provided by Syntax SQL authors [link](https://drive.google.com/file/d/1FHEcceYuf__PLhtD5QzJvexM7SNGnoBu/view?usp=sharing)
This repository contains the changed files apart from the ones already in the repository located [here](https://github.com/taoyds/syntaxSQL)
The only changes are in supermodel.py (renamed to synaxsql_supermodel.py added few methods indicated with comments), utils.py(not added -only python2 to python 3 changes), models (in progress changes for running the training part). The models defined in allen_models are taken from the original syntax sql repository itself with some changes by adding Allennlp model wrappers in order to support in allennlp. 
The newly added files are syntax_sql_predictor.py and syntax_sql_reader.py
There exists a collective model -[model.tar.gz](https://drive.google.com/file/d/1-hmi3uPKvMlGoez16kWfWeXJgbkYiW5a/view?usp=sharing) with supermodel as a topmost class created using the different pretrained models provided in the above link. 
Also, a python colab notebook in which the experiments were executed and some results files are included. 

## Acknowledgements

1. Source code of our EMNLP 2018 paper: [SyntaxSQLNet: Syntax Tree Networks for Complex and Cross-DomainText-to-SQL Task
](https://arxiv.org/abs/1810.05237).
2. Syntax sql [Github repo](https://github.com/taoyds/syntaxSQL)
3. Allennlp [Github](https://github.com/allenai/allennlp) and [Docs](https://allenai.github.io/allennlp-docs/)
4. SQLNet [Github repo](https://github.com/xiaojunxu/SQLNet)


