from .auto_flink import download_repo, explode_dir


def main():
    d_path = download_repo()
    arr = explode_dir(d_path)


if __name__ == '__main__':
    main()
