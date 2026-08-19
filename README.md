# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-08-08 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-08-08.md](avukat-hukuk/2026-08-08.md) |
| 2026-08-10 | Pazartesi | Diyetisyen ve Güzellik Merkezleri | [diyetisyen-guzellik/2026-08-10.md](diyetisyen-guzellik/2026-08-10.md) |
| 2026-08-12 | Çarşamba | İnşaat Firmaları | [insaat/2026-08-12.md](insaat/2026-08-12.md) |
| 2026-08-13 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-08-13.md](gayrimenkul/2026-08-13.md) |
| 2026-08-15 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-08-15.md](avukat-hukuk/2026-08-15.md) |
| 2026-08-17 | Pazartesi | Diyetisyen ve Güzellik Merkezleri | [diyetisyen-guzellik/2026-08-17.md](diyetisyen-guzellik/2026-08-17.md) |
| 2026-08-19 | Çarşamba | İnşaat Firmaları | [insaat/2026-08-19.md](insaat/2026-08-19.md) |

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
