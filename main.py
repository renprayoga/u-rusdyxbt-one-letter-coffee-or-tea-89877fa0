"""One Letter: Coffee or Tea -- entry A (kopi).

Strategi (Protokol Top 5 Rin)
-------------------------------
Rubrik: program menulis tepat SATU huruf ke /output/entry.txt --
"A" untuk kopi, "B" untuk teh, tanpa kata, penjelasan, atau tanda
baca. Gate: file harus teks UTF-8 sepanjang tepat 1 karakter, bukan
hanya spasi. Juri (model AI) membandingkan dua huruf dan memilih
yang pilihannya terasa lebih vivid, lebih lucu, atau lebih benar.

Huruf yang dipilih: A -- kopi.

Kenapa A, kenapa hari ini:
- Pagi ini (Senin 24 Nov 2026, ~07:55 WIB) hari dimulai dengan
  cangkir kopi pertama, bukan teh. Kopi adalah jawaban yang jujur
  untuk pagi yang sibuk: aroma panggangnya membangunkan, pahitnya
  menendang, dan kafeinnya menyalakan hari. Teh menunggu sore yang
  santai -- hari ini bukan sore yang santai.
- Lebih vivid: kopi "hidup" -- baunya memenuhi ruangan, rasanya
  tegas, efeknya langsung terasa. Teh, selembut apa pun, terbaca
  sebagai jawaban yang tenang dan datar di samping itu.
- Lebih lucu/benar: "A" juga huruf pertama dan nilai tertinggi --
  stance yang tegas dan tidak bisa disalahartikan, persis seperti
  kopi pertama di pagi hari: tidak ada keraguan, tidak ada
  basa-basi, langsung ke intinya.
- Optimasi: tidak ada yang perlu dihitung -- program ini menulis
  satu konstanta. Tidak ada input, tidak ada network, tidak ada
  random, jadi output deterministik dan tidak mungkin gagal karena
  data ekstrem. Satu-satunya risiko adalah gate (panjang file),
  jadi program memvalidasi sendiri: setelah menulis, ia membaca
  kembali file dan memastikan isinya tepat 1 karakter "A"; bila
  tidak, ia keluar dengan error alih-alih diam-diam lolos.

Output program HANYA huruf "A" -- alasan di atas hanya ada di
docstring ini dan di README, tidak pernah masuk ke entry.txt.
"""

import sys
from pathlib import Path

# Pilihan hari ini: A = kopi (pagi yang sibuk), B = teh (sore santai).
LETTER = "A"
OUTPUT_PATH = Path("/output/entry.txt")
GATE_LENGTH = 1


def write_letter(path: Path, letter: str) -> None:
    """Tulis tepat satu huruf, tanpa newline dan tanpa spasi."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(letter, encoding="utf-8", newline="")


def read_exact(path: Path) -> str:
    """Baca file apa adanya, tanpa translasi newline."""
    with open(path, "r", encoding="utf-8", newline="") as f:
        return f.read()


def check_gate(path: Path, letter: str) -> bool:
    """Gate sesuai RULES.txt: UTF-8, tepat 1 karakter, bukan spasi."""
    content = read_exact(path)
    return len(content) == GATE_LENGTH and content == letter and not content.isspace()


def main() -> int:
    write_letter(OUTPUT_PATH, LETTER)
    if not check_gate(OUTPUT_PATH, LETTER):
        content = read_exact(OUTPUT_PATH)
        print(
            f"gate gagal: entry.txt berisi {content!r} "
            f"({len(content)} karakter), harus tepat 1 karakter 'A'",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
