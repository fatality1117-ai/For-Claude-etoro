# M6 QUEUE — 付印排程

## 職責
把過審的稿子放進佇列，標上出刊時間與授權狀態。

## 輸入
M5 通過的草稿、`flow/schedule.md` 的 slot。

## 輸出
`state/post-queue.json` 的 `queue` 新增一筆：
```
id, type, publishAtTaipei, status, snapshotDate, charCount,
imageUrl, imageTitle, imageDescription, scoring, text
```

## status 只有三個值
- `ready` — 可自動發（DAILY / WEEKLY / MONTHLY，見 `standards/authority.md` §3）
- `awaiting-ed-review` — 須 Ed 核准才能發
- `approved` — Ed 已核准，等時間到

## 變體
無。

## 規則
- **text 逐字，發布時一個字都不改。**
- 修改本檔一律先讀再合併，**不准整檔重寫** —— 2026-08-26 曾因整檔重寫洗掉 postId。
- 一發布就整筆移出 queue，只留 id 進 `_publishedIndex`。
  **不要用 status 標記留在 queue 裡**，排程會再看到它。

## 失敗行為
同一個 slot 已有貼文 → 往後推 90 分鐘，超過當日上限 3 篇就順延到隔日並回報。
