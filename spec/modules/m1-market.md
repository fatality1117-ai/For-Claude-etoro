# M1 MARKET — eToro 內部資料

## 職責
把帳號當下的真實狀態撈進來。**這是所有數字的唯一來源。**

## 輸入
`state/perf-latest.json` 的 `snapshotDate`、`state/signals.json` 的 `previousFingerprint`。

## 輸出
- `state/perf-latest.json` — 績效、最多人跟單十名、beatCount
- `state/funnel-log.json` — append 一列 copiers / aumUsd
- `state/nav-log.json` — append 一列淨值與日報酬
- `state/signals.json` — 新交易訊號、更新 `previousFingerprint`

## 變體

**M1a 績效快照。** 先探 `rankings?period=AbsTwoYears` 比對 `lastActivity`
前十碼，相同就跳過其餘。不同才補撈 CurrYear、CurrMonth、most-copied 十名。
兩年一律 `AbsTwoYears`。gain 是小數，0.0485 = +4.85%。四個回應 lastActivity 必須一致。

**M1b 持倉與交易。** `get-my-portfolio-summary`、
`get-my-trading-history(minDate=前一交易日)`。
對 holdings 的 `symbol` 排序後算 sha256，跟 `previousFingerprint.sha256` 比。
不同 → 逐檔 diff 找出新開倉與平倉，寫成 rank 1 訊號。
**持倉清單與檔數不寫進任何檔案，只寫雜湊。**

**M1c 互動。** `GET /api/v1/feeds/users/13809545?take=50` ——
**參數是 `take`，不是 `pageSize`**。供 M8 使用。

## 失敗行為
重試一次。再失敗就回報並停止整趟，**不准用舊數字寫稿**。
`previousFingerprint` 為 null 時建立基準線，回報「無交易訊號，基準線已建立」。
