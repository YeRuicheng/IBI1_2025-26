# Define the input mRNA sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

def find_longest_orf(sequence):
    """
    Find the longest ORF in a given mRNA sequence
    Start codon: AUG; Stop codons: UAA, UAG, UGA
    Param sequence: mRNA string
    Return: longest ORF sequence and its length
    """
    start_codon = 'AUG'
    stop_codons = ['UAA', 'UAG', 'UGA']
    max_length = 0
    longest_orf = ''

    # Search all possible start positions for AUG
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == start_codon:
            # Scan from start codon to find the first in-frame stop codon
            for j in range(i, len(sequence) - 2, 3):
                current_codon = sequence[j:j+3]
                if current_codon in stop_codons:
                    orf_seq = sequence[i:j+3]
                    orf_len = len(orf_seq)
                    # Update the longest ORF
                    if orf_len > max_length:
                        max_length = orf_len
                        longest_orf = orf_seq
                    break
    return longest_orf, max_length

# Run function
orf_sequence, orf_length = find_longest_orf(seq)

# Output results
print("Longest ORF sequence:", orf_sequence)
print("Length of longest ORF (nucleotides):", orf_length)