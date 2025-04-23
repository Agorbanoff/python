import sys
from convert4er import Convert4er

if len(sys.argv) != 3:
    print("Usage: python converter.py input.csv output.json")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

from_format = input_file.split('.')[-1]
to_format = output_file.split('.')[-1]

converter = Convert4er(input_file)
converter.convert(from_format, to_format, output_file)

print(f"Converted {input_file} to {output_file} successfully.")
