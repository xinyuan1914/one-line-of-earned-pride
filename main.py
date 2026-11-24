import os
from pathlib import Path
LINE = "At dawn she laced her father's old work boots, now hers, and opened the shutter of the shop he had kept alive for thirty years."
def main():
    os.umask(0o022)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
    except Exception:
        pass
    out = out_dir / "entry.txt"
    try:
        out.write_text(LINE + "\n", encoding="utf-8")
    except Exception:
        out = Path(__file__).parent / "output" / "entry.txt"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(LINE + "\n", encoding="utf-8")
    try:
        os.chmod(out, 0o644)
    except Exception:
        pass
    print(LINE)
if __name__ == "__main__":
    main()
