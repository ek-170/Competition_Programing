"""
数値標準入力
"""
# 1つの整数を変数へ代入
a = int(input())
# 空白値区切りの整数を変数へ代入
a, b = map(int,input().split())
# 空白値区切りの整数をListへ代入  
l = list(map(int,input().split()))
# 複数行の空白値区切りの整数値を二次元配列へ代入
ll = [int(input()) for i in range(行数)]
"""
文字列標準入力
"""