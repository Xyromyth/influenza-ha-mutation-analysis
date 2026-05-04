from Bio import SeqIO

fasta_file = "data/raw/ha_sequences.fasta"

records = list(SeqIO.parse(fasta_file, "fasta"))

print(f"Number of sequences: {len(records)}")

for record in records[:5]:
    print("ID:", record.id)
    print("Length:", len(record.seq))
    print("First 50 amino acids:", record.seq[:50])
    print()