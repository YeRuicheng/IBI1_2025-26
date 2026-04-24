def calculate_protein_mass(sequence):
    """
    Calculate the total monoisotopic mass of a protein in atomic mass units (amu)
    Param sequence: Amino acid sequence (uppercase single-letter codes)
    Return: Total protein mass, or raises error for invalid amino acids
    """
    # Amino acid residue mass table (monoisotopic)
    aa_mass = {
        'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07,
        'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04,
        'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04,
        'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
    }

    total_mass = 0.0

    # Check each amino acid and sum masses
    for aa in sequence:
        if aa not in aa_mass:
            # "raise" instead of "print": 
            # "raise" will stop the function and signal an error, 
            # while "print" would just display a message and continue)
            raise ValueError(f"Invalid amino acid detected: {aa}. Please use standard single-letter codes.")
        total_mass += aa_mass[aa]

    return total_mass

# Get input from user and calculate mass
print("===== Protein Mass Calculator =====")
# "strip()" removes leading and trailing whitespace
# "upper()" converts the inputs to uppercase, ensuring the validity
user_sequence = input("Please enter an amino acid sequence: ").strip().upper()
total_mass = calculate_protein_mass(user_sequence)
print(f"Total protein mass (monoisotopic): {total_mass:.2f} amu")