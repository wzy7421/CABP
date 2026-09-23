#!/usr/bin/env python3
"""Reproduce focal synthetic-fixture TOPSIS values using only the Python standard library."""
import csv, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

CRITERIA = ["HC1","HC2","HC3","AQ1","AQ2","AQ3","SC1","SC2","SC3","SF1","SF2","SF3","EE1","EE2","EE3"]
COST = {"EE1"}

def read_matrix():
    rows = []
    names = []
    with open(DATA / "stage2_performance_matrix.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            names.append(r["alternative"])
            rows.append([float(r[c]) for c in CRITERIA])
    return names, rows

def read_bwm():
    d = {}
    with open(DATA / "bwm_weights.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            d[r["criterion"]] = float(r["weight"])
    w = [d[c] for c in CRITERIA]
    s = sum(w)
    return [x/s for x in w]

def topsis(x, w):
    m, n = len(x), len(x[0])
    den = [math.sqrt(sum(x[i][j]**2 for i in range(m))) for j in range(n)]
    v = [[x[i][j]/den[j]*w[j] for j in range(n)] for i in range(m)]
    ideal, anti = [], []
    for j,c in enumerate(CRITERIA):
        col = [v[i][j] for i in range(m)]
        if c in COST:
            ideal.append(min(col)); anti.append(max(col))
        else:
            ideal.append(max(col)); anti.append(min(col))
    out = []
    for i in range(m):
        dp = math.sqrt(sum((v[i][j]-ideal[j])**2 for j in range(n)))
        dm = math.sqrt(sum((v[i][j]-anti[j])**2 for j in range(n)))
        out.append(dm/(dp+dm))
    return out

names, x = read_matrix()
bwm = read_bwm()
equal = [1/len(CRITERIA)]*len(CRITERIA)

for label,w in [("BWM primary", bwm), ("Equal", equal)]:
    c = topsis(x,w)
    print(label)
    for n,v in zip(names,c):
        print(f"  {n}: {v:.4f}")
    order = [n for _,n in sorted(zip(c,names), reverse=True)]
    print("  order:", " > ".join(order))
