message = input()

final1 = sum(1 for c in message if c.isupper())
final2 = sum(1 for c in message if c.islower())

if final1 <= final2:
    print(message.lower())
else:
    print(message.upper())