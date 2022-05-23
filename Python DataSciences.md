# Python DataSciences
###### tags: `Python`
主要也是雜記,但目前規劃把資料科學相關的放過來這裡

## 用pandas 讀取檔案
讀取csv檔
```python=
data = pd.read_csv(open("檔案名稱"),index_col=0,encoding='utf8')
# index_col =0 會忽略掉第一條col(index)
# 如果有中文記得要把encoding設定好

```
讀取xlsx檔
* 不要用open
```python=
data = pd.read_excel("檔案名稱",skiprows= 1,header = None)
# skiprows 會忽略掉看設定多少行

```
## 資料合併相關
```python=
df=pd.concat([data,data1],ignore_index=True)
```
## 輸出檔案
如果我們要將df這個dataframe輸出成csv檔
```python
df.to_csv('目的資料名稱.csv',index = False)
```

## 讀取資料夾中所有資料


```python=
  
path_domestic= os.path.abspath(os.getcwd())+'\\資料夾名稱'
dataset = glob.glob(os.path.join(path_domestic,"*.csv"))
#dataset會是一個帶有資料夾中所有csv檔名的list
data = pd.read_csv(open(dataset[0]),encoding="utf-8")
#先讀這個list中的第一個檔案
for i in range(len(dataset)-1):
    data1=pd.read_csv(open(dataset[i+1]),encoding="utf-8")
    data=pd.concat([data,data1])
```

## 篩選特定名稱的欄位

有數個column組成的資料集
想取欄位名稱包含特定字的作為子集
可以用filter(regex=" ")
如下
```python=
df_0 = df.filter(regex='0')
print(df2)

```
取df這份資料中欄位包含0的作為子資料集df_0
取完資料如下:


## 計算相關係數並產出比較矩陣
```python=
# correlation f
cor_1=[]
cor_2=[]
#cor_3=[]
for i in range(0,len(avoid0_data.columns)):
    x1=np.corrcoef(avoid0_data.iloc[:,i],avoid0_data['Tagname_1'],)
    x2=np.corrcoef(avoid0_data.iloc[:,i],avoid0_data['Tagname_2'],)
    #x3=np.corrcoef(avoid0_data.iloc[:,i],avoid0_data['Tagname_3'],)
    cor_1.append(x1[1,0])
    cor_2.append(x2[1,0])
    #cor_3.append(x3[1,0])
    
# print(cor)
#sig=pd.DataFrame({'name':col_name,'corr':cor})

#print(cor[1,0])
per_cor=pd.DataFrame({'name':col_name,'Tag1':cor_1,'Tag2':cor_2})
#per_cor['check']= abs(per_cor['Tag1']*per_cor['Tag2'])**(1/2)
print(per_cor)

```

## 對dataframe裡面做動作
舉例我們有學生的身高體重要計算幾個新變數
BMI
BMI是否超標
```python=
high = [160,158,180,178,165,172]
weight = [60,45,80,60,67,55]
df =pd.DataFrame({'high':high,'weight':weight})

```
計算BMI
```python=
df['BMI']=weight/(df['high']/100)**2
```

如果BMI >24 顯示"超標"

```python=
newcol="是否超標"
df[newcol]=df['BMI'].apply(lambda x:'超標' if x>24 else "正常" )

```
另一種寫法(可用在兩個列作比較
```python=
newcol= "check"
df[newcol]=np.where(df['weight']/((df['high']/100)**2)>df['BMI'],1,0)

```
### 資料前處理

### 特徵篩選
* 迴歸係數
* 決策樹 吉尼係數
* mRMR
