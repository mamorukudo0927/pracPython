"""Python基礎学習。 ラムダ式と標準関数の利用。
    Python基礎学習。標準関数の利用によるコレクションの処理
    およびラムダ式の利用方法を学習する。
    @author mamoruKudo0927
"""

"""ラムダ式の宣言例を示す関数。
lambda 引数: 処理で記述する。
以下は引数を一つ受け、*2した値を返却するラムダ式
"""
lambdaExample = lambda x: x* 2

# 関数定義するなら以下と同様。
def lambdaExample2(x):
    return x* 2

print(lambdaExample2(2) == lambdaExample(2)) # 同値なのでtrue

"""標準関数とLambdaを組み合わせる例
    lambdaの主な使いどころは、map()やfilter()等に渡す関数として利用する。
"""
lis = [1, 2, 3, 4, 5]
list2 = list(map(lambda x: x* 2 , lis))
print(list2)

# 普通に関数でやるなら
def mapAndLambda(x) : 
    return x* 2

def checkMapAndLambda(lis) :
    lis = [1, 2, 3, 4, 5]
    list2 = list(map(mapAndLambda , lis))
    return list2

print(checkMapAndLambda(lis))

"""
lambda式は1行でしか記載できず、forループは行えない
条件分岐は可能
"""
# 奇数偶数判定
list_1 = [0,1,2,3,4,5,6,7,8,9,10]
evenCheck = lambda x: "Even" if x%2 == 0 else "Odd"
print(list(map(evenCheck, list_1)))

# FizzBuzz
fizzBuzzCheck = lambda x: "FizzBuzz" if x%3 == 0 and x%5 == 0 else "Fizz" if x%3 == 0 else "Buzz" if x%5 == 0 else x

for i in range(101) :
    print(str(fizzBuzzCheck(i)))