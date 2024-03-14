nric = input('Enter an NRIC number: ')
validity = True
# Type your code below
validity &= (nric[0] in "STFG")
validity &= (nric[1:8].isdigit())
validity &= (len(nric)== 9) and (nric[8].isalpha())
toprint = "invalid"

dw= "2765432"
if validity:
  sn = nric[1:8]
  products = sum([int(dw[i])*int(sn[i]) for i in range(len(sn))]) #too long to do without loops :(
  if nric[0] in "TG":
      products += 4
  products %= 11
  STtable = "JZIHGFEDCBA"
  FGtable = "XWUTRQPNMLK"
  if nric[0] in "ST":
      validity &= (nric[-1] == STtable[products])
  else:
      validity &= (nric[-1] == FGtable[products])

print("NRIC is "+ (int(not(validity)) * toprint[0:2]) + toprint[2:]+ ".")