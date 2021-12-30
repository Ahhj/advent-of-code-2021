import pytest

from aoc2021.solutions.day16.preprocess import preprocess
from aoc2021.solutions.day16.solve import *

EXAMPLE_DATA = """
"""


@pytest.mark.parametrize(
    "x, expected",
    [
        ("0", 0),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
        ("A", 10),
        ("B", 11),
        ("C", 12),
        ("D", 13),
        ("E", 14),
        ("F", 15),
    ],
)
def test_char2hex(x, expected):
    assert char2hex(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (0, "0000"),
        (1, "0001"),
        (2, "0010"),
        (3, "0011"),
        (4, "0100"),
        (5, "0101"),
        (6, "0110"),
        (7, "0111"),
        (8, "1000"),
        (9, "1001"),
        (10, "1010"),
        (11, "1011"),
        (12, "1100"),
        (13, "1101"),
        (14, "1110"),
        (15, "1111"),
    ],
)
def test_hex2bin(x, expected):
    assert hex2bin(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        ("0", "0000"),
        ("1", "0001"),
        ("2", "0010"),
        ("3", "0011"),
        ("4", "0100"),
        ("5", "0101"),
        ("6", "0110"),
        ("7", "0111"),
        ("8", "1000"),
        ("9", "1001"),
        ("A", "1010"),
        ("B", "1011"),
        ("C", "1100"),
        ("D", "1101"),
        ("E", "1110"),
        ("F", "1111"),
    ],
)
def test_char2bin(x, expected):
    assert char2bin(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "A"),
        (11, "B"),
        (12, "C"),
        (13, "D"),
        (14, "E"),
        (15, "F"),
    ],
)
def test_hex2char(x, expected):
    assert hex2char(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        ("0000", 0),
        ("0001", 1),
        ("0010", 2),
        ("0011", 3),
        ("0100", 4),
        ("0101", 5),
        ("0110", 6),
        ("0111", 7),
        ("1000", 8),
        ("1001", 9),
        ("1010", 10),
        ("1011", 11),
        ("1100", 12),
        ("1101", 13),
        ("1110", 14),
        ("1111", 15),
    ],
)
def test_bin2hex(x, expected):
    assert bin2hex(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        ("0000", "0"),
        ("0001", "1"),
        ("0010", "2"),
        ("0011", "3"),
        ("0100", "4"),
        ("0101", "5"),
        ("0110", "6"),
        ("0111", "7"),
        ("1000", "8"),
        ("1001", "9"),
        ("1010", "A"),
        ("1011", "B"),
        ("1100", "C"),
        ("1101", "D"),
        ("1110", "E"),
        ("1111", "F"),
    ],
)
def test_bin2char(x, expected):
    assert bin2char(x) == expected


# @pytest.fixture()
# def example_data():
#     return preprocess(EXAMPLE_DATA)


# def test_preprocess():
#     preprocess()


@pytest.mark.parametrize(
    "packet_bits, expected_version, expected_type_id, expected_remaining_bits",
    [("110100", 6, 4, "")],
)
def test_decode_literal_header(
    packet_bits, expected_version, expected_type_id, expected_remaining_bits
):
    actual_packet, actual_body_bits = decode_header(packet_bits)
    assert actual_packet.version == expected_version
    assert actual_packet.type_id == expected_type_id
    assert actual_body_bits == expected_remaining_bits


@pytest.mark.parametrize(
    "packet_bits, expected_version, expected_type_id, expected_length_type_id, expected_remaining_bits",
    [
        (
            "00111000000000000110111101000101001010010001001000000000",
            1,
            6,
            0,
            "0000000000110111101000101001010010001001000000000",
        )
    ],
)
def test_decode_operator_header(
    packet_bits,
    expected_version,
    expected_type_id,
    expected_length_type_id,
    expected_remaining_bits,
):
    actual_packet, actual_body_bits = decode_header(packet_bits)
    assert actual_packet.version == expected_version
    assert actual_packet.type_id == expected_type_id
    assert actual_body_bits == expected_remaining_bits
    assert actual_packet.length_type_id == expected_length_type_id


@pytest.mark.parametrize(
    "version, type_id, body_bits, expected_value, expected_remaining_bits",
    [(6, 4, "101111111000101000", 2021, "000")],
)
def test_decode_literal_body(
    version, type_id, body_bits, expected_value, expected_remaining_bits
):
    input_packet = LiteralPacket(version, type_id, None)
    actual_packet, actual_remaining_bits = decode_body(input_packet, body_bits)
    assert actual_packet.value == expected_value
    assert actual_remaining_bits == expected_remaining_bits


@pytest.mark.parametrize(
    "version, type_id, length_type_id, body_bits, expected_subpackets, expected_remaining_bits",
    [
        (
            1,
            6,
            0,
            "0000000000110111101000101001010010001001000000000",
            [LiteralPacket(6, 4, 10), LiteralPacket(2, 4, 20)],
            "0000000",
        ),
        (
            7,
            3,
            1,
            "0000000001101010000001100100000100011000001100000",
            [LiteralPacket(2, 4, 1), LiteralPacket(4, 4, 2), LiteralPacket(1, 4, 3)],
            "00000",
        ),
    ],
)
def test_decode_operator_body(
    version,
    type_id,
    length_type_id,
    body_bits,
    expected_subpackets,
    expected_remaining_bits,
):
    input_packet = OperatorPacket(version, type_id, length_type_id, [])
    actual_packet, actual_remaining_bits = decode_body(input_packet, body_bits)
    assert actual_packet.subpackets == expected_subpackets
    assert actual_remaining_bits == expected_remaining_bits


@pytest.mark.parametrize(
    "hex_encoded_body, expected_packet",
    [
        ("D2FE28", LiteralPacket(6, 4, 2021)),
        (
            "8A004A801A8002F478",
            OperatorPacket(
                version=4,
                type_id=2,
                length_type_id=1,
                subpackets=[
                    OperatorPacket(
                        version=1,
                        type_id=2,
                        length_type_id=1,
                        subpackets=[OperatorPacket(5, 2, 0, [LiteralPacket(6, 4, 15)])],
                    )
                ],
            ),
        ),
        (
            "620080001611562C8802118E34",
            OperatorPacket(
                version=3,
                type_id=0,
                length_type_id=1,
                subpackets=[
                    OperatorPacket(
                        version=0,
                        type_id=0,
                        length_type_id=0,
                        subpackets=[LiteralPacket(0, 4, 10), LiteralPacket(5, 4, 11)],
                    ),
                    OperatorPacket(
                        version=1,
                        type_id=0,
                        length_type_id=1,
                        subpackets=[LiteralPacket(0, 4, 12), LiteralPacket(3, 4, 13)],
                    ),
                ],
            ),
        ),
    ],
)
def test_decode_hexadecimal_packet(hex_encoded_body, expected_packet):
    actual_packet = decode_hexadecimal_packet(hex_encoded_body)
    assert actual_packet == expected_packet


@pytest.mark.parametrize(
    "packets, expected_result",
    [
        (["8A004A801A8002F478"], 16),
        (["620080001611562C8802118E34"], 12),
        (["C0015000016115A2E0802F182340"], 23),
        (["A0016C880162017C3686B18A3D4780"], 31),
    ],
)
def test_solve_a(packets, expected_result):
    assert solve_a(packets) == expected_result


@pytest.mark.parametrize(
    "packets, expected_result",
    [
        (["C200B40A82"], 3),
        (["04005AC33890"], 54),
        (["880086C3E88112"], 7),
        (["D8005AC2A8F0"], 1),
        (["F600BC2D8F"], 0),
        (["9C005AC2F8F0"], 0),
        (["9C0141080250320F1802104A08"], 1),
    ],
)
def test_solve_b(packets, expected_result):
    assert solve_b(packets) == expected_result
