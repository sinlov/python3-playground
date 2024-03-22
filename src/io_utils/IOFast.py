from typing import IO


class IOFast:
    def __init__(self):
        pass

    @staticmethod
    def _io_to_utf8(io_out: IO) -> str:
        return str(io_out.read(), "utf-8")

    @staticmethod
    def _io_to_utf8_strip(io_out: IO) -> str:
        return str(io_out.read(), "utf-8").replace("\n", "").replace("\r", "").strip()
