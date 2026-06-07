"""원스글로벌 Internal — 사내 도구 모음 랜딩 페이지."""
import os

import streamlit as st

# ============== 색상 ==============
PRIMARY = "#5B43C9"
PRIMARY_DARK = "#4A35B0"
PRIMARY_LIGHT = "#F1EEFB"

st.set_page_config(
    page_title="원스글로벌 Internal",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def get_url(key: str, default: str) -> str:
    try:
        return st.secrets.get("urls", {}).get(key, default)
    except Exception:
        return os.environ.get(key.upper(), default)


KEYWORD_URL = get_url("keyword", "https://connectdi-insights.streamlit.app")
RECRUIT_URL = get_url("recruit", "https://onesglobal-recruit.streamlit.app")
ACCOUNTING_URL = get_url("accounting", "https://finance-dashboard.streamlit.app")


st.markdown(
    f"""
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

    html, body, *, [class*="css"], button, input, select, textarea {{
        font-family: 'Pretendard', 'Malgun Gothic', '맑은 고딕', -apple-system, sans-serif !important;
    }}

    .stApp {{ background: white; padding-top: 64px; }}
    [data-testid="stAppViewContainer"] {{ background: white !important; }}
    body, html {{ background: white !important; }}

    /* Streamlit 기본 toolbar 숨김 */
    [data-testid="stHeader"], header[data-testid="stHeader"],
    div[data-testid="stToolbar"] {{
        display: none !important; height: 0 !important; visibility: hidden !important;
    }}

    /* 상단 보라 헤더 */
    .top-header {{
        background: linear-gradient(90deg, {PRIMARY} 0%, {PRIMARY_DARK} 100%);
        padding: 0 32px;
        display: flex; align-items: center; gap: 20px;
        color: white;
        position: fixed;
        top: 0; left: 0;
        width: 100vw;
        height: 64px;
        z-index: 999999;
        box-shadow: 0 1px 4px rgba(91, 67, 201, 0.15);
    }}
    .top-logo {{
        color: white; font-size: 1.2rem; font-weight: 800;
        display: flex; align-items: center; gap: 8px;
    }}
    .top-tag {{
        background: rgba(255,255,255,0.2); color: white;
        padding: 4px 10px; border-radius: 4px;
        font-size: 0.7rem; font-weight: 500;
    }}

    section[data-testid="stMain"] {{ background: white !important; }}
    [data-testid="stMainBlockContainer"] {{
        max-width: 1100px !important;
        margin: 0 auto !important;
        padding-top: 64px !important;
    }}

    /* 사이드바 숨김 */
    section[data-testid="stSidebar"] {{ display: none !important; }}
    [data-testid="stSidebarCollapsedControl"],
    [data-testid="collapsedControl"],
    [data-testid="stSidebarCollapseButton"] {{
        display: none !important;
    }}

    /* 메인 타이틀 */
    .hero {{
        text-align: center; padding: 40px 0 32px 0;
    }}
    .hero h1 {{
        font-size: 2.2rem; font-weight: 800; color: #1E1B2E;
        margin-bottom: 8px;
    }}
    .hero p {{
        color: #6B6A73; font-size: 1rem;
    }}

    /* 메뉴 카드 */
    .menu-grid {{
        display: grid; grid-template-columns: 1fr 1fr;
        gap: 24px; margin-top: 24px;
    }}
    .menu-card {{
        background: white;
        border: 1px solid #EDECF1;
        border-radius: 16px;
        padding: 32px 28px;
        text-decoration: none !important;
        color: inherit !important;
        display: block;
        transition: all 0.2s;
        box-shadow: 0 2px 8px rgba(91, 67, 201, 0.04);
    }}
    .menu-card:hover {{
        border-color: {PRIMARY};
        box-shadow: 0 8px 24px rgba(91, 67, 201, 0.15);
        transform: translateY(-2px);
    }}
    .menu-card-icon {{
        font-size: 2.8rem; margin-bottom: 14px;
    }}
    .menu-card-title {{
        color: {PRIMARY};
        font-size: 1.3rem; font-weight: 800;
        margin-bottom: 6px;
    }}
    .menu-card-desc {{
        color: #6B6A73; font-size: 0.92rem;
        line-height: 1.55; margin-bottom: 16px;
    }}
    .menu-card-cta {{
        background: {PRIMARY_LIGHT}; color: {PRIMARY};
        padding: 8px 16px; border-radius: 8px;
        font-size: 0.85rem; font-weight: 700;
        display: inline-block;
    }}
    .menu-card:hover .menu-card-cta {{
        background: {PRIMARY}; color: white;
    }}

    .footer {{
        text-align: center; padding: 40px 0 16px;
        color: #B0AFB8; font-size: 0.82rem;
    }}

    /* 모바일 (1열) */
    @media (max-width: 720px) {{
        .menu-grid {{ grid-template-columns: 1fr; }}
    }}

    h1, h2, h3 {{ color: #1E1B2E; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# 상단 헤더
st.markdown(
    f'<div class="top-header">'
    f'<div class="top-logo">🏢 원스글로벌</div>'
    f'<div class="top-tag">Internal Tools</div>'
    f'<div style="flex:1;"></div>'
    f'<div style="color:rgba(255,255,255,0.85);font-size:0.85rem;">사내 도구 모음</div>'
    f'</div>',
    unsafe_allow_html=True,
)

# 메인 콘텐츠
st.markdown(
    f"""
    <div class="hero">
      <h1>원스글로벌 사내 도구</h1>
      <p>사용하실 분석 도구를 선택해주세요</p>
    </div>

    <div class="menu-grid">
      <a href="{KEYWORD_URL}" target="_blank" class="menu-card">
        <div class="menu-card-icon">🔍</div>
        <div class="menu-card-title">검색 인사이트</div>
        <div class="menu-card-desc">
          커넥트디아이 · 커넥트디아이플러스 · 길병원 3개 사이트의 검색 키워드 통합 분석.
          매주 자동 갱신되는 데이터로 트렌드 · 키워드 비교 · 기간별 분석 가능.
        </div>
        <span class="menu-card-cta">→ 입장하기</span>
      </a>

      <a href="{RECRUIT_URL}" target="_blank" class="menu-card">
        <div class="menu-card-icon">📋</div>
        <div class="menu-card-title">채용 인사이트</div>
        <div class="menu-card-desc">
          Claude AI 기반 이력서 자동 분석. 포지션별 매칭도 점수 · 핵심역량 · 경력사항 ·
          진행 상태 관리. 사람인 공고 자동 연동.
        </div>
        <span class="menu-card-cta">→ 입장하기</span>
      </a>

      <a href="{ACCOUNTING_URL}" target="_blank" class="menu-card">
        <div class="menu-card-icon">💰</div>
        <div class="menu-card-title">회계 인사이트</div>
        <div class="menu-card-desc">
          2026 영업현황 DB 회계 관점 분석. 미수금 · 월별 발행 매출 ·
          파이프라인 상태 · 서비스별 매출 · 신규/갱신 비중 · 정산 지연 분석.
        </div>
        <span class="menu-card-cta">→ 입장하기</span>
      </a>
    </div>

    <div class="footer">
      © 2026 원스글로벌 · Internal Use Only
    </div>
    """,
    unsafe_allow_html=True,
)
