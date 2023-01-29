from libs import download_titanic_and_split_dataset, train_model_and_return_auc_titanic
from libs import create_models, mean_auc
import numpy as np
import pickle

def clean_files_with_extension(extension):
    import glob
    import os
    files = glob.glob("*." + extension)
    for file in files:
        os.remove(file)

if __name__ == "__main__":
    data = download_titanic_and_split_dataset()
    models = create_models()
    aucs = []
    for model in models:
        aucs.append(train_model_and_return_auc_titanic(model, data))
    print(aucs)
    print(mean_auc(aucs))
    best_model = models[np.argmax(aucs)]
    print(best_model)
    model_name = str(best_model).split("(")[0]
    clean_files_with_extension("h5")
    pickle.dump(model, open(model_name + ".h5", 'wb'))