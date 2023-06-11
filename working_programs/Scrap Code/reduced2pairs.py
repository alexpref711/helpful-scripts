"""
type, sequence^mods~mods, id.id.id.parent_mass~locus, charge, M+H_obs, M+H_theo, confidence, SSR_new,  RT, SSR_old, fraction, intensity, len(12)
1 AAPAPAAAAPK^P:2:17.99057~P:9:17.99057 1.1.1.15538.2~0486.2590 02 0971.5101 0971.5120 -5.2 10.39 14.707 13.41 1 11346740.237793



The classic in-append/else-add dictionary

Vic's quick solution was the dict and dict get append from two files, this is based off a single file. Depends on stochasitic nature of incorperation
I should also build this one out and see how it compares

FUN FACT: You are not allowed to modify dicts as you interate throught them --> RuntimeError: dictionary changed size during iteration

Assumptions
(0) In the case of multiple replacements site I won't see two modified whiout seing the original 

Big Design Challenges
(0) Have no control over when the non-modified sequence appears in the file
(1) Need the original peptide sequence to link out to n other sequences !!!
(2) Getting rid of sequences that do not have the PTMS that I wan't)
(Sorting based of a single value in [[]] is actually not trivial)

"""

import re
from operator import itemgetter
from pathlib import Path

INPUT = r'C:\Users\Alexandre\Desktop\Local\22-07-20_proline_expanded_BU300\BU300_exposed\prolines_bu300_mixed_1D_reduced\4RFLUOPRO-reduced.txt' # \t is the symbol for tab
# link = Path(INPUT)
pep_dict = {}
pairs_dict = {}
NCAA = '[4Rflp]'
CANNONICAL = 'P'


# Loads all peptides into simple dicts
with open(INPUT, 'r') as search_space:
    for line in search_space:
        line = line.rstrip()
        line = re.split(r"[\s^]", line)  #Uses RegEx to split over multiple delimeters
        line[0], line[1] = line[1], line[0]

        # Load everything into a dictionary (Group everything that shares a base_sequence)
        if line[0] in pep_dict:
            pep_dict[line[0]].append(line)
        else:
            pep_dict[line[0]] = [line]
        
# Makes sure to only keep peptides that have at least two copies of the same peptide, and proline is presnet
# Need to find away to get rid of all the other PTM!
for key, value in pep_dict.items():
    if len(value) > 1 and CANNONICAL in key:
        pairs_dict[key] = value

# Replace the vlaue-sequences with a string that has ncAA input
def ncaa_replacer(canonical: str, ncaa: str, seq_og: str, mod_index: str ) -> str:
    """
    A function to replace canonical amino acids by analogs in a peptide sequence
    All but the ncaa must be stricly upper cased 
    The mod index uses P:3:17.99057~P:4:17.99057 type information
    """
    modded_seq = []
    mod_positions = []
    count = 0

    for i in mod_index:
        if i == canonical:
            mod_positions.append(mod_index[count + 2])
        count += 1

    for i in seq_og:
        modded_seq.append(i)

    for i in mod_positions:
        modded_seq[int(i)] = ncaa
    modded_seq = "".join(modded_seq)
    return(modded_seq)
for value in pairs_dict.values():
    for entry in value:
        entry[0] = ncaa_replacer(CANNONICAL, NCAA, entry[0], entry[2])


# Sort value so that the non-modified one is alwas first sort sort every value based on 
# for value in pairs_dict.values():
#     value = (sorted(value, key=itemgetter(value[0][1])))

for value in pairs_dict.values():
    print(value)
    print('\n')
    print(value[0])
    print('\n')
    print(value[0][1])

# Still to-do
# Find a way to Filter out the 
# make list formatted into such that they lay out the vlaues nicely for every pair
# Use F-Strign 



"""
For a large 2D run it takes about 2.612 seconds, on ALEX-ZENBOOK
So even with all theses flexible list and dicts it is still fine, I will proabably make many offshoots of this piece of code
"""
