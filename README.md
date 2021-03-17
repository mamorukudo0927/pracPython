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

