# Website Templates Arşivi

Sektöre göre haftalık animasyonlu website taslakları araştırma arşivi.

## Son Araştırmalar
| Tarih | Gün | Sektör | Dosya |
|-------|-----|--------|-------|
| 2026-05-28 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-05-28.md](gayrimenkul/2026-05-28.md) |
| 2026-06-04 | Perşembe | Gayrimenkul Ofisleri | [gayrimenkul/2026-06-04.md](gayrimenkul/2026-06-04.md) |
| 2026-06-05 | Cuma | Psikolog ve Danışmanlık Ofisleri | [psikolog-danismanlik/2026-06-05.md](psikolog-danismanlik/2026-06-05.md) |
| 2026-06-15 | Pazartesi | Diyetisyen ve Güzellik Merkezleri | [diyetisyen-guzellik/2026-06-15.md](diyetisyen-guzellik/2026-06-15.md) |
| 2026-06-16 | Salı | Mimarlık ve İç Mimarlık Ofisleri | [mimarlik-ic-mimarlik/2026-06-16.md](mimarlik-ic-mimarlik/2026-06-16.md) |

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
