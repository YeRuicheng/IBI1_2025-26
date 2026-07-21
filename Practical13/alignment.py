# Function: Global sequence alignment without gaps
# Calculate BLOSUM62 score and sequence identity percentage

def read_fasta(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None, None

    name = ""
    sequence = ""
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            name = line[1:]
        else:
            sequence += line
    return name, sequence



def perform_alignment(seq1, seq2, matrix):
    score = 0
    identical_count = 0
    length = len(seq1)

    if len(seq1) != len(seq2):
        print("Warning: Sequences are of different lengths. Aligning up to the length of the shorter sequence.")
        length = min(len(seq1), len(seq2))

    for i in range(length):
        aa1 = seq1[i]
        aa2 = seq2[i]

        try:
            score += matrix[aa1][aa2]
        except KeyError:
            pass
     
        if aa1 == aa2:
            identical_count += 1

    return score, identical_count

import sys

# ------------------- Main execution -------------------
if __name__ == "__main__":
    human_file = "DLX5_human.fasta"
    mouse_file = "DLX5_mouse.fasta"
    random_file = "random.fasta"
    blosum_file = "BLOSUM62.txt"

    blosum_matrix = read_blosum(blosum_file)
    if not blosum_matrix:
        sys.exit("Error: BLOSUM62 matrix could not be read.")

    h_name, h_seq = read_fasta(human_file)
    m_name, m_seq = read_fasta(mouse_file)
    r_name, r_seq = read_fasta(random_file)

    if not (h_seq and m_seq and r_seq):
        sys.exit("Error: One or more sequences could not be read.")

    print(f"Human DLX5 length: {len(h_seq)}")
    print(f"Mouse DLX5 length: {len(m_seq)}")
    print(f"Random sequence length: {len(r_seq)}")
    print("-" * 30)

    comparisons = [
        ("Human vs Mouse", h_name, h_seq, m_name, m_seq),
        ("Human vs Random", h_name, h_seq, r_name, r_seq),
        ("Mouse vs Random", m_name, m_seq, r_name, r_seq)
    ]

    print(f"{'Comparison':<20} | {'Score':<10} | {'% Identity':<10}")
    print("-" * 50)

    for title, n1, s1, n2, s2 in comparisons:
        align_score, pid = perform_alignment(s1, s2, blosum_matrix)
        print(f"{title:<20} | {align_score:<10} | {pid / min(len(s1), len(s2)) * 100:.2f}%")

    print("-" * 50)