import os
from pathlib import Path
LINE = "At dawn she laced her father's old work boots, now hers, and opened the shutter of the shop he had kept alive for thirty years."
def main():
    os.umask(0o022)
    out = Path("/output/entry.txt")
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(LINE + "\n", encoding="utf-8")
        os.chmod(out.parent, 0o755); os.chmod(out, 0o644)
    except Exception:
        p = Path(__file__).parent / "output" / "entry.txt"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(LINE + "\n", encoding="utf-8")
        os.chmod(p, 0o644)
    print(LINE)
if __name__ == "__main__":
    main()
