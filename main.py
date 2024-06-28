from pysam import FastaFile
 
fasta = "human_g1k_v37.fa"
# read FASTA file
sequences_object = FastaFile(fasta)
iter = sequences_object.fetch("1", 300000, 500000)
for x in iter:
    print(str(x))
pass
#load fasql;
#CREATE OR REPLACE TABLE genome AS SELECT * FROM read_fasta('human_g1k_v37.fa') limit 5
#select * from genome where id='Y';
#SELECT * FROM genome WHERE sequence LIKE '%AGCTGGGATT%' AND id='Y';
#SELECT STRPOS(sequence, 'AGCTGGGATT') FROM genome WHERE STRPOS(sequence, 'AGCTGGGATT') > 0;