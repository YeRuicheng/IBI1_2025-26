import matplotlib.pyplot as plt
import os

def read_fasta(filename):
    """Read FASTA file using"""
    records = []
    hdr = ""
    seq = ""
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if hdr:
                    records.append((hdr, seq))
                hdr = line
                seq = ""
            else:
                seq += line
        if hdr:
            records.append((hdr, seq))
    return records

def get_longest_orf_codons(seq, target_stop):
    """Get codons from longest ORF ending with target_stop"""
    stops = ["TAA", "TAG", "TGA"]
    best_codons = []
    max_len = 0
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            current = []
            for j in range(i, len(seq)-2, 3):
                codon = seq[j:j+3]
                if codon == target_stop:
                    current.append(codon)
                    if len(current) > max_len:
                        max_len = len(current)
                        best_codons = current.copy()
                    break
                if codon in stops:
                    break
                current.append(codon)
    return best_codons

# User input
target = input("Enter stop codon (TAA/TAG/TGA): ").strip().upper()
while target not in ["TAA", "TAG", "TGA"]:
    target = input("Invalid. Enter TAA/TAG/TGA: ").strip().upper()

# Read sequences
fasta_file = "C:/Users/叶睿城/Desktop/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
all_codons = []
for _, seq in read_fasta(fasta_file):
    codons = get_longest_orf_codons(seq, target)
    if codons:
        all_codons.extend(codons[:-1])  # exclude stop codon


codon_count = {}
for codon in all_codons:
    if codon in codon_count:
        codon_count[codon] += 1
    else:
        codon_count[codon] = 1

total = sum(codon_count.values())

# Print result
print("\nCodon frequency upstream of", target)
for c, n in codon_count.items():
    print(f"{c}: {n} ({n/total*100:.1f}%)")

# Pie chart
plt.figure(figsize=(10, 6))
plt.pie(codon_count.values(), labels=codon_count.keys(), autopct='%1.1f%%', startangle=90)
plt.title(f'Codon Distribution before {target} (Longest ORF)')
plt.savefig("codon_pie_chart.png", dpi=300, bbox_inches='tight')
plt.close()

# Show full path
print("\nPie chart saved as: codon_pie_chart.png")
print("Full path:", os.path.abspath("codon_pie_chart.png"))