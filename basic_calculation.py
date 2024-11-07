import numpy as np
import sys

TIMES = 2
matrix_types = []
matrix_rows = []
matrix_elements = []
calc_kinds = ['足し算', '引き算', '掛け算']

print(f"{TIMES}つの行列の計算を行います。")
print("""
型の入力例:
3行2列の場合

3 2
(3と2の間は半角スペース)

要素の入力例：
[[5 2 ],
[3 6],
[8 9 ]]
という行列を入力する場合

1行目: 5 2 3
2行目: 6 8 9
""")

# 多重リストをnumpy配列に変換
def input_matrix(matrix_element):
    matrix = np.array(matrix_element)
    return matrix


# 行列の足し算を行う
def matrix_add(matrix1, matrix2):
    try:
        sum = matrix1 + matrix2
    # 計算ができなければNoneを返す
    except ValueError:
        return None
    else:
        return sum


# 行列の引き算を行う
def matrix_sub(matrix1, matrix2):
    try:
        difference = matrix1 - matrix2
    # 計算ができなければNoneを返す
    except ValueError:
        return None
    else:
        return difference


# 行列の掛け算を行う
def matrix_malti(matrix1, matrix2):
    try:
        matrix = np.dot(matrix1, matrix2)
    # 計算ができなければNoneを返す
    except ValueError:
        return None
    else:
        return matrix

# メインの処理
if __name__ == "__main__":
    for i in range(1, TIMES + 1):
        #行列の型を入力
        while True:
            try:
                matrix_type = list(map(int, input(f"{i}つ目の行列の型：").split(' ')))
            except ValueError:
                print("入力例に従って入力して下さい。")
            # 正しい形式で型が入力されていたらループを抜ける
            else:
                if len(matrix_type) == 2 and matrix_type[0] >= 1 and matrix_type[1] >= 1:
                    break
                # 形式に沿っていなければ再入力
                else:
                    print("2つの自然数を入力してください。")

        number_of_element = matrix_type[0] * matrix_type[1]
        matrix_types.append(matrix_type)

        counter = 0
        while True:
            # 行列の要素を入力
            try:
                matrix_element = list(map(float, input(f"{i}つ目の行列の{counter + 1}行目の要素：").split(' ')))
            except ValueError:
                print("数字を入力してください")
            else:
                # 要素数が足りている場合
                if matrix_type[1] == len(matrix_element):
                    matrix_rows.append(matrix_element)
                    counter += 1
                    # 行数が足りている場合ループを抜ける
                    if matrix_type[0] == len(matrix_rows):
                        inputed_matrix = matrix_rows.copy()
                        matrix_elements.append(inputed_matrix)
                        matrix_rows.clear()
                        break
                else:
                    print("要素数が少ないです。もういちど入力してください。")
        print(matrix_elements[i-1])

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
    calculated_matrix = input_matrix(matrix_elements[0])
    print(calculated_matrix)

    # 計算の実行
    for j in range(1, TIMES):
        # 計算を行う行列を生成
        calculating_matrix = input_matrix(matrix_elements[j])
        # print(f"calculating:{calculating_matrix}")
        try:
            # 足し算
            if calc_number == 0:
                calculated_matrix = matrix_add(calculated_matrix, calculating_matrix)
            # 引き算
            elif calc_number == 1:
                calculated_matrix = matrix_sub(calculated_matrix,calculating_matrix)
            # 掛け算
            elif calc_number == 2:
                calculated_matrix = matrix_malti(calculated_matrix,calculating_matrix)
        # 計算ができなかったら終了
        except TypeError:
            print(f"計算に失敗しました。")
            sys.exit()
        else:
            # 足した数の表示
            if calc_number == 0:
                print(" + ")
            # 引いた数の表示
            elif calc_number == 1:
                print(" - ")
            # 掛けた数の表示
            elif calc_number == 2:
                print(" @ ")
            print(calculating_matrix)

    # 計算に失敗したらエラー文を表示
    if calculated_matrix.any() == False:
        print("計算に失敗しました。")
    # 成功したら計算結果を表示
    else:
        print(f" = \n{calculated_matrix}")