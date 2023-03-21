# Pegasus_with_Longformer

## How to run the project
To run this project, clone the repo and execute the following commands:

1) Install Anaconda here: https://docs.anaconda.com/anaconda/install/linux/
2) `cd datn`
3) Create env Anaconda `conda create --name <env> --file <this file>` (requirement.txt)
4) `python3 download_data.py` for download data (arxiv, xsum, big_patent,...) 
5) `python3 preprocess_data.py` Tien xu ly du lieu
6) `python3 generate.py` Dua du lieu vao mo hinh 
7) `python3 json_to_dict` Chuyen du lieu sinh ra tu dinh dang json sang dictionary
8) `python3 eval.py` Danh gia mo hinh


