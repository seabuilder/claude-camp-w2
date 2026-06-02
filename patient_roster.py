# patient_roster.py — 患者花名册管理器
# Week 2 练习 1：字典 / 循环 / 条件 / 异常处理
# 场景：护理站快速录入、查询、删除患者基本信息

patients = {}  # 用字典存储：{ 姓名: {bed, date} }

def add_patient():
    name = input("患者姓名: ").strip()
    bed  = input("病床号:   ").strip()
    date = input("入院日期 (如 2026-05-11): ").strip()
    patients[name] = {"bed": bed, "date": date}
    print(f"  ✅ 已添加: {name} — 床位 {bed}")

def search_patient():
    name = input("查询患者姓名: ").strip()
    if name in patients:
        p = patients[name]
        print(f"  姓名: {name} | 床位: {p['bed']} | 入院: {p['date']}")
    else:
        print("  ❌ 未找到该患者")

def delete_patient():
    name = input("删除患者姓名: ").strip()
    if name in patients:
        del patients[name]
        print(f"  ✅ 已删除: {name}")
    else:
        print("  ❌ 未找到该患者")

def show_all():
    if not patients:
        print("  花名册为空")
    else:
        print(f"  共 {len(patients)} 名患者:")
        for name, info in patients.items():
            print(f"    {name:<12} 床位 {info['bed']:<6} 入院 {info['date']}")

print("=== 患者花名册管理器 ===")
while True:
    print("\n  1. 添加患者  2. 查询患者  3. 删除患者  4. 查看全部  0. 退出")
    try:
        choice = input("请选择操作: ").strip()
        if   choice == "1": add_patient()
        elif choice == "2": search_patient()
        elif choice == "3": delete_patient()
        elif choice == "4": show_all()
        elif choice == "0": print("再见！"); break
        else: print("  ⚠️ 请输入 0–4")
    except Exception as e:
        print(f"  ⚠️ 输入有误，请重试 ({e})")
