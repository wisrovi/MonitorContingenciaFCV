
import os.path as path

from Util.autoupdate import Autoupdate


@Autoupdate(name="Autoupdate WISROVI", project="wisrovi/MANITOR-Raspberry", root_path=path.dirname(path.realpath(__file__)))
def main_demo_autoupdate():
    print("update library")


if __name__ == "__main__":
    main_demo_autoupdate()
