# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-08-23 | Pazar | Haftanın En Yıldızlı Website Konseptleri | [haftalik-en-iyi/2026-08-23.md](haftalik-en-iyi/2026-08-23.md) |
| 2026-08-24 | Pazartesi | Diyetisyen ve Güzellik Merkezleri | [diyetisyen-guzellik/2026-08-24.md](diyetisyen-guzellik/2026-08-24.md) |
| 2026-08-28 | Cuma | Psikolog ve Danışmanlık Ofisleri | [psikolog-danismanlik/2026-08-28.md](psikolog-danismanlik/2026-08-28.md) |
| 2026-08-29 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-08-29.md](avukat-hukuk/2026-08-29.md) |
| 2026-09-04 | Cuma | Psikolog ve Danışmanlık Ofisleri | [psikolog-danismanlik/2026-09-04.md](psikolog-danismanlik/2026-09-04.md) |
| 2026-09-05 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-09-05.md](avukat-hukuk/2026-09-05.md) |

## Klasörler
- `diyetisyen-guzellik/` — Pazartesi
- `mimarlik-ic-mimarlik/` — Salı
- `insaat/` — Çarşamba
- `gayrimenkul/` — Perşembe
- `psikolog-danismanlik/` — Cuma
- `avukat-hukuk/` — Cumartesi
- `haftalik-en-iyi/` — Pazar

## Otomasyon

Günlük araştırmalar `.github/workflows/daily-templates.yml` ile GitHub Actions üzerinden otomatik çalışır.

**Gereksinim:** GitHub repo ayarlarında `ANTHROPIC_API_KEY` adlı bir Actions Secret tanımlanmalıdır.

**Backfill (kaçırılan günleri doldurmak için):**
GitHub → Actions → "Daily Website Templates Research" → Run workflow → `target_date` alanına `YYYY-MM-DD` girerek çalıştır.
