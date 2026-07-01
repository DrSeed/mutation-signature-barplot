import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
subs=["C>A","C>G","C>T","T>A","T>C","T>G"];bases="ACGT"
ctx=[f"{a}[{s}]{b}" for s in subs for a in bases for b in bases]
rng=np.random.default_rng(2);h=rng.uniform(0,1,96)
# enrich C>T (like a UV/ageing-ish signature)
for i,c in enumerate(ctx):
    if "C>T" in c:h[i]+=rng.uniform(2,5)
h/=h.sum()
cols=[]
palette=["#03bcee","#010101","#e42926","#cac9c9","#a1ce63","#ecc6c5"]
for s in subs:cols+=[palette[subs.index(s)]]*16
plt.figure(figsize=(13,3.5));plt.bar(range(96),h,color=cols,width=.8)
plt.xticks([]);plt.ylabel("proportion");plt.title("Mutational signature, 96 contexts (demo data)")
for i,s in enumerate(subs):plt.text(i*16+8,max(h)*1.02,s,ha="center",fontsize=9)
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("C>T dominated signature\n");print("ok")