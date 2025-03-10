
# ❤️ Heart Disease Prediction Project

### 🩺 Описание проекта:
Это проект по предсказанию риска сердечных заболеваний с использованием методов машинного обучения.  
Мы объединили данные из четырёх медицинских клиник и построили модель для определения вероятности наличия болезни сердца на основе медицинских показателей.

### 🔍 Цели проекта:
- Помочь людям заранее оценивать риск сердечных заболеваний.
- Получить опыт работы с медицинскими данными.
- Разработать удобное приложение для пользователей без медицинского образования.

### 📊 Использованные данные:
- Источник: [UCI Heart Disease Dataset](https://archive.ics.uci.edu/dataset/45/heart+disease)
- Общее количество данных: **920 записей**
- Ключевые признаки:
  - Возраст, пол
  - Уровень холестерина, давление
  - Тип боли в груди
  - Результаты ЭКГ и другие параметры

### ⚙️ Использованные технологии:
- Python
- Pandas, Numpy, Matplotlib, Seaborn
- Scikit-learn (машинное обучение)
- Streamlit (веб-интерфейс)
- Joblib (сохранение модели)

### 🧠 Применённые модели:
- Logistic Regression (финальная модель)
- Random Forest
- Gradient Boosting

### ✅ Метрики:
| Метрика   | Значение |
|-----------|----------|
| Accuracy | 83%      |
| Precision| 82%      |
| Recall   | 85%      |
| F1-score | 83%      |

### 🚀 Как запустить проект локально:
```bash
# Клонировать репозиторий
git clone https://github.com/sheather666/heart-disease.git

# Установить зависимости
pip install -r requirements.txt

# Запустить приложение
streamlit run app/app.py
```

### 🌐 Онлайн-версия приложения:
(добавишь сюда ссылку после деплоя)
```
https://heart-disease-m.streamlit.app
```

### 🔮 Планы на развитие:
- Добавить больше данных.
- Улучшить модель (XGBoost, CatBoost).
- Встроить Telegram-бот.

