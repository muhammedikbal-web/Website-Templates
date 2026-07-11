# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-06-27 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-06-27.md](avukat-hukuk/2026-06-27.md) |
| 2026-06-28 | Pazar | Haftanın En Yıldızlı Website Konseptleri | [haftalik-en-iyi/2026-06-28.md](haftalik-en-iyi/2026-06-28.md) |
| 2026-06-29 | Pazartesi | Diyetisyen ve Güzellik Merkezleri | [diyetisyen-guzellik/2026-06-29.md](diyetisyen-guzellik/2026-06-29.md) |
| 2026-06-30 | Salı | Mimarlık ve İç Mimarlık Ofisleri | [mimarlik-ic-mimarlik/2026-06-30.md](mimarlik-ic-mimarlik/2026-06-30.md) |
| 2026-07-01 | Çarşamba | İnşaat Firmaları | [insaat/2026-07-01.md](insaat/2026-07-01.md) |
| 2026-07-08 | Çarşamba | İnşaat Firmaları | [insaat/2026-07-08.md](insaat/2026-07-08.md) |
| 2026-07-11 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-07-11.md](avukat-hukuk/2026-07-11.md) |

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
