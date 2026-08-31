# M8 FEEDBACK — 回饋

## 職責
量哪些主題有效，回頭改頻率。**PDCA 的 Check 與 Act。**

## 輸入
M1c 撈回的自己貼文互動、`state/topic-performance.json`。

## 輸出
`state/topic-performance.json` 補上 likes / comments / shares / score；
滿條件時修改 `flow/schedule.md` 的頻率並在該檔變更紀錄寫一行。

## 變體
無。

## 規則
- 每週六跑一次，1 個呼叫。
- `score = likes + 3*comments + 5*shares`。發布未滿 72 小時的不計分。
- 每個主題至少 4 篇才納入判斷。
- 高於全體中位數 1.3 倍 → 頻率上一階；低於 0.7 倍 → 下一階；中間不動。
- **連續兩輪同方向才動手。** 一輪就改是在追雜訊。
- 階梯見 `state/topic-performance.json` 的 `_frequencyLadder`，一次一階不跳級。
- 同時記 `titleStance`（標題有沒有把立場講死）—— 基準線顯示這個訊號可能比主題更強。

## 失敗行為
樣本不足就不動，回報「n 不足，本輪不調整」。**不准為了有動作而動作。**
