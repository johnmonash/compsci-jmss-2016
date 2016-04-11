import socket


def create_projector(setting):
    klass = getattr(__name__, setting['class'])
    if 'password' in setting:
        return klass(setting['address'], setting['password'])
    else:
        return klass(setting['address'])


def create_projectors(projector_settings):
    projectors = []
    for setting in projector_settings:
        projectors.append(create_projector(setting))
    return projectors


class ProjectorException(Exception):
    pass


class GenericNetworkProjector(object):
    def __init__(self, address):
        self.power = None
        self.source_id = None

    def power_on(self):
        self.power = True

    def power_off(self):
        self.power = False

    def set_source(self, source_id):
        self.source_id = source_id


class EpsonProjector(GenericNetworkProjector):
    PORT = 3629
    HANDSHAKE_STRING = 'ESC/VP.net\x10\x03\x00\x00\x00\x00'
    HANDSHAKE_STRING_PW = 'ESC/VP.net\x10\x03\x00\x00\x00\x01\x01\x01'
    HANDSHAKE_RESPONSE = b'ESC/VP.net\x10\x03\x00\x00 \x00'

    def __init__(self, address, password=None):
        super().__init__(address)

        self.sock = socket.socket()
        #self.sock.setblocking(False)
        self.sock.connect((address, self.PORT))
        if password:
            handshake = self.HANDSHAKE_STRING_PW + password
        else:
            handshake = self.HANDSHAKE_STRING
        self.sock.send(bytes(handshake, "UTF-8"))
        response = self.sock.recv(4096)
        if response != self.HANDSHAKE_RESPONSE:
            raise ProjectorException
        #TODO - read power status and source ?

    def power_on(self):
        self.sock.send(bytes("PWR ON\r", "UTF-8"))
        response = self.sock.recv(4096)
        super().power_on()

    def power_off(self):
        self.sock.send(bytes("PWR OFF\r", "UTF-8"))
        response = self.sock.recv(4096)
        super().power_off()

    def set_source(self, source_id):
        self.sock.send(bytes("SOURCE {id}\r".format(id=source_id), "UTF-8"))
        response = self.sock.recv(4096)
        #TODO - check success
        super().set_source(source_id)

    def get_source(self):
        self.sock.send(b"SOURCE?\r")
        response = self.sock.recv(4096)
        return response
        #super().set_source(source_id)


    def __del__(self):
        self.sock.close()
