import math

# Add custom coefficients for the FIR filter (-1.0 to 1.0 range)
coefficients = [-0.0180, -0.0212, -0.0112, 0.0171, 0.0628, 0.1172, 0.1662, 0.1953, 0.1953, 0.1662, 0.1172, 0.0628, 0.0171, -0.0112, -0.0212, -0.0180]

# Function to convert number to binary string with specified bits
def num_to_binary(num, bits=16):

    # Convert to Q1.15 signed format
    num = math.floor(num*32768)

    # Clamp the number to fit in Q1.15 format
    if(num >= 32768):
        num = 32767
    if(num < -32768):
        num = -32768

    # Adjust for negative numbers
    if num < 0:
        num = (1 << bits) + num
    return format(num, f'0{bits}b')

# Write coefficients to file
with open("coefficients.txt", "w") as f:
    idx = 0
    for coeff in coefficients:
        f.write(f"reg signed [15:0] h{idx} = 16'b{num_to_binary(coeff)}; // {coeff}\n")
        idx += 1
f.close()