# generate fake reads:
#rm -f fake.fastq
#python fake_data.py --gene_fn genes.2K.txt

# alignment:
export BOWTIE2_INDEXES=/local/src/bowtie2/indexes
rm -f fake.sam
bowtie2 -x rna -U fake.fastq -S fake.sam

# convert .sam to .bam
rm -f fake.bam
samtools view -bS -o fake.bam fake.sam

# sort .bam
# (samtools sort automatically addes '.bam')
rm -f fake.sorted
samtools sort fake.bam fake.sorted

# call variants: bcftools mpileup
rm -f fake.vcf
samtools mpileup -f rna.fa fake.sorted.bam > fake.vcf

