import pandas as pd

def parse_attributes(attributes_str):
    """Parse the attributes column and return a dictionary of the attributes."""
    attributes = {}
    for attribute in attributes_str.split(';'):
        if attribute:
            parts = attribute.strip().split(' ', 1)
            if len(parts) == 2:  # Check if there are exactly two parts
                key, value = parts
                attributes[key] = value.strip('"')
    return attributes

# Define a function to process the GTF file and create the mapping
def process_gtf(file_path):
    # Define the column names for a GTF file
    col_names = ['seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute']
    # Read the file
    gtf_df = pd.read_csv(file_path, comment='#', sep='\t', names=col_names, na_filter=False, converters={'attribute': parse_attributes})
    
    # Filter for exons
    exon_df = gtf_df[gtf_df['feature'] == 'exon']
    
    # Extract gene_id and transcript_id
    exon_df['gene_id'] = exon_df['attribute'].apply(lambda x: x.get('gene_id', ''))
    exon_df['transcript_id'] = exon_df['attribute'].apply(lambda x: x.get('transcript_id', ''))
    
    # Create the mapping DataFrame
    mapping = exon_df[['transcript_id', 'gene_id']].drop_duplicates().rename(columns={'transcript_id': 'TXNAME', 'gene_id': 'GENEID'})
    
    # Save to CSV
    mapping.to_csv('mapping.csv', index=False)

# Replace 'genomic.gtf' with the path to your actual GTF file
process_gtf('genomic.gtf')
print("Gene-transcript association table has been saved to 'mapping.csv'.")
