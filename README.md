# NTUB_DOMJudge
<img src="https://hackmd.io/_uploads/SkhuNdgC6.png" alt="image" width="auto" height="100px">

![Static Badge](https://img.shields.io/badge/python%203--a?style=flat&logo=python&logoColor=white&color=4FCA21) 
![Static Badge](https://img.shields.io/badge/windows%2011--any?style=flat&logo=windows11&color=0074CD) ![build](https://img.shields.io/appveyor/ci/:user/:repo.svg)

> [!NOTE]  
> **練習區**
> https://onlinejudge.ntub.edu.tw/team
>https://shields.io/badges/ansible-role


## :pushpin: Table of Contents

- [NTUB\_DOMJudge](#ntub_domjudge)
  - [:pushpin: Table of Contents](#pushpin-table-of-contents)
  - [:pencil:Score](#pencilscore)
  - [題目詳解](#題目詳解)
    - [A01 Problem 哈囉](#a01-problem-哈囉)
    - [A02A Problem 簡易加法](#a02a-problem-簡易加法)
    - [A02B Problem 兩數有權重相加(單列)](#a02b-problem-兩數有權重相加單列)
    - [A03 Problem Time Limit: 1 Second](#a03-problem-time-limit-1-second)
    - [A04 Problem 民國年份](#a04-problem-民國年份)
    - [A05 Problem 妳那裡現在幾點了？](#a05-problem-妳那裡現在幾點了)
    - [A06 Problem 糟糕，我發燒了！](#a06-problem-糟糕我發燒了)
    - [A07 Problem 分組報告](#a07-problem-分組報告)
    - [A08 Problem 買鉛筆](#a08-problem-買鉛筆)
    - [B01 Problem](#b01-problem)
    - [B02 Problem](#b02-problem)
    - [B03 Problem](#b03-problem)
    - [B04 Problem ㄑㄧˊ數？](#b04-problem-ㄑㄧˊ數)
    - [B05 Problem 三人行必有我師](#b05-problem-三人行必有我師)
    - [B06 Problem 格瑞哥里的煩惱(單行版)](#b06-problem-格瑞哥里的煩惱單行版)
    - [B07 Problem 該減肥了！](#b07-problem-該減肥了)
    - [B08 Problem 剪刀石頭布單行版](#b08-problem-剪刀石頭布單行版)
    - [B09 Problem](#b09-problem)
    - [B10 Problem hh:mm hh:mm](#b10-problem-hhmm-hhmm)
    - [B11 Problem 上學去吧！](#b11-problem-上學去吧)


## :pencil:Score
> [!NOTE]  
> **記分板**

|    **Item**   	|          **Score**         	|                           **Result**                 	|
|:-----------------:	|:-------------------------:	|:-----------------------------------------------:	|
|   A01  	            |       319 	                |❌❌✅|
|   A02A               	|       302                     |✅|
|   A02B    	        |       331      			    |✅|
|   A03             	|       345     	            |✅|
|   A04                	|       406       	            |✅|
|   A05                	|       	       	            |  |
|   A06                	|       435       	            |✅|
|   A07                	|       447                     |✅|
|   A08      	        |       655                     |✅|
|   B01                	|       663                     |✅| 	
|   B02                	|       673                     |✅| 	
|   B03                	|       682                     |✅| 
|   B04                	|       1897                	|✅|
|   B05                	|       3151                   	|✅| 
|   B06 	            |       3254           	        |✅| 
|   B07                	|                 	|      	   |
|   B08               	|                  	|      	   |
|   B09                	|                   |      	   | 	
|   B10                	|                   |      	   |        	
|   B11                	|                   |      	   |       	

##    題目詳解

### A01 Problem 哈囉
---

```gherkin=
a = input()
print("hello, "+ a) characters
```
>  :bust_in_silhouette: HaaryDulia

### A02A Problem 簡易加法
---

```gherkin=
a,b = map (int,input().split())
sum= a+b
print(sum)
```
>  :bust_in_silhouette: HaaryDulia

### A02B Problem 兩數有權重相加(單列)
```gherkin=
a,b = map (int,input().split())
sum= 4*a+6*b
print(sum)
```
>  :bust_in_silhouette: HaaryDulia

### A03 Problem Time Limit: 1 Second
```gherkin=
a = int(input())
sum= a^1 
print (sum)
```
>  :bust_in_silhouette: HaaryDulia

### A04 Problem 民國年份
```gherkin=
y=int(input())
print(y-1911)
```
>  :bust_in_silhouette: HaaryDulia

### A05 Problem 妳那裡現在幾點了？
<!-- > [!CAUTION] -->
 ```gherkin=
times = int(input())
print((24+times-15)%24)
 ```



>  :bust_in_silhouette: HaaryDulia


### A06 Problem 糟糕，我發燒了！
```gherkin=
f = float(input())
c= float(5/9*(f-32))
print ('%.3f'%c)
```
>  :bust_in_silhouette: HaaryDulia

### A07 Problem 分組報告
> [!TIP]
> 如何不使用if else
```gherkin=
n = int(input())
print((n - 1) // 3 + 1) #//取整數
```
>  :bust_in_silhouette: HaaryDulia

### A08 Problem 買鉛筆
> [!TIP]
> 如何不使用if else
```gherkin=
pen = int(input())
print(pen//12*50+pen%12*5) #能整除一打就直接*50 不能就將餘數*單價
```
>  :bust_in_silhouette: HaaryDulia

### B01 Problem 
```gherkin=
m,d = map(int,(input().split())) #m月d日
S=(m*2+d)%3
print(S) 
```
>  :bust_in_silhouette: HaaryDulia

### B02 Problem 
```gherkin=
n = int(input())
print((n > 0) + (-(n < 0)))
```
>  :bust_in_silhouette: HaaryDulia

### B03 Problem 
```gherkin=
times = int(input())
print((85-times)%60)
```
>  :bust_in_silhouette: HaaryDulia

### B04 Problem ㄑㄧˊ數？
> [!TIP]
> 如何不使用if else
```gherkin=
print("1" if int(input())%2 else "0")
```
>  :bust_in_silhouette: HaaryDulia

### B05 Problem 三人行必有我師
```gherkin=
a,b,c = map(int,(input().split())) #abc代表三個數字
lists = [a,b,c]
nmax = max(lists)
print(nmax)
```
>  :bust_in_silhouette: HaaryDulia

### B06 Problem 格瑞哥里的煩惱(單行版)
```gherkin=
year = int(input())
s = "a leap year" if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "a normal year"
#閏年的條件要符合可以整除4且不會被100整除或可以被400整除，條件不符合時則進入else
print(s)
```
>  :bust_in_silhouette: HaaryDulia

### B07 Problem 該減肥了！
```gherkin=

```
>  :bust_in_silhouette: HaaryDulia

### B08 Problem 剪刀石頭布單行版
```gherkin=

```
>  :bust_in_silhouette: HaaryDulia
### B09 Problem 
```gherkin=

```
>  :bust_in_silhouette: HaaryDulia

### B10 Problem hh:mm hh:mm
```gherkin=

```
>  :bust_in_silhouette: HaaryDulia

### B11 Problem 上學去吧！
```gherkin=

```
>  :bust_in_silhouette: HaaryDulia
