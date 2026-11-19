import numpy as np
import pandas as pd


def load_data(file):
    df = pd.read_csv(file)
    if df.shape[1] < 2 or df.shape[0] < 1:
        raise ValueError("CSV needs a microorganism column plus at least one sample column.")
    df = df.rename(columns={df.columns[0]: "Microorganism"})
    df["Microorganism"] = df["Microorganism"].astype(str).str.strip()
    samples = list(df.columns[1:])
    df[samples] = df[samples].apply(pd.to_numeric, errors="coerce")
    if df[samples].isna().any().any():
        raise ValueError("Sample columns must contain only numbers.")
    if (df[samples] < 0).any().any():
        raise ValueError("Abundance values cannot be negative.")
    df = df.groupby("Microorganism", as_index=False, sort=False)[samples].sum()
    return df.set_index("Microorganism")


def total_abundance(table):
    return table.sum(axis=1).sort_values(ascending=False).rename("Total")


def most_abundant(table):
    return total_abundance(table).idxmax()


def relative_abundance(table):
    totals = table.sum(axis=0).replace(0, np.nan)
    return (table / totals * 100).fillna(0)


def richness(table):
    return (table > 0).sum(axis=0).rename("Richness")


def shannon(table):
    p = table / table.sum(axis=0).replace(0, np.nan)
    h = -(p * np.log(p.where(p > 0))).sum(axis=0)
    return h.fillna(0).rename("Shannon")


def simpson(table):
    p = table / table.sum(axis=0).replace(0, np.nan)
    return (1 - (p ** 2).sum(axis=0)).fillna(0).rename("Simpson")


def evenness(table):
    r = richness(table)
    j = shannon(table) / np.log(r.where(r > 1))
    return j.fillna(0).rename("Evenness")


def diversity_table(table):
    out = pd.concat(
        [table.sum(axis=0).rename("Total abundance"),
         richness(table), shannon(table), simpson(table), evenness(table)],
        axis=1,
    )
    return out.round(3)


def bray_curtis(table):
    samples = table.columns
    values = table.to_numpy(dtype=float)
    n = len(samples)
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            denom = values[:, i].sum() + values[:, j].sum()
            if denom > 0:
                dist[i, j] = np.abs(values[:, i] - values[:, j]).sum() / denom
    return pd.DataFrame(dist, index=samples, columns=samples).round(3)


def top_taxa(table, n=5):
    order = total_abundance(table).index
    top = table.loc[order[:n]]
    rest = table.loc[order[n:]].sum(axis=0)
    if len(order) > n:
        top = pd.concat([top, rest.to_frame("Other").T])
        top.index.name = "Microorganism"
    return top


def compare_samples(table, a, b):
    out = table[[a, b]].copy()
    out["Difference"] = out[a] - out[b]
    return out.reindex(out["Difference"].abs().sort_values(ascending=False).index)