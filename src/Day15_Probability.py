# TASK 1: The Sample Space Map
ss=[["Click","Click"],["Click","Scroll"],["Click","Exit"],
    ["Scroll","Click"],["Scroll","Scroll"],["Scroll","Exit"]]
l=len(ss)
x=0
for i in ss:
    for j in i:
        if j=='Click':
            x=x+1
            break
print("Probability of atleast one Click in two consecutive interactions:\n",x/l)

d=[[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],
   [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],
   [3,1],[3,2],[3,3],[3,4],[3,5],[3,6],
   [4,1],[4,2],[4,3],[4,4],[4,5],[4,6],
   [5,1],[5,2],[5,3],[5,4],[5,5],[5,6],
   [6,1],[6,2],[6,3],[6,4],[6,5],[6,6]]
l1=len(d)
y=0
for t in d:
    i=0
    if t[i]+t[i+1]==7:
        y=y+1
print("Probability of sum being 7 after a 1000 rolls:\n",y/l1)

# TASK 2: The Logic of Dependency

p_heads=0.5
p_6=1/6
print("Probability that we getting a 6 rolling a die after getting heads on a coin flip:",p_heads*p_6)
n_r=5
n_b=5
ballsinbag=n_r+n_b
prob_red1=n_r/ballsinbag
prob_red2=(n_r-1)/(ballsinbag-1)
prob_redred=prob_red1*prob_red2
print("Probability of getting two reds back to back without replacement:",prob_redred)

# TASK 3: The Bayesian Filter
p_spam=0.1
p_freeinspam=0.9
p_freeinnonspam=0.05
p_free=(p_freeinspam*p_spam)+(p_freeinnonspam*(1-p_spam))
print("Total Probability of Free words:",p_free)
p_spamiffree=(p_freeinspam*p_spam)/p_free
print("Probability of email being spam if word free is present:",p_spamiffree)
