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


def store_values(dictionary, key):
    try:
        value = dictionary[key]
        print("The previously entered value for ''%s'' has been used for this similar placeholder." % key)
        return value
    except KeyError:
        while True:
            value = str(input("Enter value for %s:\n" % key)).replace(" ", "")
            if value != '':
                dictionary[key] = value
                return value


def find_replace_yaml(file_path):
    param_dict = {}
    print("Editing YAML File: %s" % file_path)
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            regex_1 = r'(.*?):\s\$\{'
            p = re.compile(regex_1)
            param = p.findall(lines[i])
            if not len(param) == 0:
                param_key = param[0]
                param_value = store_values(param_dict, param_key)
                regex_2 = r'\$\{.*?}'
                new_line = re.sub(regex_2, param_value, lines[i])
                lines[i] = new_line
        f.close()
    with open(file_path, 'w') as f:
        f.writelines(lines)
        print("Closing file: %s\n" % file_path)
        f.close()


def find_replace_sh(file_path):
    param_dict = {}
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
                        param_key = param[j].split(':-${')[1]
                        param_value = store_values(param_dict, param_key)
                        lines[i] = lines[i].replace('${' + param_key + '}', param_value)
                    else:
                        if ':-' in param[j]:
                            pass
                            # Do something
                        else:
                            param_key = param[j]
                            param_value = store_values(param_dict, param_key)
                            lines[i] = lines[i].replace('${' + param_key + '}', param_value)
        f.close()
    with open(file_path, 'w') as f:
        f.writelines(lines)
        print("Closing file: %s\n" % file_path)
        f.close()
