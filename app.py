"""
AIDEOM-VN — Trang chủ
AI-Driven Decision Optimization Model for Vietnam
"""
import streamlit as st
import plotly.graph_objects as go
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from utils.data_loader import load_macro

st.set_page_config(
    page_title="AIDEOM-VN",
    page_icon="🇻🇳",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Style navigation tự động của Streamlit cho đẹp
st.markdown("""
<style>
[data-testid="stSidebarNavItems"] { padding: 0 !important; }
[data-testid="stSidebarNavItems"] a {
    display: flex !important;
    align-items: center !important;
    padding: 7px 12px !important;
    border-radius: 8px !important;
    margin-bottom: 2px !important;
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    text-decoration: none !important;
    transition: all 0.2s ease !important;
}
[data-testid="stSidebarNavItems"] a:hover {
    background: rgba(255,255,255,0.12) !important;
    border-color: rgba(255,255,255,0.2) !important;
}
[data-testid="stSidebarNavItems"] a span {
    color: #e2e8f0 !important;
    font-size: 0.76rem !important;
    font-weight: 500 !important;
}
[data-testid="stSidebarNavItems"] a[aria-current="page"] {
    background: rgba(37,99,235,0.2) !important;
    border-color: rgba(37,99,235,0.4) !important;
}
[data-testid="stSidebarNavItems"] a[aria-current="page"] span {
    color: #93c5fd !important;
    font-weight: 700 !important;
}
[data-testid="stSidebarNavSeparator"] {
    border-color: rgba(255,255,255,0.06) !important;
    margin: 6px 0 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

*, body { font-family: 'Plus Jakarta Sans', sans-serif; }
#MainMenu, header, footer { visibility: hidden; }

/* ── Nền sáng ── */
.stApp {
    background: #f0f4f8;
    background-image:
        radial-gradient(ellipse 70% 50% at 15% 0%, rgba(99,179,237,0.18) 0%, transparent 55%),
        radial-gradient(ellipse 60% 40% at 85% 90%, rgba(246,173,85,0.12) 0%, transparent 55%),
        radial-gradient(ellipse 40% 30% at 50% 50%, rgba(104,211,145,0.07) 0%, transparent 60%);
}

/* lưới nền nhẹ */
.stApp::before {
    content:'';
    position:fixed; inset:0;
    background-image:
        linear-gradient(rgba(160,180,210,0.12) 1px, transparent 1px),
        linear-gradient(90deg, rgba(160,180,210,0.12) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events:none; z-index:0;
}

/* ── Animations ── */
@keyframes fadeUp   { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:translateY(0)} }
@keyframes fadeDown { from{opacity:0;transform:translateY(-18px)} to{opacity:1;transform:translateY(0)} }
@keyframes shimmer  { 0%{background-position:-200% center} 100%{background-position:200% center} }

/* ── Hero ── */
.hero-wrap { padding: 52px 0 28px; }

.hero-eyebrow {
    display:inline-flex; align-items:center; gap:8px;
    background:rgba(37,99,235,0.08);
    border:1px solid rgba(37,99,235,0.25);
    color:#2563eb; padding:5px 18px;
    border-radius:100px; font-size:0.72rem;
    font-weight:700; letter-spacing:2.5px; text-transform:uppercase;
    animation:fadeDown 0.5s ease both; margin-bottom:20px;
}

.hero-title {
    font-family:'Playfair Display', serif;
    font-size:4.8rem; font-weight:800; line-height:1.0;
    background:linear-gradient(120deg, #1e3a5f 0%, #2563eb 45%, #0891b2 100%);
    background-size:200% auto;
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
    animation:fadeDown 0.6s ease 0.1s both, shimmer 6s linear infinite;
    margin:0 0 8px;
}

.hero-sub2 {
    font-size:1.3rem; font-weight:600; color:#334155;
    font-family:'Plus Jakarta Sans',sans-serif;
    animation:fadeDown 0.6s ease 0.15s both; margin-bottom:12px;
}

.hero-body {
    font-size:1.0rem; color:#64748b; font-weight:400;
    animation:fadeDown 0.6s ease 0.22s both;
    max-width:600px; line-height:1.75; margin-bottom:26px;
}

.hero-tags { display:flex; gap:9px; flex-wrap:wrap; animation:fadeUp 0.6s ease 0.35s both; }
.hero-tag {
    background:rgba(255,255,255,0.75);
    border:1px solid rgba(37,99,235,0.18);
    color:#475569; padding:5px 14px;
    border-radius:6px; font-size:0.72rem; font-weight:600;
    backdrop-filter:blur(4px);
    box-shadow:0 1px 4px rgba(0,0,0,0.06);
}

.hero-divider {
    height:1px; margin:36px 0; border:none;
    background:linear-gradient(90deg, transparent, rgba(37,99,235,0.4), rgba(8,145,178,0.35), transparent);
    animation:fadeDown 1s ease 0.5s both;
}

/* ── KPI ── */
.kpi-card {
    background:rgba(255,255,255,0.82);
    border:1px solid rgba(255,255,255,0.95);
    border-radius:16px; padding:22px 18px;
    position:relative; overflow:hidden;
    transition:all 0.28s ease;
    animation:fadeUp 0.55s ease both;
    backdrop-filter:blur(8px);
    box-shadow:0 2px 12px rgba(0,0,0,0.06);
}
.kpi-card::after {
    content:''; position:absolute; top:0; left:0; right:0; height:3px;
    background:var(--accent,linear-gradient(90deg,#2563eb,#0891b2));
}
.kpi-card:hover {
    transform:translateY(-5px);
    box-shadow:0 16px 40px rgba(37,99,235,0.12);
    border-color:rgba(37,99,235,0.2);
}
.kpi-icon  { font-size:1.5rem; margin-bottom:10px; }
.kpi-value { font-family:'Playfair Display',serif; font-size:1.95rem; font-weight:800; color:#1e3a5f; line-height:1; }
.kpi-label { font-size:0.66rem; color:#94a3b8; text-transform:uppercase; letter-spacing:1.5px; margin:5px 0; font-weight:700; }
.kpi-delta { font-size:0.78rem; color:#059669; font-weight:600; }

/* ── Section title ── */
.sec-title {
    font-family:'Playfair Display',serif;
    font-size:1.45rem; font-weight:700; color:#1e3a5f;
    margin:44px 0 18px;
    padding-bottom:12px;
    border-bottom:2px solid rgba(37,99,235,0.12);
    display:flex; align-items:center; gap:10px;
}
.sec-title span.acc { color:#2563eb; }

/* ── Level strip ── */
.level-strip {
    display:flex; align-items:center; gap:10px;
    padding:9px 16px; border-radius:10px;
    margin:26px 0 12px;
    font-size:0.70rem; font-weight:700;
    letter-spacing:2px; text-transform:uppercase;
}
.ls-easy   { background:rgba(5,150,105,0.07);  border:1px solid rgba(5,150,105,0.2);  color:#059669; }
.ls-medium { background:rgba(217,119,6,0.07);  border:1px solid rgba(217,119,6,0.22); color:#d97706; }
.ls-hard2  { background:rgba(234,88,12,0.07);  border:1px solid rgba(234,88,12,0.2);  color:#ea580c; }
.ls-hard   { background:rgba(220,38,38,0.07);  border:1px solid rgba(220,38,38,0.2);  color:#dc2626; }

/* ── Problem card ── */
.p-card {
    background:rgba(255,255,255,0.80);
    border:1px solid rgba(255,255,255,0.95);
    border-radius:13px; padding:18px 16px;
    height:100%; transition:all 0.25s ease;
    position:relative; overflow:hidden;
    backdrop-filter:blur(6px);
    box-shadow:0 1px 6px rgba(0,0,0,0.05);
    animation:fadeUp 0.5s ease both;
}
.p-card::before {
    content:''; position:absolute;
    top:0; left:0; bottom:0; width:3px;
    background:var(--lc,#059669); opacity:0;
    transition:opacity 0.25s;
}
.p-card:hover {
    transform:translateY(-3px);
    box-shadow:0 10px 28px rgba(0,0,0,0.10);
    border-color:rgba(37,99,235,0.2);
}
.p-card:hover::before { opacity:1; }
.p-num   { font-size:0.62rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; margin-bottom:7px; }
.p-name  { font-size:0.88rem; font-weight:700; color:#1e3a5f; margin-bottom:5px; line-height:1.35; }
.p-desc  { font-size:0.70rem; color:#64748b; line-height:1.5; }
.p-badge {
    display:inline-block; margin-top:10px;
    background:rgba(37,99,235,0.06);
    border:1px solid rgba(37,99,235,0.15);
    border-radius:4px; padding:2px 8px;
    font-size:0.60rem; color:#2563eb; letter-spacing:0.5px; font-weight:600;
}

/* ── Footer ── */
.footer {
    text-align:center; color:#cbd5e1; font-size:0.70rem;
    padding:36px 0 16px;
    border-top:1px solid rgba(37,99,235,0.1);
    margin-top:48px; line-height:2.2;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background:rgba(15,30,55,0.97) !important;
    border-right:1px solid rgba(255,255,255,0.06) !important;
}
.sb-logo { text-align:center; padding:24px 0 16px; border-bottom:1px solid rgba(255,255,255,0.06); margin-bottom:16px; }
.sb-logo-text { font-family:'Playfair Display',serif; font-size:1.25rem; font-weight:800; color:#f1f5f9; letter-spacing:1px; }
.sb-logo-sub  { font-size:0.60rem; color:#334155; letter-spacing:2px; text-transform:uppercase; margin-top:4px; }

/* page_link styling in sidebar */
[data-testid="stSidebar"] [data-testid="stPageLink"] a {
    display:flex; align-items:center;
    padding:6px 10px; border-radius:8px; margin-bottom:2px;
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.05);
    font-size:0.73rem; color:#e2e8f0 !important;
    text-decoration:none !important;
    transition:all 0.2s ease;
}
[data-testid="stSidebar"] [data-testid="stPageLink"] a:hover {
    background:rgba(255,255,255,0.12);
    border-color:rgba(255,255,255,0.2);
    color:#ffffff !important;
}

/* scrollbar */
::-webkit-scrollbar { width:5px; }
::-webkit-scrollbar-track { background:transparent; }
::-webkit-scrollbar-thumb { background:rgba(37,99,235,0.3); border-radius:99px; }
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class='sb-logo'>
        <div style='font-size:2rem;margin-bottom:6px'>🇻🇳</div>
        <div class='sb-logo-text'>AIDEOM-VN</div>
        <div class='sb-logo-sub'>Decision Optimization</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("**⚙️ AI Analyst (Groq)**")
    api_key_input = st.text_input(
        "Groq API Key", type="password",
        placeholder="gsk_...",
        help="Lấy miễn phí tại console.groq.com"
    )
    if api_key_input:
        st.session_state["groq_api_key"] = api_key_input
        st.success("✅ AI Analyst đã kết nối")

    st.markdown("""
    <hr style='border-color:rgba(255,255,255,0.05);margin:14px 0'>
    <div style='font-size:0.62rem;font-weight:700;color:#334155;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:10px'>
        📖 Giới thiệu
    </div>
    <div style='font-size:0.70rem;color:#475569;line-height:1.9;
                background:rgba(255,255,255,0.03);border-radius:8px;
                padding:10px 12px;border:1px solid rgba(255,255,255,0.05)'>
        AIDEOM-VN là hệ thống 12 bài toán mô hình hoá quyết định phát triển kinh tế
        Việt Nam trong kỷ nguyên AI — từ hàm sản xuất Cobb-Douglas đến học tăng cường
        Q-learning, bao gồm LP, MIP, TOPSIS, NSGA-II, và Stochastic Programming.
    </div>
    <hr style='border-color:rgba(255,255,255,0.05);margin:14px 0'>
    """, unsafe_allow_html=True)

    # Folder 12 bài toán — dùng st.page_link để điều hướng thực sự
    st.markdown("""
    <div style='font-size:0.62rem;font-weight:700;color:#334155;
                letter-spacing:2px;text-transform:uppercase;margin-bottom:8px'>
        📂 Mô hình Tối ưu hoá
    </div>
    """, unsafe_allow_html=True)

    page_links = [
        ("pages/01_Cobb_Douglas.py",    "🟢 B01 · Cobb-Douglas + AI"),
        ("pages/02_LP_Ngan_Sach.py",    "🟢 B02 · LP Ngân sách số"),
        ("pages/03_Priority_10_Nganh.py","🟢 B03 · Priority 10 ngành"),
        ("pages/04_LP_Nganh_Vung.py",   "🟡 B04 · LP Ngành-Vùng"),
        ("pages/05_MIP_15_Du_An.py",    "🟡 B05 · MIP 15 dự án"),
        ("pages/06_TOPSIS_6_Vung.py",   "🟡 B06 · TOPSIS 6 vùng"),
        ("pages/07_NSGA_Pareto.py",     "🟠 B07 · NSGA-II Pareto"),
        ("pages/08_Dong_2026_2035.py",  "🟠 B08 · Tối ưu động"),
        ("pages/09_Lao_Dong_AI.py",     "🟠 B09 · Lao động & AI"),
        ("pages/10_Stochastic_SP.py",   "🔴 B10 · Stochastic SP"),
        ("pages/11_Q_Learning_RL.py",   "🔴 B11 · Q-learning RL"),
        ("pages/12_AIDEOM_Tich_Hop.py", "🔴 B12 · AIDEOM tích hợp"),
    ]
    for page_path, label in page_links:
        st.page_link(page_path, label=label)

    st.markdown("""
    <hr style='border-color:rgba(255,255,255,0.05);margin:14px 0'>
    <div style='font-size:0.62rem;color:#334155;line-height:2.2'>
        📊 <b style='color:#3d4f63'>Nguồn dữ liệu</b><br>
        GSO · MoST · MIC · MPI<br>
        World Bank · GII 2025
    </div>
    """, unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class='hero-wrap'>
    <div class='hero-eyebrow'>🇻🇳 Vietnam &nbsp;·&nbsp; AI Era &nbsp;·&nbsp; 2025–2030</div>
    <div class='hero-title'>AIDEOM-VN</div>
    <div class='hero-sub2'>AI-Driven Decision Optimization Model</div>
    <div class='hero-body'>
        Hệ thống <strong>12 bài toán</strong> mô hình ra quyết định phát triển kinh tế Việt Nam
        trong kỷ nguyên AI — dữ liệu thực 2020–2025, Python, tối ưu hóa nâng cao và học tăng cường.
    </div>
    <div class='hero-tags'>
        <span class='hero-tag'>Python 3.11+</span>
        <span class='hero-tag'>Linear Programming</span>
        <span class='hero-tag'>NSGA-II · Pareto</span>
        <span class='hero-tag'>Q-learning RL</span>
        <span class='hero-tag'>Stochastic SP</span>
        <span class='hero-tag'>TOPSIS · MCDM</span>
        <span class='hero-tag'>Cobb-Douglas</span>
    </div>
</div>
<hr class='hero-divider'>
""", unsafe_allow_html=True)

# ── KPI ──────────────────────────────────────────────────────────────────────
try:
    macro  = load_macro()
    latest = macro.iloc[-1]
    prev   = macro.iloc[-2]

    gdp_usd   = latest["GDP_billion_USD"]
    gdp_grow  = latest["GDP_growth_pct"]
    dig_share = latest["digital_economy_share_GDP_pct"]
    dig_prev  = prev["digital_economy_share_GDP_pct"]
    fdi       = latest["FDI_disbursed_billion_USD"]
    fdi_prev  = prev["FDI_disbursed_billion_USD"]
    gpc       = latest["GDP_per_capita_USD"]
    gpc_prev  = prev["GDP_per_capita_USD"]

    c1, c2, c3, c4 = st.columns(4)
    kpis = [
        (c1, "🏦", f"{gdp_usd:.1f} tỷ USD", "GDP 2025",
         f"↑ +{gdp_grow:.2f}%/năm", "#2563eb,#0891b2", "0.1s"),
        (c2, "💻", f"≈{dig_share:.1f}%", "Kinh tế số / GDP",
         f"↑ +{dig_share-dig_prev:.1f} điểm", "#059669,#10b981", "0.2s"),
        (c3, "🌐", f"{fdi:.1f} tỷ USD", "FDI giải ngân",
         f"↑ +{((fdi/fdi_prev)-1)*100:.1f}%", "#d97706,#f59e0b", "0.3s"),
        (c4, "👤", f"{int(gpc):,} USD", "GDP / người",
         f"↑ +{((gpc/gpc_prev)-1)*100:.1f}%", "#7c3aed,#a78bfa", "0.4s"),
    ]
    for col, icon, val, label, delta, grad, delay in kpis:
        with col:
            st.markdown(f"""
            <div class='kpi-card' style='animation-delay:{delay};--accent:linear-gradient(90deg,{grad})'>
                <div class='kpi-icon'>{icon}</div>
                <div class='kpi-value'>{val}</div>
                <div class='kpi-label'>{label}</div>
                <div class='kpi-delta'>{delta}</div>
            </div>""", unsafe_allow_html=True)

    # ── Biểu đồ macro ────────────────────────────────────────────────────────
    st.markdown("<div class='sec-title'>📊 Tổng quan kinh tế Việt Nam <span class='acc'>2020–2025</span></div>",
                unsafe_allow_html=True)

    BASE = dict(
        height=340, margin=dict(l=0,r=0,t=10,b=0),
        plot_bgcolor="rgba(255,255,255,0.6)",
        paper_bgcolor="rgba(255,255,255,0)",
        font=dict(color="#64748b", family="Plus Jakarta Sans"),
        legend=dict(orientation="h", y=1.07, bgcolor="rgba(0,0,0,0)"),
        xaxis=dict(gridcolor="rgba(148,163,184,0.2)", zerolinecolor="rgba(0,0,0,0)",
                   tickfont=dict(color="#94a3b8")),
        yaxis=dict(gridcolor="rgba(148,163,184,0.2)", zerolinecolor="rgba(0,0,0,0)",
                   tickfont=dict(color="#94a3b8")),
    )

    t1, t2, t3 = st.tabs(["📈 GDP & Tăng trưởng", "💻 Kinh tế số & FDI", "🚢 Xuất-Nhập khẩu"])

    with t1:
        fig = go.Figure()
        fig.add_bar(x=macro["year"], y=macro["GDP_billion_USD"],
                    name="GDP (tỷ USD)", marker_color="#3b82f6", opacity=0.75,
                    marker=dict(line=dict(width=0)))
        fig.add_scatter(x=macro["year"], y=macro["GDP_growth_pct"],
                        name="Tăng trưởng (%)", yaxis="y2",
                        line=dict(color="#059669", width=3),
                        mode="lines+markers", marker=dict(size=9, color="#059669"))
        layout = {**BASE, "yaxis": {**BASE["yaxis"], "title":"GDP (tỷ USD)"},
                  "yaxis2": dict(title="%", overlaying="y", side="right",
                                 tickfont=dict(color="#059669"), gridcolor="rgba(0,0,0,0)")}
        fig.update_layout(**layout)
        st.plotly_chart(fig, use_container_width=True)

    with t2:
        fig2 = go.Figure()
        fig2.add_bar(x=macro["year"], y=macro["FDI_disbursed_billion_USD"],
                     name="FDI (tỷ USD)", marker_color="#d97706", opacity=0.75)
        fig2.add_scatter(x=macro["year"], y=macro["digital_economy_share_GDP_pct"],
                         name="Kinh tế số (%)", yaxis="y2",
                         line=dict(color="#7c3aed", width=3),
                         mode="lines+markers", marker=dict(size=9))
        layout2 = {**BASE, "yaxis": {**BASE["yaxis"], "title":"FDI (tỷ USD)"},
                   "yaxis2": dict(title="%", overlaying="y", side="right",
                                  tickfont=dict(color="#7c3aed"), gridcolor="rgba(0,0,0,0)")}
        fig2.update_layout(**layout2)
        st.plotly_chart(fig2, use_container_width=True)

    with t3:
        fig3 = go.Figure()
        fig3.add_bar(x=macro["year"], y=macro["exports_billion_USD"],
                     name="Xuất khẩu", marker_color="#0891b2", opacity=0.80)
        fig3.add_bar(x=macro["year"], y=macro["imports_billion_USD"],
                     name="Nhập khẩu", marker_color="#ea580c", opacity=0.70)
        layout3 = {**BASE, "barmode":"group",
                   "yaxis": {**BASE["yaxis"], "title":"Tỷ USD"}}
        fig3.update_layout(**layout3)
        st.plotly_chart(fig3, use_container_width=True)

except Exception as e:
    st.warning(f"Không tải được dữ liệu macro: {e}")

# ── 12 Bài toán ──────────────────────────────────────────────────────────────
st.markdown("<div class='sec-title'>🗂️ 12 Bài toán theo <span class='acc'>4 cấp độ</span></div>",
            unsafe_allow_html=True)

levels = [
    ("🟢  CẤP ĐỘ DỄ — Làm quen mô hình", "ls-easy", "#059669", [
        ("Bài 01", "Cobb-Douglas mở rộng + AI", "Growth accounting · Dự báo GDP 2030", "numpy · pandas"),
        ("Bài 02", "LP Phân bổ ngân sách số",   "scipy.optimize · Shadow price",       "scipy"),
        ("Bài 03", "Chỉ số ưu tiên 10 ngành",   "Min-max norm · Weighted scoring",     "pandas"),
    ]),
    ("🟡  CẤP ĐỘ TRUNG BÌNH — Tối ưu cổ điển", "ls-medium", "#d97706", [
        ("Bài 04", "LP Ngân sách ngành-vùng",   "24 biến · Ràng buộc công bằng vùng", "PuLP"),
        ("Bài 05", "MIP 15 dự án CĐS",          "Knapsack · Ràng buộc tiên quyết",    "PuLP / CBC"),
        ("Bài 06", "TOPSIS Xếp hạng 6 vùng",    "Entropy weights · MCDM",              "numpy"),
    ]),
    ("🟠  CẤP ĐỘ KHÁ KHÓ — Tối ưu nâng cao", "ls-hard2", "#ea580c", [
        ("Bài 07", "NSGA-II Pareto đa mục tiêu","4 mục tiêu · Biên Pareto 3D",         "pymoo"),
        ("Bài 08", "Tối ưu động 2026–2035",     "SLSQP · Quỹ đạo liên thời gian",     "scipy"),
        ("Bài 09", "Lao động & AI — NetJob",    "CVXPY · Dòng chảy Sankey",           "cvxpy"),
    ]),
    ("🔴  CẤP ĐỘ KHÓ — AI & Tích hợp", "ls-hard", "#dc2626", [
        ("Bài 10", "Stochastic LP hai giai đoạn","VSS · EVPI · 4 kịch bản",           "PuLP"),
        ("Bài 11", "Q-learning RL",              "MDP 81 trạng thái · ε-greedy",       "numpy"),
        ("Bài 12", "AIDEOM-VN Tích hợp",        "6 module · 5 kịch bản chính sách",   "tích hợp"),
    ]),
]

for label, lv_cls, lv_color, items in levels:
    st.markdown(f"<div class='level-strip {lv_cls}'>{label}</div>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i, (num, title, desc, badge) in enumerate(items):
        with cols[i]:
            st.markdown(f"""
            <div class='p-card' style='--lc:{lv_color}'>
                <div class='p-num' style='color:{lv_color}'>{num}</div>
                <div class='p-name'>{title}</div>
                <div class='p-desc'>{desc}</div>
                <div class='p-badge'>{badge}</div>
            </div>""", unsafe_allow_html=True)

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class='footer'>
    <strong style='color:#94a3b8'>AIDEOM-VN</strong> &nbsp;·&nbsp;
    Mô hình hoá kinh tế trong kỷ nguyên AI &nbsp;·&nbsp; Vietnam 2025<br>
    Dữ liệu: GSO · MoST · MIC · MPI · World Bank · GII 2025
</div>
""", unsafe_allow_html=True)
