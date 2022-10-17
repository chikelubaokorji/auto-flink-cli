import os
import time


def download_repo():
    while True:
        try:
            ssh_link = str(input("Enter the a valid GitHub SSH link:\n"))
            str_ext = ssh_link.split(':')[1].split('.')[0].replace('/', '')
            d_path = "./downloads/" + str_ext + str(time.time())
            os.system(" mkdir " + d_path + " && " + " git clone " + ssh_link + " " + d_path)
            break
        except (IndexError, ValueError):
            print("Invalid Input. Try Again.")
    return d_path


def explode_dir(d_path):
    arr_path: list = []
    for root, _, files in os.walk(d_path):
        for f in files:
            path = "{}/{}".format(root, f)
            if not path.__contains__(".git"):
                arr_path.append(path)
    return arr_path
