f=open("sample.txt","r")
lines=[]
for line in f:
    lines.append(line.strip())
print("contents of the list:")
print(lines)
f.close()