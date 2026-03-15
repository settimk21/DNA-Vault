import zlib
import hashlib
import base64

class DNAEngine:

```
def __init__(self):

    self.bit_to_dna = {
        "00": "a",
        "01": "c",
        "10": "g",
        "11": "t"
    }

    self.dna_to_bit = {v: k for k, v in self.bit_to_dna.items()}


# ----------------------------------------
# ENCODE
# ----------------------------------------
def encode(self, data: bytes) -> str:

    # Step 1: checksum
    checksum = hashlib.sha256(data).digest()

    payload = checksum + data

    # Step 2: compress
    compressed = zlib.compress(payload)

    # Step 3: base64 encode
    b64_data = base64.b64encode(compressed)

    # Step 4: binary conversion
    binary_string = "".join(format(byte, "08b") for byte in b64_data)

    dna_sequence = ""

    for i in range(0, len(binary_string), 2):

        bits = binary_string[i:i+2]

        if len(bits) < 2:
            bits += "0"

        dna_sequence += self.bit_to_dna[bits]

    return dna_sequence


# ----------------------------------------
# DECODE
# ----------------------------------------
def decode(self, dna_sequence: str) -> bytes:

    dna_sequence = dna_sequence.strip().lower()

    # Validate characters
    for nucleotide in dna_sequence:
        if nucleotide not in self.dna_to_bit:
            raise ValueError("Invalid DNA sequence")

    binary_string = ""

    for nucleotide in dna_sequence:
        binary_string += self.dna_to_bit[nucleotide]

    if len(binary_string) % 8 != 0:
        raise ValueError("Corrupted DNA sequence")

    byte_array = bytearray()

    for i in range(0, len(binary_string), 8):

        byte = binary_string[i:i+8]

        byte_array.append(int(byte, 2))

    try:

        # reverse base64
        compressed = base64.b64decode(bytes(byte_array))

        # decompress
        decompressed = zlib.decompress(compressed)

    except:
        raise ValueError("DNA sequence corrupted")

    checksum = decompressed[:32]

    original_data = decompressed[32:]

    new_checksum = hashlib.sha256(original_data).digest()

    if checksum != new_checksum:
        raise ValueError("DNA tampering detected")

    return original_data
```
