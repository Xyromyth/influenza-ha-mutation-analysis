from Bio import AlignIO
import pandas as pd

alignment_file = "data/processed/ha_aligned.fasta"

alignment = AlignIO.read(alignment_file, "fasta")

reference = alignment[0].seq
results = []

for i in range(len(reference)):
    ref_aa = reference[i]

    if ref_aa == "-":
        continue

    column = [record.seq[i] for record in alignment]

    mutations = 0
    for aa in column:
        if aa != ref_aa and aa != "-":
            mutations += 1

    results.append({
        "alignment_position": i + 1,
        "reference_amino_acid": ref_aa,
        "mutation_count": mutations,
        "total_sequences": len(alignment),
        "mutation_frequency": mutations / len(alignment)
    })

df = pd.DataFrame(results)
df.to_csv("results/mutation_counts.csv", index=False)

print(df.head())
print("Saved results to results/mutation_counts.csv")