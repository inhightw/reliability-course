import json

def update_assets():
    with open('assets.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # We will just rewrite it to properly include Lesson 4 data.
    
    lesson_4_data = {
        "canvas": {
            "coreConcepts": [
                {
                    "title": "隨機性與領域特異性",
                    "subtitle": "Degrees of Randomness",
                    "content": "物理科學的隨機來自測量誤差與材料微觀差異；社會科學存在「霍桑效應 (Hawthorne effect)」，受試者意識到被觀察就會改變行為；生化領域有「安慰劑效應 (Placebo effect)」。隨機性必須有「程度 (Degree)」方能被量化比較。"
                },
                {
                    "title": "公理化 vs. 主觀機率",
                    "subtitle": "Kolmogorov Axioms vs. Ramsey",
                    "content": "Kolmogorov 在1933年將傳統機率公理化 (頻率學派)。但 Ramsey 提出主觀機率 (Subjective Probability)：機率不是客觀絕對的存在，而是根據個人知識與經驗所產生的「信念程度 (Degree of belief)」的展現。"
                },
                {
                    "title": "母體參數的本質",
                    "subtitle": "Classical vs. Bayesian View",
                    "content": "古典統計將母體參數 (如壽命分佈) 視為「未知但固定的常數」。貝氏統計則徹底顛覆，認為參數本身就具備不確定性，是「隨機變數 (Uncertain quantities)」，藉由整合過去經驗建立先驗分佈，結合測試數據來降低所需樣本。"
                }
            ],
            "practicalExamples": [
                {
                    "title": "案例 1：連續出正面的銅板 (Accumulating Evidence)",
                    "content": "若一個銅板連續投10次正面，數學家可能會說是機率極小的巧合(1024分之一)。但若連出 20 次正面，機率低至 100萬分之一。隨著實證證據(Empirical evidence)的累積，你的主觀機率會判定這枚硬幣是「出老千被動過手腳」。"
                },
                {
                    "title": "案例 2：西屋工廠的神秘提效 (Hawthorne Effect)",
                    "content": "芝加哥西屋這家工廠為測試環境對產能的影響，進行實驗。結果驚人：無論是改善照明，還是故意把燈弄暗，甚至什麼都不做，工人的效率都提高了！因為人們意識到「自己正在被觀察檢測」，自發改變了行為，破壞了統計的獨立性。"
                },
                {
                    "title": "案例 3：願不願意賭一把？ (Measuring Belief)",
                    "content": "Ramsey 主張，測試一個人的「主觀信念程度」，最客觀的方法就是看他是否願意把信念化作「行動 (Action)」。如果你非常確定明天會下雨，你願不願意為此下賭注或投資？信念必須能被測量且具有一致性。"
                }
            ],
            "teacherWarnings": [
                "「避免允許多次失效的 RDT 測試」：理論上 RDT 可以允許 1 個或多個失效，但實務上，若產品壞了，供應商會盡全力推託這跟設計無關(為求過關)，而客戶則會死咬不放。為了避免災難性的爭議與扯皮，實務上寧可宣稱零失效並增加測試時間或樣本！",
                "「Empirical 不等於 Experiential」：Empirical (實證) 是指基於客觀數據與觀察的事實，而 Experiential 是單純的主觀經驗。實證證據的厚度決定了貝氏統計中後驗機率的說服力，千萬不要英譯混用。",
                "「備受爭議但不可或缺的貝氏理論」：引入過往經驗可大幅降低高可靠性產品的測試時間。但也因過於依賴先驗假設 (Prior)，有些狀況下你不做測試也能證明達標，這飽受頻率學派的抨擊。但對於無法大量重現的事件(如核外洩)，這卻是唯一解方。"
            ]
        },
        "quiz": [
            {
                "id": 1,
                "question": "講義提及，機率學發展史中，有位蘇聯數學家在 1933 年首次將機率「公理化 (Axiom System)」，指出所有機率大於等於 0，總和為 1 等等。這位數學家是誰？",
                "options": [
                    { "id": "A", "text": "拉普拉斯 (Laplace)" },
                    { "id": "B", "text": "科爾莫哥洛夫 (Andrey Kolmogorov)" },
                    { "id": "C", "text": "托馬斯·貝葉斯 (Thomas Bayes)" },
                    { "id": "D", "text": "法蘭克·拉姆齊 (Frank Ramsey)" }
                ],
                "correctAnswer": "B",
                "explanation": "講義 P.162 與錄音提到，Andrey Kolmogorov 是在 1933 年首次提出機率的三大公理，將傳統機率理論正式公理化 (Axiom System of Probability) 的人。"
            },
            {
                "id": 2,
                "question": "授課錄音中分析了物理、社會與生化不同領域的「隨機性」。在社會科學中，有一種效應指出：「當受測者察覺到自己正在被觀察或被實驗時，其行為模式會自發改變，導致實驗結果失去隨機性」。此效應稱為什麼？",
                "options": [
                    { "id": "A", "text": "安慰劑效應 (Placebo effect)" },
                    { "id": "B", "text": "霍桑效應 (Hawthorne effect)" },
                    { "id": "C", "text": "雙盲測試效應 (Double blind effect)" },
                    { "id": "D", "text": "大數法則逆反作用" }
                ],
                "correctAnswer": "B",
                "explanation": "來自 P.160。在西方電器工廠的實驗發現，受試者只要知道自己在被實驗，就會有不同於自然狀態的表現，這被稱為 Hawthorne effect (霍桑效應)。"
            },
            {
                "id": 3,
                "question": "講義中提問：「當你連續投擲 20 次銅板都是正面，你會如何判斷？」在貝氏觀點下，比起只丟 10 次，當「連續出現正面的次數」越多，因為什麼因素的累積，會使得你的主觀機率堅信這枚銅板是有問題的 (出老千)？",
                "options": [
                    { "id": "A", "text": "平均維修時間 (MTTR) 的顯著下降" },
                    { "id": "B", "text": "先驗偏見 (Prior prejudice)" },
                    { "id": "C", "text": "實證證據的累積 (Accumulating empirical evidence)" },
                    { "id": "D", "text": "獨立且相同事件原則 (IID) 被印證" }
                ],
                "correctAnswer": "C",
                "explanation": "根據講義 P.165 說明，當不可思議的巧合一再發生，是 \"The accumulating empirical evidence\" (逐步累積的實證證據) 改變了我們對於該事件的主觀機率。"
            },
            {
                "id": 4,
                "question": "根據 Frank Ramsey 提出的主觀概論，一個人對於某件事情的「信念程度 (Degree of belief)」究竟有多強大，最直接客觀的衡量方式是什麼？",
                "options": [
                    { "id": "A", "text": "計算他的智商與資歷。" },
                    { "id": "B", "text": "讓他寫一份發誓聲明。" },
                    { "id": "C", "text": "看他願不願意用實際的行動或金錢來做「打賭 (Betting/Action)」。" },
                    { "id": "D", "text": "使用常態分佈去套用他的說法。" }
                ],
                "correctAnswer": "C",
                "explanation": "講義 P.166 提到，Ramsey 主張信念可透過行動衡量：\"measured by finding what odds the individual would accept when betting on that outcome\"。願意真的去賭，才代表信念真實存在。"
            },
            {
                "id": 5,
                "question": "在可靠度工程中，古典統計與貝氏統計對於「產品母體參數 (Population parameters)」(例如 Weibull 的 Beta 值) 有著根本不同的認知。以下哪一個描述符合貝氏統計的強烈主張？",
                "options": [
                    { "id": "A", "text": "參數是固定但不為人知的常數 (Fixed but unknown constants)。" },
                    { "id": "B", "text": "參數本身也是具備不確定性的，應被視為隨機變數，有其自身的分佈 (Uncertain quantities)。" },
                    { "id": "C", "text": "參數應該是固定已知，且全球通用的真理數值。" },
                    { "id": "D", "text": "產品壽命不具備任何母體參數，全是純然的隨機。" }
                ],
                "correctAnswer": "B",
                "explanation": "講義 P.169 (Classical vs. Bayesian 2/2) 說明，古典派認為參數是固定卻未知的。但貝氏派認為 \"treat these population parameters as uncertain, not fixed, quantities\"。"
            }
        ]
    }
    
    # Let's extract everything inside `courseData = [...]`
    import re
    match = re.search(r'const courseData = \[(.*?)\];\s*export default courseData;', content, re.DOTALL)
    if not match:
        print("Could not find courseData.")
        return
        
    array_content = match.group(1)
    
    # Replace lesson 4 placeholder.
    # Searching for: { id: 4, title: "第 4 堂課", isLocked: true, data: null }
    # We will replace it with the new object.
    
    new_lesson_4_json = json.dumps(lesson_4_data, ensure_ascii=False)
    
    # We just do string replace for Lesson 4
    old_l4 = '{ id: 4, title: "第 4 堂課", isLocked: true, data: null }'
    new_l4 = f'{{ id: 4, title: "第 4 堂課：隨機性與主觀機率 (貝氏前傳)", isLocked: false, data: {new_lesson_4_json} }}'
    
    new_content = content.replace(old_l4, new_l4)
    
    with open('assets.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == '__main__':
    update_assets()
