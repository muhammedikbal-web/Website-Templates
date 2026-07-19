"""
Daily website template research script.
Uses Claude API with web search to find 5 animated templates for each sector.
Run via GitHub Actions (cron) or manually:
  python scripts/daily_research.py
  TARGET_DATE=2026-04-29 python scripts/daily_research.py
"""

import anthropic
import os
import sys
from datetime import datetime
from pathlib import Path

SECTORS = {
    1: ("Diyetisyen ve Güzellik Merkezleri",       "diyetisyen-guzellik",    "Pazartesi"),
    2: ("Mimarlık ve İç Mimarlık Ofisleri",         "mimarlik-ic-mimarlik",   "Salı"),
    3: ("İnşaat Firmaları",                          "insaat",                 "Çarşamba"),
    4: ("Gayrimenkul Ofisleri",                      "gayrimenkul",            "Perşembe"),
    5: ("Psikolog ve Danışmanlık Ofisleri",          "psikolog-danismanlik",   "Cuma"),
    6: ("Avukat ve Hukuk Ofisleri",                  "avukat-hukuk",           "Cumartesi"),
    7: ("Haftanın En Yıldızlı Website Konseptleri", "haftalik-en-iyi",        "Pazar"),
}


def main():
    target_date_str = os.environ.get("TARGET_DATE", "").strip()
    target_dt = (
        datetime.strptime(target_date_str, "%Y-%m-%d")
        if target_date_str
        else datetime.now()
    )

    date_str = target_dt.strftime("%Y-%m-%d")
    day_num  = target_dt.isoweekday()   # 1=Pazartesi … 7=Pazar
    sector, folder, day_tr = SECTORS[day_num]
    output_path = Path(folder) / f"{date_str}.md"

    if output_path.exists():
        print(f"Zaten mevcut: {output_path} — atlanıyor.")
        sys.exit(0)

    output_path.parent.mkdir(exist_ok=True)

    client = anthropic.Anthropic()

    prompt = f"""Sen bir website taslağı araştırma uzmanısın. \
'{sector}' sektörü için web araması yaparak 5 animasyonlu website taslağı bul.

Şu aramaları yap:
1. "{sector} website template animated Framer Motion GSAP 2025 2026"
2. "{sector} HTML Tailwind CSS animated template free GitHub"
3. "{sector} React Next.js website template animation scroll"

Her taslak için doğrula:
- Demo URL (canlı ve erişilebilir)
- Animasyon kütüphanesi (Framer Motion / GSAP / AOS / Lottie / CSS transitions)
- GitHub yıldız sayısı (varsa)
- Fiyat (ücretsiz / ücretli + tutar)
- Teknoloji stack

KRİTİK: Animasyonsuz taslak KABUL EDİLMEZ.

SADECE şu Markdown formatında yanıt ver (başka açıklama ekleme):

# {sector} — {date_str}

> Oluşturulma: {date_str} | Bulunan taslak sayısı: 5

---

## Taslak 1: [AD]
- **Demo**: [URL]
- **GitHub**: [URL veya N/A] ⭐ [yıldız veya N/A]
- **Stack**: [teknoloji]
- **Animasyon**: [kütüphane + özellikler]
- **Fiyat**: [ücretsiz / ücretli + tutar]
- **Açıklama**: [2 cümle]

## Taslak 2: [AD]
[aynı format]

## Taslak 3: [AD]
[aynı format]

## Taslak 4: [AD]
[aynı format]

## Taslak 5: [AD]
[aynı format]

---

## Hızlı Karşılaştırma
| Taslak | Demo | Stack | Animasyon | Fiyat |
|--------|------|-------|-----------|-------|
| [AD] | [LINK] | [STACK] | [ANİM] | [FİYAT] |
| [AD] | [LINK] | [STACK] | [ANİM] | [FİYAT] |
| [AD] | [LINK] | [STACK] | [ANİM] | [FİYAT] |
| [AD] | [LINK] | [STACK] | [ANİM] | [FİYAT] |
| [AD] | [LINK] | [STACK] | [ANİM] | [FİYAT] |

---
*Otomatik oluşturuldu — Claude Code Günlük Rutin*"""

    print(f"Araştırılıyor: {sector} ({date_str}) ...")

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=8096,
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": 6,
        }],
        messages=[{"role": "user", "content": prompt}],
    )

    content = next(
        (block.text for block in response.content if getattr(block, "type", "") == "text"),
        ""
    ).strip()

    if not content:
        print("HATA: Claude API'den boş yanıt alındı.")
        sys.exit(1)

    output_path.write_text(content, encoding="utf-8")
    print(f"Oluşturuldu: {output_path}")

    _update_readme(date_str, day_tr, sector, str(output_path))

    Path("/tmp/commit_message.txt").write_text(
        f"feat: {day_tr} {sector} taslakları — {date_str}"
    )
    print("Tamamlandı.")


def _update_readme(date_str: str, day_tr: str, sector: str, file_path: str) -> None:
    readme = Path("README.md")
    content = readme.read_text(encoding="utf-8")

    new_row = f"| {date_str} | {day_tr} | {sector} | [{file_path}]({file_path}) |"
    if new_row in content:
        return

    separator = "|-------|-----|--------|-------|"
    content = content.replace(separator, separator + "\n" + new_row, 1)

    # Son 7 girdiyi tut
    lines = content.splitlines()
    header = "| Tarih | Gün | Sektör | Dosya |"
    header_idx = next((i for i, l in enumerate(lines) if header in l), None)
    if header_idx is not None:
        data_start = header_idx + 2   # header + separator
        data_rows  = [i for i in range(data_start, len(lines)) if lines[i].startswith("| ")]
        while len(data_rows) > 7:
            del lines[data_rows.pop(0)]
            data_rows = [x - 1 for x in data_rows]
        content = "\n".join(lines) + "\n"

    readme.write_text(content, encoding="utf-8")
    print("README.md güncellendi.")


if __name__ == "__main__":
    main()
