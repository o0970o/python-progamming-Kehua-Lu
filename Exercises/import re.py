import re

# 输入文本字符串
text = "29535123p48723487597645723645"

# 使用正则表达式查找以相同数字开头和结尾的子字符串
pattern = r'(\d)(.*\d)?\1'
matches = re.finditer(pattern, text)

# 存储匹配结果的列表
matching_strings = []

# 遍历所有匹配项并将它们存储在列表中
for match in matches:
    matching_strings.append(match.group(0))

# 打印所有首尾相同数字的子字符串
for matching_string in matching_strings:
    print(matching_string)
