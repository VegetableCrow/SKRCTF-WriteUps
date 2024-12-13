def convert_to_binary(dot_dash_sequence):
    # Replace dots and dashes with binary equivalents
    binary_sequence = dot_dash_sequence.replace(".", "1").replace("_", "0")

    # Break the binary sequence into chunks of 8 bits
    binary_chunks = [binary_sequence[i:i+8] for i in range(0, len(binary_sequence), 8)]

    # Pad the last chunk with zeros if necessary to make it 8 bits
    if len(binary_chunks[-1]) < 8:
        binary_chunks[-1] = binary_chunks[-1].ljust(8, '0')

    return binary_chunks

# Example usage
dot_dash_sequences = [
    "_._.__.._.__._..",
    "_._.__.__...._..",
    "_.____.___..___.",
    "_.._...___.._.__",
    "_...__.__....__.",
    "_._.....__..___.",
    "_.._...__._.....",
    "_.__.._._..._._.",
    "_...__..__..___.",
    "_..___.._....._."
]

grouped_binaries = []
for sequence in dot_dash_sequences:
    grouped_binaries.extend(convert_to_binary(sequence))

print("Binary Representation in 8-bit chunks:")
decimal_values = []
ascii_characters = []
for chunk in grouped_binaries:
    print(chunk)
    decimal_value = int(chunk, 2)
    decimal_values.append(decimal_value)

    # Convert to ASCII character if within printable range
    if 32 <= decimal_value <= 126:
        ascii_characters.append(chr(decimal_value))
    else:
        ascii_characters.append("?")  # Placeholder for non-printable characters

print("\nDecimal Values:")
for value in decimal_values:
    print(value)

print("\nASCII Characters:")
print("".join(ascii_characters))
