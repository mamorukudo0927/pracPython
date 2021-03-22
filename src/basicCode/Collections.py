"""
Pythonにおけるコレクションの宣言や扱い方を練習。
"""
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

pracList()

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

pracArray()

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
pracDict()