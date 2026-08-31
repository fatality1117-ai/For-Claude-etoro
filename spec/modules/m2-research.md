# M2 RESEARCH — 外部研究

## 職責
把外面發生的事撈進來，並確認每個數字有出處。

## 輸入
`state/source-digest.json` 的 lastSeenUrl、`state/figures-ledger.json`。

## 輸出
`state/signals.json` 的 signals 陣列（rank 2-6），
`state/figures-ledger.json` 新增的一手數字，
`state/source-digest.json` 更新 lastSeen。

## 變體

**M2a 財經頭條（web_search，5 個呼叫）。** 查詢字串綁 thesis 層次，不綁「熱門」：
```
1. "AI infrastructure" OR semiconductor acquisition merger <日期>
2. earnings beat OR guidance <本週有財報的持倉>
3. AI data center OR power OR critical minerals policy tariff <日期>
4. agentic AI OR AI agents payments OR enterprise adoption <日期>
5. biggest stock movers today <日期>
```
取前三名交給 M3。**排程 session 可用，不受 WebFetch 限制。**

**M2b 一手來源（RSS，6 個呼叫）。** 來源與封鎖清單見 `state/source-digest.json`。
走 WebFetch，排程 session 可能需要互動核可而整段失效。

**M2c 財報深挖。** 順序不准跳：新聞稿 → **CFO Commentary PDF** → 法說會逐字稿
→ 10-Q/10-K → 前四季的以上四項。完整流程見 `standards/verification-protocol.md`。

**M2d 行事曆。** 0 個呼叫。財報日、SEAJ、台灣月營收、中國管制到期日，事先已知。

## 失敗行為
單一來源失敗 → 記錄，跳過，繼續。
**整條線失敗 → 明確回報「M2b 未執行」，不准當成沒事，也不准拿舊素材硬寫。**
查不到不等於不存在，宣稱不存在前必須換第二種方式驗證。
