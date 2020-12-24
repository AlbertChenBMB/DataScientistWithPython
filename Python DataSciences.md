# Python DataSciences
###### tags: `Python`
主要也是雜記,但目前規劃把資料科學相關的放過來這裡
## 讀取資料夾中所有資料


```python=
  
    
path_domestic = os.path.abspath(os.getcwd()) + '/Data1'
Data1=glob.glob(os.path.join(path_domestic,"*.csv"))
df_Data1=pd.concat((pd.read_csv(open(f),header=0) for f in Data1))

```
讀取Data1這個資料夾中所有csv檔


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
## 資料合併相關
