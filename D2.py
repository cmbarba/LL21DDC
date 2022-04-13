## Day 2 Challenge ##

# Provided

name = '  Dot  '

# Work

sname = name.strip()
uname = sname.upper()
print("#" + uname + "!")

#Alternative way, chaining methods together

name2 = name.upper().strip()
print(f"#{name2}!")
