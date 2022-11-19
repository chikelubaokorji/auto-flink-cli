import os
import re
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
            if not ('/.git/' in path):
                arr_path.append(path)
    return arr_path


def find_replace_yaml(file_path):
    print("Editing YAML File: %s" % file_path)
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            p = re.compile(r'(.*?):\s\$\{')
            param = p.findall(lines[i])
            if not len(param) == 0:
                replace_str = str(input("Enter value for %s:\n" % param[0]))
                regex = r'\$\{.*?}'
                new_line = re.sub(regex, replace_str, lines[i])
                lines[i] = new_line
        f.close()
    with open(file_path, 'w') as f:
        f.writelines(lines)
        print("Closing file: %s\n" % file_path)
        f.close()


def replace_placeholder_sh(file_path):
    print("Editing Bash File: %s" % file_path)
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            regex = r'(?:\:\-\$\{.*?\}\})|(?:\$\{(.*?)})'
            p = re.compile(regex)
            param = p.findall(lines[i])
            if not len(param) == 0:
                print("\nEditing placeholders in line: %s" % lines[i])
                for j in range(0, len(param)):
                    if ':-${' in param[j]:
                        replace_str = str(input("Enter value for %s:\n" % param[j].split(':-${')[1])).replace(" ", "")
                        lines[i] = lines[i].replace('${' + param[j].split(':-${')[1] + '}', replace_str)
                    else:
                        if ':-' in param[j]:
                            pass
                            # Do something
                        else:
                            print(param[j])
                            replace_str = str(input("Enter value for %s:\n" % param[j])).replace(" ", "")
                            lines[i] = lines[i].replace('${' + param[j] + '}', replace_str)
                            print(lines[i])
        f.close()
    with open(file_path, 'w') as f:
        f.writelines(lines)
        print("Closing file: %s\n" % file_path)
        f.close()
