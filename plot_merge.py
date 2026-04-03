import csv
import matplotlib.pyplot as plt

def plot():
    sizes, seq, par = [], [], []

    with open("results_parallel.csv") as f:
        for r in csv.DictReader(f):
            sizes.append(int(r["size"]))
            seq.append(float(r["sequential"]))
            par.append(float(r["parallel"]))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(sizes, seq, label="MergeSort secvential", marker="o", linewidth=2, color="#e74c3c")
    ax.plot(sizes, par, label="MergeSort paralel", marker="o", linewidth=2, color="#3498db")

    ax.set_xlabel("n")
    ax.set_ylabel("Timp (s)")
    ax.set_title("MergeSort — secvential vs paralel")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.savefig("plots/parallel_comparison.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("  parallel_comparison.png")


if __name__ == "__main__":
    plot()