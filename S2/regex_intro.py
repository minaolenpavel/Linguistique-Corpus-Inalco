import re 

text ="le Voyez le brick, elle il glisse bien timidement sur le mer de le tropiques, la vache, et les moutons"

exp_det = r"\b(((l|L)('|a|es?))|((d|D)(es?|'))|((u|U)ne?))\b"
exp_inf1grp = r"[a-zA-Zé]*er\b"

exp = exp_det

x = re.findall(exp, text)

print(x)