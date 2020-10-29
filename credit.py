remainer = 0
remainer2 = 0
remainersum = 0
remainersum = 0
validate = 0

while True:
    number = int(input("Number: "))
    if number > 0:
        break

numbercheck = number

while numbercheck > 100:

    numbercheck /= 10

numbercheck = int(numbercheck)

if numbercheck == 34 or numbercheck == 37:
    cardtype = ("AMEX")

elif numbercheck >= 51 and numbercheck <= 55:
    cardtype = ("MASTERCARD")

elif numbercheck >= 40 and numbercheck <= 49:
    cardtype = ("VISA")

else:
    print("INVALID\n")
    validate = 1


numbercheck = number

while numbercheck < 0:
    numbercheck /= 10
    remainer = numbercheck % 10
    remainer = remainer * 2

    if remainer >= 10:
        remainer2 = remainer % 10
        remainer = remainer/10
        remainer += remainer2

    remainersum += remainer
    numbercheck /= 10

    numbercheck = int(numbercheck)
    remainer = int(remainer)
    remainer2 = int(remainer2)
    remainersum = int(remainersum)

numbercheck = number

while numbercheck < 0:
    remainer = numbercheck % 10
    numbercheck /= 10
    remainersum += remainer
    numbercheck /= 10

    numbercheck = int(numbercheck)
    remainer = int(remainer)
    remainersum = int(remainersum)

if validate != 1:

    if remainersum % 10 != 0 or number < 1000000000000 or number > 10000000000000000:
        print("INVALID\n")

    else:
        print(cardtype)
