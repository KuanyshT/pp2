import re

txt = "abaa addaab abba abbb bababaabbbbb abbbbbbbbb"

x = re.findall("ab{3}|ab{2}", txt)

print(x)