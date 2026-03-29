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


def load():
    rows = []
    with open("results.csv") as f:
        for r in csv.DictReader(f):
            if r["avg_time_s"]:
                r["size"] = int(r["size"])
                r["avg_time_s"] = float(r["avg_time_s"])
                rows.append(r)
    return rows


def plot(rows):
    os.makedirs(PLOTS_DIR, exist_ok=True)

    for dt in sorted(set(r["data_type"] for r in rows)):
        fig, ax = plt.subplots(figsize=(10, 6))

        for algo in sorted(set(r["algorithm"] for r in rows)):
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
        ax.set_title(TITLES.get(dt, dt))
        ax.legend(fontsize=8)
        ax.set_yscale("log")  # motivul ptr care toate arata ca graficul lui log n, le am pus asa ca sa incapa in grafic
        ax.grid(True, alpha=0.3)
        fig.savefig(f"{PLOTS_DIR}/{dt}.png", dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"  {dt}.png")


if __name__ == "__main__":
    plot(load())