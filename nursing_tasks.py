# nursing_tasks.py — 护理任务清单（带文件保存）
# Week 2 练习 3：列表 / 字典 / JSON 文件 / 异常处理

import json

FILE = "nursing_tasks.json"

def load():
    try:
        return json.load(open(FILE, encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # 文件不存在时不崩溃，返回空列表

def save(tasks):
    json.dump(tasks, open(FILE, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

tasks = load()
print(f"=== 护理任务清单 === (已加载 {len(tasks)} 条)")

while True:
    print("\n  1. 添加  2. 完成  3. 查看  0. 退出")
    try:
        choice = input("请选择: ").strip()
        if choice == "1":
            t = input("  任务内容: ").strip()
            if t:
                tasks.append({"task": t, "done": False}); save(tasks)
                print("  ✅ 已保存")
        elif choice == "2":
            pending = [t for t in tasks if not t["done"]]
            if not pending:
                print("  没有待完成的任务")
            else:
                for i, t in enumerate(pending, 1): print(f"  {i}. {t['task']}")
                pending[int(input("  输入编号: ")) - 1]["done"] = True
                save(tasks); print("  ✅ 已标记完成")
        elif choice == "3":
            if not tasks: print("  清单为空")
            for i, t in enumerate(tasks, 1):
                print(f"  {'✓' if t['done'] else '○'} {i}. {t['task']}")
        elif choice == "0":
            print("再见！"); break
        else:
            print("  ⚠️ 请输入 0–3")
    except (ValueError, IndexError):
        print("  ⚠️ 编号无效，请重试")
    except Exception as e:
        print(f"  ⚠️ 出错了: {e}")
