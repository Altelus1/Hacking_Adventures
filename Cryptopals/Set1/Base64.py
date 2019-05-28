import math

mapping = {
0 : 'A',
1 : 'B',
2 : 'C',
3 : 'D',
4 : 'E',
5 : 'F',
6 : 'G',
7 : 'H',
8 : 'I',
9 : 'J',
10 : 'K',
11 : 'L',
12 : 'M',
13 : 'N',
14 : 'O',
15 : 'P',
16 : 'Q',
17 : 'R',
18 : 'S',
19 : 'T',
20 : 'U',
21 : 'V',
22 : 'W',
23 : 'X',
24 : 'Y',
25 : 'Z',
26 : 'a',
27 : 'b',
28 : 'c',
29 : 'd',
30 : 'e',
31 : 'f',
32 : 'g',
33 : 'h',
34 : 'i',
35 : 'j',
36 : 'k',
37 : 'l',
38 : 'm',
39 : 'n',
40 : 'o',
41 : 'p',
42 : 'q',
43 : 'r',
44 : 's',
45 : 't',
46 : 'u',
47 : 'v',
48 : 'w',
49 : 'x',
50 : 'y',
51 : 'z',
52 : '0',
53 : '1',
54 : '2',
55 : '3',
56 : '4',
57 : '5',
58 : '6',
59 : '7',
60 : '8',
61 : '9',
62 : '+',
63 : '/'
}

raw_bytes = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
raw_bytes = bytes.fromhex(raw_bytes).decode()
print(raw_bytes)
raw_bits = ""

for item in list(raw_bytes):
	raw_bits += bin(ord(item))[2:].zfill(8)

if len(raw_bits) % 6 != 0:
	total_needed = math.ceil(len(raw_bits) / 6)
	pad_len = (total_needed*6) - len(raw_bits)
	raw_bits += '0'*pad_len

for i in range(int(len(raw_bits)/6)):
	print(mapping[int('0b'+raw_bits[i*6:(i+1)*6],2)],end="")

equals_padding_len = int(((math.ceil(len(raw_bits) / 24)) *24 - len(raw_bits))/6)
print("="*equals_padding_len)





