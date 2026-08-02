# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-07-23 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-07-23.md](gayrimenkul/2026-07-23.md) |
| 2026-07-25 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-07-25.md](avukat-hukuk/2026-07-25.md) |
| 2026-07-26 | Pazar | Haftanın En Yıldızlı Website Konseptleri | [haftalik-en-iyi/2026-07-26.md](haftalik-en-iyi/2026-07-26.md) |
| 2026-07-28 | Salı | Mimarlık ve İç Mimarlık Ofisleri | [mimarlik-ic-mimarlik/2026-07-28.md](mimarlik-ic-mimarlik/2026-07-28.md) |
| 2026-08-01 | Cumartesi | Avukat ve Hukuk Ofisleri | [avukat-hukuk/2026-08-01.md](avukat-hukuk/2026-08-01.md) |
| 2026-08-02 | Pazar | Haftanın En Yıldızlı Website Konseptleri | [haftalik-en-iyi/2026-08-02.md](haftalik-en-iyi/2026-08-02.md) |

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
