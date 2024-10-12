import numpy as np

TIMES = 2
matrix_types = []
matrix_elements = []
calc_kinds = ['足し算', '引き算', '掛け算']

print(f"{TIMES}つの行列の計算を行います。")
print(f"""
型の入力例:
3行2列の場合

3 2
(3と2の間は半角スペース)

要素の入力例：
[[5 2 ],
[3 6],
[8 9 ]]
という行列を入力する場合

5 2 3 6 8 9
""")

# 要素と型を入力して行列に変換
def input_matrix(matrix_type, matrix_element):
    matrix = np.array(matrix_element).reshape(matrix_type[0], matrix_type[1])

    return matrix

# 行列の足し算を行う
def matrix_add(matrix1, matrix2):
    # 2つの行列の型が同じであれば計算を行う
    if matrix1.shape() == matrix2.shape():
        sum = matrix1 + matrix2
        return sum
    # 計算ができなければ―1を返す
    else:
        return -1

# 行列の引き算を行う
def matrix_sub(matrix1, matrix2):
    # 2つの行列の型が同じであれば計算を行う
    if matrix1.shape() == matrix2.shape():
        difference = matrix1 - matrix2
        return difference
    # 計算ができなければ―1を返す
    else:
        return -1

# 行列の掛け算を行う
def matrix_malti(matrix1, matrix2):
    # 1つ目の行列の列数と2つ目の行列の行数が同じならば計算を行う
    if matrix1.shape()[1] == matrix2.shape()[0]:
        matrix = matrix1 @ matrix2
        return matrix
    # 計算ができなければ―1を返す
    else:
        return -1

for i in range(1, TIMES + 1):
    #行列の型を入力
    matrix_type = list(map(int, input(f"{i}つ目の行列の型：").split(' ')))
    number_of_element = matrix_type[0] * matrix_type[1]
    matrix_types.append(matrix_type)

    while True:
        # 行列の要素を入力
        matrix_element = list(map(int, input(f"{i}つ目の行列の要素：").split(' ')))
        # 要素数が足りていれば、ループを抜ける
        if number_of_element == len(matrix_element):
            break
        print("要素数が少ないです。もういちど入力してください。")
    matrix_elements.append(matrix_element)

# 計算の種類を選択
print("""
計算の種類を選択して、番号を入力してください。
足し算: 0    引き算: 1    掛け算: 2
      """)
while True:
    calc_number = int(input())
    if calc_number == 0 or calc_number == 1 or calc_number == 2:
        break
    else:
        print("0, 1, 2のいずれかを入力してください。")
print(f"{TIMES}つの行列の{calc_kinds[calc_number]}を行います。")

# 1つ目の行列を生成
calculated_matrix = input_matrix(matrix_types[0], matrix_elements[0])
print(calculated_matrix)

# 計算の実行
for j in range(1, TIMES - 1):
    # 計算を行う行列を生成
    calculating_matrix = input_matrix(matrix_types[j], matrix_elements[j])
    # 足し算
    if calc_number == 0:
        calculated_matrix = matrix_add(calculated_matrix, calculating_matrix)
        print(f" + {calculating_matrix}")
    # 引き算
    elif calc_number == 1:
        calculated_matrix = matrix_sub(calculated_matrix,calculating_matrix)
        print(f" - {calculating_matrix}")
    # 掛け算
    elif calc_number == 2:
        calculated_matrix = matrix_malti(calculated_matrix,calculating_matrix)
        print(f"{calculating_matrix}")

print(f" = {calculated_matrix}")
