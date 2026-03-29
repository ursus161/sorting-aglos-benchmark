import csv
import os
import matplotlib.pyplot as plt

PLOTS_DIR = "plots"

COLORS = {
    "BubbleSort": "#e74c3c",
    "CocktailSort": "#e67e22",
    "InsertionSort": "#f1c40f",
    "MergeSort": "#2ecc71",
    "HeapSort": "#3498db",
    "RadixSort": "#9b59b6",
    "sorted()": "#1a1a2e",
}

TITLES = {
    "random": "Date aleatoare",
    "sorted": "Date sortate crescator",
    "reversed": "Date sortate descrescator",
    "nearly_sorted": "Date aproape sortate",
    "duplicates": "Date cu multe duplicate",
}

SLOW = {"BubbleSort", "CocktailSort", "InsertionSort"}
FAST = {"MergeSort", "HeapSort", "RadixSort", "sorted()"}


def load():
    rows = []
    with open("results.csv") as f:
        for r in csv.DictReader(f):

            if r["avg_time_s"]:


                r["size"] = int(r["size"])
                r["avg_time_s"] = float(r["avg_time_s"])
                rows.append(r)
                
    return rows


def plot_group(ax, rows, dt, algos, subtitle):
    for algo in sorted(algos):
        pts = sorted(
            [r for r in rows if r["data_type"] == dt and r["algorithm"] == algo],
            key=lambda r: r["size"],
        )
        if not pts:
            continue
        ax.plot(


            [p["size"] for p in pts],
            [p["avg_time_s"] for p in pts],
            label=algo, marker="o",
            color=COLORS.get(algo, "#999"), linewidth=2,
        )


    ax.set_xlabel("n")
    ax.set_ylabel("Timp (s)")
    ax.set_title(subtitle)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)


def plot(rows):
    os.makedirs(PLOTS_DIR, exist_ok=True)

    for dt in sorted(set(r["data_type"] for r in rows)):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        title = TITLES.get(dt, dt)
        plot_group(ax1, rows, dt, SLOW, f"{title} — O(n^2)")
        plot_group(ax2, rows, dt, FAST, f"{title} — eficienti")
        fig.tight_layout()
        fig.savefig(f"{PLOTS_DIR}/{dt}.png", dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"  {dt}.png")


if __name__ == "__main__":
    plot(load())