import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print(s)
        return s + "*"

    def reverseString(self, s, current=None):
        result = s[::-1]
        print(result)
        return result

    def isPalindrome(self, s, current=None):
        cleaned = s.replace(" ", "").lower()
        result = cleaned == cleaned[::-1]
        print(f"'{s}' is palindrome: {result}")
        return result

communicator = Ice.initialize(sys.argv)

adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 5678")
object = PrinterI()
adapter.add(object, communicator.stringToIdentity("SimplePrinter"))
adapter.activate()

communicator.waitForShutdown()