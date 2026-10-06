# Setup (5 min)

1. GitHub pe ek **public** repo banao jiska naam EXACTLY tumhara username ho: `akashmishra18`
2. Is folder ki saari files us repo me push kar do (branch: `main`)
3. Repo → Settings → Actions → General → Workflow permissions → **Read and write permissions**
4. Actions tab → "Update profile art" → **Run workflow** (ek baar). Isse `data/contributions.json`
   aur `contrib-heatmap.svg` tumhare real data se bhar jayenge. Uske baad roz khud update hoga.

## Apni photo ka ASCII portrait
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r scripts/requirements.txt
python scripts/prep_photo.py my-photo.jpg   # background hata ke source-prepped.png banata hai
python scripts/make_ascii_svg.py            # akash-ascii.svg overwrite
```
`akash-ascii.svg` ab tumhari photo (`source-photo.png`) se bana hua hai. Agar chehra bahut dark/blank lage to `ASCII_GAMMA` aur `WHITE_FLOOR` env vars se tune karo, e.g. `ASCII_GAMMA=0.9 WHITE_FLOOR=0.97 python scripts/make_ascii_svg.py`.

## Info card badalna
`scripts/make_info_card.py` ke upar `CARD` list edit karo, phir `python scripts/make_info_card.py`.
