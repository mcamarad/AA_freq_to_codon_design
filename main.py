# -*- coding: utf-8 -*-
"""
Created on Sat Feb  10 15:00:28 2018

@author: Marcos Cámara-Donoso
"""
import pandas as pd
import copy

def aa_to_codon_freq(codonmap_path, aafreq_path, codfreq_path):
    #Loading CODON MAPPING and make a DataFrame with codons per aa
    cod = pd.read_csv(codonmap_path, sep='|', header = None)
    print("Codon map loaded from: ", codonmap_path)
    cod.columns = ['del']
    cols = list('0123456')
    cod[cols] = cod.loc[:,'del'].str.split(',', n=6, expand=True)
    cod = cod.drop('del',axis=1)
    cod = cod.set_index(cod['0'])
    cod = cod.drop('0',axis=1)
    cod.columns = [0,1,2,3,4,5]
    #Loading AA frequencies
    aa_frq = pd.read_csv(aafreq_path, header = None, index_col = 0)
    print("AA frequencies loaded from: ", aafreq_path)
    #Initializing codons frequencies
    print("Initializing codon frequencies")
    cod_frq = pd.DataFrame(0,index = ['A','T','C','G'], columns = [0,1,2])
    #Start Program
    print("Starting computation of Codon design frequencies")
    cod_tmp = copy.deepcopy(cod_frq)
    #For each aa in the aa frequencies
    for aa in aa_frq.index:
        aa_cod = copy.deepcopy(cod_tmp)
        #for each codon codifying for that aa
        for codon in cod.loc[aa,:]:
            if codon == None:
                continue
            else:
                #for each nucleotide and position in the codon quantify nucleotide per position
                for nuc, pos in zip(codon, [0,1,2]):
                    aa_cod.loc[nuc, pos] = aa_cod.loc[nuc, pos] + 1
        #Compute the frequency for all codons codifying for that aa
        aa_cod = (aa_cod/aa_cod.sum(axis=0))*float(aa_frq.loc[aa,:])*100
        #Round the decimal to have 0.5 resolution
        aa_cod = aa_cod.applymap(lambda x: round(x * 2) / 2)
        #Sum the codon for a aminoacid frequencies
        cod_frq = cod_frq + aa_cod
    print("Computation of codon design frequencies finished")
    #save to csv file the result
    cod_frq.to_csv(codfreq_path, sep = ',')
    print("Successfully saved on: ", codfreq_path)
    return cod_frq


if __name__ == '__main__':
    codon_frequencies = aa_to_codon_freq("AA TO CODON MAPPING.csv", "AAFREQ.txt", "Solution.csv" )       