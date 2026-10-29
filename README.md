# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-10-21 | Çarşamba | İnşaat Firmaları | [insaat/2026-10-21.md](insaat/2026-10-21.md) |
| 2026-10-23 | Cuma | Psikolog ve Danışmanlık Ofisleri | [psikolog-danismanlik/2026-10-23.md](psikolog-danismanlik/2026-10-23.md) |
| 2026-10-24 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-10-24.md](avukat-hukuk/2026-10-24.md) |
| 2026-10-27 | Salı | Mimarlık ve İç Mimarlık Ofisleri | [mimarlik-ic-mimarlik/2026-10-27.md](mimarlik-ic-mimarlik/2026-10-27.md) |
| 2026-10-28 | Çarşamba | İnşaat Firmaları | [insaat/2026-10-28.md](insaat/2026-10-28.md) |
| 2026-10-29 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-10-29.md](gayrimenkul/2026-10-29.md) |

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
