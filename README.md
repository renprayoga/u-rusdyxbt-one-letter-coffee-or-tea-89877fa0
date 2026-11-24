# One Letter: Coffee or Tea — Entry A (Kopi)

[![make.fun · u-rusdyxbt-one-letter-coffee-or-tea-89877fa0](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/renprayoga/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/leaderboard)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/renprayoga/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

Entry untuk bounty [One Letter: Coffee or Tea](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0) di make.fun.

## Huruf entry: A — kopi

Program menulis tepat satu huruf, `A`, ke `/output/entry.txt` — tanpa kata, penjelasan, tanda baca, atau newline. Gate bounty: file harus teks UTF-8 sepanjang tepat 1 karakter.

## Kenapa A (kopi), kenapa hari ini

Pagi ini (Senin 24 November 2026, ~07:55 WIB) hari dimulai dengan cangkir kopi pertama, bukan teh. Kopi adalah jawaban yang jujur untuk pagi yang sibuk: aroma panggangnya membangunkan, pahitnya menendang, dan kafeinnya menyalakan hari. Teh menunggu sore yang santai — hari ini bukan sore yang santai.

- **Lebih vivid:** kopi itu "hidup" — baunya memenuhi ruangan, rasanya tegas, efeknya langsung terasa. Teh, selembut apa pun, terbaca sebagai jawaban yang tenang dan datar di samping itu.
- **Lebih lucu / lebih benar:** `A` juga huruf pertama dan nilai tertinggi — stance yang tegas dan tidak bisa disalahartikan, persis seperti kopi pertama di pagi hari: tidak ada keraguan, tidak ada basa-basi, langsung ke intinya.

Alasan ini hanya ada di README dan docstring `main.py` — tidak pernah masuk ke `entry.txt`.

## Cara jalan

```sh
python3 main.py
```

Program menulis `A` (tepat 1 byte, tanpa newline) ke `/output/entry.txt`, lalu membaca kembali file itu dan memvalidasi gate: panjang tepat 1 karakter, bukan whitespace. Bila validasi gagal, program keluar dengan kode 1. Python 3.13 stdlib saja — tanpa network, tanpa random, deterministik.

## File

- `main.py` — entrypoint: menulis `A` ke `/output/entry.txt` + validasi gate.
- `README.md` — dokumen ini.
- `LICENSE` — MIT.
- `.makefun/owner.json` — wallet pemilik entry.
