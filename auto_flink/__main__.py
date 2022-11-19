from .auto_flink import *


def main():
    d_path = download_repo()
    arr = explode_dir(d_path)
    for i in arr:
        if '.sh' in i[-len('.sh')::]:
            find_replace_sh(i)
        elif '.yaml' in i[-len('.yaml')::]:
            find_replace_yaml(i)


if __name__ == '__main__':
    main()
