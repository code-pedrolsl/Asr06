import sys, Ice
import Demo

communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:tcp -h 3.239.175.168 -p 5678")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

rep = printer.printString("Hello World!")
print("printString retornou:", rep)

rep = printer.reverseString("Hello World!")
print("reverseString retornou:", rep)

result = printer.isPalindrome("arara")
print("isPalindrome('arara') retornou:", result)

result = printer.isPalindrome("Hello")
print("isPalindrome('Hello') retornou:", result)

communicator.destroy()
