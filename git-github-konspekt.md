# Git & GitHub — Qısa Konspekt (Addım 4-dən)

## ADDIM 4 — Repository başlatmaq
```bash
git init
```
Folderi Git repository-yə çevirir (gizli `.git` folderi yaranır). **Yalnız 1 dəfə**, layihənin əvvəlində.

---

## ADDIM 5 — Vəziyyəti yoxlamaq
```bash
git status
```
Hansı faylların yeni (untracked), dəyişmiş (modified) və ya hazır (staged) olduğunu göstərir. Zərərsizdir, istənilən vaxt yazıla bilər.

---

## ADDIM 6 — Faylları hazırlamaq (staging)
```bash
git add .
```
Bütün faylları **staging area**-ya əlavə edir (növbəti commit-ə hazır edir).

Digər variantlar:
```bash
git add fayl_adi.py       # yalnız bir fayl
git add -A                # silinmiş fayllar daxil, hamısı
git restore --staged fayl # staging-dən geri çıxarmaq
```

---

## ADDIM 7 — Commit (save point) yaratmaq
```bash
git config --global user.name "Adiniz"
git config --global user.email "email@example.com"
```
Yalnız **ilk dəfə**, Git-ə kim olduğunuzu bildirir (email GitHub-dakı ilə eyni olmalıdır).

```bash
git commit -m "Qisa ve aydin mesaj"
```
Staged faylların o anki halını tarixçəyə **həmişəlik** yazır. `-m` = mesaj (nə etdiyinizi izah edir).

Yoxlama:
```bash
git status          # "nothing to commit, working tree clean" görməlisiniz
git log --oneline   # commit tarixçəsi
```

---

## ADDIM 8 — GitHub-da boş repo yaratmaq
GitHub saytında: **New repository** → ad ver → Public/Private seç → **README/.gitignore/license qutularını BOŞ burax** → **Create repository**.

Səbəb: local-da artıq commit var; GitHub-da da fayl yaradılsa, tarixçələr toqquşar (push zamanı xəta).

---

## ADDIM 9 — Branch adını `main` etmək
```bash
git branch -M main
```
Əsas branch-in adını `main` edir (GitHub bunu gözləyir; köhnə Git-də ilkin ad `master` olur).

Yoxlama:
```bash
git branch     # * main görünməlidir
```

---

## ADDIM 10 — GitHub ilə əlaqə qurmaq
```bash
git remote add origin https://github.com/ISTIFADECI/REPO_ADI.git
```
Local repo ilə GitHub repo-su arasında əlaqə (ləqəb: `origin`). Heç nə göndərmir, yalnız ünvanı yadda saxlayır.

Yoxlama:
```bash
git remote -v
```
Ünvanı dəyişmək:
```bash
git remote set-url origin YENI_URL
```

---

## ADDIM 11 — GitHub-a göndərmək (push)
```bash
git push -u origin main
```
Local commit-ləri GitHub-a göndərir. `-u` sayəsində sonrakı dəfələr sadəcə `git push` yazmaq kifayətdir.

İlk dəfə giriş (brauzer və ya Personal Access Token) tələb oluna bilər.

---

## BONUS — `.gitignore`
`.gitignore` faylı yaradıb (əlavə etmədən, `git add`-dan **əvvəl**) içinə yazın:
```
__pycache__/
*.pyc
.env
.ipynb_checkpoints/
.venv/
```
Bu fayllar Git-ə göndərilmir (parollar, keş, virtual mühit).

---

## Gündəlik iş dövrü (init/remote artıq lazım deyil)
```bash
git status
git add .
git commit -m "Ne etdiyimin qisa tesviri"
git push
```

## Faydalı əlavə əmrlər
```bash
git log --oneline     # tarixçə
git diff               # nə dəyişib, sətir-sətir
git pull                # GitHub-dakı yeniliyi çəkmək
git clone URL           # repo-nu ilk dəfə köçürmək
```
