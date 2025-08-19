import sys
import os

if os.name != "nt":
    import readline

VERSION = "v0.0.6"

# ================== EVERYTHIN' ==================

def say(msg: str = " ") -> str:
    """
    This cow talks
    """
    eyes = "oo" # much line mawww
    tongue = "  "
    bubble = f"< {msg} >"
    overline = "_" * (len(bubble) - 2)
    underline = "-" * (len(bubble) - 2)

    return rf"""
  {overline}
 {bubble}
  {underline}
        \   ^__^
         \  ({eyes})\_______
            (__)\       )\/\
             {tongue} ||----w |
                ||     ||
            """

# ================== TESTS ==================

if __name__ == "__main__":
    print(f"mooPoint {VERSION}")
    try:
        while True:
            userInput = input("YOU: ").strip()
            if not userInput:
                continue
            if userInput in ["quit", "exit"]:
                sys.exit("Hasta La Vista... Baby!!!")
            print(say(userInput))
    except KeyboardInterrupt:
        sys.exit("Moo's sleepin'!")

"""
this cow's opinion does matter... it's not joe's cow!!!

oh yes... there will be more... much more...
you thought the game was over... but it has only begun!!!
"""

