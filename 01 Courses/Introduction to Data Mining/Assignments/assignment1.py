import matplotlib.pyplot as plt

# -------------------------------------------------------------
# 1. Binary Dissimilarity
# -------------------------------------------------------------
def contingency(v1, v2):
    q = sum(1 for a, b in zip(v1, v2) if a == 1 and b == 1)
    r = sum(1 for a, b in zip(v1, v2) if a == 1 and b == 0)
    s = sum(1 for a, b in zip(v1, v2) if a == 0 and b == 1)
    t = sum(1 for a, b in zip(v1, v2) if a == 0 and b == 0)
    return q, r, s, t

def d_smc(v1, v2):
    q, r, s, t = contingency(v1, v2)
    return (r + s) / (q + r + s + t)

def d_jaccard(v1, v2):
    q, r, s, t = contingency(v1, v2)
    return (r + s) / (q + r + s)

# Sample Data
data = {
    "P1": [1, 1, 0, 0],
    "P2": [1, 0, 1, 0],
    "P3": [0, 1, 1, 1],
    "P4": [0, 0, 0, 1],
}

names = list(data.keys())

print("Jaccard Dissimilarity Matrix (Asymmetric):")
for p1 in names:
    print(p1, [round(d_jaccard(data[p1], data[p2]), 3) for p2 in names])

print("\nSimple Matching Matrix (Symmetric):")
for p1 in names:
    print(p1, [round(d_smc(data[p1], data[p2]), 3) for p2 in names])

# -------------------------------------------------------------
# 2. Pie Chart
# -------------------------------------------------------------
labels = ["Class A", "Class B", "Class C"]
counts = [50, 30, 20]

plt.figure(figsize=(5, 5))
plt.pie(counts, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Class Distribution")
plt.tight_layout()
plt.show()
