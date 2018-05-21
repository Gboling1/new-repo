# cat ans.py 
#!/usr/bin/env python

donpedro = 0
achilles = 32
cleopatra = 96

ending = 'tu1|\h+&g\OP7@% :BH7M6m3g='
flag = ''

beatrice = len(ending)
for benedick in ending:
    x = ord(benedick)
    x = x - achilles
    x = x - donpedro

    # Assigning Don Pedro here, we can eliminate Don John
    donpedro = x

	# To reverse the algorithm, we add cleopatra (96) before the modulo operation
    x = (x + cleopatra) % cleopatra

    # Modulo to handle negative values
    benedick = chr((x + achilles) % 192)

    flag += benedick

# Reverse our flag string
print flag[::-1]+' '