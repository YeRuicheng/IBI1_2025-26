import matplotlib.pyplot as plt
import numpy as np


# create a dictionary to store gene expression levels
gene_expression = {
    'TP53': 12.4,
    'EGFR': 15.1,
    'BRCA1': 8.2,
    'PTEN': 5.3,
    'ESR1': 10.7
}

# add gene MYC to the dictionary
gene_expression['MYC'] = 11.6

# print the gene expression dictionary
print("Gene expression dictionary:")
for gene, expr in gene_expression.items():
    print(f"{gene}: {expr}")

# make a barf chart with labels and title
genes = list(gene_expression.keys())
expressions = list(gene_expression.values())

plt.figure(figsize=(8, 5))
plt.bar(genes, expressions, color='#2E86AB')
plt.xlabel('Gene', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
plt.title('Gene Expression Levels in Biological Sample', fontsize=14, pad=15)
plt.ylim(0, max(expressions) + 2)  # set y-axis limit for better visualization
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# query the expression level of a specific gene (psedocode marker)
gene_of_interest = "TP53"  # <-- This variable can be modified to query different genes

if gene_of_interest in gene_expression:
    print(f"\nExpression value of {gene_of_interest}: {gene_expression[gene_of_interest]}")
else:
    print(f"\nError: Gene '{gene_of_interest}' not found in the dataset.")

# calculate and print the average expression level
average_expr = np.mean(list(gene_expression.values()))
print(f"\nAverage gene expression level: {average_expr:.2f}")