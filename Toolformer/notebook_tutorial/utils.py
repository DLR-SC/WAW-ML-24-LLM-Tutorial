import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def text_blue(text):
    return bcolors.OKBLUE + str(text) + bcolors.ENDC
def text_cyan(text):
    return bcolors.OKCYAN + str(text) + bcolors.ENDC
def text_green(text):
    return bcolors.OKGREEN + str(text) + bcolors.ENDC
def text_red(text):
    return bcolors.FAIL + str(text) + bcolors.ENDC
def text_bold(text):
    return bcolors.BOLD + str(text) + bcolors.ENDC
def text_underline(text):
    return bcolors.UNDERLINE + str(text) + bcolors.ENDC

def remove_non_ascii_and_newline(string:str) -> str:
    string = re.sub(r'[^\x00-\x7F]', '', string)
    string = re.sub(r'[\n\r]', '', string)
    return string