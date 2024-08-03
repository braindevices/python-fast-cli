from typing import Dict
from packaging import version
from glob import glob
import os

PROJECT_NAME = "fast_com_cli"
dist_dir = os.path.realpath("./dist")


def write_to_github_output(data: Dict[str, str]):
    # Get the path to the GitHub output file
    github_output_path = os.getenv('GITHUB_OUTPUT')

    if github_output_path:
        with open(github_output_path, 'a') as f:
            for key, val in data.items():
                f.write(f"{key}={val}\n")
    else:
        print(data)


def main():
    is_pypi_compatible = False
    gz_files = glob(f"{dist_dir}/{PROJECT_NAME}-*.tar.gz")
    if not gz_files:
        raise RuntimeError(f"there is no gz package file in {dist_dir}")
    for i in gz_files:
        file_ver = os.path.basename(i).lstrip(PROJECT_NAME + "-").rstrip(".tar.gz")
        if version.parse(file_ver).local:
            is_pypi_compatible = False
            break
        else:
            is_pypi_compatible = True
    write_to_github_output({"is_pypi_compatible": str(is_pypi_compatible).lower()})
    

if __name__ == "__main__":
    main()
