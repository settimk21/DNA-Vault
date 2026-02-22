import binascii

class DNAEngine:
    def __init__(self):
        self.bit_to_dna = {
            '00': 'A',
            '01': 'C',
            '10': 'G',
            '11': 'T'
        }
        self.dna_to_bit = {v: k for k, v in self.bit_to_dna.items()}

    # ---------------- ENCODE ----------------
    def encode(self, data: bytes) -> str:
        binary_string = ''.join(format(byte, '08b') for byte in data)

        dna_sequence = ''
        for i in range(0, len(binary_string), 2):
            bits = binary_string[i:i+2]
            dna_sequence += self.bit_to_dna[bits]

        return dna_sequence

    # ---------------- DECODE ----------------
    def decode(self, dna_sequence: str) -> bytes:
        binary_string = ''

        for nucleotide in dna_sequence:
            if nucleotide not in self.dna_to_bit:
                raise ValueError("Invalid DNA sequence")
            binary_string += self.dna_to_bit[nucleotide]

        byte_array = bytearray()

        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            byte_array.append(int(byte, 2))

        return bytes(byte_array)