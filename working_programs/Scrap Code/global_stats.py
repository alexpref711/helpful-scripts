"""
Input, One of Vic's reduced files, theese files are desingned to give the list of non-redundants only
Output, A list of parameters

Parameters that need caluculating
- all unique peptide sequences
- all peptide sequences that had one or more mods

- total amino acids by kind
- all prolines (of any kind)
- this is what lets you have the

a good first step is to get everything into a data frame

"""
import pandas as pd
import numpy as np
import regex as re



full_path = r"C:\Users\Alexandre\Desktop\22-10-17_RP-HPLC_Flp_by_SPI\FlpRaw + align (copy)\1DRUNS_second_try\4RFLUOPRO-reduced.txt"

# df = pd.read_csv(full_path)
# print(df)


with open(full_path, 'r') as search_space:
    for line in search_space:
        print(line.strip())