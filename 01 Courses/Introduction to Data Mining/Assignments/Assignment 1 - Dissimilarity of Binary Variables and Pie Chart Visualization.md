---
course: "[[01 Courses/Introduction to Data Mining/Course|Introduction to Data Mining]]"
type: assignment
due:
status: done
tags:
  - data-mining
  - binary-dissimilarity
  - visualization
---
# Assignment 1 — Binary Dissimilarity & Pie Chart

Code file: [`assignment1.py`](file:///Users/amirabaris/Documents/uni-fall/01%20Courses/Introduction%20to%20Data%20Mining/Assignments/assignment1.py)

---

## 1. Formulas

Contingency table ($2 \times 2$) for objects $i$ and $j$:
- $q$: both $1$
- $r$: $i=1, j=0$
- $s$: $i=0, j=1$
- $t$: both $0$

$$\text{SMC Dissimilarity (Symmetric): } d_{\text{SMC}} = \frac{r + s}{q + r + s + t}$$

$$\text{Jaccard Dissimilarity (Asymmetric): } d_{\text{Jaccard}} = \frac{r + s}{q + r + s}$$

---

## 2. Python Code

```python
import matplotlib.pyplot as plt

# 1. Binary Dissimilarity Functions
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

# Distance Matrices
names = list(data.keys())
print("Jaccard Matrix:")
for p1 in names:
    print(p1, [round(d_jaccard(data[p1], data[p2]), 3) for p2 in names])

# 2. Pie Chart
labels = ["Class A", "Class B", "Class C"]
counts = [50, 30, 20]
plt.pie(counts, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Class Distribution")
plt.show()
```

---

## 3. Output

```text
Jaccard Matrix:
P1 [0.0, 0.667, 0.75, 1.0]
P2 [0.667, 0.0, 0.75, 1.0]
P3 [0.75, 0.75, 0.0, 0.667]
P4 [1.0, 1.0, 0.667, 0.0]
```
