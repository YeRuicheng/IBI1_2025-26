# Define the input mRNA sequence
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'

def find_longest_orf(sequence):
    """
    Find the longest ORF in a given mRNA sequence
    Start codon: AUG; Stop codons: UAA, UAG, UGA
    Param sequence: mRNA string
    Return: longest ORF sequence and its length
    """
    # Define start and stop codons for ORF identification
    start_codon = 'AUG'
    stop_codons = ['UAA', 'UAG', 'UGA']

    # Initialize variables to store the longest ORF information
    max_length = 0
    longest_orf = ''

    # Search all possible start positions for AUG
    for i in range(len(sequence) - 2):
        # Check if current triplet is the start codon
        if sequence[i:i+3] == start_codon:
            # Scan from start codon to find the first in-frame stop codon
            for j in range(i, len(sequence) - 2, 3):
                current_codon = sequence[j:j+3]
                # Check if current codon is a stop codon
                if current_codon in stop_codons:
                    # Extract the complete ORF sequence from start to stop codon
                    orf_seq = sequence[i:j+3]
                    orf_len = len(orf_seq)

                    # Update the longest ORF
                    if orf_len > max_length:
                        max_length = orf_len
                        longest_orf = orf_seq

                    # Exit loop after finding the first in-frame stop codon
                    break
    # Return the longest ORF sequence and its length
    return longest_orf, max_length

# Execute the ORF finding function
orf_sequence, orf_length = find_longest_orf(seq)

# Output results
print("Longest ORF sequence:", orf_sequence)
print("Length of longest ORF (nucleotides):", orf_length)