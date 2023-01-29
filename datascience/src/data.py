import requests
import os

URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

def download_data():
    response = requests.get(URL)
    file_path = "src/" + URL.split("/")[-1]
    open(file_path, "wb").write(response.content)
    return file_path

def remove_data(file_path):
    os.remove(file_path)
