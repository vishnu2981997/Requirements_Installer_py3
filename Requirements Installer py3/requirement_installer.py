"""
Requirement Installer PY3 : Given a python project directory searches for python imports from py files and installs them if doesnt exist.
"""
import os

def get_files(directory):
    """
    :param directory: Path to the python project folder
    :return: All available file paths in the specified directory
    """

    file_paths = []

    # Fetching .py file paths

    for subdir, dirs, files in os.walk(directory):

        dirs = dirs

        for file in files:

            path = str(os.path.join(subdir, file))

            if path[-3:] == ".py":

                file_paths.append(path)

    return file_paths

def fetch_imports(files):
    """
    :param files: A list of all avaliable .py file paths
    :return: A list of imports present in all the .py files
    """

    imports = []

    keys = ["import", "from"]

    # Fetching import statements

    for file in files:

        imports.extend(i.split() for i in open(file, "r") if i.split() and i.split()[0] in keys)

    return imports

def install(imports):
    """
    :param imports: A list of python packages(imports)
    :return: Null
    """

    # Installing required imports

    for imp in imports:

        if imp[0] == "import":

            imp = " ".join(i for i in imp)

            try:

                exec(imp)

            except ImportError:

                imp = imp.split()

                print(imp[1]+" dosent exist")

                option = input("do u want to install it(y/n) : ").lower()

                if option == "y":

                    os.system("pip install "+imp[1])
        else:

            if "." in imp[1]:

                imp = "import "+imp[1].split(".")[0]

                try:

                    exec(imp)

                except ImportError:

                    imp = imp.split()

                    print(imp[1]+" dosent exist")

                    option = input("do u want to install it(y/n) : ").lower()

                    if option == "y":

                        os.system("pip install "+imp[1])

def main():
    """
    :return: Null
    """

    files = get_files(input("Enter the python project die path : "))

    imports = fetch_imports(files)

    install(imports)

if __name__ == "__main__":
    main()
