# beginning of 3rd question
message = input("Cümle ")
usinp = input("aranacak kelime: ")
index = message.find(usinp)
a = len(usinp)
for i in range(index-1, index+a+1):
    print(message[i], end='')