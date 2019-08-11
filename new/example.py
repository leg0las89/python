fname = " viktor "
fname = fname.strip()
lname = "kozinskiy"
print(f"Hello {fname.title()}\n {lname.title()}")

slist=["first", "second", "third"]
slist.append(4)
print(slist[-1])
print(slist)

del slist[-1]

pop_list=slist.pop(0)

print(slist)
print(pop_list)
