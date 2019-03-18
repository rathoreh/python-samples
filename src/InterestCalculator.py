from time import sleep

print(">>>>> Interest Calculator <<<<<\n")

principal = float(input('Enter Principal: '))
roi = float(input("Enter Rate of Interest: "))
yrs = int(input("No. of Years: "))

print("\nCalculating interest...")

#Sleep is in seconds...
sleep(1)

maturityAmt = principal * (1 + (roi/100) * yrs) 

interest = maturityAmt - principal

print("\nMaturity amount will be %0.2f on Principal of %0.2f for %i years @%0.2f%%" %(maturityAmt, principal, yrs, roi))
print("earning interest of %0.2f" %interest)