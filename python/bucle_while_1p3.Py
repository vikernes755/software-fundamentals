s={k:0 for k in"t su pa im po ne".split()}
while 1:
    n=int(input()); 
    if n<1:break
    s["t"]+=1; s["su"]+=n; p=1-n%2; q=n>0; s["pa"]+=p; s["im"]+=1-p; s["po"]+=q; s["ne"]+=1-q
print(*[f"{k}:{s[k]}" for k in s],sep="\n")
