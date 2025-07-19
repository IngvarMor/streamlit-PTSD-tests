This repository contains a set of interactive psychological screening tools implemented in Python using the Streamlit framework. The applications are designed to be delivered via a web interface, allowing respondents to complete standardized self-report questionnaires and receive immediate automated feedback.

Currently supported assessments include:
- ACE (Adverse Childhood Experiences Questionnaire) – screens for early adverse experiences linked to long-term health and psychological risks.
- SIDES-SR (Structured Interview for Disorders of Extreme Stress – Self-Report) – evaluates symptom clusters related to complex trauma and affect dysregulation.
- YSQ-S3R (Young Schema Questionnaire – Short Form, Version 3) – assesses early maladaptive schemas across 18 domains based on schema therapy theory.
- ITQ (International Trauma Questionnaire) – identifies symptom profiles consistent with ICD-11 PTSD and Complex PTSD (CPTSD).

The tools are optimized for individual use in research or psychoeducational settings and provide real-time scoring and interpretation directly in the browser. These applications are not intended to serve as clinical diagnoses but may be useful for initial screening and awareness-raising.


# ACE Questionnaire App

This is a simple Streamlit application that implements the ACE (Adverse Childhood Experiences) questionnaire.

## 🔧 How to Run Locally

1. Clone the repository or download the code.
2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run ace_app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 🌐 Deployment on Render.com

To deploy this application on [Render](https://render.com):

1. Create a public GitHub repository and push the following files:
   - `ace_app.py`
   - `requirements.txt`

2. On Render, create a **new Web Service** linked to your GitHub repo.

3. Set the Start Command to:

```
streamlit run ace_app.py --server.port=10000 --server.enableCORS=false
```

4. Choose "Python" as the environment.

## 📋 Описание на русском

Этот репозиторий содержит набор интерактивных психологических опросников, реализованных на Python с использованием фреймворка Streamlit. Пользователь может пройти тест через веб-интерфейс и немедленно получить интерпретацию результатов.

Поддерживаемые опросники:
- **ACE** — выявление неблагоприятного детского опыта;
- **SIDES-SR** — диагностика нарушений, связанных с комплексной травмой;
- **YSQ-S3R** — оценка ранних дезадаптивных схем (согласно теории схем-терапии);
- **ITQ** — выявление симптомов ПТСР и КПТСР по МКБ-11.

Инструменты предназначены для научных исследований и психообразовательных целей. Не являются средством клинической диагностики.


## 📫 Контакты

Код создан при помощи ChatGPT. Разработчик — Ингвар Морев, психолог.  
Email: [ingwar.corvus@gmail.com](mailto:ingwar.corvus@gmail.com)
