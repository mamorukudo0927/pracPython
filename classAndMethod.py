# コメント。 #から初めて1行が認識される。

# 変数宣言。型はない。初期化するなら任意の値も
a = 'Hello world'
print(a) # Hello world
a = 1
print(a) # 1

# 関数宣言。 def 関数名 (引数) :で定義。
def addNumber(num1, num2) :
    return num1 + num2

# 呼び出しは名称と引数を合わせるだけ
print(addNumber(1 ,2)) # 3

# class宣言もできる。
"""
DocString。ダブルクォートで囲った範囲に適応される。

このクラスは共通処理を提供しています。
"""
class BasicUtil :
    # コンストラクタ。インスタンス生成時に呼び出される。
    def __init__(self , num) :
        self.num = num
    
    # デストラクタ。インスタンス破棄時に呼び出される。
    def __del__(self) :
        self.num = 0
        print('インスタンスを破棄しました。')

    # 引数のうち1つめはselfという名称を指定する。
    def concatStr(self, target, param) :
        return self.num + target + param

    def concatNum(self, target, param) :
        return target + param
#　クラス内メソッドはインスタンス生成を行って呼び出す。
util = BasicUtil(10)
print(util.concatNum(20,30))

# インスタンスの破棄
del util

# クラスの継承も可能
class utilTest(BasicUtil) :
    def __init__(self, num) :
        self.num = num

    # スーパークラスのメソッド呼び出し。
    @classmethod    
    def concatNumTest(cls) :
        print(super().concatNum(15, 10, 20))

test = utilTest(15)
print(test.concatNumTest())
