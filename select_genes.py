'''
Select some number of genes from rna.fa, and write the descriptions
to stdout.  The output file can be used as the -gene_fn parameter to fake_data.py.
Genes are selected at random.
'''

import sys, argparse, random
from fastq_parser import FastqParser

def main(opts):
    descs=read_descs(opts.rna_fn, opts.use_predicted, opts.use_uRNA)
    if opts.v:
        print '%d usable descs in %s' % (len(descs), opts.rna_fn)
    keepers=random.sample(descs, opts.N)
    for desc in keepers:
        print desc


def read_descs(rna_fn, use_predicted, use_uRNA):
    descs=[]
    fastq=FastqParser(rna_fn)
    for desc,seq in fastq:
        if 'PREDICTED' in desc and not use_predicted:
            continue
        if 'microRNA' in desc and not use_uRNA:
            continue
        descs.append(desc)
    return descs
        

def getopts():
    parser = argparse.ArgumentParser(description='Generate fake FASTQ data')
    parser.add_argument('N', type=int)
    parser.add_argument('--rna_fn', default='/local/src/bowtie2/indexes/rna.fa')
    parser.add_argument('--use_predicted', action='store_true')
    parser.add_argument('--use_uRNA', action='store_true')

    parser.add_argument('-v', action='store_true', help='verbose')
    parser.add_argument('-d', action='store_true', help='debugging flag')

    opts=parser.parse_args()
    if opts.d:
        print >> sys.stderr, opts
    return opts


if __name__=='__main__':
    sys.exit(main(getopts()))
