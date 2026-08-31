# M3 EDIT — 選材與評分

## 職責
決定這一篇寫什麼、給多少篇幅。**判斷只在這裡發生。**

## 輸入
`state/signals.json` 的 signals、`flow/schedule.md` 今天排定的主題、
`standards/thesis.md` 的層次表、`state/thesis-ledger.json` 的收據。

## 輸出
`state/signals.json` 每則訊號標上 score、五項拆解、拉新線或留存線、status。

## 變體
無。公式只有一套，見 `standards/authority.md` 第二部分：
```
分數 = 興趣 + 關聯 + 稀缺 + 量級 + 早期紀錄
>=6 主篇幅 ｜ 4-5 短段落 ｜ <=3 不寫
```

## 邊界（`standards/authority.md` 第一部分）
- **排定的貼文一律要寫。** 素材不足是執行問題，回去補來源，不是跳過。
- 評分只決定**一篇之內**的取捨，不決定一篇該不該存在。
- 訊號不足 → 安靜日自我回顧，不是湊數。
- 早期紀錄那 2 分**必須有收據**，查不到就是 0，不准腦補。

## 失敗行為
訊號全部低於門檻 → 走安靜日自我回顧，回報「無素材過門檻」。
