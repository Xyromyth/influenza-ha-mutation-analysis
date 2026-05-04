# Influenza A Hemagglutinin Mutation Analysis

This repository contains code and data for a BIO 383 project analyzing mutation patterns in Influenza A hemagglutinin (HA) sequences.

## Research Question

Do mutations in Influenza A hemagglutinin occur more frequently in immune-exposed regions than in internal regions?

## Hypothesis

Mutations will occur at higher frequency in immune-exposed or antigenic regions of HA compared with internal regions.

## Workflow

1. Download HA sequences from Influenza A strains.
2. Save raw FASTA files in `data/raw/`.
3. Align sequences using MAFFT.
4. Count amino acid differences relative to a reference sequence.
5. Visualize mutation frequency across HA.

## Repository Structure

- `data/raw/`: original FASTA files
- `data/processed/`: aligned FASTA files
- `scripts/`: Python analysis scripts
- `results/`: CSV output files
- `figures/`: generated plots
- `notebooks/`: optional exploratory notebooks