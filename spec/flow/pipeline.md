# 生產線 v1

出版社的流程。**選題 → 採訪 → 撰稿 → 編審 → 付印排程 → 出刊 → 檢討。**

---

## 一、兩個時鐘（這是整份改版的重點）

舊設計只有一個時鐘：排程時間到了才開始想要寫什麼。
結果是 slot 到了才發現沒素材，只能臨時湊或整天空白。

**改成生產與出刊分離：**

| | 生產線 | 出刊 |
|---|---|---|
| 何時 | **在 slot 之前跑完** | slot 時間到 |
| 做什麼 | M1 撈資料 → M2 研究 → M3 選材 → M4 撰稿 → M5 編審 → M6 進佇列 | M7 讀佇列，逐字發布，複查 |
| 成本 | 貴，大量 token | 便宜，幾個呼叫 |
| 產出 | 佇列裡多一篇 **status: ready** | 貼文上線 |
| 失敗時 | 還有時間補救，或呈報 Ed | 佇列空 → 立刻回報異常，不臨時寫 |

**出刊那一趟絕對不寫稿。** 到了 slot 還在寫，就是設計失敗。

### 提前量

| 出刊 slot | 生產線何時跑 | 提前 |
|---|---|---|
| 07:00 Slot B | **04:30**（美股 04:00 EDT 收盤後 30 分） | 2.5 小時 |
| 12:00 PULSE | 04:30 那趟一起產出 | 7.5 小時 |
| 18:00 Slot A | **15:00**（台股 13:30、日股 15:00 收盤後） | 3 小時 |
| 19:30 第二篇 | 15:00 那趟一起產出 | 4.5 小時 |

Ed 在 06:00-07:00 之間醒著審稿，剛好落在 04:30 產出與 07:00 出刊中間。
須審核的類型（見 `standards/authority.md` §3）就卡在這個窗口。

---

## 二、流程圖

```
                    ┌──────────── 排程觸發（flow/schedule.md）
                    v
   [M0] 日期關卡  TZ=Asia/Taipei date，結果進回報第一行
                    v
   [M1] MARKET    eToro：績效、持倉、交易、跟單者      ← 一律現撈
                    v
   [M2] RESEARCH  外部：頭條、一手來源、財報數字
                    v
   [M3] EDIT      評分選材，決定這一篇寫什麼、多少篇幅
                    v
   [M4] WRITE     依主題變體的 brief 撰稿
                    v
   [M5] REVIEW    對規範逐項檢查
                    v
   [M6] QUEUE     進 state/post-queue.json，標 publishAt
                    │
        ══════════ 時間分界 ══════════
                    │
   [M7] PUBLISH   到點讀佇列，發布，複查，寫回
                    v
   [M8] FEEDBACK  每週收互動，回頭調頻率
                    v
   [M9] AUDIT     每趟自檢：契約、規範、完整性、改善
                    v
              報告 → state/run-log.md    缺陷 → state/defects.json
```

**M0 進場前先做兩件事：實測日期，以及讀 `run-log.md` 比對有沒有漏跑。**
漏跑的處理與補跑條件見 `flow/resilience.md` §4。

**方向永遠一致，差別只在每一趟叫用哪些模組、用哪個變體。**
模組介面見 `modules/README.md`。

---

## 三、四種趟次

| 趟次 | 叫用 | 典型呼叫數 |
|---|---|---|
| **生產（早）** 04:30 | M0 M1 M2a M3 M4 M5 M6 M9 | 14-20 |
| **生產（晚）** 15:00 | M0 M2 M3 M4 M5 M6 M9 | 10-16 |
| **出刊** 07:00 / 12:00 / 18:00 / 19:30 | M0 M7 M9 | 3-5 |
| **回饋** 週六 08:00 | M0 M1c M8 M9 | 2-3 |

**M0 與 M9 每趟必跑，其餘按需。** 這是省資源的來源：
出刊趟不碰 M1 M2 M3 M4，成本從二十幾個呼叫掉到 3-5 個。

### 每趟讀哪些檔（2026-08-31 新增，`standards/requirements.md` 第六條）

**呼叫數不是成本的全部。** 每趟真正的固定成本是讀規格與讀寫 state 檔，
它比出刊趟的 2-3 個外部呼叫貴一個數量級。所以一趟只讀該趟需要的檔。

| 趟次 | 必讀 | 不讀 |
|---|---|---|
| **生產** | `/INDEX.md`、`flow/pipeline.md`、`flow/resilience.md`、`modules/README.md`、`flow/schedule.md`、該趟叫用的 `modules/m*.md`、`standards/` 中該變體指名的規範、`state/run-log.md`、`state/defects.json`、`state/queue.json` | 沒叫用的模組檔、`archive/` |
| **出刊** | `/INDEX.md`、`modules/m7-publish.md`、`modules/m0-clock.md`、`flow/resilience.md` §4、`state/queue.json`、`state/published-index.json`、`state/run-log.md`、`state/defects.json` | **`flow/pipeline.md`、`modules/README.md`、`standards/writing-rules.md` 等撰稿類規範全部不讀** —— 這一趟不寫稿 |
| **回饋** | `/INDEX.md`、`modules/m8-feedback.md`、`modules/m9-audit.md`、`state/topic-performance.json`、`state/published-index.json`、`state/run-log.md`、`state/defects.json` | 撰稿與出刊類規範 |

**不確定要不要讀，就先不讀，需要時再讀。** 少讀一份檔的代價是多一次 `project_read`，
多讀一份的代價是那份檔的全文，兩者差一個數量級。

出刊趟不跑 M1。它只讀佇列，不重算報酬率 ——
**報酬率在 M4 撰稿當下寫死，文末標 snapshot 日期**（`writing-rules.md` §5.3）。

---

## 四、鐵則

1. **有變動性的東西不准進任何檔案。** 持倉檔數、報酬率、發布歷史、跟單者數，
   一律當場撈。檔案只存「怎麼撈」與「上一次的雜湊」，不存清單與數值。
   2026-08-29 廢止 `positionsFingerprint` 的持倉清單，就是這條。
2. **出刊趟不寫稿。** 佇列空就回報異常，不臨時生產。
3. **空手也要回報。** 沒有回報等於排程沒跑，見 `standards/run-report-spec.md`。
4. **一件事一個家。** 規範在 `standards/`，流程在 `flow/`，角色在 `modules/`，
   會變的在 `state/`。跨層複製內容視為錯誤。
5. **模組失敗要往上報，不要靜默降級。** M2 掛了就說 M2 掛了，
   不要用舊素材硬寫成一篇看起來正常的稿。降級路徑見 `flow/resilience.md` §3。
6. **每個 state 檔只有一個 writer。** 見 `modules/README.md` §1。
   兩個模組寫同一個檔案，就是改 A 壞 B 的來源。
7. **每趟都要自檢。** M9 不准缺席，就算前面全部失敗也要產出報告。
8. **缺陷不准過夜。** 同一個缺陷連續三趟未解，就是規格錯了，回頭改規格。
9. **Token 花在產出上，不花在重讀重寫上。** 見 `standards/requirements.md` 第六條。
   一趟只讀該趟需要的檔（上面 §3 的表），空手趟用短報，
   只 append 的檔案要輪替。**「新增一趟」幾乎永遠是錯的答案** ——
   固定成本大於可變成本，加趟數等於加固定成本。
