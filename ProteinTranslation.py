# This file translates an RNA sequence into a select group of proteins
# Will later be updated to have all codons for all amino acids. 
def proteins(strand):
    aminos = []
    protein = ""
    protein_mapping = {"Methionine": ["AUG"], "Phenylalanine": ["UUU", "UUC"], "Leucine" : ["UUA", "UUG"], "Serine" : ["UCU", "UCC", "UCA", "UCG"], "Tyrosine" : ["UAU", "UAC"], "Cysteine" : ["UGU", "UGC"], "Tryptophan" : ["UGG"], "STOP" : ["UAA", "UAG", "UGA"]}
    for char in strand: 
        protein += char 
        if len(protein) == 3: 
            for key in protein_mapping: 
                if protein in protein_mapping[key]: 
                    if key == "STOP": 
                        return aminos
                    aminos.append(key)
                    protein = ""
        else: 
            continue
    return aminos
