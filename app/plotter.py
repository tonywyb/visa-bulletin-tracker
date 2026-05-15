import matplotlib.pyplot as plt
from datetime import datetime

def to_index(date_str):
    if not date_str or date_str == "C":
        return None
    try:
        dt = datetime.strptime(date_str, "%d%b%Y")
        return dt.year * 12 + dt.month
    except:
        return None

def plot(data):
    months, final_vals, filing_vals = [], [], []

    for row in data:
        month, f, fi, _ = row
        months.append(month)
        final_vals.append(to_index(f))
        filing_vals.append(to_index(fi))

    x = list(range(len(months)))

    plt.figure()
    plt.plot(x, final_vals, label="Final Action")
    plt.plot(x, filing_vals, label="Filing")

    for i, m in enumerate(months):
        if "-10" in m:
            plt.axvline(i, linestyle="--")

    plt.xticks(x, months, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig("visa_trend.png")
