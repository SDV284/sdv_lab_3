import re

t = str(input("Введіть рядок: "))

t = re.split("[,. !?]", t)
t.sort(key=len)
l = " ".join(t)

print("Слова в порядку неспадання:", l)