# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-05-30 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-05-30.md](avukat-hukuk/2026-05-30.md) |
| 2026-05-31 | Pazar | Haftanın En Yıldızlı Website Konseptleri | [haftalik-en-iyi/2026-05-31.md](haftalik-en-iyi/2026-05-31.md) |
| 2026-06-01 | Pazartesi | Diyetisyen ve Güzellik Merkezleri | [diyetisyen-guzellik/2026-06-01.md](diyetisyen-guzellik/2026-06-01.md) |
| 2026-06-02 | Salı | Mimarlık ve İç Mimarlık Ofisleri | [mimarlik-ic-mimarlik/2026-06-02.md](mimarlik-ic-mimarlik/2026-06-02.md) |
| 2026-06-03 | Çarşamba | İnşaat Firmaları | [insaat/2026-06-03.md](insaat/2026-06-03.md) |
| 2026-06-04 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-06-04.md](gayrimenkul/2026-06-04.md) |
| 2026-06-06 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-06-06.md](avukat-hukuk/2026-06-06.md) |

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
