def proteins(strand):
    protein = []
    ct = 0
    while ct < len(strand):
        codon = ""
        for i in range(3):
            codon += strand[ct]
            ct += 1
            
        if codon == "UAA" or codon == "UAG" or codon == "UGA":
            return ", ".join(protein)
        
        if codon == "AUG":
            protein.append("Methionine")
            continue
                           
        if codon == "UUU" or codon == "UUC":
            protein.append("Phenylalanine")
            continue

        if codon == "UUA" or codon == "UUG":
            protein.append("Leucine")
            continue

        if codon == "UCU" or codon == "UCC" or codon == "UCA" or codon == "UCG":
            protein.append("Serine")
            continue

        if codon == "UAU" or codon == "UAC":
            protein.append("Tyrosine")
            continue

        if codon == "UGU" or codon == "UGC":
            protein.append("Cysteine")
            continue

        if codon == "UGG":
            protein.append("Tryptophan")
            continue
        
    return ", ".join(protein)            
            
