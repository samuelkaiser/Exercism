def proteins(strand):
    # splice strand into thirds to retrieve list of codons
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]

    # these are the codons that translate to the required proteins for the exercise but there are many more
    codonDictionary = {
        'AUG': 'Methionine', 
        'UUU': 'Phenylalanine', 
        'UUC': 'Phenylalanine',
        'UUA': 'Leucine',
        'UUG': 'Leucine',
        'UCU': 'Serine',
        'UCA': 'Serine',
        'UCG': 'Serine',
        'UCC': 'Serine',
        'UAU': 'Tyrosine',
        'UAC': 'Tyrosine',
        'UGU': 'Cysteine',
        'UGC': 'Cysteine',
        'UGG': 'Tryptophan',
        'UAA': 'STOP',
        'UAG': 'STOP',
        'UGA': 'STOP'
    }

    proteinsByName = []
    for codon in codons:
        if(codonDictionary[codon] != "STOP"):
            print(codonDictionary[codon])
            proteinsByName.append(codonDictionary[codon])
            print(proteinsByName)
        else:
            break
    return proteinsByName
