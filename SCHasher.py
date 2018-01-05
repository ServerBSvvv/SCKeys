import binascii
import struct

HASH_MAP = [0xB699, 0x8D95, 0x89E4, 0xE6B0, 0x9A6E, 0xD6E1, 0xE75D, 0x40C5,
            0x24C2, 0xD8B4, 0x9FF3, 0xC25A, 0xEBCA, 0x42A3, 0xF8A8, 0xCEFA]
A_MAP = [1, 0xFFFF0003, 0xFFFF0007, 0xFFFF001F]
B_MAP = [0x7FFF, 0x3FFF, 0x1FFF, 0x07FF]
MUL_MAP = [2, 4, 8, 32]
SHIFT_MAP = [0, 15, 14, 13, 15, 11, 0, 14, 0, 0, 13, 11, 14, 15, 14, 15]


def get_values(shift_key):
    if shift_key == 15:
        return [A_MAP[0], B_MAP[0], MUL_MAP[0]]
    elif shift_key == 14:
        return [A_MAP[1], B_MAP[1], MUL_MAP[1]]
    elif shift_key == 13:
        return [A_MAP[2], B_MAP[2], MUL_MAP[2]]
    elif shift_key == 11:
        return [A_MAP[3], B_MAP[3], MUL_MAP[3]]


# result
r = bytearray()
# hold the last 2 bytes
s = 0

while len(HASH_MAP) > 0:
    hash_key = HASH_MAP.pop(0)
    shift_key = SHIFT_MAP.pop(0)
    if shift_key > 0:
        v = get_values(shift_key)
        s = ((s ^ hash_key) >> shift_key) & v[0] | v[2] * ((s ^ hash_key) & v[1])
        r += struct.pack("H", s)
    else:
        s = s ^ hash_key
        r += struct.pack("H", s)

print(binascii.hexlify(r))
