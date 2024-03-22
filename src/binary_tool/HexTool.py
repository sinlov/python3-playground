class HexTool:
    @staticmethod
    def hex_str_to_bytes(hex_str):
        # type: (str) -> bytes
        return bytes.fromhex(hex_str)

    @staticmethod
    def bytes_to_hex_str(bs):
        # type: (bytes) -> str
        return "".join(["%02X" % b for b in bs])

    @staticmethod
    def bytes_to_hex_str_arr(bs):
        # type: (bytes) -> str
        return "".join(["%02X " % b for b in bs])

    @staticmethod
    def str_to_bytes(target):
        # type: (str) -> bytes
        return bytes(target, encoding="utf8")

    @staticmethod
    def bytes_to_str(bs):
        # type: (bytes) -> str
        return bytes.decode(bs, encoding="utf8")
