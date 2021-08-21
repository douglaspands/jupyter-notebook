import os
import platform
from typing import Any, Dict, List, Union

import toml

if platform.system() == "Windows":
    os.environ["COMSPEC"] = "powershell"


cache = {}


# ===================================================
# SUPPORT FUNCTIONS
# ===================================================


def import_pyproject() -> Dict[str, Any]:
    global cache
    if not cache.get("pyproject"):
        with open("pyproject.toml", "r") as file_input:
            cache["pyproject"] = toml.loads(file_input.read())
    return cache["pyproject"]


def get_app_basename() -> str:
    pyproject = import_pyproject()
    return pyproject["tool"]["poetry"]["name"]


def get_app_path() -> str:
    app_path = os.path.join(os.getcwd(), get_app_basename())
    return app_path


def shell_run(command: Union[str, List[str]]) -> bool:
    res = True
    for cmd in command if isinstance(command, list) else [command]:
        print(f"$ {cmd}")
        if os.system(cmd):
            res = False
            break
    return res


# ===================================================
# POETRY SCRIPTS
# ===================================================


def start():
    cmd = "jupyter lab --no-browser --notebook-dir={notebook_folder}".format(
        notebook_folder=os.path.join(get_app_path(), "notebook")
    )
    shell_run(cmd)


def install_extensions():
    cmd = "jupyter contrib nbextension install --user"
    shell_run(cmd)


def create_ps1():
    script_ps1 = f"cd {os.getcwd()}; poetry run start"
    with open(os.path.join(os.getcwd(), "start.ps1"), "w") as file:
        file.write(script_ps1)


def create_sh():
    script_sh = f"cd {os.getcwd()}; poetry run start"
    with open(os.path.join(os.getcwd(), "start.sh"), "w") as file:
        file.write(script_sh)


def create_script():
    if platform.system() == "Windows":
        create_ps1()
    else:
        create_sh()


def requirements_gen():
    cmd = "poetry export -f requirements.txt --without-hashes --output requirements.txt"
    shell_run(cmd)
