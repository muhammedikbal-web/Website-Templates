# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-05-18 | Pazartesi | Diyetisyen ve Güzellik Merkezleri | [diyetisyen-guzellik/2026-05-18.md](diyetisyen-guzellik/2026-05-18.md) |
| 2026-05-20 | Çarşamba | İnşaat Firmaları | [insaat/2026-05-20.md](insaat/2026-05-20.md) |
| 2026-05-21 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-05-21.md](gayrimenkul/2026-05-21.md) |
| 2026-05-22 | Cuma | Psikolog ve Danışmanlık Ofisleri | [psikolog-danismanlik/2026-05-22.md](psikolog-danismanlik/2026-05-22.md) |
| 2026-05-24 | Pazar | Haftanın En Yıldızlı Website Konseptleri | [haftalik-en-iyi/2026-05-24.md](haftalik-en-iyi/2026-05-24.md) |

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
