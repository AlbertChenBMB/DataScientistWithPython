# this is practice of statistical inference with python

###
# statistical inference lets scientists formulate conclusions from data and quantify the uncertainty arising from using incomplete data
####

# 共同機率
# 寫一個class 裡面放不同的function, 先放簡單的機率function
from tokenize import Ignore
import sys


def Prob_fu(x1,x2,Ptype="AND"):
    AND_P= (float(x1)*float(x2))
    if Ptype == "AND":
        return AND_P
    elif Ptype=="OR":
        return float(x1+x2)-float(AND_P)
    else:
        return "wrong prob_type!"


x1=input("fist probability:")
x2=input("second probability:")
Ptype=input("ptype:")

print(Prob_fu(x1,x2,Ptype)) 

## PMF : 機率質量函數
def PMF():
    return()
### PDF : 機率密度函數
def PDF():
    return()

### CDF : 累積分布函數
def CDF_pract(x,y):
    return (float(x)*float(y))/2
## 當隨機變量是連續的, PDF是CDF的導數
## PDF的積分會是CDF
## 當CDF取積分則是一個面積(機率)
# 所以寫一個 integrate(PDF, 範圍)可以得到一個面積 = 機率


### Conditional probability
def conditional_prob(A,B):
    return (A*B)/B

