# Statistical inference
###### tags: statistical


## Probability
Given a random experiment a probability measure is a population quantity that summarizes the randomness.
Specifically, probability takes a possible outcome from the expertiment and :
* assigns it a number between 0 to 1
* the probability that something occurs is 1
* the probabiltiy of the union of any two sets of outcomes that have nothing in common is the sum of their respective probabilities.

## Rules probability must follow
* the probability that nothing occurs is 0
* the probability that nothing occurs is 1
* the probability of something is 1 minus the porbability that the opposite occurs.
* the probability of at least one of two(or more) things that can not simultaneously occur(mutually exclusive) is the sum of their respective probailities
* if an event A implies the occurrence of event B, then the probability of A occurring is less than the probability that B occurs.
* For any two events the probability that at leasst one occurs is the sum of their probabilities minus their intersection.


## probability mass function
在機率論和統計學中，機率質量函數（probability mass function，簡寫作pmf）是離散隨機變數在各特定取值上的機率[1]。有時它也被稱為離散密度函數。 機率質量函數通常是定義離散機率分布的主要方法，並且此類函數存在於其定義域是離散的純量變數或多元隨機變數。

A probability mass function evaluated at a value corresponds to the probability that a random variable takes that value.
to be a valid pmf a function, *p*, must satisfy
1. it must always be large than or equal to 0
2. the sum of the possible values that the random variable can take has to add up to one.
#### example
*X* =0 represents tails and *X* =1 represents heads.
*p(x) = (1/2)^x * (1/2)^(1-x)* for *x* =0,1

伯努利分布就是一個很好的例子
reference : https://zh.wikipedia.org/zh-tw/%E6%A6%82%E7%8E%87%E8%B4%A8%E9%87%8F%E5%87%BD%E6%95%B0

## probability density functions
在數學中，連續型隨機變數的機率密度函數（Probability density function，簡寫作PDF [1]），在不致於混淆時可簡稱為密度函數，是一個描述這個隨機變數的輸出值，在某個確定的取值點附近的可能性的函數。圖中，橫軸為隨機變數的取值，縱軸為機率密度函數的值，而隨機變數的取值落在某個區域內的機率為機率密度函數在這個區域上的積分。當機率密度函數存在的時候，累積分布函數是機率密度函數的積分。


reference:https://zh.wikipedia.org/zh-tw/%E6%A9%9F%E7%8E%87%E5%AF%86%E5%BA%A6%E5%87%BD%E6%95%B8