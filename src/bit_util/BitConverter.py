import struct


class BitConverter:
    _converter_big = True

    def __init__(self):
        BitConverter._converter_big = True
        pass

    @staticmethod
    def _check_little_endian():
        val = 0x12345678
        pk = struct.pack('i', val)
        hex_pk = hex(pk[0])

        if hex_pk == '0x78':
            return True
        elif hex_pk == '0x12':
            return False

    @staticmethod
    def is_big_endian():
        # type: () -> bool
        return not BitConverter._check_little_endian()

    @staticmethod
    def get_bytes_bool(val):
        # type: (bool) -> bytes
        if BitConverter._check_little_endian():
            if BitConverter._converter_big:
                return struct.pack('>b', val)
            else:
                return struct.pack('<b', val)
        else:
            if BitConverter._converter_big:
                return struct.pack('>b', val)
            else:
                return struct.pack('<b', val)

    @staticmethod
    def to_bool(data):
        # type: (bytes) -> bool
        if BitConverter._check_little_endian():
            if BitConverter._converter_big:
                return struct.unpack('>?', data)[0]
            else:
                return struct.unpack('<?', data)[0]
        else:
            if BitConverter._converter_big:
                return struct.unpack('>?', data)[0]
            else:
                return struct.unpack('<?', data)[0]

    @staticmethod
    def get_bytes_short(val):
        # type: (float) -> bytes
        if BitConverter._check_little_endian():
            if BitConverter._converter_big:
                return struct.pack('>h', val)
            else:
                return struct.pack('<h', val)
        else:
            if BitConverter._converter_big:
                return struct.pack('>h', val)
            else:
                return struct.pack('<h', val)

    @staticmethod
    def to_short(data):
        # type: (bytes) -> float
        if BitConverter._check_little_endian():
            if BitConverter._converter_big:
                return struct.unpack('>h', data)[0]
            else:
                return struct.unpack('<h', data)[0]
        else:
            if BitConverter._converter_big:
                return struct.unpack('>h', data)[0]
            else:
                return struct.unpack('<h', data)[0]

    @staticmethod
    def get_bytes_int(val):
        # type: (float) -> bytes
        if BitConverter._check_little_endian():
            if BitConverter._converter_big:
                return struct.pack('>i', val)
            else:
                return struct.pack('<i', val)
        else:
            if BitConverter._converter_big:
                return struct.pack('>i', val)
            else:
                return struct.pack('<i', val)

    @staticmethod
    def to_int(data):
        # type: (bytes) -> float
        if BitConverter._check_little_endian():
            if BitConverter._converter_big:
                return struct.unpack('>i', data)[0]
            else:
                return struct.unpack('<i', data)[0]
        else:
            if BitConverter._converter_big:
                return struct.unpack('>i', data)[0]
            else:
                return struct.unpack('<i', data)[0]

    @staticmethod
    def get_bytes_str_utf8(val: str):
        return val.encode('utf-8', errors='strict')

    @staticmethod
    def to_str_utf8(data):
        # type: (bytes) -> str
        return data.decode('utf-8')
