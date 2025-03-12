# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 09:20:24 2024

@author: Marina Moro López
"""


from tkinter.filedialog import askopenfile

def main():

    print('Please select the file with the gene of reference')
    gene_file = askopenfile(mode='r')
    gene_seq = gene_file.readlines()[1:]
    gene_seq = ''.join(gene_seq).replace('\n', '')
    
    print('Please select the file with the patient sequence')
    patient_file = askopenfile(mode='r')
    patient_seq = patient_file.readlines()[1:]
    patient_seq = ''.join(patient_seq).replace('\n', '')
    
    seq_alignment = []
    for i in range(len(gene_seq)):
        pos_align = (gene_seq[i]==patient_seq[i])
        seq_alignment.append(pos_align)
        
    mutation_pos = [i for i, val in enumerate(seq_alignment) if not val]
    mutation_pos_corrected = [x+1 for x in mutation_pos]
    for i in range(len(mutation_pos)):
        original_bases = gene_seq[mutation_pos[i]]
        mutated_bases = patient_seq[mutation_pos[i]]
    print ("Mutation position: " + str(mutation_pos_corrected[i]))
    print("Original base: " + original_bases)
    print("Mutated base: " + mutated_bases)

main()
