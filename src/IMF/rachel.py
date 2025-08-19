"""
S
"""

import time

VERSION = "v0.4.5"

# ================== FIRST STEPS ==================

XSC = "\033["    # XSCape

RST = XSC + "0m" # ReSeT
MON = XSC + "2J" # MONica geller

# ================== TEXT STYLES ==================

BLD = XSC + "1m" # BoLD
DIM = XSC + "2m" # DIM
ITL = XSC + "3m" # ITaLic
UND = XSC + "4m" # UNDerscore
BLK = XSC + "5m" # BLinK
REV = XSC + "7m" # REVerse
HID = XSC + "8m" # HIDden
STR = XSC + "9m" # STRike

# ================== FG COLORS ==================

BLACK        = XSC + "30m"
RED          = XSC + "31m"
GREEN        = XSC + "32m"
YELLOW       = XSC + "33m"
BLUE         = XSC + "34m"
MAGENTA      = XSC + "35m"
CYAN         = XSC + "36m"
WHITE        = XSC + "37m"

B_BLACK   = XSC + "90m"
B_RED     = XSC + "91m"
B_GREEN   = XSC + "92m"
B_YELLOW  = XSC + "93m"
B_BLUE    = XSC + "94m"
B_MAGENTA = XSC + "95m"
B_CYAN    = XSC + "96m"
B_WHITE   = XSC + "97m"

# ================== BG COLORS ==================

BG_BLACK        = XSC + "40m"
BG_RED          = XSC + "41m"
BG_GREEN        = XSC + "42m"
BG_YELLOW       = XSC + "43m"
BG_BLUE         = XSC + "44m"
BG_MAGENTA      = XSC + "45m"
BG_CYAN         = XSC + "46m"
BG_WHITE        = XSC + "47m"

BG_B_BLACK   = XSC + "100m"
BG_B_RED     = XSC + "101m"
BG_B_GREEN   = XSC + "102m"
BG_B_YELLOW  = XSC + "103m"
BG_B_BLUE    = XSC + "104m"
BG_B_MAGENTA = XSC + "105m"
BG_B_CYAN    = XSC + "106m"
BG_B_WHITE   = XSC + "107m"

# ================== TESTS ==================

if __name__ == "__main__":
    print("rachel v0.5.1")

    for S in [BLD, DIM, ITL, UND, BLK, REV, HID, STR]:
        time.sleep(0.1)
        print(f"{S}STYLES{RST}")

    for FG in [BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE,
               B_BLACK, B_RED, B_GREEN, B_YELLOW,
               B_BLUE, B_MAGENTA, B_CYAN, B_WHITE]:
        time.sleep(0.2)
        print(f"{FG}FG COLOR{RST}")

    for BG in [BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_MAGENTA, BG_CYAN, BG_WHITE,
               BG_B_BLACK, BG_B_RED, BG_B_GREEN, BG_B_YELLOW,
               BG_B_BLUE, BG_B_MAGENTA, BG_B_CYAN, BG_B_WHITE]:
        time.sleep(0.3)
        print(f"{BG}BG COLOR TXT{RST}")
