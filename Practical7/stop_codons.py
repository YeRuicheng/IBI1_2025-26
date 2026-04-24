import os

def read_fasta(filename):
    """Read FASTA file and return list of (header, sequence) tuples"""
    records = []
    current_header = ""
    current_seq = ""
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if current_header:
                    records.append((current_header, current_seq))
                current_header = line
                current_seq = ""
            else:
                current_seq += line
        if current_header:
            records.append((current_header, current_seq))
    return records

def extract_gene_name(header):
    """Extract gene name from FASTA header"""
    parts = header.split()
    for p in parts:
        if p.startswith("gene:"):
            return p.split(":")[1]
    return "unknown_gene"

def find_in_frame_stop_codons(seq):
    """Find in-frame stop codons (TAA, TAG, TGA) after ATG"""
    stops = ["TAA", "TAG", "TGA"]
    found = set()
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stops:
                    found.add(codon)
            break
    return sorted(list(found))

# Main
input_file = "C:/Users/叶睿城/Desktop/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"

records = read_fasta(input_file)

with open(output_file, 'w') as out:
    for header, seq in records:
        gene = extract_gene_name(header)
        stops = find_in_frame_stop_codons(seq)
        if stops:
            new_header = f">{gene} stop_codons:{','.join(stops)}"
            out.write(new_header + "\n")
            out.write(seq + "\n")

print(f"File generated: {output_file}")
print(f"Full path: {os.path.abspath(output_file)}")