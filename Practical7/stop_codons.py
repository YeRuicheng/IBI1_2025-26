import os

def read_fasta(filename):
    """Read FASTA file and return list of (header, sequence) tuples"""
     # Initialize an empty list to store FASTA records
    records = []
    current_header = ""
    current_seq = ""

    # Open and read the input FASTA file line by line
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            # Skip empty lines
            if not line:
                continue
            # Check if the line is a FASTA header (starts with >)
            if line.startswith(">"):
                # If a previous record exists, save it to the list
                if current_header:
                    records.append((current_header, current_seq))
                # Update to the new header and reset sequence
                current_header = line
                current_seq = ""
            else:
                # Append sequence lines to the current sequence
                current_seq += line
        if current_header:
            records.append((current_header, current_seq))
    return records

def extract_gene_name(header):
    """Extract gene name from FASTA header"""
    # Split header into individual components
    parts = header.split()
    # Find the part that starts with "gene:"
    for p in parts:
        if p.startswith("gene:"):
            # Return the actual gene name
            return p.split(":")[1]
    # Return default if no gene name found
    return "unknown_gene"

def find_in_frame_stop_codons(seq):
    """Find in-frame stop codons (TAA, TAG, TGA) after ATG"""
    stops = ["TAA", "TAG", "TGA"]
    # Use a set to store unique stop codons found
    found = set()

    # Search for the start codon ATG
    for i in range(len(seq) - 2):
        if seq[i:i+3] == "ATG":
            # Scan codons in frame (step of 3) for stop codons
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stops:
                    found.add(codon)
            # Stop after first ATG is processed
            break
    # Return sorted list of unique stop codons
    return sorted(list(found))

# Main execution
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"

# Read all FASTA records from the input file
records = read_fasta(input_file)

# Write filtered sequences to output file
with open(output_file, 'w') as out:
    for header, seq in records:
        # Extract gene name from header
        gene = extract_gene_name(header)
        # Find in-frame stop codons
        stops = find_in_frame_stop_codons(seq)
        # Only write genes with identified stop codons
        if stops:
            # Create new header with gene name and stop codons
            new_header = f">{gene} stop_codons:{','.join(stops)}"
            out.write(new_header + "\n")
            out.write(seq + "\n")

print(f"File generated: {output_file}")
print(f"Full path: {os.path.abspath(output_file)}")