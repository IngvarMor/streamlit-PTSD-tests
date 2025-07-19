import streamlit as st

st.set_page_config(page_title="Опросник ACE", layout="centered")

st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-size: 18px !important;
            line-height: 1.6;
        }

        label, div[role="radiogroup"] {
            font-size: 18px !important;
        }

        .stRadio > div {
            gap: 0.75rem;
        }

        .stMarkdown p {
            font-size: 18px !important;
        }

        h1, h2, h3, h4 {
            font-weight: 700;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Опросник ACE (Неблагоприятный детский опыт)")

questions = [
    "В детстве вас часто оскорбляли, унижали или запугивали взрослые?",
    "Вас били или причиняли физическую боль?",
    "Кто-то из взрослых нарушал ваши сексуальные границы?",
    "Вы чувствовали, что в семье вас не любят или не поддерживают?",
    "Не удовлетворялись базовые потребности: еда, одежда, медицинская помощь?",
    "Кто-то из родителей употреблял алкоголь/наркотики?",
    "Были психические болезни или попытки самоубийства в семье?",
    "Кто-то из родителей сидел в тюрьме?",
    "Вы были свидетелем домашнего насилия?",
    "Родители развелись или долго не жили вместе?"
]

score = 0

st.markdown("Ответьте **Да** или **Нет** на каждый вопрос:")

for i, q in enumerate(questions):
    answer = st.radio(q, ["Нет", "Да"], key=i)
    if answer == "Да":
        score += 1

st.markdown("---")
st.subheader(f"✨ Ваш ACE-балл: **{score}** из 10")

if score == 0:
    st.success("Поздравляем! У вас не было факторов риска по ACE.")
elif score <= 3:
    st.info("Ваш ACE-балл невысокий. Вероятность отсроченных последствий — умеренная.")
elif score <= 6:
    st.warning("ACE-балл средний. Возможны последствия в поведении и эмоциях.")
else:
    st.error("Высокий ACE-балл. Рекомендуется консультация со специалистом.")