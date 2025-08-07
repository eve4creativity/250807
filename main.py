import streamlit as st

# ------------------- 데이터 정의 -------------------
mbti_data = {
    "INTJ": {
        "career": "🔬 과학자, 🧠 인공지능 연구원, 🧑‍💻 데이터 사이언티스트",
        "english_tip": "🧘‍♀️ 구조적인 문법 책 + 🎧 TED 강연 반복 듣기"
    },
    "INTP": {
        "career": "🧪 이론 물리학자, 💡 발명가, 👨‍💻 프로그래머",
        "english_tip": "📖 논리적인 에세이 읽기 + 🧩 영어 퍼즐 앱 활용"
    },
    "ENTJ": {
        "career": "💼 CEO, 🎯 전략 컨설턴트, 🧑‍⚖️ 법조인",
        "english_tip": "🎤 영어 토론 클럽 참여 + ✍️ 비즈니스 이메일 작성 연습"
    },
    "ENTP": {
        "career": "🎙️ 방송인, 🧠 창업가, 🎮 게임 개발자",
        "english_tip": "🎭 역할극 기반 회화 + 🎧 팟캐스트 듣고 요약하기"
    },
    "INFJ": {
        "career": "📚 작가, 🧘‍♂️ 심리상담가, 🌏 NGO 활동가",
        "english_tip": "📝 영어 일기 쓰기 + 🌿 명상 영어 듣기"
    },
    "INFP": {
        "career": "🎨 예술가, ✍️ 시인, 🧸 아동문학가",
        "english_tip": "📖 감성적인 영어 소설 읽기 + 🎧 잔잔한 영어 노래 따라 부르기"
    },
    "ENFJ": {
        "career": "👩‍🏫 교사, 🎤 연설가, 🌍 국제 협력가",
        "english_tip": "🗣️ 발표 영어 연습 + 🧑‍🤝‍🧑 친구들과 영어 토론"
    },
    "ENFP": {
        "career": "🎬 영화감독, 🌈 콘텐츠 크리에이터, ✈️ 여행가이드",
        "english_tip": "🎥 유튜브 영상 따라 말하기 + 🌍 다양한 문화 영어 탐색"
    },
    "ISTJ": {
        "career": "📊 회계사, 🏛️ 공무원, 🧰 엔지니어",
        "english_tip": "🧱 문법과 단어 암기 + 🗂️ 학습 계획표 만들기"
    },
    "ISFJ": {
        "career": "🏥 간호사, 🍳 제과제빵사, 🧸 사회복지사",
        "english_tip": "📚 교과서 중심 학습 + 👂 느린 속도 듣기 훈련"
    },
    "ESTJ": {
        "career": "🏛️ 행정가, 📋 프로젝트 매니저, 🛠️ 기술 관리자",
        "english_tip": "🎯 목표 설정 학습 + 🧑‍🏫 영어 발표 훈련"
    },
    "ESFJ": {
        "career": "🎓 교사, 🧑‍🍳 서비스 매니저, 👨‍👩‍👧‍👦 상담사",
        "english_tip": "👥 친구들과 회화 연습 + ✍️ 상황별 이메일 쓰기"
    },
    "ISTP": {
        "career": "🛠️ 기술자, 🚗 자동차 정비사, 🧗‍♂️ 탐험가",
        "english_tip": "🔧 실생활 관련 영어 표현 학습 + 🎮 게임으로 듣기 훈련"
    },
    "ISFP": {
        "career": "🎨 디자이너, 🎼 작곡가, 🐾 동물 보호사",
        "english_tip": "🎧 음악 듣기 중심 학습 + 🖌️ 창작 영어 일기 쓰기"
    },
    "ESTP": {
        "career": "🚀 마케터, 🧗‍♀️ 스포츠 선수, 🎤 이벤트 플래너",
        "english_tip": "🎮 액션 중심 회화 게임 + 📱 모바일 영어 앱 활용"
    },
    "ESFP": {
        "career": "🎭 배우, 🎉 파티 플래너, 📸 인플루언서",
        "english_tip": "📹 영상 찍으며 말하기 + 🎶 노래로 영어 배우기"
    },
}

# ------------------- UI 구성 -------------------
st.set_page_config(page_title="MBTI 진로 & 영어학습 상담소 🎓🌍", layout="centered")

st.title("🎓 MBTI 기반 진로 & 영어 학습 상담소")
st.write("당신의 MBTI를 선택하면 👇 진로 추천과 ✨ 영어 학습 팁을 알려드릴게요!")

# MBTI 선택
mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("당신의 MBTI는 무엇인가요? 🔍", mbti_list)

# 결과 출력
if selected_mbti:
    st.subheader(f"🌟 {selected_mbti} 학생을 위한 추천 🌟")

    st.markdown(f"""
    **🎯 추천 진로:**  
    {mbti_data[selected_mbti]["career"]}
    
    **📘 영어 학습 팁:**  
    {mbti_data[selected_mbti]["english_tip"]}
    """)

    st.success("너만의 색깔을 살려 멋지게 성장하길 응원해! 💪🚀")

# 하단 안내
st.markdown("---")
st.caption("🧠 이 앱은 재미로 보는 참고용입니다. 다양한 경험을 통해 진짜 나를 발견해보세요!")

