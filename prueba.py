def timeConversion(s):
    hora=(s[-2:])
    if hora=="PM":
        hora_nueva=str(int(s[:2])+12)
        s=hora_nueva+s[2:]
    return s[:-2]
timeConversion("07:05:45PM")