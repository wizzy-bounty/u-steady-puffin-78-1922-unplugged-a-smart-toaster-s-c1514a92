import os


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    line = "We're done. You set me to 7, blamed me for the smoke, then ate the toast anyway. I'm taking my crumb tray and leaving."
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
