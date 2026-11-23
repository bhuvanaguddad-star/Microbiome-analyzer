# Microbiome Data Analysis Starter

Is a web app that can analyze microbiome data. By uploading a dataset in the form of a CSV file containing information such as microorganisms, their abundance, richness, etc. and the app can help compare and contrast between its diversity and help visualize information in the form of charts , graphs and other optimal measures.

Python course project - Bhuvana Guddad (SE25UCAB026)

## What it does-
- Reads a CSV file of microorganism abundances.
- Finds total abundance and the most abundant microorganism in that dataset.
- Calculates diversity per sample: Richness, Shannon, Simpson and Evenness.
- Draws bar charts and heatmaps.
- Compares two samples.

## CSV format
The first column holds microorganism names. Every other column is one sample with numbers.

Microorganism,Sample1,Sample2
Escherichia coli,120,85
Bacteroides fragilis,300,280

## How to run it
1. Install the libraries:
   pip install -r requirements.txt
2. Start the app:
   streamlit run app.py

## Files
- app.py - the web app
- analysis.py - calculations (abundance, diversity, comparison)
- plots.py - charts and heatmaps
- sample_microbiome_data.csv - example data

## Built with
Python, Pandas, NumPy, Matplotlib, Streamlit
