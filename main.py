import pandas as pd

data = [
    {"name": "Косілов", "height": 182},
    {"name": "Крамарчук", "height": 178},
    {"name": "Микитюк", "height": 174},
    {"name": "Шевчук", "height": 165},
    {"name": "Дмитренко", "height": 164},
    {"name": "Захарчук", "height": 163},
    {"name": "Ярмоленко", "height": 160},
    {"name": "Пономаренко", "height": 158},
    {"name": "Мірошниченко", "height": 157},
    {"name": "Мельниченко", "height": 155},
]

df = pd.DataFrame(data)
print("Дані у вигляді датафрейму:")
print(df)
agg_result = df.groupby('name')['height'].mean()

print("\nРезультати агрегації та групування:")
print(agg_result)