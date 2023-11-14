#!/usr/bin/env python
from intermine.webservice import Service
import pandas as pd
import csv

# Initialize the YeastMine service
service = Service("https://yeastmine.yeastgenome.org/yeastmine/service")

# Function to fetch GO terms for a given gene ID
def fetch_gene_data(gene_id):
    query = service.new_query("Gene")
    query.add_view(
        "primaryIdentifier", "secondaryIdentifier", "symbol", "featureType",
        "qualifier", "goAnnotation.ontologyTerm.identifier",
        "goAnnotation.ontologyTerm.name", "goAnnotation.ontologyTerm.namespace",
        "goAnnotation.evidence.code.code", "goAnnotation.qualifier",
        "goAnnotation.evidence.code.withText", "goAnnotation.annotationExtension",
        "goAnnotation.evidence.code.annotType",
        "goAnnotation.evidence.publications.pubMedId",
        "goAnnotation.evidence.publications.citation"
    )
    query.add_constraint("organism.shortName", "=", "S. cerevisiae")
    query.add_constraint("Gene", "LOOKUP", gene_id)

    # Fetch the results and return them
    for row in query.rows():
        return {
            "GeneID": gene_id,
            "GO Identifier": row["goAnnotation.ontologyTerm.identifier"],
            "GO Name": row["goAnnotation.ontologyTerm.name"],
            "GO Namespace": row["goAnnotation.ontologyTerm.namespace"]
        }
    return None

# Load the DataFrame containing the gene IDs
df = pd.read_csv('../data/annotated_genes.csv')

# Prepare the output file
with open('gene_data_with_go_terms.csv', 'w', newline='') as csvfile:
    fieldnames = ["GeneID", "GO Identifier", "GO Name", "GO Namespace"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate over each gene ID and write the GO term data to the CSV file
    for gene_id in df['GeneID']:
        gene_data = fetch_gene_data(gene_id)
        if gene_data:
            writer.writerow(gene_data)

