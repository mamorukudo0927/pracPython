"""
Python基礎第二回。条件分岐とループの記法。
"""

# if文の例。 if 比較条件式 : trueの場合の処理。
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

print(branchPtn3('ABCD'))

"""
ループ処理。標準関数を利用して処理を記述する事が多い。
"""
def rangeLoop() :
    rangeCount = 0
    # 回数を指定するループはrange()関数を呼び出す。
    for i in range(5) :
        rangeCount = i
    print(rangeCount)

rangeLoop()

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

enumerateLoop()

def loopWhile() :
    targetDict = {'abc' : 1 ,'def' : 2}
    while 'def' == targetDict.keys() :
        print('defがキーに含まれています。')
    else :
        print('defが来ました。')

loopWhile()