class Projector(object):
    def __init__(self, network_address):
        self.address = network_address
        self._power_status = read_from_projector("POWER", network_address)

    def power_on(self):
        send_command_to_projector(network_address)
        self._power_status = True

    def power_off(self):
        self._power_status = False
        

proj_2b7 = Projector("118.139.125.169")
proj_1b1 = Projector("118.139.125.122")

del proj_2b7

proj_2b7.power_on()

proj_2b7.power_status = True