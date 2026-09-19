# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-09-13 | Pazar | Haftanın En Yıldızlı Website Konseptleri | [haftalik-en-iyi/2026-09-13.md](haftalik-en-iyi/2026-09-13.md) |
| 2026-09-14 | Pazartesi | Diyetisyen ve Güzellik Merkezleri | [diyetisyen-guzellik/2026-09-14.md](diyetisyen-guzellik/2026-09-14.md) |
| 2026-09-15 | Salı | Mimarlık ve İç Mimarlık Ofisleri | [mimarlik-ic-mimarlik/2026-09-15.md](mimarlik-ic-mimarlik/2026-09-15.md) |
| 2026-09-16 | Çarşamba | İnşaat Firmaları | [insaat/2026-09-16.md](insaat/2026-09-16.md) |
| 2026-09-17 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-09-17.md](gayrimenkul/2026-09-17.md) |
| 2026-09-18 | Cuma | Psikolog ve Danışmanlık Ofisleri | [psikolog-danismanlik/2026-09-18.md](psikolog-danismanlik/2026-09-18.md) |
| 2026-09-19 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-09-19.md](avukat-hukuk/2026-09-19.md) |

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
