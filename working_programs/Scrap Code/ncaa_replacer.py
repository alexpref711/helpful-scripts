"""
Input
1 ['DQGPPDLDDIFR', 'P:3:17.99057~P:4:17.99057']

Output
2 ['DGQ[4FLP][4FLP]DLDDIFR', 'P:3:17.99057~P:4:17.99057']

Note: one month later this solution did not make sense to me
Therfore: not an ideal solution
When you deposit something for the long term do not be afraid to included a mini novel up top
"""



CANONICAL = 'P'
NCAA = '[4Rflp]'
seq_og = 'DQGPPDLDDIFR'
mod_index = 'P:3:17.99057~P:4:17.99057'

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

print(ncaa_replacer(CANONICAL, NCAA, seq_og, mod_index))


"""
The Enumerate function could have been used here, but whatever
"""



