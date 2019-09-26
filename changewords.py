def changewords(words):
    checkword=("why", "what", "who", "did", "how")
    capital=words.title()
    if words.startswith(checkword):
        return f"{capital}?"
    else:
        return f"{capital}."
extra=[]
while True:
    word=input("please enter any words: ")
#    word+=print("Type /end if you wanna finish")
    if word == "/end":
        break
    else:
        extra.append(changewords(word))

print("\n".join(extra))
