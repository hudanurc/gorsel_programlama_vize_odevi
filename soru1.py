# beginning of 1st question
def control(str):
    count = 0
    for ch in str:
        if ch == '@':
            count = count + 1

    if count == 1:
        return True
    else:
        return False


mail = input('Maili yazın : ')
if (control(mail) == True):
    print('True')
else:
    print('False')
