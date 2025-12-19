# Drug Target Interaction
This repository contains the code for the INFO-H 518 Deep Learning Neural Networks Final Project, titled '_Drug–Protein Interaction Analysis: Accelerating Drug Discovery_'. In this project, we present an artificial neural network (ANN)-based framework that uses drug SMILES strings and target protein sequences as inputs to predict drug-protein binding affinity, enabling efficient prioritization of candidate interactions.

## Dataset
The dataset used in this study was obtained from [BindingDB](http://www.bindingdb.org), a publicly available database that curates experimentally measured drug–target binding affinities. The dataset comprises approximately 3.17 million drug–target interaction records, encompassing 1,390,080 unique compounds and 11,382 protein targets. Each entry includes molecular and protein descriptors, quantitative binding affinity measurements, and literature references providing experimental evidence for the reported interactions.

## Project Contents
1. `DataPreprocessing_NumericSmiles.ipynb` : Preprocesses the raw dataset by removing unused columns, handling missing values, cleaning and validating key biological fields. This notebook also generates numeric representations of drug SMILES using RDKit Morgan fingerprints.
2. `ProteinEmbedding.ipynb` : Generates vector embeddings for protein amino acid sequences using the pre-trained ESM-2 transformer model (esm2_t6_8M_UR50D).
3. `ANN3_Training_Testing.ipynb` : Constructs the final dataset by integrating SMILES fingerprints and protein embeddings, and trains and evaluates an artificial neural network (ANN) for IC50 prediction.
4. `ModelPerformance.ipynb` : Evaluates the trained model by predicting IC50 values for three selected drug–protein pairs.

## Schematic of the ANN Model Architecture
<p align="center">
  <img width="600" alt="DeepLearning_Project" src="https://github.com/user-attachments/assets/cfdeff4a-db0f-4f8e-9ec2-a535949fcfc9" />
</p>
