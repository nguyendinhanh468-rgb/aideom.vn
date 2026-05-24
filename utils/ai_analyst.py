"""
AI Analyst - dùng Groq API phân tích kết quả từng bài toán.
Lấy API key miễn phí tại: console.groq.com
"""
import streamlit as st
from groq import Groq

# Câu hỏi thảo luận chính sách cho từng bài
DISCUSSION_QUESTIONS = {
    "Bài 1": [
        "TFP của Việt Nam có xu hướng tăng hay giảm trong giai đoạn 2020-2025? Điều đó nói lên gì về chất lượng tăng trưởng?",
        "Trong các yếu tố mới D, AI, H — yếu tố nào đóng góp nhiều nhất cho tăng trưởng giai đoạn vừa qua? Vì sao?",
        "Mục tiêu Việt Nam đạt 30% kinh tế số/GDP vào 2030 có khả thi không nếu dựa trên mô hình này? Cần ràng buộc gì?",
    ],
    "Bài 2": [
        "Khi ngân sách tổng tăng thêm 1 tỷ VND, GDP kỳ vọng tăng thêm bao nhiêu? Đây có phải là cận trên hợp lý của chi phí cơ hội của vốn công?",
        "Vì sao R&D có hệ số tác động cao nhất nhưng lại có ràng buộc tối thiểu thấp nhất?",
        "Tỷ lệ 35% công nghệ chiến lược (AI + R&D) có khả thi không khi ngân sách nhà nước Việt Nam 2025 ưu tiên hạ tầng giao thông và an sinh xã hội?",
    ],
    "Bài 3": [
        "Theo kết quả, ba ngành nào nên được ưu tiên đẩy mạnh chuyển đổi số và AI trước? Kết quả có phù hợp với Nghị quyết 57-NQ/TW không?",
        "Tại sao ngành Khai khoáng có năng suất rất cao nhưng vẫn không nằm trong nhóm ưu tiên?",
        "Bộ trọng số nên do ai quyết định: chuyên gia kỹ thuật, hội đồng chính sách, hay quy trình đối thoại công khai? Bàn về governance và tính chính danh chính sách.",
    ],
    "Bài 4": [
        "Nếu bỏ ràng buộc công bằng, vốn sẽ chảy về vùng nào? Tại sao? Hậu quả xã hội dài hạn ra sao?",
        "Ràng buộc trần ngân sách mỗi vùng (C3) có thể coi như một 'chính sách phân quyền'. Nó làm giảm Z* bao nhiêu phần trăm? Mức giảm này có chấp nhận được không?",
        "Vùng Tây Nguyên có sàn 5.000 tỷ nhưng hệ số AI rất thấp (0,45). Nên đầu tư vào AI tại Tây Nguyên hay tập trung H và I trước?",
    ],
    "Bài 5": [
        "Vì sao mô hình bỏ qua dự án P15 (Open Data) dù tỷ suất lợi ích/chi phí rất cao? Đây có phải là kết quả mong muốn về mặt chính sách?",
        "Ràng buộc 'bắt buộc P14 (an ninh mạng)' có làm giảm Z* không? Việc bắt buộc này có hợp lý không?",
        "Mô hình giả định các dự án độc lập về lợi ích, nhưng P8 (AI quốc gia) và P13 (bán dẫn) có lợi ích cộng hưởng. Làm thế nào để mô hình hóa hiệu ứng cộng hưởng này?",
    ],
    "Bài 6": [
        "Vùng nào dẫn đầu theo TOPSIS với trọng số chuyên gia? Đây có phải vùng nên triển khai trung tâm AI quốc gia đầu tiên không?",
        "Khi dùng trọng số Entropy, vùng nào có sự thay đổi xếp hạng lớn nhất? Vì sao?",
        "Theo Quyết định 127/QĐ-TTg, Việt Nam đặt mục tiêu xây dựng 3 trung tâm AI lớn. Chọn 3 vùng nào dựa trên kết quả TOPSIS? Có cần điều chỉnh thêm tiêu chí địa-chính trị không?",
    ],
    "Bài 7": [
        "Khi quan sát đường biên Pareto, đánh đổi giữa tăng trưởng và bao trùm có rõ ràng không? Mức đánh đổi đó nói lên điều gì về cơ cấu kinh tế Việt Nam?",
        "Trọng số (0,40; 0,25; 0,20; 0,15) có phản ánh đúng ưu tiên hiện tại của Việt Nam theo văn kiện Đại hội XIII không? Nên điều chỉnh thế nào để phù hợp với cam kết COP26?",
        "Vai trò của NSGA-II ở đây có gì khác so với LP đơn mục tiêu? Nó có thay thế được quyết định chính trị không?",
    ],
    "Bài 8": [
        "Quỹ đạo tối ưu của K, D, AI, H có 'front-loaded' hay 'back-loaded' không? Vì sao mô hình đề xuất như vậy?",
        "Tỷ lệ đầu tư AI/đầu tư H theo thời gian có ổn định không? Mô hình ngụ ý gì: đào tạo nhân lực nên đi trước hay đồng thời với đầu tư AI?",
        "Hệ số chiết khấu ρ=0,97 ngụ ý chính phủ quan tâm nhiều đến dài hạn. Nếu ρ=0,90 (ngắn hạn hơn), kết quả thay đổi thế nào? Đây có phải lý do các chính phủ thường 'dưới đầu tư' vào R&D?",
    ],
    "Bài 9": [
        "Ngành nào cần đầu tư đào tạo lại nhiều nhất theo kết quả tối ưu? Có khớp với cảm nhận thực tế ở Việt Nam không?",
        "Ngành Tài chính-Ngân hàng có nguy cơ thay thế 52% nhưng cũng có hệ số tạo việc làm mới rất cao. Mô hình khuyến nghị chiến lược gì cho ngành này?",
        "Có nên đầu tư x_AI vào ngành Nông-Lâm-Thủy sản không, vì hệ số tạo việc làm AI thấp (8,5) nhưng số lao động dịch chuyển lại rất lớn?",
    ],
    "Bài 10": [
        "So với lời giải xác định, lời giải SP có xu hướng đầu tư H nhiều hơn hay ít hơn? Vì sao?",
        "VSS dương nói lên điều gì về giá trị của tư duy xác suất trong hoạch định chính sách Việt Nam?",
        "COVID-19 (2020-2022) và bão Yagi (2024) là các cú sốc thực tế. Liệu Việt Nam có đang 'dưới đầu tư' vào nhân lực số như một hàng hóa bảo hiểm?",
    ],
    "Bài 11": [
        "Khi nền kinh tế ở trạng thái GDP growth thấp, D thấp, U cao — chính sách π*(s) chọn hành động gì? Có khớp với 'quick win' không?",
        "Khi GDP growth cao, AI cao, U thấp — chính sách chọn gì? Phù hợp với 'consolidation' không?",
        "Mục 11 bài báo nhấn mạnh 'AI không thay thế quyết định chính trị-xã hội'. Tích hợp π* vào quy trình hoạch định chính sách Việt Nam như thế nào để không vi phạm nguyên tắc này?",
    ],
    "Bài 12": [
        "So sánh 5 kịch bản: kịch bản nào cho GDP 2030 cao nhất? Kịch bản nào cân bằng nhất giữa tăng trưởng và rủi ro?",
        "Kịch bản S5 (Tối ưu cân bằng) có phù hợp với mục tiêu Việt Nam 2030 theo Nghị quyết 57-NQ/TW không?",
        "Nếu phải chọn một kịch bản để trình Chính phủ, bạn chọn kịch bản nào và lý do?",
    ],
}


def analyze(
    bai_so: str,
    ten_bai: str,
    context: str,
    api_key: str,
    extra_instruction: str = "",
    question: str = "",
) -> str:
    system_prompt = (
        "Bạn là chuyên gia kinh tế phát triển Việt Nam, am hiểu chính sách công và mô hình toán học. "
        "Phân tích bằng tiếng Việt, rõ ràng, có số liệu cụ thể, gắn với thực tiễn chính sách Việt Nam. "
        "Dùng bullet points, trình bày có cấu trúc. Tối đa 500 từ."
    )

    if question:
        user_prompt = (
            f"{bai_so} — {ten_bai}\n\n"
            f"Kết quả mô hình:\n{context}\n\n"
            f"Câu hỏi thảo luận chính sách:\n{question}\n\n"
            "Hãy trả lời câu hỏi trên một cách sâu sắc, có dẫn chứng số liệu từ kết quả mô hình, "
            "và gắn với thực tiễn chính sách Việt Nam (Nghị quyết 57-NQ/TW, QĐ 749, QĐ 127...)."
        )
    else:
        user_prompt = (
            f"{bai_so} — {ten_bai}\n\n"
            f"Kết quả mô hình:\n{context}\n\n"
            f"{extra_instruction}\n\n"
            "Hãy: (1) nhận xét kết quả có hợp lý không, "
            "(2) chỉ ra ý nghĩa chính sách quan trọng nhất, "
            "(3) đề xuất 1-2 khuyến nghị cụ thể cho Việt Nam."
        )

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=1200,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Lỗi: {e}"


def render_analyst_box(
    bai_so: str,
    ten_bai: str,
    context: str,
    extra_instruction: str = "",
):
    """
    Hiển thị phân tích AI + tab câu hỏi thảo luận chính sách.
    Gọi hàm này ở cuối mỗi trang bài toán.
    """
    st.markdown("---")
    st.subheader("🤖 Phân tích AI (Groq)")

    api_key = st.session_state.get("groq_api_key", "")
    if not api_key:
        st.warning(
            "Chưa có API key. Nhập Groq API key ở **sidebar** để dùng tính năng này. "
            "Lấy miễn phí tại: console.groq.com"
        )
        return

    tab_phan_tich, tab_cauhoi = st.tabs(["📊 Phân tích kết quả", "💬 Câu hỏi thảo luận"])

    # ── Tab 1: Phân tích kết quả ─────────────────────────────────────────────
    with tab_phan_tich:
        if st.button(f"✨ Phân tích kết quả {bai_so}", key=f"btn_analyze_{bai_so}"):
            with st.spinner("Đang phân tích..."):
                result = analyze(bai_so, ten_bai, context, api_key, extra_instruction)
            st.session_state[f"analysis_{bai_so}"] = result

        if f"analysis_{bai_so}" in st.session_state:
            with st.expander("📋 Kết quả phân tích", expanded=True):
                st.markdown(st.session_state[f"analysis_{bai_so}"])

    # ── Tab 2: Câu hỏi thảo luận chính sách ─────────────────────────────────
    with tab_cauhoi:
        questions = DISCUSSION_QUESTIONS.get(bai_so, [])
        if not questions:
            st.info("Chưa có câu hỏi thảo luận cho bài này.")
            return

        st.markdown("#### Câu hỏi thảo luận chính sách từ đề bài")
        for i, q in enumerate(questions, 1):
            st.markdown(f"**Câu {i}:** {q}")

        st.markdown("---")
        selected_q = st.radio(
            "Chọn câu hỏi để AI trả lời:",
            options=[f"Câu {i}: {q[:80]}..." for i, q in enumerate(questions, 1)],
            key=f"radio_{bai_so}",
        )

        idx = int(selected_q.split(":")[0].replace("Câu ", "")) - 1
        full_question = questions[idx]

        if st.button(f"🧠 AI trả lời câu {idx+1}", key=f"btn_q_{bai_so}_{idx}"):
            with st.spinner("Đang suy nghĩ..."):
                answer = analyze(
                    bai_so, ten_bai, context, api_key,
                    question=full_question
                )
            st.session_state[f"q_answer_{bai_so}_{idx}"] = answer

        key_ans = f"q_answer_{bai_so}_{idx}"
        if key_ans in st.session_state:
            with st.expander(f"💡 Trả lời câu {idx+1}", expanded=True):
                st.markdown(st.session_state[key_ans])
