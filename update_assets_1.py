import json
import re

def update_assets():
    
    lesson_5_data = {
        "canvas": {
            "coreConcepts": [
                {
                    "title": "古典頻率學派 vs. 貝氏統計",
                    "subtitle": "Classical vs. Bayesian Statistics",
                    "content": "貝氏統計將參數視為具不確定性的「未知量 (Unknown quantities)」，而古典統計則將參數量化為固定不變的值。貝氏機率是一種「對知識狀態的主觀評估 (Subjective assessment of the state of knowledge)」，亦即「信念程度 (Degree of belief)」。"
                },
                {
                    "title": "條件機率與貝氏定理",
                    "subtitle": "Conditional Probability & Bayes Theorem",
                    "content": "透過整合新的測試資料或證據 (New event/evidence)，我們能更新原本的「先驗機率 (Prior probability)」，進而推算出「後驗機率 (Posterior probability)」。此一不斷迭代的學習過程被稱為反向機率 (Inverse probability)。"
                },
                {
                    "title": "可信區間與少樣本測試",
                    "subtitle": "Credible Interval & Small Sample Size",
                    "content": "相較於古典的信賴區間 (Confidence interval)，貝氏的可信區間能直接解釋為機率陳述。在工程應用上，貝氏方法能藉由結合專家判斷與歷史數據建立先驗分佈，從而在「小樣本數 (Small sample size)」檢測的情境下達成可靠度驗證。"
                }
            ],
            "practicalExamples": [
                {
                    "title": "案例 1：乳癌檢測 (Mammogram Test)",
                    "content": "一位 40 歲女性得到陽性檢測結果。雖然檢測本身的準確率(靈敏度)高達 87%，且偽陽性率為 12.5%，但因為 40 歲女性患病的先驗機率極低(僅約 1.55%)，最後從貝氏定理算出的實際得病(後驗)機率其實只有約 10% (1 in 10)。這打破了人們對高準確率檢測的直覺迷思。"
                },
                {
                    "title": "案例 2：伴侶出軌 (Underwear Example)",
                    "content": "出差回家發現陌生性感內衣，結合原本對伴侶出軌預設 26%的先驗機率，後驗機率可能高達 78%。更重要的是，如果對伴侶早有一旦出軌的成見(如設定先驗為 90%)，那無論對方如何解釋降低了偽陽性率，後驗機率都會逼近 100%。這說明了「先入為主的成見 (Prior dominates posterior)」很難被新數據推翻。"
                },
                {
                    "title": "案例 3：911 恐怖攻擊 (Terror Attack)",
                    "content": "在第一架飛機撞上世貿中心之前，飛機撞摩天大樓的先驗機率極低(歷史統計約 0.005%)。但當第一架飛機撞上的新證據出現後，反向推斷出「恐怖分子攻擊」的後驗機率瞬間暴升至 33%，這預示了第二架飛機的撞擊。貝氏定理能用來評估這類難以重複實驗的「罕見事件 (Rare events)」。"
                }
            ],
            "teacherWarnings": [
                "注意檢測的「倒置機率誤區」：貝氏理論常常會顛覆傳統直覺。檢測本身準確率高，不代表陽性就一定患病，必須綜合考慮該事件在群體中的先驗機率與偽陽性率。",
                "「成見是一座大山」：貝氏定理告訴我們，如果你的「先驗機率 (Prior)」設定得非常極端(成見極深)，那麼再多的新證據與數據也很難挽回你的想法。擁有貝氏思維的人應該對數據保持開放的態度。",
                "「工程與臨床實務上的優勢」：在實際進行硬體工程驗證或醫藥臨床試驗(如 FDA 指引)時，不可能一直無限制地投入資源(時間/金錢)做大樣本測試。貝氏理論允許我們利用歷史測試資訊(Prior)加上少量的目前測試數據(Data)來不斷疊代更新結果，這對現代工程師與科學家非常關鍵。"
            ]
        },
        "quiz": [
            {
                "id": 1,
                "question": "你在進行一項可靠度工程測試，你的同事認為機率是建立在無限次重複相同實驗上的頻率。但你決定採用貝氏統計方法，請問根據講義，貝氏統計對「機率」的定義為何？",
                "options": [
                    { "id": "A", "text": "參數落在某個隨機區間的固定頻率。" },
                    { "id": "B", "text": "對於當下知識狀態的主觀評估 (Subjective assessment of the state of knowledge)。" },
                    { "id": "C", "text": "測量系統 (Measurement system) 的精確度與準確度誤差。" },
                    { "id": "D", "text": "一個在重複實驗中無法被預測的物理隨機性。" }
                ],
                "correctAnswer": "B",
                "explanation": "此觀點源自講義 P.196 (Core Principle 2)，貝氏機率被認為是對模型參數狀態的主觀評估，亦即「信念程度 (Degree of belief)」，而非古典統計所強調的重複實驗頻率。"
            },
            {
                "id": 2,
                "question": "在分析產品設計參數時，古典統計學派會將分佈參數 (Distribution parameters) 視為「未知但固定的常數 (Fixed but unknown constants)」。請問在貝氏統計中，對於分佈參數的認知有何不同？",
                "options": [
                    { "id": "A", "text": "參數被視為已知且固定的常數。" },
                    { "id": "B", "text": "參數被視為不具任何不確定性的絕對真理。" },
                    { "id": "C", "text": "參數被當作具不確定性的「未知量 (Unknown quantities)」/ 具分佈的隨機變數。" },
                    { "id": "D", "text": "參數完全被忽略不計。" }
                ],
                "correctAnswer": "C",
                "explanation": "講義 P.196 (Core Principle 1) 提到，在貝氏統計中參數被視為 \"unknown quantities\"，也就如同錄音稿中老師強調「參數本身就是一個會變動的隨機分布」，這與古典統計將其視為固定數值截然不同。"
            },
            {
                "id": 3,
                "question": "當工程團隊計算出一個區間，並宣稱「我們可以將這個區間直接解釋為參數落在此範圍內的機率陳述 (Probability statement)」時，請問他們使用的是哪一種區間概念？",
                "options": [
                    { "id": "A", "text": "頻率學派的信賴區間 (Confidence Interval)" },
                    { "id": "B", "text": "貝氏統計的可信區間 (Credible Interval)" },
                    { "id": "C", "text": "六標準差的製程寬容區間 (Tolerance Interval)" },
                    { "id": "D", "text": "假設檢驗的拒絕區間 (Rejection Region)" }
                ],
                "correctAnswer": "B",
                "explanation": "根據講義 P.197 (Core Principle 3)，貝氏區間 (credible interval) 的估計可以直接被解釋為關於給定參數落於其中的「機率陳述」，而古典統計的 confidence interval 則是指抽樣區間本身的機率邊界特性。"
            },
            {
                "id": 4,
                "question": "你使用貝氏定理來分析某次失效發生的原因。一開始你根據歷史經驗預估了一個初始的機率判斷，隨後觀察到了新的測試數據。請問這個「結合歷史信念與新數據」後所更新計算出來的機率稱為什麼？",
                "options": [
                    { "id": "A", "text": "貝塔分佈 (Beta Distribution)" },
                    { "id": "B", "text": "概似函數 (Likelihood)" },
                    { "id": "C", "text": "先驗機率 (Prior Probability)" },
                    { "id": "D", "text": "後驗機率 (Posterior Probability)" }
                ],
                "correctAnswer": "D",
                "explanation": "根據講義 P.192 說明 (Bayes Theorem 3/5)，\"Prior Probability\" (歷史先驗信念) 與 \"Likelihood\" (新數據概似) 結合後，會產生出更新後的 \"Posterior Probability\" (後驗機率)。"
            },
            {
                "id": 5,
                "question": "有一位患有感冒的病人前來看診，醫生想要知道「既然這個病人出現了劇烈咳嗽 (新證據)，那麼他感染特定肺炎的機率是多少？」這個提問方式，體現了貝氏定理相較於傳統古典機率的哪一個重要特性？",
                "options": [
                    { "id": "A", "text": "無限迴圈測試 (Infinite loop testing)" },
                    { "id": "B", "text": "大數法則 (Law of large numbers)" },
                    { "id": "C", "text": "反向機率 (Inverse Probability)" },
                    { "id": "D", "text": "獨立事件假設 (Independent events assumption)" }
                ],
                "correctAnswer": "C",
                "explanation": "來自講義 P.184 (The \"Inverse Probability\" of Bayes Theorem)。古典醫學統計(如計算 Sensitivity)通常會問「如果得病，發出咳嗽的機率是多少」，但貝氏定理問的是反向機率：「既然已出現咳嗽症狀 (Test positive/Evidence)，那麼實際得病的機率是多少？」。"
            }
        ]
    }
    
    lesson_1_data = {
        "canvas": {
            "coreConcepts": [
                {
                    "title": "機率密度函數 (PDF) 與 危害率 (Hazard Rate)",
                    "subtitle": "PDF vs. Hazard Rate",
                    "content": "PDF 不是機率本身，而是「機率的密度」。Hazard Rate 則是站在某一時間點往後看一小段時間內，從「還存活的件數」中會失效的比例。工業界常誤稱為 Failure Rate。"
                },
                {
                    "title": "平均故障時間 (MTTF)",
                    "subtitle": "Mean Time To Failure",
                    "content": "MTTF 是一個期望值。在指數分佈 (Exponential Distribution) 的前提下，產品抵達 MTTF 時，實際上已經有高達 63.2% 的產品失效了，而不是代表產品「保證能活到這個壽命」。"
                },
                {
                    "title": "假設備定 (Hypothesis Testing) 與 判定風險",
                    "subtitle": "Producer vs. Consumer Risk",
                    "content": "做出檢驗決策時永遠帶有風險。生產品管中，把好產品誤判為不良品稱為「生產者風險 (Producer's Risk / Type I Error)」；把不良品誤判為好產品賣給客戶，則為「消費者風險 (Consumer's Risk / Type II Error)」。"
                }
            ],
            "practicalExamples": [
                {
                    "title": "案例 1：壓縮機的壽命測試 (Compressor Hazard Rate)",
                    "content": "20台壓縮機進行測試，第3天還有19台存活，但在第3到第4天之間死去了9台。計算第3天的 Hazard Rate，也就是在這 19 台存活的機器中，有高達將近 47.4% 的機率會在下一天內失效。"
                },
                {
                    "title": "案例 2：燈泡的22.8年壽命 (Light Bulb MTTF)",
                    "content": "某燈泡標榜每日使用3小時可達 22.8 年的「壽命 (Life)」。但這其實是 MTTF。經果指數分佈計算，第一年就會有 4% 的燈泡壞掉，活到第 10 年時僅剩 64% 存活。因此千萬別認為每個燈泡都能活 22.8 年而不壞。"
                },
                {
                    "title": "案例 3：路口計算各色車輛 (Complex System Failures)",
                    "content": "站在路口算不同顏色的車子，黑色代表溫度造成的失效、紅色是震動造成。當這些各自具備不同分佈的獨立失效模式，全部組合在一個龐大的複雜系統中時，系統整體的失效時間分佈會逼近「指數分佈 (Exponential Distribution)」。"
                }
            ],
            "teacherWarnings": [
                "「不要被機率給騙了 (Don't be fooled by chance)」：依靠非常有限的樣本進行驗證測試時，產品可能只是靠運氣剛好通過。如果不了解抽樣誤差 (Sampling Error)，直接把幸運通過的產品量產，之後在客戶端將會面對巨大災難。",
                "「不要誤解 MTTF 就是保證壽命」：很多客戶或工程師會將 MTTF 為 10,000 小時解讀為『這東西能活 10,000 小時』，大錯特錯。在 10,000 小時之前，其實已經有 63.2% 損壞了。MTTF 只是統計學上的期望值！",
                "「釐清生產者與消費者的風險差異」：老闆或客戶問你 Risk 時，你要先問清楚是 Whose risk？因為生產者的 Alpha Risk（錯殺好件）和消費者的 Beta Risk（放過壞件）在決策層面上是完全對立且截然不同的。"
            ]
        },
        "quiz": [
            {
                "id": 1,
                "question": "你在測試一台壓縮機，總共有 20 台，到了第 3 天有 19 台存活，可是第 3 天到第 4 天之間竟然死掉了 9 台。你想計算『站在第 3 天這個時間點，剩下存活的機器在下一個時間段會失效的比例』。根據講義，這個指標稱為什麼？",
                "options": [
                    { "id": "A", "text": "機率密度函數 (Probability Density Function)" },
                    { "id": "B", "text": "危害率 (Hazard Rate)" },
                    { "id": "C", "text": "累積次數分佈 (Cumulative Distribution Function)" },
                    { "id": "D", "text": "平均失效時間 (Mean Time to Failure)" }
                ],
                "correctAnswer": "B",
                "explanation": "講義 P.20 提到，Hazard Rate (h(t)) 是 Number of failures in interval / (Number of working parts at t) * dt。工業界常誤用 Failure Rate 稱呼它。"
            },
            {
                "id": 2,
                "question": "你想求得特定時間區間內的失效機率，例如產品在營運 30 到 45 天之間失效的機率。根據講義，你可以對下列哪一個函數的曲線下方求取面積 (Area under the curve) 來得到這個機率？",
                "options": [
                    { "id": "A", "text": "累積危害率 (Cumulative Hazard Rate, H(t))" },
                    { "id": "B", "text": "中位壽命 (Median Life)" },
                    { "id": "C", "text": "機率密度函數 (Probability Density Function, pdf)" },
                    { "id": "D", "text": "均方根誤差 (Root Mean Square)" }
                ],
                "correctAnswer": "C",
                "explanation": "講義 P.15 和 P.16 明確說明，pdf 本身不是機率，而是機率的密度。要計算任何兩點間的機率，需要積分解求 pdf 曲線下方的面積。"
            },
            {
                "id": 3,
                "question": "你的供應商宣稱他們的燈泡根據測試，MTTF 達到 22.8 年（呈現指數分佈）。你的不知情同事認為燈泡一定能用 22.8 年不壞。根據指數分佈的特性，當時間達到 22.8 年 (MTTF) 時，已經有多大比例的燈泡失效了？",
                "options": [
                    { "id": "A", "text": "4%" },
                    { "id": "B", "text": "36.8%" },
                    { "id": "C", "text": "50%" },
                    { "id": "D", "text": "63.2%" }
                ],
                "correctAnswer": "D",
                "explanation": "講義 P.43 說明，對於指數分佈，抵達 MTTF 時的可靠度為 R(MTTF) = e^-1 = 36.8%。也就是說，有高達 1 - 36.8% = 63.2% 的產品已經失效。"
            },
            {
                "id": 4,
                "question": "你的公司開發了優良的新產品，但是品管部門在出貨抽樣測試時，不慎因為抽樣誤差 (Sampling error) 而把這批好產品判定為不合格並全數報廢。按照假設檢定，公司承擔了何種風險？",
                "options": [
                    { "id": "A", "text": "消費者的風險 (Consumer's Risk) / Type II Error" },
                    { "id": "B", "text": "生產者的風險 (Producer's Risk) / Type I Error" },
                    { "id": "C", "text": "統計檢定力損失 (Statistical Power Drop)" },
                    { "id": "D", "text": "隨機分佈失效 (Random Distribution Failure)" }
                ],
                "correctAnswer": "B",
                "explanation": "講義 P.50 定義 Producer's Risk (Type I Error, Alpha) 是 Calling a good product bad and rejecting it。因為抽樣誤差錯殺良品，這是生產者（即自家公司）得自行承擔報廢成本的風險。"
            },
            {
                "id": 5,
                "question": "一個龐大而複雜的伺服器系統內涵了成千上萬個獨立零件，每個零件可能有自己的壽命分佈（疲勞、溫度、化學老化等）。根據講義，當所有獨立的串聯失效模式統整在同一個複雜系統中時，這整個『系統層級』的失效時間會逼近於哪一種分佈？",
                "options": [
                    { "id": "A", "text": "常態分佈 (Normal Distribution)" },
                    { "id": "B", "text": "韋伯分佈 (Weibull Distribution) 當 Beta > 1 時" },
                    { "id": "C", "text": "指數分佈 (Exponential Distribution)" },
                    { "id": "D", "text": "二項式分佈 (Binomial Distribution)" }
                ],
                "correctAnswer": "C",
                "explanation": "講義 P.48 與課堂舉例 (Drenick's Theorem) 發布的內容顯示，當許多具不同失效機制的獨立元件組合成串聯 (in series) 的複雜巨型系統時，系統整體的失效時間分佈會逼近指數分佈 (Exponential Distribution)。"
            }
        ]
    }
    
    output = f"""const courseData = [
  {{ id: 1, title: "第 1 堂課：基本統計與分佈 (基礎)", isLocked: false, data: {json.dumps(lesson_1_data, ensure_ascii=False)} }},
  {{ id: 2, title: "第 2 堂課", isLocked: true, data: null }},
  {{ id: 3, title: "第 3 堂課", isLocked: true, data: null }},
  {{ id: 4, title: "第 4 堂課", isLocked: true, data: null }},
  {{ id: 5, title: "第 5 堂課：貝氏統計與推論", isLocked: false, data: {json.dumps(lesson_5_data, ensure_ascii=False)} }},
  {{ id: 6, title: "第 6 堂課", isLocked: true, data: null }},
  {{ id: 7, title: "第 7 堂課", isLocked: true, data: null }},
  {{ id: 8, title: "第 8 堂課", isLocked: true, data: null }}
];

export default courseData;"""

    with open('assets.js', 'w', encoding='utf-8') as f:
        f.write(output)
    
if __name__ == '__main__':
    update_assets()
