import matplotlib.pyplot as plt
import os

def read_fasta(filename):
    """Read FASTA file using"""
    # Initialize empty lists to store header and sequence
    records = []
    hdr = ""
    seq = ""

    # Open FASTA file and parse line by line
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines
            if not line:
                continue
            # Identify FASTA header line starting with '>'
            if line.startswith(">"):
                # Save previous record if exists
                if hdr:
                    records.append((hdr, seq))
                # Update to new header and reset sequence
                hdr = line
                seq = ""
            else:
                # Append sequence lines to current sequence
                seq += line
        # Add the last record after loop finishes
        if hdr:
            records.append((hdr, seq))
    return records

def get_longest_orf_codons(seq, target_stop):
    """Get codons from longest ORF ending with target_stop"""
    stops = ["TAA", "TAG", "TGA"]
    best_codons = []
    max_len = 0

    # Search for start codon ATG to begin ORF
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            current = []
            # Scan codons in frame (step of 3)
            for j in range(i, len(seq)-2, 3):
                codon = seq[j:j+3]
                # Check if current codon is the target stop codon
                if codon == target_stop:
                    current.append(codon)
                    # Update longest ORF if current is longer
                    if len(current) > max_len:
                        max_len = len(current)
                        best_codons = current.copy()
                    break
                # Stop if encountering other stop codons
                if codon in stops:
                    break
                current.append(codon)
    return best_codons

# Get user input for stop codon
target = input("Enter stop codon (TAA/TAG/TGA): ").strip().upper()
# Repeat until valid codon is entered
while target not in ["TAA", "TAG", "TGA"]:
    target = input("Invalid. Enter TAA/TAG/TGA: ").strip().upper()

# Read sequences in FASTA file
fasta_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
all_codons = []

# Process each sequence from FASTA file
for _, seq in read_fasta(fasta_file):
    codons = get_longest_orf_codons(seq, target)
    # Collect codons if ORF is found, exclude the final stop codon
    if codons:
        all_codons.extend(codons[:-1])  # exclude stop codon

# Count the frequency of each codon
codon_count = {}
for codon in all_codons:
    if codon in codon_count:
        codon_count[codon] += 1
    else:
        codon_count[codon] = 1

# Calculate total number of codons
total = sum(codon_count.values())

# Print codon frequency results
print("\nCodon frequency upstream of", target)
for c, n in codon_count.items():
    print(f"{c}: {n} ({n/total*100:.1f}%)")

# Pie chart for codon distribution
plt.figure(figsize=(15, 15))
plt.pie(codon_count.values(), labels=codon_count.keys(), autopct='%1.1f%%', startangle=90, textprops={'fontsize': 8}, pctdistance=0.85)
plt.title(f'Codon Distribution before {target} (Longest ORF)', fontsize=16)
plt.savefig("codon_pie_chart.png", dpi=300, bbox_inches='tight')
plt.close()

# Output file path information
print("\nPie chart saved as: codon_pie_chart.png")
print("Full path:", os.path.abspath("codon_pie_chart.png"))