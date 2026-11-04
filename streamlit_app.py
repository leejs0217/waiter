import streamlit as st
from datetime import date, time, datetime
import random

st.set_page_config(
    page_title="waiter",
    page_icon="🕰️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 기본 스타일
st.markdown("""
<style>
    .block-container { padding-top: 1.5rem; }
    h1 { font-size: 1.8rem !important; }
    h2 { font-size: 1.3rem !important; }
    .stButton > button { width: 100%; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# 세션 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "text": "안녕하세요. 성수 팝업 웨이팅 의뢰 확인했습니다.", "time": "14:02"},
        {"role": "user", "text": "오늘 2시부터 가능하신가요?", "time": "14:03"},
        {"role": "assistant", "text": "네 가능합니다. 번호표 수령 후 사진으로 인증드릴게요.", "time": "14:04"},
    ]
if "report_done" not in st.session_state:
    st.session_state.report_done = False
if "report_id" not in st.session_state:
    st.session_state.report_id = ""

# 사이드바
with st.sidebar:
    st.title("waiter")
    st.caption("대리 웨이팅 플랫폼")
    menu = st.radio(
        "메뉴 선택",
        ["홈", "시세 보기", "의뢰하기", "웨이터 목록", "익명 채팅", "치터 신고"],
        index=0
    )
    st.markdown("---")
    st.caption("안전결제 · 익명채팅 · 신고시스템")

# ========== 홈 ==========
if menu == "홈":
    st.title("waiter")
    st.subheader("줄 서는 시간을 돈으로 바꾸세요")
    st.write("인기 상품, 팝업, 맛집 웨이팅을 안전하게 맡기세요.")
    st.write("익명 채팅 · 안전결제 · 실시간 시세 지원")

    st.markdown("---")
    st.markdown("### 왜 waiter인가요?")

    col1, col2 = st.columns(2)
    with col1:
        st.info("**안전결제**\n\n에스크로로 의뢰금 보호")
        st.info("**익명 채팅**\n\n개인정보 노출 없이 시작")
    with col2:
        st.info("**가격 투명성**\n\n시세 + 웨이터 수 표시")
        st.info("**치터 신고**\n\n증거 기반 신고 시스템")

    st.markdown("---")
    st.markdown("### 이용 방법")
    st.markdown("1. **의뢰 등록** — 장소, 시간, 웃돈 입력")
    st.markdown("2. **웨이터 매칭** — 익명 채팅으로 조율")
    st.markdown("3. **수행 & 정산** — 인증 후 안전결제")

# ========== 시세 ==========
elif menu == "시세 보기":
    st.title("시세 & 웨이터 현황")
    st.caption("원하는 가격에 몇 명의 웨이터가 있는지 확인하세요")

    st.markdown("#### 성수 ○○ 팝업 웨이팅")
    c1, c2 = st.columns(2)
    c1.metric("현재 시세", "28,000원", "+12%")
    c2.metric("평균 비용", "22,000원")

    st.markdown("**최근 가격 추이**")
    chart_data = {
        "날짜": ["10/28", "10/30", "11/01", "11/03"],
        "가격(원)": [18000, 21000, 24000, 28000]
    }
    st.bar_chart(chart_data, x="날짜", y="가격(원)", height=220)

    st.markdown("---")
    st.markdown("#### 원하는 가격대 웨이터 수")
    price = st.slider("제시 금액 (원)", 10000, 50000, 25000, 1000)

    if price >= 30000:
        count = 14
    elif price >= 25000:
        count = 9
    elif price >= 20000:
        count = 5
    elif price >= 15000:
        count = 2
    else:
        count = 0

    st.success(f"**{price:,}원** 기준 현재 **{count}명** 가능")
    st.progress(min(count / 14, 1.0))

# ========== 의뢰하기 ==========
elif menu == "의뢰하기":
    st.title("새 의뢰 등록")

    title = st.text_input("의뢰 제목", placeholder="예: 성수 팝업스토어 웨이팅")
    location = st.text_input("장소", placeholder="예: 서울 성수동")

    c1, c2 = st.columns(2)
    with c1:
        d = st.date_input("날짜", value=date.today())
    with c2:
        t = st.time_input("시간", value=time(14, 0))

    price = st.slider("제시 웃돈 (원)", 10000, 50000, 20000, 1000)

    if price >= 30000:
        count = 14
    elif price >= 25000:
        count = 9
    elif price >= 20000:
        count = 5
    elif price >= 15000:
        count = 2
    else:
        count = 0

    st.info(f"이 가격에 **{count}명**의 웨이터가 가능합니다")

    detail = st.text_area("상세 요청사항", placeholder="번호표만 받아주세요")

    st.caption("안전결제: 수행 인증 후 정산됩니다.")

    if st.button("의뢰 등록하기", type="primary"):
        if not title or not location:
            st.error("제목과 장소를 입력해 주세요.")
        else:
            st.success("의뢰가 등록되었습니다! (데모)")
            st.balloons()

# ========== 웨이터 목록 ==========
elif menu == "웨이터 목록":
    st.title("웨이터 목록")
    st.caption("인증 · 평점 확인 후 요청하세요")

    waiters = [
        {"name": "서울줄서기러", "rating": 4.9, "done": 87, "loc": "강남", "min": 15000, "ok": True},
        {"name": "팝업헌터", "rating": 4.8, "done": 52, "loc": "성수", "min": 12000, "ok": True},
        {"name": "대기마스터", "rating": 4.7, "done": 134, "loc": "서울전체", "min": 20000, "ok": True},
        {"name": "익명웨이터02", "rating": 4.5, "done": 21, "loc": "홍대", "min": 10000, "ok": False},
    ]

    for w in waiters:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                badge = " ✓" if w["ok"] else ""
                st.markdown(f"**{w['name']}**{badge}")
                st.caption(f"★ {w['rating']} · {w['done']}건 · {w['loc']}")
            with col2:
                st.write(f"**{w['min']:,}원~**")
                if st.button("요청", key=w["name"]):
                    st.session_state.messages = [
                        {"role": "assistant", "text": f"안녕하세요. {w['name']}입니다.", "time": datetime.now().strftime("%H:%M")}
                    ]
                    st.success("채팅 메뉴로 이동해 대화를 시작하세요.")
            st.divider()

# ========== 익명 채팅 ==========
elif menu == "익명 채팅":
    st.title("익명 채팅")
    st.caption("상대방: 서울줄서기러 · 인증됨")

    st.warning("채팅은 익명으로 시작됩니다.")

    if st.button("이 상대방 신고하기"):
        st.info("왼쪽 메뉴에서 **치터 신고**를 선택하세요.")

    st.markdown("---")

    for m in st.session_state.messages:
        if m["role"] == "user":
            with st.chat_message("user"):
                st.write(m["text"])
                st.caption(m["time"])
        else:
            with st.chat_message("assistant"):
                st.write(m["text"])
                st.caption(m["time"])

    prompt = st.chat_input("메시지 입력 (익명 전송)")
    if prompt:
        now = datetime.now().strftime("%H:%M")
        st.session_state.messages.append({"role": "user", "text": prompt, "time": now})
        st.rerun()

# ========== 치터 신고 ==========
elif menu == "치터 신고":
    st.title("치터 신고하기")
    st.caption("사기 · 노쇼 · 허위인증 등을 신고해 주세요")

    if st.session_state.report_done:
        st.success("신고가 접수되었습니다.")
        st.write(f"**접수번호:** `{st.session_state.report_id}`")
        st.write("검토 후 결과를 안내해 드리겠습니다.")
        if st.button("새 신고 작성"):
            st.session_state.report_done = False
            st.rerun()
    else:
        target = st.text_input("신고 대상", value="서울줄서기러")
        reason = st.selectbox(
            "신고 사유",
            ["선택하세요", "사기 (돈만 받고 수행 안 함)", "노쇼", "허위 인증", "불쾌한 언행", "기타"]
        )
        detail = st.text_area("상세 내용", height=120, placeholder="언제, 어떤 일이 있었는지 구체적으로 적어주세요.")
        files = st.file_uploader("증거 자료 (선택)", accept_multiple_files=True, type=["png", "jpg", "jpeg", "pdf"])

        st.caption("허위 신고는 제재 대상이 될 수 있습니다.")

        if st.button("신고 접수하기", type="primary"):
            if reason == "선택하세요":
                st.error("신고 사유를 선택해 주세요.")
            elif not detail.strip():
                st.error("상세 내용을 입력해 주세요.")
            else:
                st.session_state.report_id = "R" + str(random.randint(10000000, 99999999))
                st.session_state.report_done = True
                st.rerun()
