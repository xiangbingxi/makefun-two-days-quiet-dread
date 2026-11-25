import os
import sys

ENTRY = "Approved; the fallback is documented, which will be a comfort to whoever finds us."

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("ERROR: entry.txt does not match ENTRY exactly", file=sys.stderr)
        print(f"expected {len(ENTRY)} chars, got {len(written)} chars", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
