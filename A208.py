pin = input().split("WUB")
for i in pin:
    if i == '':
        pin.remove(i)

pout = ' '.join(pin)

print(pout)