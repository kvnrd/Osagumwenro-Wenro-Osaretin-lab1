import os
import random

#try to implement more comments about your methods in order to explain what you are doing in each method. 
#great usage of variable names 
#clean code.


def get_dirs_and_files(path):
    print(path)
  
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    print(dir_list)
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):

    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

    # Your code goes here
    for file in file_list:
        prob = classify_pic(path + file)
        if prob > 0.5:
            dog_list.append(file)
        else:
            cat_list.append(file)
    for dir in dir_list:
        if os.path.exists(path):
           continue
        if not dir_list:
           return path + dir
        elif dir_list:
             c,d = process_dir(path + dir)
             cat_list = os.path.join(c, cat_list)
             dog_list = os.path.join(d, dog_list)
    return cat_list, dog_list

def main():
    start_path = 'C:/Users/wenro/Documents/1.1 CatsDogs' # current directory

    process_dir(start_path)


main()
