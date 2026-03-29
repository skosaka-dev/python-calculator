def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("0で割ることはできません")
        return a / b
    else:
        raise ValueError(f"無効な演算子: {op}")


def main():
    print("簡単な計算機")
    print("使い方: 数値 演算子 数値 (例: 3 + 5)")

    expr = input("> ").split()
    if len(expr) != 3:
        print("エラー: 「数値 演算子 数値」の形式で入力してください")
        return

    try:
        a = float(expr[0])
        op = expr[1]
        b = float(expr[2])
        result = calculate(a, op, b)
        print(f"結果: {result}")
    except ValueError as e:
        print(f"エラー: {e}")


if __name__ == "__main__":
    main()