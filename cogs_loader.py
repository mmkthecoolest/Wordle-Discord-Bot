from os import listdir
from os.path import isfile, join


def load_cog_list():
    onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
    non_cogs = ["bot.py", "cogs_loader.py"]
    py_files = [x.split(".py")[0] for x in onlyfiles if (
        x.lower().endswith(".py") and x not in non_cogs)]
    return py_files
