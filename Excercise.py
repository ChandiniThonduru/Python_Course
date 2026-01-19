'''Sentence:    nothing is impossible to a willing heart
Encryption:  ntraehg ni lliwaotelb is s opmisig nihto

Sentence:   GOOGLE IS A SEARCH ENGINE
Encryption: GENIGN EH C RAESAS IELGOO

Sentence:   Talk Is Cheap Show Me The Code
Encryption: Tedo Ce hTeMw ohSp ae hCs Ikla
'''

x = input("Enter String :")

updated_str = str((x[0] + x[len(x):0:-1])).replace(" ", "")
print(updated_str)
out = ""
j = 0
for i in range(0, len(x)):
    if x[i] == " ":
        out += " "
    else:
        out += updated_str[j]
        j = j + 1

print(out)
