# Claude Camp Week 2 — Python 自动化 + 异常处理
**主题：护理工作场景 Python 练习**

本周 4 个练习均以**医疗护理**为应用场景，运用 Python 列表、字典、循环与异常处理实现实用工具。

---

## 练习 1：患者花名册管理器 `patient_roster.py`

护理站快速录入、查询、删除患者基本信息。

**涉及知识：** 字典、while 循环、try/except 异常处理

**运行方法：**
```bash
python patient_roster.py
```
**操作说明：** 按提示输入 1（添加）/ 2（查询）/ 3（删除）/ 4（查看全部）/ 0（退出）

---

## 练习 2：护理记录词频统计器 `word_counter.py`

输入一段护理记录文字，统计每个词出现的次数，按频率从高到低排序。

**涉及知识：** 字典、for 循环、sorted() 排序、忽略大小写

**运行方法：**
```bash
python word_counter.py
```
**操作说明：** 输入文字后直接按 Enter（空行）结束，程序自动输出词频统计结果

---

## 练习 3：护理任务清单（带文件保存）`nursing_tasks.py`

护士当班任务管理，数据保存到本地 `nursing_tasks.json`，程序重启后数据不丢失。

**涉及知识：** 列表、字典、JSON 文件读写、FileNotFoundError 异常处理

**运行方法：**
```bash
python nursing_tasks.py
```
**操作说明：** 按提示选择 1（添加）/ 2（完成）/ 3（查看）/ 0（退出）

---

## 练习 4：安全的药物剂量计算器 `safe_calculator.py`

支持 + - * / 四则运算，输入除数为 0、非数字时不崩溃，输入 quit 优雅退出。

**涉及知识：** try/except、ValueError、ZeroDivisionError、while 循环

**运行方法：**
```bash
python safe_calculator.py
```
**操作说明：** 输入格式为 `数字 运算符 数字`，例如 `500 / 250`，输入 `quit` 退出

---

## 运行环境

- Python 3.x
- 无需安装第三方库（仅用 Python 标准库 `json`）

---

*Healthcare Nursing Tools — Claude Camp W2 by Ning*
