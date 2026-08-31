# Ed 的思考框架與句法

**來源：他自己 2026-06 到 2026-08 的 30 篇 eToro 貼文，逐篇讀出來的。**
不是我歸納給他的建議，是他實際在用的推理模式。
寫稿前先讀本文，再讀 `claude/thesis.md`。

---

# 第一部分：句法（我最常搞砸的地方，放在最前面）

## 每一句都要有真正的主詞在做動作

**禁用空主詞的敘述句型。** `it is`、`it sits`、`there is`、`this is the case that`
—— 沒有人在做事，讀者要回頭找 it 指誰。

| 垃圾（我寫的） | 正解 |
|---|---|
| `This quarter it is not broken out at all. It sits inside Edge Computing.` | `Nvidia gave no physical AI number this quarter. Edge Computing carries the whole category.` |
| `A country can hand land and power to a regional cloud partner in a way it will not hand them to a foreign hyperscaler.` | `No government hands land and power to a foreign hyperscaler. It hands them to a local operator.` |
| `48.7bn USD from the hyperscalers, up 13% QoQ` | `The hyperscalers - Amazon, Google, Meta, Microsoft, Oracle: 48.7bn USD, 55% of the total.` |
| `...were all named on the call` | 直接陳述事實，不要寫誰在哪裡講的 |

## 我原本在寫的是賣方研究報告的句法

被動語態、層層限定子句、把主張藏在從句裡。那種寫法的目的是**降低被抓錯的風險**，
代價是讀者要拆解才懂。Ed 的句法相反：

> Bitcoin is structurally incapable of functioning as either an efficient
> medium of exchange or a reliable value anchor.

> Infra is the moat.

> Compute demand is real; power delivery is the constraint.

**主詞在前、動詞明確、一句一件事、結論不藏。**

## 檢查表（每句都要過）

1. 這句的主詞是誰？是不是 `it` / `there`？→ 換成真正的行為者
2. 這句有沒有超過一個子句？→ 拆成兩句
3. 這句有沒有讓讀者更快知道誰做了什麼？→ 沒有就刪
4. 結論有沒有藏在從句裡？→ 拉出來自己成一句

---

# 第二部分：推理框架

## 一、從架構推，不從價格或新聞推

BTC 那篇從頭到尾**沒有提過比特幣的價格**：

> Viewed through the lens of foundational architecture, this premise collapses.

論點全部是結構性的：吞吐量限制、結算層會遷移到哪、機器經濟在架構上需要什麼。
價格、情緒、催化劑都不是他的語言。

## 二、把技術和資產分開

> blockchain triumphs as a transformative protocol, but native cryptocurrencies
> do not - the victor is the technological rail itself, not Bitcoin.

看到一個趨勢，先問「誰真的收得到錢」，而不是「誰是這個趨勢的代名詞」。

## 三、護城河 = 買不到的東西

判準不是「有沒有技術」，而是**「對手能不能用錢買到」**。

> Anyone can buy AI software, but executing personalized medicine is a supply
> chain nightmare... legacy Big Pharma cannot replicate simply by acquiring
> software startups.

護城河被指認成 Norwood 那座能做 batch of 1 的工廠，不是模型，不是專利。

> Infra is the moat.
> Standalone NeoCloud captures a one-time build value with no recurring moat.

## 四、重新分類，錯誤定價來自錯誤分類

> Why Moderna is a Tech Platform, Not Just a Vaccine Stock
> treating mRNA companies as one-hit vaccine wonders is a fundamental mispricing

「市場把它放在哪一類、應該放在哪一類」本身就可以是一篇文章的主軸。

## 五、地緣政治對齊是一個定價因子

> We underweight Korea despite strong fundamentals in memory - a noncommittal
> US-China stance and a track record of Chinese fabs probing its process tech
> make geopolitical alignment a real risk.

**基本面好但對齊有疑慮就低配。** 主流框架沒有這個變數。

## 六、瓶頸在哪裡，價值就在哪裡

> Compute demand is real; power delivery is the constraint.

需求是共識，供給約束才是差異。每個題材都問一次瓶頸在哪一層。

## 七、時機與 S-curve 位置是明寫的變數

> Real alpha requires positioning 2-3 years ahead, which is high-risk, so this
> is our largest cluster: core holdings ... act as ballast against the
> speculative front-runs.

投機性的早期押注要配壓艙的核心持股。不是單純看多，是有結構的部位設計。

## 八、第二階效應：誰不論上層誰贏都收得到錢

> the real winners are the network/edge infrastructure and cybersecurity layer,
> which scales with volume regardless of which application sits on top.

這就是 $NET 在組合裡的原因。不賭誰贏，找收過路費的那一層。

## 九、明講自己跟誰不同意，以及為什麼

> Where we differ: he keeps adding to bitcoin-miners-turned-AI-datacenters.
> We still read that as one-time build value.

## 十、缺陷主動講在前面，不等人問

> a 13F is a June 30 snapshot with a 45-day lag... It tells you where a book
> was, not where it is.

資料的限制自己先說完。這建立的可信度比多一個數字高。

---

# 第三部分：語氣

- 幾乎一律用 **"we"**，不是 "I"。
- 對讀者：`Dear Copiers`、`Hello everyone`。
- 難懂的機制用**類比**：
  > Keytruda removes the cancer's "invisibility cloak", while Moderna's
  > AI-designed mRNA acts as the GPS.
- 結尾常邀請討論：`Let me know your thoughts in the comments`。
- `▫️` 與一般 emoji 是他既有風格。壞掉的只有 `→` `—` `·` `≈`。

---

# 第四部分：互動數據

| 貼文 | 讚 |
|---|---|
| Why $BTC has no future | **8** |
| $BSP is a trap | 6 |
| Hello Stranger（自我介紹） | 5 |
| Why Cloudflare is Relative Strength Leader | 5 |
| The Memory Bill Reaches the Top of the Stack | 5 |
| The Korean Meltdown Tailwind continues | 5 |
| THE FULL THESIS | 4 |
| SECTOR BRIEF: Aschenbrenner Just Flipped | 3 |
| The Second Wave of mRNA | 2 |
| SECTOR BRIEF 關鍵礦產 / 資安（我寫的） | 2 / 2 |

**排前面的都是標題就把立場講死的**：has no future、is a trap、Why X is Y。
中性描述型的排後面。

---

# 我最常犯的錯

| 我的預設 | 他的做法 |
|---|---|
| 空主詞、被動、層層子句 | 主詞在前、動詞明確、一句一件事 |
| 從新聞事件出發 | 從系統架構出發 |
| 報導趨勢 | 問誰在這個趨勢裡真的收得到錢 |
| 描述公司優勢 | 問對手能不能用錢買到那個優勢 |
| 接受市場給的分類 | 主張分類本身是錯的 |
| 只看基本面 | 加一層地緣政治對齊 |
| 講需求成長 | 講供給瓶頸在哪一層 |
| 中性、避免立場 | 立場講死，理由給足，缺陷自己先說 |
| 找最多人引用的事實（＝最沒差異的事實） | 找符合既有框架的事實 |
| 寫出處給讀者看 | 出處是查核者的事，讀者只要事實 |
