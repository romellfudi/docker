// JupyterLab
docker pull jupyter/minimal-notebook
docker volume create demo-volume
docker run -p 8888:8888 -v demo-volume:/home/jovyan/work jupyter/minimal-notebook
docker volume create prueba_v
docker run -p 8888:8888 \
    -v demo-volume:/home/jovyan/work \
    -v prueba_v:/home/jovyan/prueba \
    jupyter/minimal-notebook

docker volume create all_data

docker run -p 8888:8888 \
    -v demo-volume:/home/jovyan/work \
    -v prueba_v:/home/jovyan/prueba \
    -v all_data:/home/jovyan/ \
    jupyter/minimal-notebook

volume all_data:
.bash_logout
.bashrc
.cache
.conda
.ipynb_checkpoints
.ipython
.jupyter
.local
.npm
.profile
.wget-hsts
numpy.ipynb
prueba
work



