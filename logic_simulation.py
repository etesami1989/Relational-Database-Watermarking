import hashlib

# This script simulates the logic of Relational Database Watermarking 
# from my Bachelor's Project (2013-2014)

def generate_watermark(primary_key, secret_key):
    # Combining PK and Secret Key to decide where to hide the watermark bit
    combined_string = str(primary_key) + secret_key
    hash_result = hashlib.sha256(combined_string.encode()).hexdigest()
    
    # Using the hash to determine the attribute and bit position
    return int(hash_result, 16) % 2 == 0  # True/False for watermark bit

# My research focused on resistance against tuple deletion and alteration attacks.
