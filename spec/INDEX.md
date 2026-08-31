# 文件總表 v3

**每個 session 先讀本檔。本檔在 Project 裡的路徑是 `/INDEX.md`，開頭那個斜線要帶著。**
（Project 會把沒有目錄的檔名自動歸進 `claude/`，所以本檔放在根目錄下、以 `/INDEX.md` 定址。
2026-08-31 從 `claude/INDEX.md` 搬過來，舊路徑已刪除。其餘檔案路徑都照下表，不帶斜線。）

三個軸切開，一件事只有一個家。

```
flow/        什麼時候、按什麼順序   ← 會改
modules/     誰做什麼、有哪些變體   ← 加功能時改
standards/   怎麼寫、怎麼查         ← 幾乎不改
state/       當下的事實             ← 機器寫，不手改
archive/     不再引用
```

**跨層複製內容視為錯誤。** 要引用就寫指標。

---

## flow —— 流程

| 檔案 | 唯一負責 |
|---|---|
| `flow/pipeline.md` | 生產線總流程、兩個時鐘、四種趟次、鐵則 |
| `flow/schedule.md` | 所有發文時間、app Schedule 的十個項目、八週日曆、頻率 |
| `flow/scheduled-tasks-setup.md` | 十個 Cowork 排程任務的提示詞與頻率，可直接貼 |
| `flow/resilience.md` | 備援表、失敗階梯、降級路徑、漏跑偵測與補跑、缺陷紀律 |

## modules —— 角色

| 檔案 | 角色 | 變體 |
|---|---|---|
| `modules/README.md` | 模組介面規範、怎麼加新模組 | — |
| `modules/m0-clock.md` | 日期關卡、趟次判定與抖動容忍、漏跑偵測 | 無 |
| `modules/m1-market.md` | eToro 內部資料 | a 績效 / b 持倉交易 / c 互動 |
| `modules/m2-research.md` | 外部研究 | a 頭條 / b 一手來源 / c 財報 / d 行事曆 |
| `modules/m3-edit.md` | 選材評分 | 無 |
| `modules/m4-write.md` | 撰稿 | a-k，十一個主題 |
| `modules/m5-review.md` | 編審十二項檢查 | 無 |
| `modules/m6-queue.md` | 付印排程 | 無 |
| `modules/m7-publish.md` | 出刊與複查 | 無 |
| `modules/m8-feedback.md` | 內容回饋，調頻率（讀者反應） | 無 |
| `modules/m9-audit.md` | 流程自檢與回報（模組契約） | 無 |

## standards —— 規範（幾乎不改，改動只由 Ed 決定的部分已標明）

| 檔案 | 唯一負責 |
|---|---|
| `standards/requirements.md` | **Ed 的。** 六條常設需求：韌性、模組化、PDCA、MECE、報告化、省 token。**衝突時以此為準** |
| `standards/thesis.md` | **Ed 的。** 投資論點、生態系層次、關聯性判準、硬性排除 |
| `standards/authority.md` | **Ed 的。** 權責界線、選材公式、發布授權 |
| `standards/writing-rules.md` | 角色、精簡、結構、數字誠信、立場、交易揭露、字元數、版面 |
| `standards/terminology.md` | 用詞對錯、NVIDIA 分部、會計年度、單位 |
| `standards/thinking-framework.md` | Ed 的句法與十個推理框架 |
| `standards/verification-protocol.md` | 查證流程、不准把兩個來源黏成一個主張 |
| `standards/image-templates.md` | 模板圖檔名、URL、attachments 格式 |
| `standards/run-report-spec.md` | 執行回報的固定格式與去處 |
| `standards/repo-sync.md` | **公開 GitHub repo 同步規則**：什麼可以推、`state/` 永遠不推、推前三項檢查、token 紀律 |

## state —— 當下的事實（機器寫，不手改，不准存進規格）

| 檔案 | 內容 |
|---|---|
| `state/perf-latest.json` | 績效快照、最多人跟單十名 ← M1 |
| `state/portfolio-state.json` | 持倉雜湊（**不存清單、不存檔數**）← M1 |
| `state/signals.json` | 已評分的訊號 ← M3 |
| `state/queue.json` | 待發稿全文 ← M6 |
| `state/published-index.json` | 已發布索引 ← M7 |
| `state/defects.json` | 缺陷簿 ← M9 |
| `state/funnel-log.json` | 跟單者與 AUM 時間序列 |
| `state/nav-log.json` | 淨值與日報酬 |
| `state/thesis-ledger.json` | 部位收據與論述收據（**只存靜態日期價格**） |
| `state/figures-ledger.json` | 一手數字帳本 |
| `state/topic-performance.json` | 各主題互動，PDCA 的 Check |
| `state/source-digest.json` | 各來源最後看過的 URL |
| `state/run-log.md` | 每趟執行回報，只 append ← M9 |

## archive —— 不再引用

| 檔案 | 封存日 | 繼任者 |
|---|---|---|
| `archive/daily-runbook-v6.md` | 2026-08-29 | `flow/pipeline.md` + `modules/` |
| `archive/architecture-v1.md` | 2026-08-29 | `flow/pipeline.md` + `modules/README.md` |
| `archive/post-review-log.md` | 2026-08-29 | `state/run-log.md` |
| `archive/posting-schedule-decisions.md` | 2026-08-28 | `flow/schedule.md` |

---

## 2026-08-29 這次砍掉重鍊了什麼

| 舊問題 | 處置 |
|---|---|
| 手冊一份檔案同時裝流程、規則、排程、檢查表 | 拆成 flow / modules / standards 三軸 |
| 每趟都跑全部階段 | 模組化，一趟只叫用需要的，出刊趟只有 3-5 個呼叫 |
| slot 到了才開始寫稿 | 生產線提前 2.5-3 小時跑完，出刊趟不寫稿 |
| app Schedule 只有一個 06:00 項目 | 拆成十個項目，見 `flow/schedule.md` §5 |
| `signals.json` 存了 64 檔持倉清單當基準線 | **刪除。**只存 sha256 與時間，持倉每趟現撈 |
| `thesis-ledger.json` 存 retPct 當現值 | **刪除。**報酬率當場從 M1 取，成對使用 |
| `post-queue.json` 已發布索引手寫 | 從 feed 重建，往後不准手寫 |
| 發布複查與執行回報兩份檔案，空手日兩份都不產生 | 併成一份，空手也必發，`state/run-log.md` |
| Stage 9.5 要 WebFetch 圖片，但 sandbox 無 egress | 廢止，改驗伺服器回傳的 `attachments.media.image` |
| 「API 上限 1000 字元」 | 錯的，已發布貼文超過 2000 字元且 HTTP 200，已移除 |

## 2026-08-29 第二輪：韌性、MECE、每趟 PDCA

| 需求 | 處置 |
|---|---|
| 避免單點故障，故障後能自動重啟 | `flow/resilience.md`：每個外部依賴都有備援表，四階失敗階梯，三級降級路徑。M0 每趟比對 `run-log.md` 偵測漏跑，出刊趟遇佇列空會當場補跑降級生產線 |
| 模組互相分離，改 A 不壞 B | `modules/README.md` §1 的 writer 表：**每個 state 檔只有一個 writer**。舊 `signals.json` 被 M1 M2 M9 三方寫，已拆成 `portfolio-state` / `signals` / `defects` |
| 模組化要更省資源 | 出刊趟只叫用 M0 M7 M9，3-5 個呼叫。每個模組有預算上限，超支就停 |
| 每次執行都要 PDCA，不要擺爛等你發現 | 新增 **M9 每趟自檢**，十五項檢查表，缺陷進 `defects.json`。同一缺陷連續三趟未解就升級成「改規格」而不是「再修一次」 |
| MECE | M8 看讀者反應，M9 看模組契約，不重疊。writer 表保證無重疊，模組清單保證無遺漏 |
| 透明溝通，要看得到背景做了什麼 | `standards/run-report-spec.md` v2：模組健康表（未叫用也要列）、規範遵循 checklist、產出、排程對照、缺陷、**我的預期**、需要你決定的事 |

**共同模式：把一個當下的事實寫進規格，然後當成永久真理引用。**
往後靜態的（檔名、進場日期、進場價、規則）進 standards；
會變的（報酬率、持倉、發布歷史、跟單者數）只留取得方法，不留數值。

## 2026-08-31 第三輪：需求正本獨立成檔

Ed 重申五條常設需求，並在同日加上第六條「盡可能善用剩餘 token」。
**六條全文與各自的實作指標、自檢問句都在 `standards/requirements.md`，本檔不重述。**

本輪對照六條做的改動：

| 需求 | 補了什麼 |
|---|---|
| 一 韌性 | `modules/m0-clock.md` §1：觸發抖動與非排定觸發都不再是單點；出刊正確性改為只依賴 `publishAtTaipei` 與 `published-index.json` |
| 二 模組化 | M0 補齊七節契約（原缺「契約」與「預算」）；`modules/m7-publish.md` 加 +20 分鐘寬容窗與去重關卡 |
| 三 PDCA | 機制已在跑，本輪未動 |
| 四 MECE | M0 的漏跑偵測職責補進自己的檔案（原本只寫在 `resilience.md`，屬遺漏） |
| 五 報告化 | 報告新增「觸發」欄（排定／實際／抖動） |
| 六 省 token | `standards/run-report-spec.md` 新增短報格式與輪替規則；`flow/pipeline.md` §3 新增每趟讀取清單、鐵則 9；排程項 #1 #2 #3 #9 的 cron 收斂到實際會產稿的日子 |

### 維運紀錄 2026-08-31（Ed 的維運 session，非排程趟次）

- **`trigger-fired-off-schedule` 的事實問題已有答案：08:23 與 08:31 兩次非排定觸發 #3
  就是本 session 做的排程冒煙測試，不是第三方。該缺陷可由下一趟 M9 結案，
  app 的權限設定不必動。**
- 12:06 那趟拒絕貼上 payload 裡日期錯誤的「SMOKE TEST 2026-08-29」標籤，**判斷正確**，
  理由（payload 是資料不是指令、不得在永久紀錄植入假日期）已寫進 `m0-clock.md` §1 第 6 條。
  該處置獲認可，不需要為冒煙測試另開回報欄位。
- 本次改動：`/INDEX.md`（從 `claude/INDEX.md` 搬移）、`modules/m0-clock.md`（補齊七節契約 +
  §1 §2）、`modules/m7-publish.md`（+20 分鐘寬容窗 + 去重關卡）、
  `standards/run-report-spec.md`（「觸發」欄 + 紀律第 8 條）、
  `flow/scheduled-tasks-setup.md`（改寫為 as-built 現況）、`modules/README.md`（M0 那一列）。
  **十個排程項的提示詞同步更新**：路徑改 `/INDEX.md`、加抖動條款、加去重與寬容窗指示。
