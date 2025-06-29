import math
import random
import matplotlib.pyplot as plt

# Sampling parameters
fs = 1000
t = [i / fs for i in range(0, int(fs))]

# Random noise frequency factor
r1 = random.random()
r2 = random.random()
r3 = random.random()

# Generate noisy sine wave
sine = [(math.sin(2 * math.pi * 50 * ti) + math.sin(2 * math.pi * r1 * 500 * ti) + math.sin(2 * math.pi * r2 * 500 * ti) + math.sin(2 * math.pi * r3 * 500 * ti)) for ti in t]

# Print the random factors used for noise generation
print("r1:", r1, "r2:", r2, "r3:", r3)

# Normalize the sine wave
max_sine = max(sine)
sine_norm = [round(s / max_sine, 13) for s in sine]

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

# Function to convert binary string back to number
def binary_to_num(binstr):
    num = int(binstr, 2)

    # Adjust for negative numbers in Q1.15 format
    if binstr[0] == '1':
        num -= (1 << len(binstr))

    # Scale back to original range
    return num / 32768.0

# Array for checking precision after conversion
newsine = []

# For storing the binary results
with open("input_data.txt", "w") as f:
    for i in sine_norm:
        binary = num_to_binary(i)
        num = binary_to_num(binary)
        newsine.append(num)
        f.write(f"{binary}\n")
f.close()

# Plotting the results
plt.subplot(3, 1, 1)
plt.plot(t, sine, label="Input (Noisy)", linewidth=1.5)
plt.title("Original input signal with Noise")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.tight_layout()

plt.subplot(3, 1, 2)
plt.plot(t, sine_norm, label="Input normalised (Noisy)", linewidth=1.5)
plt.title("Normalised input signal with Noise")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.tight_layout()

plt.subplot(3, 1, 3)
plt.plot(t, newsine, label="Input discretized (Noisy)", linewidth=1.5)
plt.title("Discretized input signal with Noise")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()