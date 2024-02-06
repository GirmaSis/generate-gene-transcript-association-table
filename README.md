# generate-gene-transcript-association-table

Annotation features **genomic.gtf** dataset is downloaded from ***Genome assembly GRCm39:***  <br> https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001635.27/

***generate_transcript.py*** generates gene transcript association table.  

1. Read the GTF file, which is in this case **genomic.gtf**
2. Filter for exon features
3. Extract gene_id and transcript_id from the attributes column
4. Remove duplicates
5. Save the unique mappings to a CSV file

