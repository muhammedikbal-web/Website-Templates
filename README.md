# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-07-23 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-07-23.md](gayrimenkul/2026-07-23.md) |
| 2026-07-24 | Cuma | Psikolog ve Danışmanlık Ofisleri | [psikolog-danismanlik/2026-07-24.md](psikolog-danismanlik/2026-07-24.md) |
| 2026-07-25 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-07-25.md](avukat-hukuk/2026-07-25.md) |
| 2026-07-26 | Pazar | Haftanın En Yıldızlı Website Konseptleri | [haftalik-en-iyi/2026-07-26.md](haftalik-en-iyi/2026-07-26.md) |
| 2026-07-27 | Pazartesi | Diyetisyen ve Güzellik Merkezleri | [diyetisyen-guzellik/2026-07-27.md](diyetisyen-guzellik/2026-07-27.md) |
| 2026-07-29 | Çarşamba | İnşaat Firmaları | [insaat/2026-07-29.md](insaat/2026-07-29.md) |
| 2026-07-30 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-07-30.md](gayrimenkul/2026-07-30.md) |

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
