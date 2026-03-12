import json
import os

def update_assets():
    with open('assets.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # The canvas data for Lesson 6
    lesson_6_data = {
        "canvas": {
            "title": "Lesson 6 核心觀念畫布",
            "content": """
<div class=\"canvas-section\">
    <h3>💡 核心觀念畫布</h3>
    <ul>
        <li><strong>貝氏定理與信賴度 (Bayesian Confidence & Odds)</strong>: 貝氏統計中，我們用主觀信心度 (Subjective Confidence) 來看待參數發生的機率。而賠率 (Odds) 是該事件發生機率與不發生機率的比值。</li>
        <li><strong>設計變更與可靠度活動指標 (DCC & RAM Factor)</strong>: 透過評估設計變更條件 (DCC) 與可靠度活動成熟度 (RAM)，能將過往產品資料的可靠度水平轉換到新設計上。</li>
        <li><strong>共軛分佈對 (Conjugate Pairs)</strong>: 當事前分配 (Prior) 與事後分配 (Posterior) 屬於同一個參數家族時，稱為共軛對。這可大幅減少數學運算的複雜度。</li>
        <li><strong>Beta 事前分配 (Beta Prior Distribution)</strong>: 常作為二項式測試 (Binomial testing) 中失效機率的共軛事前分配，其中參數 a 與 b 可視為「偽失效數」與「偽零失效存活數」。</li>
    </ul>
</div>

<div class=\"canvas-section\">
    <h3>🛠️ 實務案例拆解</h3>
    <blockquote>
        老師在錄音中舉了底特律三大車廠的例子：2008 年金融海嘯時，多數車廠宣告破產重組，因此衍生了 LCC (Low Cost Country) 的零件替換方案 (Cost cutting)。為了評估將美國供應商換成其他國家的低成本零件，需要重新量測其可靠度。這時就可以使用貝氏方法，根據過往測試資料、供應商提供的資訊以及小幅度設計變更的 DCC 指標，推算出我們已具備多少的事前信心度 (Prior Confidence)，進而減少實體驗證的樣本數需求，省下可觀的測試成本。
    </blockquote>
</div>

<div class=\"canvas-section warning-section\">
    <h3>⚠️ 老師特別叮嚀</h3>
    <p><em>很多人常誤以為 Odds 10:1 代表 90% 的信心度 (Confidence)，其實這是不對的！10:1 的 Confidence 是 10 / (1+10) = 90.9%。而 19:1 才是真正的 95% Confidence！大家在做主觀信心度評估時，往往會「過度自信 (overconfident)」，要特別注意校正自己對機率的直覺。</em></p>
</div>
"""
        },
        "quiz": [
            {
                "id": "q1",
                "question": "根據講義，Odds (賠率) 的定義為？",
                "options": ["A. 事件發生機率與不發生機率的比值", "B. 發生機率的自然對數", "C. 信賴區間的寬度", "D. 事前與事後機率的乘積"],
                "answer": "A. 事件發生機率與不發生機率的比值",
                "explanation": "講義 P.200 中提到：Odds is calculated as the ratio of the number of events producing that outcome to the number of events that do not."
            },
            {
                "id": "q2",
                "question": "Logit 變換的數學定義為何？",
                "options": ["A. ln(Probability)", "B. ln(Odds)", "C. Odds / (1+Odds)", "D. exp(Probability)"],
                "answer": "B. ln(Odds)",
                "explanation": "講義 P.202 定義：Logit = ln(Odds)。它能將介於 0 與 1 之間的機率值轉換為範圍更廣的數值以利運算。"
            },
            {
                "id": "q3",
                "question": "在計算貝氏可靠度更新時，用來評估「設計變更對可靠度的衝擊」的指標為何？",
                "options": ["A. RAM Factor", "B. Conjugate Pair", "C. DCC Factor", "D. Beta Prior"],
                "answer": "C. DCC Factor",
                "explanation": "講義 P.205 中定義 DCC (Design Change Condition) Factor 為：This is the assessment by Engineering of the impact of design change to reliability."
            },
            {
                "id": "q4",
                "question": "關於共軛對 (Conjugate Pairs) 的特性，下列何者正確？",
                "options": ["A. 指的是兩個完全不同的機率分佈", "B. 事前分配與事後分配具有相同的參數形式", "C. 只能應用於韋伯分配 (Weibull)", "D. 事前分配與事後分配的平均值必定為 0"],
                "answer": "B. 事前分配與事後分配具有相同的參數形式",
                "explanation": "講義 P.213 定義：a prior distribution and the posterior distribution are of the same parametric form is called conjugacy."
            },
            {
                "id": "q5",
                "question": "在 Beta 事前分配 (Beta Prior Distribution) 中，參數 a 與 b 在貝氏更新的實務意涵代表什麼？",
                "options": ["A. a 為變異數，b 為平均值", "B. a 為對數勝率，b 為置信區間", "C. a 為形狀參數，b 為尺度參數", "D. a 為偽失效數，b 為偽存活數"],
                "answer": "D. a 為偽失效數，b 為偽存活數",
                "explanation": "講義 P.228 說明：'a' represents the pseudo number of failures, and 'b' represents the pseudo number of survivors."
            }
        ]
    }

    # Find where courseData is defined
    start_idx = content.find('const courseData = [')
    if start_idx == -1:
        print("Could not find 'const courseData = [' in assets.js")
        return

    # Extract the JSON part of lessons
    # We'll just carefully replace the slot for lesson 6
    
    # Simple replace since we control the structure
    lesson_6_str = f'''  {{ id: 6, title: "第 6 堂課：主觀信心度與事前分配", isLocked: false, data: {{ "canvas": {json.dumps(lesson_6_data["canvas"], ensure_ascii=False)}, "quiz": {json.dumps(lesson_6_data["quiz"], ensure_ascii=False)} }} }},'''

    # It's currently locked:
    search_str_1 = '  { id: 6, title: "第 6 堂課", isLocked: true, data: null },'
    search_str_2 = '  { id: 6, title: "第 6 堂课", isLocked: true, data: null },'

    if search_str_1 in content:
        new_content = content.replace(search_str_1, lesson_6_str)
    elif search_str_2 in content:
        new_content = content.replace(search_str_2, lesson_6_str)
    else:
        # regex or manual insertion
        import re
        new_content = re.sub(r'  \{\s*id:\s*6,\s*title:\s*".*?",\s*isLocked:\s*true,\s*data:\s*null\s*\},', lesson_6_str, content)


    with open('assets.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Lesson 6 added successfully!")

if __name__ == "__main__":
    update_assets()
