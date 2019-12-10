import random
import os
from tqdm import tqdm
import shutil
import pathlib

data_dir = "original_images"
classes = ["im_Dyskeratotic", "im_Koilocytotic", "im_Metaplastic", "im_Parabasal", "im_Superficial-Intermediate"]
output_dir = "images"
ratio = [0.8, 0.1, 0.1]

def split_folder(data_dir, output_dir, ratio):
    # for each cell 
    for cell in classes:
        cell_path = os.path.join(data_dir, cell)
        files = os.listdir(cell_path)
        files = [os.path.join(cell_path, f) for f in files if f.endswith('.bmp')]

        # Split the images in 'train_signs' into 80% train and 20% val
        # Make sure to always shuffle with a fixed seed so that the split is reproducible
        random.seed(230)
        files.sort()
        random.shuffle(files)

        # ratio for train, validation and test
        split_train = int(ratio[0] * len(files))
        split_val = split_train + int(ratio[1] * len(files))

        # split files 
        files_train = files[:split_train]
        files_val = files[split_train:split_val] 
        files_test = files[split_val:]
        files_type = [(files_train, "train"), (files_val, "val"), (files_test, "test")]

        # copy files into output directory
        for (files, folder_type) in files_type:
            full_path = os.path.join(output_dir, folder_type)
            full_path = os.path.join(full_path, cell)
            pathlib.Path(full_path).mkdir(parents=True, exist_ok=True)
            for f in files:
                shutil.copy2(f, full_path)

split_folder(data_dir, output_dir, ratio)