import streamlit as st
import analysis as an
import plots

st.title("Microbiome Data Analysis Starter")

# 1. Get the data
uploaded = st.file_uploader("Upload a CSV file", type="csv")
if uploaded is None:
    st.info("No file uploaded, so the sample data is being used.")
    uploaded = "sample_microbiome_data.csv"

table = an.load_data(uploaded)

# 2. Show the data
st.header("Data")
st.dataframe(table)

# 3. Abundance
st.header("Abundance")
st.write("Most abundant microorganism:", an.most_abundant(table))
st.dataframe(an.total_abundance(table))
st.pyplot(plots.abundance_bar(table))

# 4. Relative abundance and heatmap
st.header("Relative abundance and heatmap")
rel = an.relative_abundance(table)
st.pyplot(plots.composition_bar(rel))
st.pyplot(plots.heatmap(table, title="Abundance Heatmap", cbar_label="Abundance"))

# 5. Diversity
st.header("Diversity")
div = an.diversity_table(table)
st.dataframe(div)
measure = st.selectbox("Choose a measure to plot", ["Richness", "Shannon", "Simpson", "Evenness"])
st.pyplot(plots.diversity_bar(div[measure], measure + " per sample", measure))

# 6. Compare two samples
st.header("Compare two samples")
samples = list(table.columns)
a = st.selectbox("Sample A", samples, index=0)
b = st.selectbox("Sample B", samples, index=1)
if a != b:
    st.pyplot(plots.compare_bar(an.compare_samples(table, a, b), a, b))
else:
    st.warning("Pick two different samples.")

