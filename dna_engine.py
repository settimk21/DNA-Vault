import zlib

class DNAEngine:
    def __init__(self):
        # Mapping bits -> DNA
        self.bit_to_dna = {
            '00': 'a',
            '01': 'c',
            '10': 'g',
            '11': 't'
        }

        # Reverse mapping DNA -> bits
        self.dna_to_bit = {v: k for k, v in self.bit_to_dna.items()}

    # -----------------------
    # ENCODE FUNCTION
    # -----------------------
    def encode(self, data: bytes) -> str:
        """
        Convert digital data to DNA sequence
        """

        # Compress data to reduce DNA length
        compressed_data = zlib.compress(data)

        # Convert bytes -> binary
        binary_string = ''.join(format(byte, '08b') for byte in compressed_data)

        dna_sequence = ""

        # Convert binary pairs -> DNA letters
        for i in range(0, len(binary_string), 2):
            bits = binary_string[i:i+2]

            # padding protection
            if len(bits) < 2:
                bits = bits + "0"

            dna_sequence += self.bit_to_dna[bits]

        return dna_sequence


    # -----------------------
    # DECODE FUNCTION
    # -----------------------
    def decode(self, dna_sequence: str) -> bytes:
        """
        Convert DNA sequence back to original data
        """

        dna_sequence = dna_sequence.strip().lower()

        # Validate characters
        for nucleotide in dna_sequence:
            if nucleotide not in self.dna_to_bit:
                raise ValueError("Invalid DNA sequence: only a,c,g,t allowed")

        binary_string = ""

        # Convert DNA -> binary
        for nucleotide in dna_sequence:
            binary_string += self.dna_to_bit[nucleotide]

        # Ensure proper byte alignment
        if len(binary_string) % 8 != 0:
            raise ValueError("Corrupted DNA sequence length")

        byte_array = bytearray()

        # Convert binary -> bytes
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            byte_array.append(int(byte, 2))

        try:
            # Decompress data
            original_data = zlib.decompress(bytes(byte_array))
        except:
            raise ValueError("DNA sequence corrupted or incomplete")

        return original_data
