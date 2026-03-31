def find_largest_orf(seq):
    start_codon = 'AUG'
    stop_codons = ['UAA', 'UAG', 'UGA']
    max_length = 0

    for i in range(len(seq)):
        if seq[i:i+3] == start_codon:
            for j in range(i+3, len(seq), 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    length = j + 3 - i
                    if length > max_length:
                        max_length = length
                    break
    return max_length
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
largest_length = find_largest_orf(seq)
print(f"The length of the largest ORF is: {largest_length} nucleotides.")