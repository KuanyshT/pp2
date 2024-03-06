import re

txt = "Hi abba, hi arara , abbaa aaa"

x = re.findall("ab*", txt)
print(x)