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
