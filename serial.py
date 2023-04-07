"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start):
        """ Initilize the number generator by a starting number"""
        
        self.start = self.next = start
        
    def __repr__(self):

        return f"The generator is initilized at start = {self.start}, the next number is = {self.next}"

    def generate(self):
        """ return serial number"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        self.next = self.start
        
    

    