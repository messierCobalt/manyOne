"""
he Jumps between CASEs... 
don't be fooled... 
even tho. he's named CASE... 
he's more like TARS
"""

import os
import shlex
from IMF.hunt import *

VERSION = "v0.4.1"

HELP += f"""
{B_BLUE}CASE cmds{RST}:
    low [txt] ------- lower case
    up [txt] -------- UPPER CASE
    tit [txt] ------- Title Case
    cap [txt] ------- Capitailzed case
    swap [txt] ------ SwAp CaSe -> sWaP cAsE
    alt [txt] ------- aLtErNaTiNg CaSe
    cam [txt] ------- camelCase
    pas [txt] ------- PascalCase
    snake [txt] ----- snake_case
    const [txt] ----- CONSTANT_CASE
    kebab [txt] ----- kebab-case
    dot [txt] ------- dot.case
    path [txt] ------ path/case
    train [txt] ----- Train-Case
    random [txt] ---- rAnDOm cAsE (BmtH'd lOve tHIs)
    cul [txt] ------- cullenCASE (iMADEhim)
    altcul [txt] ---- ALTcullenCASE (HIMtoo)

{B_BLUE}GOD cmd{RST}:
    test ---- run all the cmds!
"""

filename = os.path.basename(__file__)

def div(txt: str, seps=None) -> list:
    seps = seps or ["-", "_", ".", ",", ";"]
    if not txt:
        return []
    cleaned = txt.casefold()
    for sep in seps:
        cleaned = cleaned.replace(sep, " ")
    return shlex.split(cleaned)

def flatcase(txt: str, upper=False) -> str:
    nW = ""
    for char in txt:
        if char.isalnum():
            nW += char.casefold()
    if upper:
        nW = nW.upper()
    return nW


def toLis(words: list | str) -> list:
    if isinstance(words, str):
        return div(words)
    return words


def spread(words: str | list, sep: str):
    words = toLis(words)
    return sep.join(words)


def alt(txt: str) -> str:
    simiFinal = []
    lookUp = True  # isUpper()
    for char in txt:
        if char.isalpha():
            simiFinal.append(char.upper() if lookUp else char.casefold())
            lookUp = not lookUp  # = lookOnDownFromTheBridge
        else:
            simiFinal.append(char)
    return "".join(simiFinal)  # now that is final!!!


def pascal(words: list) -> str:
    nW = ""
    for word in words:
        nW += word.capitalize()
    return nW


def camel(words: list) -> str:
    first = words[0].casefold()
    theOthers = pascal(words[1:])  # just a kidman movie... yet to watch!!!
    return first + theOthers


def sep(words: list, which: str = "_", upper=False) -> str:
    almostPerfect = spread(words, which)
    return almostPerfect.upper() if upper else almostPerfect.casefold()


def train(words: list):
    return "-".join(w.capitalize() for w in words)


def rand(txt: str) -> str:
    nW = ""
    for char in txt:
        if char.isalpha():
            nW += random.choice([char.upper(), char.casefold()])
        else:
            nW += char
    return nW


def cullen(words: list, alt=False) -> str:
    nW = ""
    for i, word in enumerate(words):
        if (i % 2 == 0) == alt:
            nW += word.upper()
        else:
            nW += word.casefold()
    return nW


def jump(words: list | str, style: str) -> str:
    """
    i get up... and nothing gets me down...
    (wish that were true... being an INFP is a curse)
    """
    words = toLis(words)
    key = flatcase(
        style
    )  # the key is only the beginning... whereever it leads... whatever it takes to get there...
    if not words or not key:
        return ""
    txt = " ".join(words)

    cases = {
        "up": lambda: txt.upper(),
        "low": lambda: txt.lower(),
        "tit": lambda: txt.title(),  # oh boy!
        "cap": lambda: txt.capitalize(),
        "swap": lambda: txt.swapcase(),
        "alt": lambda: alt(txt),
        "cam": lambda: camel(words),
        "pas": lambda: pascal(words),
        "snake": lambda: sep(words, "_"),
        "const": lambda: sep(words, "_", upper=True),
        "kebab": lambda: sep(words, "-"),
        "dot": lambda: sep(words, "."),
        "path": lambda: sep(words, "/"),
        "train": lambda: train(words),
        "random": lambda: rand(txt),
        "cul": lambda: cullen(words),
        "altcul": lambda: cullen(words, alt=True),
    }

    return cases.get(key, lambda: "")()


def main() -> None:
    """
    Testing time!
    """
    print(f"{filename} {VERSION}\n")
    activate(version=VERSION, help=HELP)
    while True:
        try:
            pointer = "▷ "
        except UnicodeError:
            pointer = "→ "
        except:
            pointer = "-> "

        try:
            userInput = input(pointer).strip()
        except KeyboardInterrupt:
            flag(13, close=True)

        if not userInput:
            continue

        if userInput in registry:
            registry[userInput]()
            continue

        if userInput.startswith("test"):
            samples = [
                "in five years time. i might not know you.",
                "something elemental, something terrifying.",
            ]  # i'll add more later
            sample = (
                str(userInput[4:].strip())
                if len(userInput.strip()) != 4
                else random.choice(samples)
            )

            for case in [
                "low",
                "up",
                "tit", # woah!
                "cap",
                "swap",
                "alt",
                "cam",
                "pas",
                "snake",
                "const",
                "kebab",
                "dot",
                "path",
                "train",
                "random",
                "cul",
                "altcul",
            ]:
                print(f"{case:>8}: {jump(sample, case)}")
            continue

        parts = shlex.split(userInput)

        cmd, *txt = parts
        result = jump(txt, cmd)
        print(result)

if __name__ == "__main__":
    main()
