---
course: "[[01 Courses/Introduction to Data Mining/Course|Introduction to Data Mining]]"
date: "2026-10-13"
type: lecture
---
# Introduction to Data Mining

## Main ideas
-

## Definitions and formulas
- **Data mining:** Finding useful patterns and relationships in large datasets to support decisions and predictions.
- **Term frequency (TF):** How often a word appears in a document. Raw TF is its occurrence count; normalized TF divides that count by the document's total number of tokens.

$$
\operatorname{TF}_{\text{normalized}}(w,d)=\frac{\text{count of word }w\text{ in document }d}{\text{total tokens in document }d}
$$

### Ordered (ordinal) data

**Ordinal data** has categories with a meaningful order, such as **low < medium < high** or satisfaction ratings from **very dissatisfied** to **very satisfied**. The order is known, but the gaps between categories are not necessarily equal.

In data mining, we can encode low, medium, and high as **1, 2, and 3** to preserve their ranking. These numbers represent positions; they do not mean that high is three times low or that each step has the same size.

## Examples

### Simple tokenizer in Python

Tokenization splits text into smaller units called **tokens**, useful for analyzing text in data mining. This example converts text to lowercase and extracts words, ignoring punctuation.

```python
import re

def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())

text = "Data mining finds useful patterns!"
print(tokenize(text))
# ['data', 'mining', 'finds', 'useful', 'patterns']
```

### Count words and calculate TF

Using the `tokenize()` function above, Python's `Counter` counts each token:

```python
from collections import Counter

text = "Data mining uses data. Data reveals patterns."
tokens = tokenize(text)
counts = Counter(tokens)
total_tokens = len(tokens)
normalized_tf = {word: count / total_tokens for word, count in counts.items()}

print(dict(counts))
# {'data': 3, 'mining': 1, 'uses': 1, 'reveals': 1, 'patterns': 1}
print(normalized_tf["data"])
# 0.42857142857142855
```

The word **data** appears **3 times** in **7 tokens**: raw TF = 3, normalized TF = $3/7 \approx 0.429$. Normalization expresses frequency relative to document length.

### Save the counts in SQLite

This continues the example above. SQLite is included with Python and saves the database in a local file called `text_mining.db`.

```python
import sqlite3

with sqlite3.connect("text_mining.db") as db:
    db.execute("PRAGMA foreign_keys = ON")
    db.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY,
            text TEXT NOT NULL,
            total_tokens INTEGER NOT NULL
        )
    """)
    db.execute("""
        CREATE TABLE IF NOT EXISTS word_counts (
            document_id INTEGER NOT NULL REFERENCES documents(id),
            word TEXT NOT NULL,
            count INTEGER NOT NULL,
            PRIMARY KEY (document_id, word)
        )
    """)

    cursor = db.execute(
        "INSERT INTO documents (text, total_tokens) VALUES (?, ?)",
        (text, total_tokens),
    )
    document_id = cursor.lastrowid
    db.executemany(
        "INSERT INTO word_counts (document_id, word, count) VALUES (?, ?, ?)",
        [(document_id, word, count) for word, count in counts.items()],
    )

db.close()
```

For the first document, the stored word counts are:

| document_id | word | count |
| --- | --- | --- |
| 1 | data | 3 |
| 1 | mining | 1 |
| 1 | uses | 1 |
| 1 | reveals | 1 |
| 1 | patterns | 1 |

**Why save this?** The database preserves the results after the program closes and lets us query word frequencies across many documents without tokenizing them again. The document ID keeps each document's counts separate; the primary key allows only one row per word per document. We store raw counts and total tokens so normalized TF can be calculated when needed. Each run of this example adds a new document.

## Questions to resolve
-

## Recall questions
- What are the main ideas?
- Can I explain the key terms without looking?

## After-class summary
Write a short explanation from memory, then check it against the lecture material.

## Related concepts
-
