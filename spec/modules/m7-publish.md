# M7 PUBLISH — 出刊與複查

## 職責
到點把佇列裡的東西發出去，並證明讀者真的看得到。

## 輸入
`state/queue.json` 的 queue，篩 `publishAtTaipei <= now + 20 分鐘` 且
status 為 `ready` 或 `approved`。
（2026-08-29 12:10 修正：原寫 `state/post-queue.json`，該檔名已不存在。）
（2026-08-31 修正：原為 `<= now`。改成 +20 分鐘寬容窗，因為排程觸發可能早於或晚於
排定時間，`now` 卡在邊界會讓一篇該發的稿等到下一趟。見 `modules/m0-clock.md` §1。）

`state/published-index.json`：發布前逐筆比對，**已在索引裡的不准再發**。

## 輸出
貼文上線；`state/published-index.json` 新增一列；
`state/topic-performance.json` 新增一列（互動數留白）；
複查結果進執行回報。
（2026-08-29 12:10 修正：原寫 `_publishedIndex`，那是舊檔內的欄位名，非現行檔案。）

## 變體
無。

## 流程
0. **去重關卡。** 每一筆候選稿先比對 `state/published-index.json`
   （id 或標題＋類型）。命中就整筆移出 queue、記錄「已發布，跳過」，不再 POST。
   **這一關讓「發哪些稿」只取決於到期與已發，不取決於這一趟叫什麼名字、幾點觸發。**
1. `POST /api/v1/posts`，body 的 message 是純字串，attachments 照
   `standards/image-templates.md` 的格式。
2. `GET /api/v1/posts/{postId}` 取回，逐字比對。
3. 檢查伺服器回傳的 `attachments.media.image` 尺寸與 `tags` 解析結果。
   ~~發布前 WebFetch 圖片 URL~~ **已廢止** —— sandbox 對該 host 無 egress，
   那一步永遠失敗。要驗就驗伺服器真的存下來的東西。
4. 不符 → 當場 `PUT` 修正，重驗，寫進報告。
5. 整筆移出 queue。

## 失敗行為
- **佇列空 → 立刻回報異常，不臨時寫稿。** 生產線該在幾小時前跑完。
  **例外一：12:00 MARKET PULSE（排程項 #3）與 19:30 第二篇（排程項 #9）佇列空是正常狀態，
  記錄「無到期貼文」後結束，不補跑、不記 hard 缺陷。** 這兩個 slot 本來就是候選制。
  依據 `flow/schedule.md` §5，優先於 `flow/resilience.md` §4 的補跑條款。
  **例外二：同一日同一 slot 的稿已由更早觸發的相鄰趟次發掉**（見 `m0-clock.md` §1 第 5 條），
  佇列空是預期結果，記錄「已由 #n 發出」後結束。
- HTTP 非 2xx → 重試一次，再失敗回報並保留佇列，不重複發。
- 只有兩種情況升級給 Ed：需要他的決策，或我修不了（要寫明為什麼修不了）。
