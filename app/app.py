import streamlit as st
import pandas as pd
import joblib

# Загрузка модели и scaler
model = joblib.load('app/heart_disease_model.pkl')
scaler = joblib.load('app/scaler.pkl')

st.title("❤️ Предсказание риска сердечного заболевания")

st.markdown("Пожалуйста, введите свои данные для анализа:")

# Ввод данных
age = st.slider('Возраст', 20, 100, 50, help="Ваш возраст в годах.")
sex = st.radio('Пол', [0, 1], format_func=lambda x: 'Женщина' if x == 0 else 'Мужчина',
               help="Укажите ваш пол.")
cp = st.selectbox(
    'Тип боли в груди', 
    [1, 2, 3, 4], 
    format_func=lambda x: {
        1: "Ангинозная боль при нагрузке",
        2: "Боль не связана с физической нагрузкой",
        3: "Неангиозная боль",
        4: "Боль без типичных признаков"
    }[x],
    help="Типы болей в груди, которые могут быть связаны с работой сердца."
)
trestbps = st.slider('Давление в покое', 80, 200, 120, help="Артериальное давление в состоянии покоя (мм рт. ст.).")
chol = st.slider('Холестерин', 100, 600, 200, help="Уровень общего холестерина в крови (мг/дл).")
fbs = st.radio(
    'Уровень сахара натощак >120 мг/дл', 
    [0, 1], 
    format_func=lambda x: 'Нет' if x == 0 else 'Да',
    help="Был ли уровень сахара в крови выше 120 мг/дл при сдаче анализов натощак."
)
restecg = st.selectbox(
    'ЭКГ в покое', 
    [0, 1, 2], 
    format_func=lambda x: {
        0: "Норма",
        1: "Аномалия ST-T",
        2: "Гипертрофия левого желудочка"
    }[x],
    help="Результаты электрокардиограммы в состоянии покоя."
)
thalach = st.slider('Максимальный пульс', 60, 220, 150, help="Максимально достигнутый пульс при нагрузке (уд/мин).")
exang = st.radio(
    'Стенокардия при нагрузке', 
    [0, 1], 
    format_func=lambda x: 'Нет' if x == 0 else 'Да',
    help="Появлялась ли стенокардия при физической нагрузке."
)
oldpeak = st.slider(
    'Депрессия ST', 
    0.0, 6.2, 0.0, step=0.1, 
    help="Показатель депрессии сегмента ST на ЭКГ, измеряется в мм."
)
slope = st.selectbox(
    'Наклон сегмента ST', 
    [1, 2, 3], 
    format_func=lambda x: {
        1: "Восходящий",
        2: "Плоский",
        3: "Нисходящий"
    }[x],
    help="Форма сегмента ST на ЭКГ, отражает изменения в работе сердца."
)
ca = st.slider(
    'Количество крупных сосудов (0-3)', 
    0, 3, 0, 
    help="Количество крупных сосудов, окрашенных флюороскопией."
)
thal = st.selectbox(
    'Талассемия', 
    [3, 6, 7], 
    format_func=lambda x: {
        3: "Норма",
        6: "Фиксированный дефект",
        7: "Обратимый дефект"
    }[x],
    help="Тип талассемии — заболевания крови, влияющего на гемоглобин."
)
# Формирование данных
input_data = pd.DataFrame({
    'age': [age], 'sex': [sex], 'cp': [cp], 'trestbps': [trestbps], 'chol': [chol],
    'fbs': [fbs], 'restecg': [restecg], 'thalach': [thalach],
    'exang': [exang], 'oldpeak': [oldpeak], 'slope': [slope], 'ca': [ca], 'thal': [thal]
})

# Масштабирование
numeric_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'ca']
input_data[numeric_features] = scaler.transform(input_data[numeric_features])

# One-Hot кодирование
input_encoded = pd.get_dummies(input_data).reindex(columns=model.feature_names_in_, fill_value=0)

# Кнопка предсказания
if st.button('🔍 Предсказать'):
    pred = model.predict(input_encoded)
    proba = model.predict_proba(input_encoded)[0, 1]

    st.subheader("📝 Результат:")

    if proba >= 0.7:
        st.error(f"❗ **Высокий риск болезни сердца**\n\n🔴 Вероятность: **{proba:.2%}**\n\nРекомендуется срочно обратиться к врачу!")
    elif proba >= 0.4:
        st.warning(f"⚠️ **Средний риск**\n\n🟠 Вероятность: **{proba:.2%}**\n\nРекомендуется профилактическое обследование.")
    else:
        st.success(f"✅ **Низкий риск**\n\n🟢 Вероятность: **{proba:.2%}**\n\nВсё хорошо, поддерживайте здоровый образ жизни!")
