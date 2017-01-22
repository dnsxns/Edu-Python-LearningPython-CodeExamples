while True:
    reply = raw_input('Enter text:')
    if reply == 'stop': break
    print(reply.upper())

while True:
    reply = raw_input('Enter number:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')

while True:
    reply = raw_input('Enter number:')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Bad!' * 8)
    else:
        print(num ** 2)
print('Bye')