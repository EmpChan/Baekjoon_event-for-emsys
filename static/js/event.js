// 폼 제출 처리
document.getElementById('registerForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const userId = document.getElementById('userId').value;
    const password = document.getElementById('password').value;
    const handle = document.getElementById('handle').value;
    
    if (userId && password && handle) {
        alert(`환영합니다, ${handle}님! 이벤트 참가 신청이 완료되었습니다.`);
        
        // 폼 초기화
        this.reset();
    }
});

// 실시간 점수 업데이트 시뮬레이션
function updateScores() {
    const scoreElements = document.querySelectorAll('.score');
    scoreElements.forEach(element => {
        const currentScore = parseInt(element.textContent.replace(',', ''));
        const randomIncrease = Math.floor(Math.random() * 50);
        const newScore = currentScore + randomIncrease;
        element.textContent = newScore.toLocaleString();
    });
}

// 30초마다 점수 업데이트
setInterval(updateScores, 30000);

// 페이지 로드 애니메이션
window.addEventListener('load', function() {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});