# safe_calculator.py — 安全的药物剂量计算器
# Week 2 练习 4：try/except / 除零保护 / 非数字保护 / quit 退出
# 场景：护士快速计算给药剂量，输入错误不崩溃

print("=== 安全的药物剂量计算器 ===")
print("支持运算：+  -  *  /")
print("输入格式：数字 运算符 数字  （例：500 / 250）")
print("输入 quit 退出")
print("-" * 38)

while True:
    try:
        expr = input("\n请输入计算式: ").strip()

        if expr.lower() == "quit":
            print("再见！")
            break

        parts = expr.split()
        if len(parts) != 3:
            print("  ⚠️ 格式错误，请输入：数字 运算符 数字")
            continue

        a  = float(parts[0])
        op = parts[1]
        b  = float(parts[2])

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op in ("*", "x", "×"):
            result = a * b
        elif op in ("/", "÷"):
            if b == 0:
                print("  ⚠️ 除数不能为 0")
                continue
            result = a / b
        else:
            print(f"  ⚠️ 不支持运算符「{op}」，请用 + - * /")
            continue

        print(f"  结果：{a} {op} {b} = {result:.4g}")

    except ValueError:
        print("  ⚠️ 请输入有效数字，不能包含文字")
    except Exception as e:
        print(f"  ⚠️ 出错了: {e}")
