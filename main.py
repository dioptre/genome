from pysam import FastaFile
 
fasta = "human_g1k_v37.fa"
# read FASTA file
sequences_object = FastaFile(fasta)
iter = sequences_object.fetch("1", 300000, 500000)
for x in iter:
    print(str(x))
pass
#~/Documents/fasql/build/release/duckdb
#load fasql;
#CREATE OR REPLACE TABLE genome AS SELECT * FROM read_fasta('human_g1k_v37.fa') limit 5
#select * from genome where id='Y';
#SELECT * FROM genome WHERE sequence LIKE '%AGCTGGGATT%' AND id='Y';
#SELECT STRPOS(sequence, 'AGCTGGGATT') FROM genome WHERE STRPOS(sequence, 'AGCTGGGATT') > 0;
#check if you have a gene at a position
#for rs114525117
#SELECT *, CASE WHEN substr(sequence, 759036, 2) = 'GG' THEN true ELSE false END AS is_rs114525117 FROM genome where id='1';