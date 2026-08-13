# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-08-02 | Pazar | Haftanın En Yıldızlı Website Konseptleri | [haftalik-en-iyi/2026-08-02.md](haftalik-en-iyi/2026-08-02.md) |
| 2026-08-05 | Çarşamba | İnşaat Firmaları | [insaat/2026-08-05.md](insaat/2026-08-05.md) |
| 2026-08-06 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-08-06.md](gayrimenkul/2026-08-06.md) |
| 2026-08-08 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-08-08.md](avukat-hukuk/2026-08-08.md) |
| 2026-08-10 | Pazartesi | Diyetisyen ve Güzellik Merkezleri | [diyetisyen-guzellik/2026-08-10.md](diyetisyen-guzellik/2026-08-10.md) |
| 2026-08-12 | Çarşamba | İnşaat Firmaları | [insaat/2026-08-12.md](insaat/2026-08-12.md) |
| 2026-08-13 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-08-13.md](gayrimenkul/2026-08-13.md) |

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
