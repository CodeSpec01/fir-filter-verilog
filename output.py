import matplotlib.pyplot as plt

# Function to convert number to binary string with specified bits
def binary_to_num(binstr, bits):
    num = int(binstr, 2)
    if binstr[0] == '1':
        num -= (1 << len(binstr))

    # Scale back to original range
    return num / (1 << bits) 

# Filtered output conversion
output_data = []
with open("output_data.txt", "r") as fout:
    for line in fout:
        output_data.append(binary_to_num(line.strip(), 30)) # Output is in Q4.30 format
fout.close()

# Original Noise input conversion
input_data = []
with open("input_data.txt", "r") as fin:
    for i in fin:
        input_data.append(binary_to_num(i.strip(), 15)) # Input is in Q1.15 format
fin.close()

# Sampling parameters
fs = 1000
t = [i / fs for i in range(0, int(fs))]

# Plotting the results
plt.subplot(2, 1, 1)
plt.plot(t, input_data, label="Input (Noisy)", linewidth=1.5)
plt.title("Original input signal with Noise")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.tight_layout()

plt.subplot(2, 1, 2)
plt.plot(t, output_data, label="Output (Filtered)", linewidth=1.5)
plt.title("Filtered output signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()