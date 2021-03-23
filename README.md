# Python練習用リポジトリ

## Pythonのインストール

ダウンロードサイトからダウンロードするのも手っ取り早いけど、Chocolateyを使うと速い。

```
choco install -y python
```

## 基本文法

### 変数宣言
Pythonは動的言語。型は必要ない。

```python
num = 10
str = 'abc'
```

### 関数宣言
def 関数名(引数) : で定義する。インデントが処理のブロックを兼ねる。

```python
def test(num1, num2) :
    if (num1 == num2) :
        return num1 + num2
```

### クラス宣言
class クラス名 :で定義する。

```python
class class1 :
    # コンストラクタは__init__で定義。
    def __init__(self, result) :
        self.result = result
    # デストラクタは__del__で定義
    def __del__() :
        print('インスタンスが破棄されました。')

    def add(self, num1, num2) :
        return self.result + num1 + num2

# インスタンス生成
class1 = class1(10)
# メソッド呼び出し。
class1.add(11, 12)
# インスタンス破棄
del class1
```

### 継承
もちろん継承もできる。class クラス名(親クラス) : で定義する。

```python
class class2(class1) :
    # 何もしないときはpassを書く。
    pass
```

### 分岐
if-elif-elseと条件演算子を用いる。
```python
def branchABC(target) :
    # 文字列比較（完全一致）は == で行う。
    if target == 'ABC' :
        return target + "DEF"
    # else if。記法はifと変わらない。文字列比較（不一致）は !=
    elif target != 'DEF' :
        print('DEFがなくABCでもありません。')
    # if elifすべてに合致しない場合。 else :のみ
    else :
        print('不明な値が入力されました。')

print(branchABC('ABC'))

# 条件演算子。値を返せる。
def branchDEF(target) :
    return target + 'です。' if target == 'DEF' else  'DEFではありません。'

print(branchDEF('DEFG'))

# 同じような分岐はin。not inでまとめてしまうのも有効。
def branchPtn3(target) :
    if target in {'ABC', 'DEF'} :
        return 'ABCかDEFです。'
    elif target not in {'GHI', 'JKL'} :
        return 'GHIかJKLではありません。'

```

### ループ
while、for...inを用いる。
```python
def rangeLoop() :
    rangeCount = 0
    # 回数を指定するループはrange()関数を呼び出す。
    for i in range(5) :
        rangeCount = i
    print(rangeCount)

# enumerate()関数を利用すると対象リストのインデックスをとれる。
def enumerateLoop() :
    targetList = ['abc', 'ghi', 'deaf']
    for idx, i in enumerate(targetList) :
        # ループを抜けるbreakと繰り返しスキップのcontinue
        if i == 'def' :
            break
        elif i == 'ghi' :
            continue
        print ("{0}: {1} ".format(idx, i))
    # ループを抜けたときに行う処理はelse : 処理で書く。
    else :
        print('Loop End')

def loopWhile() :
    targetDict = {'abc' : 1 ,'def' : 2}
    while 'def' == targetDict.keys() :
        print('defがキーに含まれています。')
    else :
        print('defが来ました。')

```

## コレクション
List, Array, Dict, tuple, setを扱える。
List/Array/Dictはミュータブル。破壊的な変更が可能。
tupleはイミュータブル。変更時にはタプル同士、Setどうしで結合する。
set中の値は一意である。

```python
import array
def pracList() :
    # List。Javaと違い組み込み
    list = [1, 2, 3]
    # 値の取得はインデックス指定でとれる。
    print('list index zero value is : ' + str(list[0])) # 1
    # スライス([:])で複数取得も可能。
    print('list index one and two value is : ' + str(list[1:3])) # 2 3
    # 最大、最小、合計、要素数を返す関数もある。
    print('list value max : ' + str(max(list)) )
    print('list value min : ' + str(min(list)) )
    print('list value sum : ' + str(sum(list)) ) 
    print('list value len : ' + str(len(list)) )

def pracArray() :
    # 標準ライブラリのarrayを利用して宣言。第一引数に扱いたい型を指定する。
    # 整数の配列
    intArray = array.array('i', [1, 2, 3])
    # 小数の配列
    floatArray = array.array('f', [1, 2, 3])

    # アクセスや処理はList同様。
    print(intArray[0])
    print(floatArray[0])
    print(sum(floatArray))

def pracDict() :
    # 辞書型。k-vの形式で値を格納する。
    dict = {'First': 1, 'second': 2, 'third': 3}
    # 当然キーを指定して値を取得できる。
    print(dict.get('First'))
    # 辞書型はミュータブル。後から要素を変更可能。(型が無いって怖い…)
    dict['First'] = '1ではない。'
    print(dict.get('First'))
    # 新規追加も可能。
    dict['fourth'] = 4.0
    print(dict.get('fourth'))
    # 当然削除も
    print(dict)
    # キーが含まれるかを判定し、含まれる場合削除
    if 'First' in dict :
        dict.pop('First')
    elif 'second' not in dict :
        pass
    print(dict)
    # 辞書中のすべてのキーはkeys()で取得可能。
    print(dict.keys())
    # すべての値はvalues()で取得可能。
    print(dict.values())

def pracTuple() :
    # (要素,)で宣言可能。1要素でもカンマが必要な点に注意。
    tuple = (2, 4)
    # 不変なので、関数の戻り値としてはListより優れる場合もある。
    return tuple
```

### 関数とlambdaの利用
Pythonではlambdaキーワードで無名関数を定義できる。
無名関数はループができず、１行で記載するという制約があるが
map()やfilter()といった処理の引数に渡すことでコードを完結にできる。

```Python
lambdaExample = lambda x: x* 2

# 関数定義するなら以下と同様。
def lambdaExample2(x):
    return x* 2

print(lambdaExample2(2) == lambdaExample(2))

lis = [1, 2, 3, 4, 5]
list2 = list(map(lambda x: x* 2 , lis))
print(list2)
def mapAndLambda(x) : 
    return x* 2

def checkMapAndLambda(lis) :
    lis = [1, 2, 3, 4, 5]
    list2 = list(map(mapAndLambda , lis))
    return list2

print(checkMapAndLambda(lis))
```