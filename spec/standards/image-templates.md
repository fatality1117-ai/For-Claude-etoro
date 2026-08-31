# 貼文配圖模板

Repo：`fatality1117-ai/For-Claude-etoro`，目錄 `pics/`，全部 1080x1080。
檔名於 2026-08-26 與 2026-08-31 兩次用 `git clone` 直接列出核對，**不是推測**。

## 鐵則：eToro 貼文一律掛圖（2026-08-31 Ed 裁示）

**每一篇貼文都要有圖，沒有例外。** 這是 Ed 訂的，優先於任何「配圖效果 PARKED」的實測結論——
那個實測講的是「有圖會不會提高互動」，這條講的是版面一致性與品牌，兩件事。

- M5 的配圖檢查對**所有**變體都是必檢項，**不准標 n/a**。
- 找不到對應模板 → **hard 缺陷，稿件不發**，回報寫明缺哪一張。
  不准無圖硬發，也不准拿別的類型的圖頂替。

## 存取方式（重要，前面踩過三次坑）

| 路徑 | 狀態 |
|---|---|
| `git clone https://github.com/...`（git 協定） | **通** — 讀檔名、讀內容都可以 |
| `https://api.github.com/repos/...` | 擋（git proxy 未授權此 repo） |
| `curl https://raw.githubusercontent.com/...` | 不通（sandbox 對該主機無 egress） |
| `WebFetch https://github.com/.../tree/...` | 擋（robots.txt） |
| `git push` | **擋** — proxy 403、API 403、直連 token 是佔位值。歷史上也從來沒推成功過，見下方 git log 查證 |

**要查檔名就 `git clone --depth 1`，不要用其他三種，也不要猜。**

raw URL 本身在 eToro 端是可以正常抓取的（daily 那張已驗證會顯示），
不通的只有我的 sandbox。

## URL 對照

base = `https://raw.githubusercontent.com/fatality1117-ai/For-Claude-etoro/main/pics/`

| 貼文類型 | 變體 | 檔名 | 完整 URL |
|---|---|---|---|
| DAILY BRIEF | M4a | `tpl_daily.png` | base + `tpl_daily.png` |
| WEEKLY REVIEW | M4b | `tpl_weekly.png` | base + `tpl_weekly.png` |
| MONTHLY REVIEW | M4c | `tpl_monthly.png` | base + `tpl_monthly.png` |
| MARKET PULSE | M4d | `tpl_pulse.png` | base + `tpl_pulse.png` |
| SECTOR BRIEF AI Infra | M4e | `tpl_sector_ai.png` | base + `tpl_sector_ai.png` |
| SECTOR BRIEF 關鍵礦產 | M4f | `tpl_sector_minerals.png` | base + `tpl_sector_minerals.png` |
| SECTOR BRIEF 能源 | M4g | `tpl_sector_energy.png` | base + `tpl_sector_energy.png` |
| SECTOR BRIEF 生技 | M4h | `tpl_sector_biotech.png` | base + `tpl_sector_biotech.png` |
| SECTOR BRIEF 資安 | M4i | `tpl_sector_netsec.png` | base + `tpl_sector_netsec.png` |
| DEEP DIVE | M4j | `tpl_deepdive.png` | base + `tpl_deepdive.png` |
| THE ASIA READ | M4k | `tpl_asiaread.png` | base + `tpl_asiaread.png` |

**十一個主題對十一張圖，一一對應，沒有共用，沒有缺口。**

## 模板是怎麼做出來的：repo 自己有生成器

**`docs/make_templates.py`（在同一個 repo 裡）就是產這十一張圖的腳本。**
2026-08-31 才重新發現它 —— 08-29 改版成 v3 文件時，把指向這個 repo 內容的指標弄丟了，
結果這一趟為了補 ASIA READ 那張，是拿 `tpl_pulse.png` 逆向去字重排做出來的，
而不是直接跑生成器。**要加新模板就改那個腳本的 `TEMPLATES` 清單再跑，不要再逆向。**

腳本的設計（讀出來記在這裡，免得再忘）：
- 1080x1080，底色 `(11,15,20)`，左側直線 spine 在 x=96，文字左緣 x=140
- 每個主題有自己的 accent 色，用在 spine、標題底下的短線、`@Edwardhwang888`
- accent 色會在左上做一團高斯模糊的光暈，四周有 vignette
- 字型 Liberation Sans：品牌 Bold 30、副標 Regular 18、標題 Bold 92/66/52（依長度）、
  descriptor Regular 34、handle Bold 28
- 標題超過 16 字元降到 66，超過 22 降到 52；`·` 會被拆成兩行

**Repo 的分工（2026-08-31 定案）：repo 只放圖與生成器，規格正本在 Claude Project。**
repo 裡 `SKILL.md`、`SNAPSHOT.md`、`docs/`、`schedule.md`、`sources.md` 那批是
2026-08-25 的 v0.4 舊規格，**已被 Project 的 v3 文件取代，不要再讀、不要再引用**。

## repo 的寫入權：這一版才是對的（2026-08-31 更正）

**先前寫在這裡的「我從來沒有寫入權」是錯的判讀，已作廢。**
我看到 `git log` 每筆的 committer 都是 `GitHub <noreply@github.com>` 就下結論說
「這些都是 Ed 用網頁上傳的」。**那個判讀站不住腳**：committer 是 GitHub 只代表
commit 是在 GitHub 伺服器端產生的，**網頁上傳與 REST Contents API 兩者都長這樣**。
`Spec v0.4`、`docs for claude on etoro's post` 這種自訂訊息，比較像 API 寫進去的。
換句話說，2026-08-25 那批規格檔很可能就是當時的 session 用 GitHub API 寫的，
**寫入權存在過**。

**今天不能寫的原因是 session 授權，不是能力上限。** 現在的錯誤訊息是
`GitHub access to this repository is not enabled for this session`，
也就是這個 repo 沒有掛進本 session 的 sources；proxy 因此不注入憑證，
環境變數裡的 `GH_TOKEN` 只是 `proxy-injected` 佔位字串。

**所以正確的結論是：把 repo 掛進 session 的 sources，我就能自己維護它** ——
推模板圖、修 `%20 tpl_daily.png` 那個檔名、把規格快照同步上去，都不需要 Ed 動手。
沒掛的時候就只能讀。**不要再寫「我永遠不能寫」這種話。**

**新主題沒有模板圖不准進排程。** 不然會長出一個永遠發不出去的 slot。

## 檔名的空格：已修（2026-08-31）

原本只有 DAILY 那張的檔名開頭有一個空格，URL 必須寫成 `%20tpl_daily.png`，
2026-08-25 曾因為漏掉 `%20` 發出破圖。

**2026-08-31 拿到 repo 寫入權後處置：新增一份乾淨檔名的 `pics/tpl_daily.png`，
舊的 ` tpl_daily.png`（含前置空格）暫時保留不刪。**
理由：已發布的貼文 attachment 還指著舊網址，先刪會讓歷史貼文當場破圖。
順序是——新檔上線 → 規格改用新網址 → 把歷史貼文的 attachment `PUT` 成新網址 →
確認沒有貼文再引用舊檔 → 才刪掉帶空格的那個。

**新稿一律用 `tpl_daily.png`，不要再寫 `%20`。**

## attachments 格式

```json
{
  "url": "<完整 URL>",
  "title": "<貼文類型>",
  "description": "<貼文類型>",
  "mediaType": "Image",
  "media": {"image": {"width": 1080, "height": 1080, "url": "<同上完整 URL>"}}
}
```
