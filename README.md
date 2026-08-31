# For-Claude-etoro

eToro Popular Investor **@Edwardhwang888**（AI Alpha）自動化發文系統的公開資產庫。

| 目錄 | 內容 |
|---|---|
| `pics/` | 十一張 1080x1080 貼文模板圖，eToro 直接抓 raw URL |
| `docs/make_templates.py` | 產出 `pics/` 那些圖的生成器。**加新模板改這裡再跑，不要手工做圖** |
| `spec/` | 現行規格 v3：`flow/` 流程、`modules/` 模組、`standards/` 規範 |
| `archive/v0.4/` | 2026-08-25 的舊規格與工具，**不再引用**，只留作歷史 |

## 這裡沒有什麼

**沒有任何帳戶數據。** 淨值、精確 AUM、每日報酬序列、部位進場價、執行紀錄
一律留在 Claude Project 的 `state/`，不進本 repo。理由與檢查清單見
`spec/standards/repo-sync.md`。

**本 repo 是公開的。** 推任何東西之前先過 `repo-sync.md` 第三節那三項檢查。

## 正本在哪裡

**規格的正本是 Claude Project，不是這裡。** 本 repo 的 `spec/` 是快照，
由維運 session 手動同步；排程趟次一律不碰這個 repo。
兩邊不一致時以 Project 為準。
