import secrets
import bitcoin
from bech32 import encode
import hashlib
import time

# List of vanity tokens.
vanities = ["sammy"]

# Generate a Bech32 address from a public key.
def generate_bech32_address(public_key, hrp='bc'):
    # Convert a public key to a P2WPKH witness program.
    sha256_hash = hashlib.sha256(public_key).digest()
    witness_program = hashlib.new('ripemd160', sha256_hash).digest()
    bech32_address = encode(hrp, 0, witness_program)
    return bech32_address

def compress_public_key(uncompressed_pubkey_hex: str) -> str:
    # Ensure the public key is the correct format and length
    if len(uncompressed_pubkey_hex) != 130 or not uncompressed_pubkey_hex.startswith('04'):
        raise ValueError("Invalid uncompressed public key format")
    # Extract x and y coordinates as bytes from the uncompressed public key
    x = bytes.fromhex(uncompressed_pubkey_hex[2:66])
    y = bytes.fromhex(uncompressed_pubkey_hex[66:130])
    # Determine the prefix based on the parity of y
    prefix = '02' if int.from_bytes(y, byteorder='big') % 2 == 0 else '03'
    # Return the compressed public key as a hexadecimal string
    return prefix + x.hex()

counter = 0
output_file = 'vanities.txt'
count_file = 'count.txt'
while True:
    # To not annihilate my cpu
    time.sleep(0.02)

    # Generate a random 256-bit private key.
    private_key = '{:064x}'.format(secrets.randbits(256))

    # Convert private key to a public key.
    public_key = bitcoin.privtopub(private_key)
    comp_pubkey = compress_public_key(public_key)
    comp_pubkey = bytes.fromhex(comp_pubkey)
    bech32_address = generate_bech32_address(comp_pubkey)
    #print(bech32_address)  # Prints the Bech32 address

    # Slice off the 'bc1' prefix if you want vanity at start.
    #address_suffix = bech32_address[4:]

    # Check against each vanity prefix
    for vanity in vanities:
        # Compare vanity prefix with corresponding part of address suffix
        #if address_suffix.startswith(vanity):
        if bech32_address.endswith(vanity):
            #print(f"Match found! Address: {bech32_address}, Vanity: {vanity}")
            with open(output_file, 'a') as f:
                f.write(f"Private Key: {private_key}, Address: {bech32_address}\n")
            break  # Exit the loop if a match is found
    counter += 1 
    if counter == 1000:
        counter = 0
        with open(count_file, "a") as count:
            count.write("x")
