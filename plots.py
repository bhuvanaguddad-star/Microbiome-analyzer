import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def abundance_bar(table, stacked=False):
    fig, ax = plt.subplots()
    table.plot(kind="bar", stacked=stacked, ax=ax)
    ax.set_title("Microorganism Abundance")
    ax.set_ylabel("Abundance")
    return fig


def composition_bar(rel_table):
    fig, ax = plt.subplots()
    rel_table.T.plot(kind="bar", stacked=True, ax=ax)
    ax.set_title("Relative Abundance per Sample")
    ax.set_ylabel("Percent")
    return fig


def heatmap(df, title="Heatmap", cbar_label="Value", cmap="coolwarm"):
    fig, ax = plt.subplots()
    picture = ax.imshow(df.to_numpy(dtype=float), cmap=cmap)
    ax.set_xticks(range(len(df.columns)))
    ax.set_xticklabels(df.columns)
    ax.set_yticks(range(len(df.index)))
    ax.set_yticklabels(df.index)
    ax.set_title(title)
    fig.colorbar(picture, ax=ax, label=cbar_label)
    return fig


def diversity_bar(series, title, ylabel):
    fig, ax = plt.subplots()
    series.plot(kind="bar", ax=ax)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    return fig


def compare_bar(df, a, b):
    fig, ax = plt.subplots()
    df[[a, b]].plot(kind="bar", ax=ax)
    ax.set_title(a + " vs " + b)
    ax.set_ylabel("Abundance")
    return fig
