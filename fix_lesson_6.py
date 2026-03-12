import json

# Proper Lesson 6 data
lesson_6_data = {
    "canvas": {
        "coreConcepts": [
            {"title": "貝氏定理與賠率 (Odds)", "subtitle": "Bayesian Confidence & Odds", "content": "貝氏統計中，我們用主觀信心度 (Subjective Confidence) 來看待參數發生的機率。而賠率 (Odds) 是該事件發生機率與不發生機率的比值。"}, 
            {"title": "設計變更與可靠度活動指標", "subtitle": "DCC & RAM Factor", "content": "透過評估設計變更條件 (DCC) 與可靠度活動成熟度 (RAM)，能將過往產品資料的可靠度水平轉換到新設計上，進而發展出我們的事前信心度。"}, 
            {"title": "共軛分佈對 (Conjugate Pairs)", "subtitle": "Mathematical Convenience", "content": "當事前分配 (Prior) 與事後分配 (Posterior) 屬於同一個參數家族時，稱為共軛對。這可大幅減少運用貝氏定理時數學運算的複雜度。"}, 
            {"title": "Beta 事前分配", "subtitle": "Beta Prior Distribution", "content": "Beta 分配常作為二項式測試 (Binomial testing) 中失效機率的共軛事前分配，其中參數 a 與 b 可分別視為「偽失效數」與「偽零失效存活數」。"}
        ],
        "practicalExamples": [
            {"title": "案例 1：底特律車廠的 LCC 策略 (Cost cutting)", "content": "2008年金融海嘯時，車廠必須將美國供應商換成其他國家的低成本零件以求生存。為了評估新零件的可靠度，他們便利用貝氏方法，根據過往資料及設計變更的 DCC 指標推算出事前信心度，成功減少了實體驗證的樣本數需求與成本。"}, 
            {"title": "案例 2：工程測試對策法", "content": "當你面對一個微幅改版的控制器設計，若用古典統計可能要打十幾個樣本才能證明可靠度；但因為是微小變更(Minor Improvement)，搭配不錯的可靠度測試成熟度(RAM)，我們就具備了高自信度的先驗(Prior)，可以讓所需的測試樣本驟降至原本的三分之一。"}
        ],
        "teacherWarnings": [
            "「不要對信心度過度自信」：很多人常誤以為 Odds 10:1 代表 90% 的信心度 (Confidence)，這是不對的！10:1 的 Confidence 是 10 / (1+10) = 90.9%。而 19:1 才是真正的 95% Confidence！大家在做主觀信心度評估時，往往會忽略這種數學直覺上的誤差！", 
            "「確保共軛對的適用性」：選擇 Beta 作為事前分配是因為二項式驗證具有數學上的共助性。如果在處理其他非二項式失效分佈時，必須選用其他對應的共軛分配如 Gamma，不要一招走天下。"
        ]
    },
    "quiz": [
        {"id": 1, "question": "根據講義，Odds (賠率) 的定義為？", "options": [{"id": "A", "text": "事件發生機率與不發生機率的比值"}, {"id": "B", "text": "發生機率的自然對數"}, {"id": "C", "text": "信賴區間的寬度"}, {"id": "D", "text": "事前與事後機率的乘積"}], "correctAnswer": "A", "explanation": "講義 P.200 中提到：Odds is calculated as the ratio of the number of events producing that outcome to the number of events that do not."}, 
        {"id": 2, "question": "Logit 變換的數學定義為何？", "options": [{"id": "A", "text": "ln(Probability)"}, {"id": "B", "text": "ln(Odds)"}, {"id": "C", "text": "Odds / (1+Odds)"}, {"id": "D", "text": "exp(Probability)"}], "correctAnswer": "B", "explanation": "講義 P.202 定義：Logit = ln(Odds)。它能將介於 0 與 1 之間的機率值轉換為範圍更廣的數值 (-∞ 到 +∞) 以利資料處理與運算。"}, 
        {"id": 3, "question": "在計算貝氏可靠度更新時，用來評估「設計變更對可靠度的衝擊」的指標為何？", "options": [{"id": "A", "text": "RAM Factor"}, {"id": "B", "text": "Conjugate Pair"}, {"id": "C", "text": "DCC Factor"}, {"id": "D", "text": "Beta Prior"}], "correctAnswer": "C", "explanation": "講義 P.205 中定義 DCC (Design Change Condition) Factor 為：This is the assessment by Engineering of the impact of design change to reliability。評估設計改善或妥協的影響程度。"}, 
        {"id": 4, "question": "關於共軛對 (Conjugate Pairs) 的特性，下列何者正確？", "options": [{"id": "A", "text": "指的是兩個完全不同的機率分佈"}, {"id": "B", "text": "事前分配與事後分配具有相同的參數形式"}, {"id": "C", "text": "只能應用於韋伯分配 (Weibull)"}, {"id": "D", "text": "事前分配與事後分配的平均值必定為 0"}], "correctAnswer": "B", "explanation": "講義 P.213 定義：a prior distribution and the posterior distribution are of the same parametric form is called conjugacy. 這會讓更新公式變得數學好處理。"}, 
        {"id": 5, "question": "在 Beta 事前分配 (Beta Prior Distribution) 中，參數 a 與 b 在貝氏更新的實務意涵代表什麼？", "options": [{"id": "A", "text": "a 為變異數，b 為平均值"}, {"id": "B", "text": "a 為對數勝率，b 為置信區間"}, {"id": "C", "text": "a 為形狀參數，b 為尺度參數"}, {"id": "D", "text": "a 為偽失效數，b 為偽存活數"}], "correctAnswer": "D", "explanation": "講義 P.228 說明：'a' represents the pseudo number of failures, and 'b' represents the pseudo number of survivors. 這與進行測試後獲得的真實失效與存活數能直接相加進行事後機率更新。"}
    ]
}

lesson_6_str = f'  {{ id: 6, title: "第 6 堂課：主觀信心度與事前分配", isLocked: false, data: {json.dumps(lesson_6_data, ensure_ascii=False)} }},'

with open("assets.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Replace line 7 (which is index 6)
lines[6] = lesson_6_str + "\n"

with open("assets.js", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Lesson 6 fixed in assets.js")
