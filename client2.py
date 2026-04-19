import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)

base1 = communicator.stringToProxy("SimplePrinter1:tcp -h 3.239.175.168 -p 5678")
base2 = communicator.stringToProxy("SimplePrinter2:tcp -h 3.239.175.168 -p 5678")
printer1 = Demo.PrinterPrx.checkedCast(base1)
printer2 = Demo.PrinterPrx.checkedCast(base2)
if (not printer1) or (not printer2):
    raise RuntimeError("Invalid proxy")

rep = printer1.printString("Hello World from printer1!")
print(rep)
rep = printer2.printString("Hello World from printer2!")
print(rep)

rep = printer1.reverseString("Hello from printer1!")
print("reverseString (printer1):", rep)
rep = printer2.reverseString("Hello from printer2!")
print("reverseString (printer2):", rep)

result = printer1.isPalindrome("arara")
print("isPalindrome printer1 ('arara'):", result)
result = printer2.isPalindrome("Hello")
print("isPalindrome printer2 ('Hello'):", result)

communicator.destroy()
