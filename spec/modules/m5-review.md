# M5 REVIEW — 編審

## 職責
在進佇列之前，拿規範逐項掃過草稿。**不過就不進佇列。**

## 輸入
M4 的草稿、`standards/` 全部。

## 輸出
通過 → 交給 M6。不過 → 退回 M4，記錄退回原因。

## 變體
無。

## 檢查項（逐項，不准跳）
1. 字元數在 `standards/writing-rules.md` §7 的區間內
2. 類型標籤在標題方括號內
3. 每個提到的標的都有 `$`
4. `Not investment advice.`（若含績效或持倉）
5. 署名 `@Edwardhwang888 | Copy for AI Alpha`
6. 所有績效數字來自本趟 M1，且標了 snapshot 日期
7. 報酬率與進場價**同一個基準**（成對取 `pnlPercent` 與 `avgOpenRate`，
   不可與 firstOpen 的 openRate 混寫）
8. 沒有 `→` `—` `·` `≈`
9. 沒有禁止句型：「這不是 X，而是 Y」、先否定再肯定、無主詞斷句
10. 圖片 URL **逐字複製自** `standards/image-templates.md`
11. 沒有把兩個來源黏成一個主張（`verification-protocol.md` 第零條）
12. 沒有查核痕跡進本文（`writing-rules.md` §1）
13. **來源分級**：本文引用或指名的每一個來源，都要在
    `standards/verification-protocol.md` §5 的第 1-3 級裡。
    命中禁用清單（Tom's Hardware 這類消費硬體媒體、內容農場、論壇、
    技術分析媒體）→ **退回 M4**，把那個事實往上游重查或整段拿掉。

## 失敗行為
任一項不過 → 退回 M4 修，修完重跑全部 12 項，**不是只重跑失敗那項**。
三次退回仍不過 → 呈交 Ed，寫明卡在哪一項。
