import dataclasses
import operator as op
from typing import Callable, Iterable
from functools import partial, reduce

MAX_PACKETS = 1000
VERSION_SIZE = 3
TYPE_ID_SIZE = 3
HEADER_SIZE = VERSION_SIZE + TYPE_ID_SIZE


def solve(data):
    answers = {}
    # answers["a"] = solve_a(data)
    answers["b"] = solve_b(data)
    return answers


def solve_a(encoded_packets):
    def get_nested_versions(packet, versions=[]):
        new_versions = [*versions, packet.version]

        if packet.type_id == 4:
            return new_versions
        else:
            for subpacket in packet.subpackets:
                new_versions += get_nested_versions(subpacket, [])

        return new_versions

    answer_a = 0

    for encoded_packet in encoded_packets:
        packet = decode_hexadecimal_packet(encoded_packet)
        answer_a += sum(get_nested_versions(packet, versions=[]))

    return answer_a


def solve_b(encoded_packets):
    for encoded_packet in encoded_packets:
        packet = decode_hexadecimal_packet(encoded_packet)
        return packet.value


def decode_hexadecimal_packet(packet_hex):
    packet_bits = "".join(map(char2bin, packet_hex))
    packet, _ = decode_body(*decode_header(packet_bits))
    return packet


@dataclasses.dataclass()
class Packet:
    version: int
    type_id: int

    def __mul__(self, other):
        return self.apply(op.mul, other)

    def __add__(self, other):
        return self.apply(op.add, other)

    def __sub__(self, other):
        return self.apply(op.sub, other)

    def __gt__(self, other):
        return self.apply(op.gt, other)

    def __lt__(self, other):
        return self.apply(op.lt, other)

    def __eq__(self, other):
        return self.apply(op.eq, other)

    def apply(self, operation, other):
        return operation(self.value, other.value)


@dataclasses.dataclass()
class LiteralPacket(Packet):
    value: int


@dataclasses.dataclass()
class OperatorPacket(Packet):
    length_type_id: int
    subpackets: Iterable[Packet]
    operation: Callable = dataclasses.field(init=False)

    operations = {
        0: partial(reduce, op.add),
        1: partial(reduce, op.mul),
        2: min,
        3: max,
        5: partial(reduce, op.gt),
        6: partial(reduce, op.lt),
        7: partial(reduce, op.eq),
    }

    def __post_init__(self):
        self.operation = self.operations[self.type_id]

    @property
    def value(self):
        return int(self.operation([p.value for p in self.subpackets]))


def decode_header(packet_bits):
    header_bits = packet_bits[:HEADER_SIZE]
    body_bits = packet_bits[HEADER_SIZE:]
    version = int(bin2char(header_bits[:VERSION_SIZE].zfill(4)))
    type_id = int(bin2char(header_bits[VERSION_SIZE:].zfill(4)))

    if type_id == 4:
        packet = LiteralPacket(version, type_id, None)
    elif body_bits:
        length_type_id = int(body_bits[0], base=2)
        body_bits = body_bits[1:]
        packet = OperatorPacket(version, type_id, length_type_id, [])
    else:
        return Packet(version, type_id), ""

    return packet, body_bits


def decode_body(packet, body_bits):
    if not body_bits:
        return Packet(None, None), ""

    if packet.type_id == 4:
        # Literal packet
        value = []

        # Decode each 4-bit integer chunk
        for i in range(len(body_bits) // 5):
            chunk_bits = body_bits[i * 5 : (i + 1) * 5]
            value.append(chunk_bits[1:])
            remaining_bits = body_bits[(i + 1) * 5 :]

            if chunk_bits[0] == "0":
                break

        value = "".join(value)
        packet = dataclasses.replace(packet, value=int(value, base=2))
        return packet, remaining_bits

    else:
        # Operator packet
        subpackets = []

        if packet.length_type_id == 0:
            n_subpackets = MAX_PACKETS
            n_bits_remaining = int(body_bits[:15], base=2)
            remaining_bits = body_bits[15 : 15 + n_bits_remaining]
            leftover_bits = body_bits[15 + n_bits_remaining :]
        elif packet.length_type_id == 1:
            n_subpackets = int(body_bits[:11], base=2)
            remaining_bits = body_bits[11:]
            leftover_bits = ""
        else:
            raise Exception(f"Unexpected length_type_id: {packet.length_type_id}")

        # Decode the subpackets
        for _ in range(n_subpackets):
            subpacket, remaining_bits = decode_body(*decode_header(remaining_bits))
            subpackets.append(subpacket)

            if not remaining_bits:
                break

        packet = dataclasses.replace(packet, subpackets=subpackets)

        return packet, leftover_bits + remaining_bits


def char2hex(x, base=16):
    return int(str(x), base=base)


def hex2bin(x):
    return f"{x:04b}"


def char2bin(x):
    return hex2bin(char2hex(x))


def bin2hex(x):
    return char2hex(x, base=2)


def hex2char(x):
    return hex(x).upper()[2:]


def bin2char(x):
    return hex2char(bin2hex(x))
