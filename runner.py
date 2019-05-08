from utils import *
from Sets import Sets
from time import perf_counter
import math
from scipy.special import comb

def read_digits():
    with open("data/rosalind_data.txt", "r") as f:
        line = f.readline().strip()
        n = list(map(int, line.split()))
    return n


def for_fasta():
    for id, string in fasta_file_iter("data/rosalind_data.txt"):
        result = all_possible_gene_transcription(string)
    for r in result:
        print(r, file=open("data/answer.txt", "a"))


def read_file():
    with open("data/rosalind_data.txt", "r") as f:
        for line in f:
            yield line.strip()
        #i, j = read_digits(dna)


if __name__ == '__main__':
    #file=open("data/answer.txt", "w")
    #data = read_fasta("data/rosalind_data.txt", without_id=True)
    n = read_digits()
    print(n_expected_dominant_phenotype(n, n_children=2))
