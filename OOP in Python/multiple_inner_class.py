class Computer:
    def __init__(self):
        self.cpu = self.CPU()
        self.ram = self.RAM()

    class CPU:
        def process(self):
            print("Processing data ...")

    class RAM:
        def process(self):
            print("Stroing data ...")

computer=Computer()
computer.cpu.process()
computer.ram.process()