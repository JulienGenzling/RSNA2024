### RSNA2024

In order to use the code :

- Download the challenge data : `kaggle competitions download -c rsna-2024-lumbar-spine-degenerative-classification` in `/Data/RSNA/` or update `config.py` paths (warning : the data is 35.34 GB)
- run `preprocess.py` to create 3D crops using the original dicoms.
- run `train.py` to train 3D maxxvit model. 

Feel free to change model / loss or preprocessing steps. 

