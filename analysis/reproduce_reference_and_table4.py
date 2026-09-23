import numpy as np
import pandas as pd

CRIT = ["HC1","HC2","HC3","AQ1","AQ2","AQ3","SC1","SC2","SC3","SF1","SF2","SF3","EE1","EE2","EE3"]
COST = {"EE1"}

def minmax_oriented(df):
    z = pd.DataFrame(index=df.index)
    for c in CRIT:
        x = df[c].astype(float)
        lo, hi = x.min(), x.max()
        if c in COST:
            z[c] = (hi - x) / (hi - lo)
        else:
            z[c] = (x - lo) / (hi - lo)
    return z

def entropy_weights(z):
    a = z.to_numpy(float)
    p = a / a.sum(axis=0, keepdims=True)
    k = 1.0 / np.log(a.shape[0])
    e = -k * np.sum(np.where(p > 0, p * np.log(p, where=p>0, out=np.ones_like(p)), 0.0), axis=0)
    d = 1.0 - e
    return d / d.sum()

def critic_weights(z):
    a = z.to_numpy(float)
    sd = a.std(axis=0, ddof=1)
    corr = np.corrcoef(a, rowvar=False)
    info = sd * np.sum(1.0 - corr, axis=1)
    return info / info.sum()

def topsis(x, w):
    a = x[CRIT].to_numpy(float)
    r = a / np.sqrt((a*a).sum(axis=0))
    v = r * w
    best = np.empty(len(CRIT)); worst = np.empty(len(CRIT))
    for j,c in enumerate(CRIT):
        if c in COST:
            best[j], worst[j] = v[:,j].min(), v[:,j].max()
        else:
            best[j], worst[j] = v[:,j].max(), v[:,j].min()
    dp = np.sqrt(((v-best)**2).sum(axis=1))
    dm = np.sqrt(((v-worst)**2).sum(axis=1))
    return dm/(dp+dm)

ref = pd.read_csv("data/reference_projects_36_synthetic.csv")
stage2 = pd.read_csv("data/stage2_performance_matrix.csv")
bwm = pd.read_csv("data/bwm_weights.csv").set_index("criterion").loc[CRIT,"weight"].to_numpy(float)
reported = pd.read_csv("data/comparator_weights_draft.csv").set_index("criterion")

z = minmax_oriented(ref)
cw = critic_weights(z)
ew = entropy_weights(z)
gw = np.sqrt(bwm*cw); gw /= gw.sum()
eq = np.ones(len(CRIT))/len(CRIT)

calc = pd.DataFrame({
    "criterion":CRIT,
    "BWM_primary":bwm,
    "CRITIC_reference":cw,
    "geometric_BWMxCRITIC_lambda_0_5":gw,
    "entropy_reference":ew,
    "equal":eq
})
print(calc.round(6).to_string(index=False))

for name,w in [("BWM primary",bwm),("BWMxCRITIC lambda=.5",gw),("Entropy-ref",ew),("Equal",eq)]:
    c=topsis(stage2,w)
    print(name, np.round(c,4))

# manuscript targets
targets={
"BWM primary":[0.3660,0.5984,0.8224,0.4849],
"BWMxCRITIC lambda=.5":[0.3665,0.5710,0.8038,0.5049],
"Entropy-ref":[0.2360,0.5093,0.8215,0.5597],
"Equal":[0.3503,0.5729,0.8047,0.5196],
}
for name,w in [("BWM primary",bwm),("BWMxCRITIC lambda=.5",gw),("Entropy-ref",ew),("Equal",eq)]:
    assert np.allclose(np.round(topsis(stage2,w),4), targets[name], atol=1e-4), name
print("All Table 4 TOPSIS targets reproduced to four decimals.")
