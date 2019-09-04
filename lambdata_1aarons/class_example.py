"""
Sample class created for 312 assignment purposes.
"""


class Desktop_Computer:
    """Attributes of a desktop computer's hardware."""

    def __init__(self):
        self.cpu = "Intel"
        self.mobo = "Asus"
        self.gpu = "Integrated"
        self.monitor = "Dell"
        self.mouse = "Anker"
        self.powersupply = "Corsair"
        self.ram = "Crucial"

    def print_cpu_mobo:
        """Prints the motherboard and cpu combination."""
        print(f'This is a {self.cpu} CPU on a {self.mobo} motherboard.')

    def hardware_values:
        """Assigns values to the types of hardware if available."""
        self.ram_amount = 16
        self.powersupply_amount = 500


class Gift_Computer(Desktop_Computer):
    """Child class for a computer given as a gift."""

    def print_cpu_mobo(self):
        print(f'Congratulations! I got you a {self.cpu} CPU on a {self.mobo}
              motherboard!')

    def __init__(self):
        super(Desktop_Computer, self).__init__()
        self.cpu = "AMD"
        self.gpu = "Nvidia"
