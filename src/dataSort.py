import os
import shutil

file_path = "C:\\Users\\joon0\\Desktop\\Coding\\I&D\\datasets\\metamorphic"
file_names = os.listdir(file_path)

os.mkdir("../datasets/ori/metamorphic")

for i, name in enumerate(file_names):
    src = os.path.join(file_path, name)
    shutil.copy2(src, f"/datasets/ori\\metamorphic\\metamorphic_{i}.jpg")

