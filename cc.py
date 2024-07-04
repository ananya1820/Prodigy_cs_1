print("caeser cipher encoder decoder")
print("to encode provide positive shift value")
print("to decode provide negative shift value")
print()

print("enter your message")
message = input()
print("enter shift value")
shift = int(input())


def cc(mess,shif):
    cc = ""

    LASTCHAR = ord("Z")
    FIRSTCHAR = ord("A")
    CHAR_RANGE = LASTCHAR-FIRSTCHAR+1

    for i in message.upper():
        if i.isalpha():
            char = ord(i)
            newchar = char+shift

            if newchar>LASTCHAR:
                newchar -= CHAR_RANGE

            if newchar < FIRSTCHAR:
                newchar +=CHAR_RANGE

            res = chr(newchar)

            cc += res
        else:
            cc += i

    print(cc)


cc(message,shift)


