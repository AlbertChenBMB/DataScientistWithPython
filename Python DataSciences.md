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
* index_col很好用, 記得如果某一行要當作是index,就直接用index_col指定, 對畫圖很方便

讀取xlsx檔
* 不要用open
```python=
data = pd.read_excel("檔案名稱",skiprows= 1,header = None)
# skiprows 會忽略掉看設定多少行

```
讀取特殊資料
1. 掠過某幾row和忽略空格問題
```python=
data1 = pd.read_csv(open("L8BBS1_test.csv"), error_bad_lines=False, header=None,sep=",",decimal=" ", skiprows=3,skipinitialspace=True)
```
上面閃掉了前3行

2. 選擇特定條件的row(這邊是=AI)和特定幾個columns(這邊只取0~1列)
```python=
AI_data = data1.loc[data1[0]=='AI', 0:2]
len(AI_data)

```

## 資料合併相關
```python=
df=pd.concat([data,data1],ignore_index=True)
```
### 合併時間index

```
python=df=pd.concat([data,data3],axis=1)
df
```
上面範例data和data3有相同的時間index,只要注意使用axis=1即可
若只有要合併某些特定的column,就要加上keys

參考:
https://stackoverflow.com/questions/11714768/concat-pandas-dataframe-along-timeseries-indexes

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
## NA 處理與檢查
```python=
missing_val_count_by_column = (資料集.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])

```
可以檢查哪些欄位有NA, Na有多少
## print哪幾個欄位有NA
```python=

if len(df.columns[df.isna().any()].tolist()) >0:
    print(','.join(df.columns[df.isna().any()].tolist())+ " has na value")
```

## print哪幾個index有NA
```python=

df.index[np.where(np.isnan(df))[0]]
```

### NA 補值
時序資料常用往前（或是往後）遇到的第一個非 nan 值
Original Dataframe


example:

```python=
In [3]: df = pd.DataFrame({'ColA':[1, np.nan, np.nan, 4, 5, 6, 7], 'ColB':[1, 1, 1, 1, 2, 2, 2]})
In [4]: df
Out[4]:
ColA  ColB
0   1.0     1
1   NaN     1
2   NaN     1
3   4.0     1
4   5.0     2
5   6.0     2
6   7.0     2
# 往前
In [11]: df['ColA'].fillna(method='ffill', inplace=True)
In [12]: df
Out[12]:
ColA  ColB
0   1.0     1
1   1.0     1
2   1.0     1
3   4.0     1
4   5.0     2
5   6.0     2
6   7.0     2

#往後

In [14]: df['ColA'].fillna(method='bfill', inplace=True)
In [15]: df
Out[15]:
ColA  ColB
0   1.0     1
1   4.0     1
2   4.0     1
3   4.0     1
4   5.0     2
5   6.0     2
6   7.0     2

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
### 如果要對資料對處理時加上一些條件或計算新的東西
```python=
FD=srs1[['Date','SRS_RD1_VFT','SRS_RD1_VV']]
FD.head(5)
FD['VFT_VV'] = 0 
for idx, row in  FD.iterrows():  # 請務必記得加上idx，不然跑回圈的item會變成(idx, row)
    SRS_RD1_VV = row['SRS_RD1_VV']
    SRS_RD1_VFT = row['SRS_RD1_VFT']
    if SRS_RD1_VV < 0.1:
        VFT_VV = 0
    else :
        VFT_VV = SRS_RD1_VFT / SRS_RD1_VV
    FD.loc[idx, 'VFT_VV'] = VFT_VV

```

### 比較最高值

```python=
owwr['max_freq'] = 0 
for idx, row in  owwr.iterrows():  # 請務必記得加上idx，不然跑回圈的item會變成(idx, row)
    max_freq = max(row['B415D_Output_Frequency'],row['B415E_Output_Frequency'],row['B415F_Output_Frequency'])    
    owwr.loc[idx, 'max_freq'] = max_freq
```

### 去除掉不需要的
FD.drop(['B', 'C'], axis=1)




## 時間範圍
# Select observations between two datetimes
df[(df['date'] > '2002-1-1 01:00:00') & (df['date'] <= '2002-1-1 04:00:00')]


newcol="Need PM"
FD[newcol]=np.where((FD['Date_one'] > '2019-10-10 11:00:00') & (FD['Date_one'] <= '2020-2-19 08:00:00') ,1, 0 )

## 異常資料處理

想找shortset這個資料集裡面,變數'DO_spread'>0.75%的值
```python=
upper_lim= shortset['DO_spread'].quantile(0.75)
#設定 0.75以上的為upper_lim
shortset.loc[(abs(shortset['DO_spread'])>upper_lim),"DO_spread"]
#找出高於upper_lim的資料
```

## Kaggle上的pandas練習

##  資料異常處理
```python=
#將'????'資料設為遺失值
file = 'data.csv'
data = pd.read_csv(open(file), header=0) 
data.where(data != '????', np.nan, inplace=True)
```

```python
#判斷時間間格
x = []
for i in range(1,len(data)):
    x = np.append(x,(data.loc[i,'Date'] - data.loc[i-1,'Date']).seconds)
timedelta = int(stats.mode(x)[0][0]) #單位:sec
#補齊缺少的時間
len_t_NA = 0
if len(np.unique(x))>1: #若時間間格值>1種，則表示時間資料有缺
    #找出缺少資料的時間
    t_all = pd.date_range(data.loc[0,'Date'],data.loc[len(data)-1,'Date'], freq= str(timedelta) +'s')
    t_NA = pd.DataFrame(data = list(set(t_all).difference(set(data['Date']))), columns = ['Date'])
    len_t_NA = len(t_NA)
    col_NA = pd.DataFrame(columns = data.columns[1:],index = range(len_t_NA))
    data_NA = pd.concat([t_NA, col_NA], axis = 1)
    data = pd.concat([data, data_NA])
    data = data.sort_values(by='Date').reset_index(drop=True) #依時間重新排序
```