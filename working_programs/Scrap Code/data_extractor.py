import re
import os
from pathlib import Path

def spec_cleaner(source: str, destination: str, reg_ex: str):
    """
    Source must be data only. Not performant for large of complex files. Non-destructive.
    Confirmed working: 2022-04-01.Need to add attribute headers by hand.
    """
    pattern = re.compile(reg_ex)
    for file in os.listdir(source):
        file = Path(file)   # converts file path to a path object
        full_path = source / file  # makes the absPaths out of every file in chosen folder
        with open(full_path, 'r') as search_space:
            matches = pattern.findall(search_space.read())
            with open(destination, 'a') as output:
                output.write(','.join(matches[1:]) + '\n')
    print(f'program complete:\nread from - {source}\nPlaced file into - {destination}\nCurrent dir - {os.getcwd()}')

# Main line
SRC = r"C:\Users\Alexandre\Desktop\Budisa lab\Projects\22-04-01__FlpEvo\ALE data Take 4 mutants"
OUT = 'short_double_mutant_ale.csv'
Ex = r'\d\.\d\d\d'

spec_cleaner(SRC, OUT, Ex)

"""
Note to self: add better descriptions of how things work/how the problem was solved, future self will thankyou
"""