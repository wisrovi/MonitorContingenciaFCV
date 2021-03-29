
import os.path as path
from decouple import config

from Util.autoupdate import Autoupdate


@Autoupdate(name="Autoupdate WISROVI", project=config('project', default=''), root_path=path.dirname(path.realpath(__file__)))
def main_demo_autoupdate():
    print("update library")


if __name__ == "__main__":

    print()
    print("*********************************************************")
    print("*\t", "Autor: " "\t\t\t\t\t\t\t\t\t\t\t*")
    print("*\t", config('autor', default=''), "\t\t\t\t*")
    print("*\t", config('alias_autor', default=''), "\t\t\t\t\t\t\t\t\t\t\t*")
    print("*\t", config('email_autor', default=''), "\t\t\t\t\t\t*")
    print("*\t", config('linkedin_autor', default=''), "\t*")
    print("*********************************************************")
    main_demo_autoupdate()
