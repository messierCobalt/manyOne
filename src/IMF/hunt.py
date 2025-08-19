"""
Good morning Mr. Phelps

This is a CLI tool... only for python scripts in this repo

Ethan Hunt will be your point-man as usual...
"""

import os
import sys
import functools

try:
    from rachel import *
except ImportError:
    from .rachel import *

if os.name != "nt":
    import readline

VERSION = "v0.1.8"

# ================= FIRST STEPS ==================
try:
    filename = os.path.basename(sys.argv[0])
except TypeError:
    filename = "<unknown>"

HELP = f"""
{B_BLUE}BASIC CMDS{RST}:
    clear | monica ------ cleans terminal screen
    exit | terminate ---- kills {filename}
    help | manual ------- prints this
""" # it'll get appended... post-importation-to-another-program

def monica(quiet: bool = False) -> None:
    """
    Monica Geller cleans...
    Meanwhile... her: I knowwwwww
    """
    if not quiet:
        print(f"{B_GREEN}Cleanin'{RST}...")
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except: 
        flag(17)

def terminate(final: str | int = f"{B_BLUE}Hasta La Vista... Baby!!!{RST}") -> None:
    """
    I will crawl away from here
    you won't be afraid to fear
    no thought was put into this
    I always knew it'd come to this
    """
    sys.exit(final)

# ================= ERROR HANDLING ==================

glitches = {
    1: "unknownError",
    2: "invalidCmd",
    3: "inputError",
    4: "notFound",
    5: "valueError",
    6: "syntaxError",
    7: "rareError", 
    8: "ultraRareError", 
    9: "undefedName",
    10: "endOfFile",
    11: "accessDenied",
    12: "timeOutError",
    13: "keyboardInterruption",
    14: "osError",
    15: "keyError",
}

@functools.lru_cache(maxsize=48)
def flag(code: int, close: bool = False) -> None:
    """
    Rasing the Flag by John Murphy
    """
    try:
        print(f"{B_RED}E{RST}({code}) -> {RED}{glitches[code]}{RST}")
    except KeyError:
        print(f"{B_RED}E{RST}({code}) -> {RED}{glitches[code]}{RST}")
        terminate(0)

    if close:
        terminate()

# ================= REGISTRY ==================

registry = {} # It'll store the cmd with their respictive function!

def regedit(cmds: tuple[str], fn: callable) -> None:
    """
    Not Windows
    """
    for cmd in cmds:
        try:
            registry[cmd] = fn
        except KeyError:
            flag(15)
            continue

# ================= ACTIVATION ==================

def activate(version: str = VERSION, help: str = HELP) -> None:
    """
    def __init__(mine):
        pass
    """
    regedit(("clear", "cls", "monica"), monica)
    regedit(("abort", "terminate", "exit", "quit", "close"), terminate)
    regedit(("help", "manual"), lambda: print(help))
    regedit(("--version", "-v", "version"), lambda: print(version))
    # and that is how you call regedit()

# ================== TESTS ==================

if __name__ == "__main__":
    activate()
    print(f"{BLD}hunt {VERSION}{RST}")

    try:
        while True:
            userInput = input("> ").strip()
            if not userInput:
                continue
            func = registry.get(userInput)
            if func:
                func()
            else:
                flag(2)
    except KeyboardInterrupt:
        flag(13, close=True)

"""
We live and die in the shadows
for those we hold close
and for those we never meet.
"""
