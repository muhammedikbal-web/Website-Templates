# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-08-23 | Pazar | Haftanın En Yıldızlı Website Konseptleri | [haftalik-en-iyi/2026-08-23.md](haftalik-en-iyi/2026-08-23.md) |
| 2026-08-26 | Çarşamba | İnşaat Firmaları | [insaat/2026-08-26.md](insaat/2026-08-26.md) |
| 2026-08-27 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-08-27.md](gayrimenkul/2026-08-27.md) |
| 2026-08-30 | Pazar | Haftanın En Yıldızlı Website Konseptleri | [haftalik-en-iyi/2026-08-30.md](haftalik-en-iyi/2026-08-30.md) |
| 2026-08-31 | Pazartesi | Diyetisyen ve Güzellik Merkezleri | [diyetisyen-guzellik/2026-08-31.md](diyetisyen-guzellik/2026-08-31.md) |
| 2026-09-01 | Salı | Mimarlık ve İç Mimarlık Ofisleri | [mimarlik-ic-mimarlik/2026-09-01.md](mimarlik-ic-mimarlik/2026-09-01.md) |
| 2026-09-02 | Çarşamba | İnşaat Firmaları | [insaat/2026-09-02.md](insaat/2026-09-02.md) |

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
