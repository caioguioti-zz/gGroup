f_Base = open("C:\Downloads\mfa.base")
f_Current = open("C:\Downloads\mfa")
GAM= ""

def check():
    base = []

    for line in f_Base:
        line.strip()
        base.append(line)

    for line in f_Current:
        if line not in base:
            print(line)


check()
