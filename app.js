import courseData from './assets.js?v=4';

document.addEventListener('DOMContentLoaded', () => {
    // === Elements ===
    // Views
    const viewCanvas = document.getElementById('view-canvas');
    const viewQuiz = document.getElementById('view-quiz');
    const viewResult = document.getElementById('view-result');
    const quizProgressNav = document.getElementById('quiz-progress-nav');

    // Canvas Containers
    const canvasLessonBadge = document.getElementById('canvas-lesson-badge');
    const canvasLessonTitle = document.getElementById('canvas-lesson-title');
    const canvasLessonSubtitle = document.getElementById('canvas-lesson-subtitle');
    const coreConceptsContainer = document.getElementById('core-concepts-container');
    const practicalExamplesContainer = document.getElementById('practical-examples-container');
    const teacherWarningsContainer = document.getElementById('teacher-warnings-container');

    // Buttons
    const startQuizBtn = document.getElementById('start-quiz-btn');
    const backToHomeBtn = document.getElementById('back-to-home-btn');
    const backToCanvasBtn = document.getElementById('back-to-canvas-btn');
    const nextQuestionBtn = document.getElementById('next-question-btn');
    const restartQuizBtn = document.getElementById('restart-quiz-btn');
    const returnHomeBtn = document.getElementById('return-home-btn');
    const canvasBackToHomeBtn = document.getElementById('canvas-back-to-home-btn');

    // Quiz Elements
    const qNumberEl = document.getElementById('q-number');
    const questionTextEl = document.getElementById('question-text');
    const optionsContainer = document.getElementById('options-container');
    const feedbackArea = document.getElementById('feedback-area');
    const feedbackHeader = document.getElementById('feedback-header');
    const explanationText = document.getElementById('explanation-text');
    const currentScoreEl = document.getElementById('current-score');
    const progressFill = document.getElementById('progress-fill');

    // Result Elements
    const finalScoreEl = document.getElementById('final-score');
    const resultMessageEl = document.getElementById('result-message');

    // State Variables
    let currentLessonData = null;
    let currentQuestionIndex = 0;
    let score = 0;
    let isAnswered = false;

    // === Initialization ===
    initHome();

    // === Functions: Home Generation ===
    function initHome() {
        const lessonGridContainer = document.getElementById('lesson-grid-container');
        lessonGridContainer.innerHTML = ''; // clear

        courseData.forEach((lesson) => {
            const card = document.createElement('div');

            if (lesson.isLocked) {
                card.className = 'glass-card lesson-card locked-lesson';
                card.innerHTML = `
                    <div class="lesson-icon">🔒</div>
                    <h3>${lesson.title}</h3>
                    <p>敬請期待 (Coming Soon)</p>
                `;
            } else {
                card.className = 'glass-card lesson-card active-lesson';
                card.innerHTML = `
                    <div class="lesson-icon pulse-anim-subtle">📖</div>
                    <h3>${lesson.title}</h3>
                    <p>點擊進入課程精華畫布</p>
                `;
                card.addEventListener('click', () => loadLesson(lesson));
            }
            lessonGridContainer.appendChild(card);
        });
    }

    function loadLesson(lesson) {
        currentLessonData = lesson.data;

        // Populate Canvas Header
        canvasLessonBadge.textContent = lesson.title + " Analysis Complete";

        // Dynamically set title based on lesson (For now, assume lesson 1 has specific title)
        if (lesson.id === 1) {
            canvasLessonTitle.innerHTML = `課程精華摘要<br/><span class="gradient-text">貝氏統計與推論</span>`;
        } else {
            canvasLessonTitle.innerHTML = `課程精華摘要<br/><span class="gradient-text">${lesson.title}</span>`;
        }

        initCanvas(currentLessonData);
        showView(viewCanvas);
    }

    // === Functions: Canvas Generation ===
    function initCanvas(data) {
        // Clear containers
        coreConceptsContainer.innerHTML = '';
        practicalExamplesContainer.innerHTML = '';
        teacherWarningsContainer.innerHTML = '';

        // Core Concepts
        data.canvas.coreConcepts.forEach((concept) => {
            const card = document.createElement('div');
            card.className = 'glass-card concept-card';
            card.innerHTML = `
                <h3 class="card-title">${concept.title}</h3>
                <h4 class="card-subtitle">${concept.subtitle}</h4>
                <p class="card-content">${concept.content}</p>
            `;
            coreConceptsContainer.appendChild(card);
        });

        // Practical Examples
        data.canvas.practicalExamples.forEach((example) => {
            const block = document.createElement('blockquote');
            block.className = 'example-quote blur-card';
            block.innerHTML = `
                <h4>${example.title}</h4>
                <p>${example.content}</p>
            `;
            practicalExamplesContainer.appendChild(block);
        });

        // Teacher Warnings
        data.canvas.teacherWarnings.forEach((warning) => {
            const warnCard = document.createElement('div');
            warnCard.className = 'warning-card glass-card';
            warnCard.innerHTML = `
                <div class="warning-icon">!</div>
                <p class="warning-text">${warning}</p>
            `;
            teacherWarningsContainer.appendChild(warnCard);
        });
    }

    // === Functions: View Navigation ===
    const viewHome = document.getElementById('view-home');
    function showView(viewToShow) {
        [viewHome, viewCanvas, viewQuiz, viewResult].forEach(v => {
            v.style.display = 'none';
            v.classList.remove('active-view');
        });
        viewToShow.style.display = 'block';

        // Allow a tiny delay so display:block applies before opacity transition
        setTimeout(() => {
            viewToShow.classList.add('active-view');
        }, 10);
    }

    // === Functions: Quiz Logic ===
    function startQuiz() {
        showView(viewQuiz);
        quizProgressNav.classList.remove('hidden');
        currentQuestionIndex = 0;
        score = 0;
        updateScoreDisplay();
        loadQuestion();
    }

    function loadQuestion() {
        isAnswered = false;
        feedbackArea.classList.add('hidden');
        nextQuestionBtn.classList.add('hidden');

        const currentQ = currentLessonData.quiz[currentQuestionIndex];
        qNumberEl.textContent = `Question ${currentQuestionIndex + 1} of ${currentLessonData.quiz.length}`;
        questionTextEl.textContent = currentQ.question;

        // Progress bar formatting
        const progressPercentage = ((currentQuestionIndex) / currentLessonData.quiz.length) * 100;
        progressFill.style.width = `${progressPercentage}%`;
        quizProgressNav.querySelector('.progress-text').textContent = `${currentQuestionIndex} / 5`;

        // Clear existing options
        optionsContainer.innerHTML = '';

        // Generate options
        currentQ.options.forEach(opt => {
            const optBtn = document.createElement('button');
            optBtn.className = 'option-btn input-transition';
            optBtn.dataset.id = opt.id;
            optBtn.innerHTML = `<span class="opt-label">${opt.id}</span> <span class="opt-text">${opt.text}</span>`;

            optBtn.addEventListener('click', () => handleOptionClick(optBtn, currentQ.correctAnswer, currentQ.explanation));
            optionsContainer.appendChild(optBtn);
        });
    }

    function handleOptionClick(selectedBtn, correctId, explanation) {
        if (isAnswered) return; // Prevent multiple clicks
        isAnswered = true;

        const allOptions = optionsContainer.querySelectorAll('.option-btn');
        allOptions.forEach(btn => {
            btn.disabled = true; // disable all

            if (btn.dataset.id === correctId) {
                btn.classList.add('correct');
            } else if (btn === selectedBtn && btn.dataset.id !== correctId) {
                btn.classList.add('incorrect');
            } else {
                btn.style.opacity = '0.5'; // fade out non-selected/non-correct
            }
        });

        // Check if selected is correct
        const isCorrect = selectedBtn.dataset.id === correctId;

        if (isCorrect) {
            score++;
            updateScoreDisplay();
            feedbackHeader.textContent = '✅ 解析與出處';
            feedbackHeader.className = 'feedback-header success-text';
        } else {
            feedbackHeader.textContent = '❌ 原來如此...';
            feedbackHeader.className = 'feedback-header error-text';
        }

        explanationText.textContent = explanation;
        feedbackArea.classList.remove('hidden');

        // Show Next / Finish Button
        nextQuestionBtn.classList.remove('hidden');
        if (currentQuestionIndex === currentLessonData.quiz.length - 1) {
            nextQuestionBtn.textContent = "查看測驗結果";
        } else {
            nextQuestionBtn.textContent = "下一題";
        }
    }

    function nextQuestion() {
        currentQuestionIndex++;
        if (currentQuestionIndex < currentLessonData.quiz.length) {
            loadQuestion();
        } else {
            finishQuiz();
        }
    }

    function updateScoreDisplay() {
        currentScoreEl.textContent = `得分: ${score}`;
    }

    function finishQuiz() {
        showView(viewResult);
        quizProgressNav.classList.add('hidden');

        finalScoreEl.textContent = score;

        if (score === 5) {
            resultMessageEl.textContent = "太棒了！你完美掌握了講義與錄音的所有觀念，貝氏統計難不倒你！";
        } else if (score >= 3) {
            resultMessageEl.textContent = "表現不錯！你已經抓住了核心精神，可以再針對錯題複習一下講義。";
        } else {
            resultMessageEl.textContent = "再接再厲！貝氏統計的有些觀念滿反直覺的，回到畫布重新吸收精華吧！";
        }
    }

    function resetToCanvas() {
        showView(viewCanvas);
        quizProgressNav.classList.add('hidden');
    }

    function goHome() {
        showView(viewHome);
        quizProgressNav.classList.add('hidden');
    }

    // === Event Listeners ===
    startQuizBtn.addEventListener('click', startQuiz);
    backToCanvasBtn.addEventListener('click', resetToCanvas);
    backToHomeBtn.addEventListener('click', goHome);
    nextQuestionBtn.addEventListener('click', nextQuestion);
    restartQuizBtn.addEventListener('click', startQuiz);
    returnHomeBtn.addEventListener('click', resetToCanvas);
    canvasBackToHomeBtn.addEventListener('click', goHome);
});
