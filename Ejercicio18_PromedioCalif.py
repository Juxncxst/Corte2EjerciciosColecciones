cal = {}
while True:
    e = input()
    if e.lower()=="fin":
        break
    n, v = e.split(":")
    cal[n.strip()] = float(v.strip())
vals = cal.values()
print(sum(vals)/len(vals) if len(vals)>0 else 0)
