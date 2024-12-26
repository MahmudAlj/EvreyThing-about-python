import pandas as pd
import numpy as np
import math
from collections import defaultdict

# Veri kümesini oku
data = pd.read_csv('letter_recognition.data', header=None)

# Sütun isimlerini ayarlayalım
columns = ['Letter'] + [f'F{i}' for i in range(16)]
data.columns = columns

# Eğitim ve test setlerine ayıralım
train_data = data[:16000]
test_data = data[16000:]

# Eğitim verisinde harflerin öncül olasılıklarını hesaplayalım
letter_counts = train_data['Letter'].value_counts()
total_samples = len(train_data)

# P(Letter) hesapla
P_letter = letter_counts / total_samples

# Özelliklerin her harf için koşullu olasılıklarını hesapla
# Özelliklerin ayrık olduğunu varsayalım (Her özellik için olasılıkları sayalım)
P_F_given_Letter = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

# Her harf için özelliklerin dağılımlarını hesaplayalım
for _, row in train_data.iterrows():
    letter = row['Letter']
    features = row[1:].values  # 16 özelliği alalım
    for i, feature_value in enumerate(features):
        P_F_given_Letter[letter][f'F{i}'][feature_value] += 1

# Laplace düzgünleştirmesi uygulayarak koşullu olasılıkları hesaplayalım
P_F_given_Letter_laplace = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))

for letter, feature_counts in P_F_given_Letter.items():
    total_letter_count = letter_counts[letter]
    for feature, value_counts in feature_counts.items():
        total_feature_count = sum(value_counts.values())
        for value, count in value_counts.items():
            P_F_given_Letter_laplace[letter][feature][value] = (count + 1) / (total_feature_count + len(value_counts))


# Test verisi üzerinde tahmin yapalım
def naive_bayes_predict(test_sample):
    max_log_prob = -math.inf
    predicted_letter = None

    for letter in P_letter.index:
        # P(Letter) ve P(F1|Letter) * P(F2|Letter) * ... * P(F16|Letter) hesapla
        log_prob = math.log(P_letter[letter])

        features = test_sample[1:].values  # Test örneğinin özellikleri
        for i, feature_value in enumerate(features):
            log_prob += math.log(P_F_given_Letter_laplace[letter][f'F{i}'].get(feature_value,
                                                                               1e-10))  # Laplace düzgünleştirmesi ile sıfır olasılığını engelle

        if log_prob > max_log_prob:
            max_log_prob = log_prob
            predicted_letter = letter

    return predicted_letter


# Test verisi ile modelin doğruluğunu hesaplayalım
correct_predictions = 0
for _, row in test_data.iterrows():
    actual_letter = row['Letter']
    predicted_letter = naive_bayes_predict(row)
    if actual_letter == predicted_letter:
        correct_predictions += 1

accuracy = (correct_predictions / len(test_data)) * 100
print(f"Model doğruluğu: {accuracy:.2f}%")

import matplotlib.pyplot as plt

# Öncül olasılık dağılımını çizdir
plt.figure(figsize=(10, 6))
P_letter.plot(kind='bar')
plt.title("Öncül Olasılık Dağılımı (P(Letter))")
plt.xlabel("Harfler")
plt.ylabel("Öncül Olasılık")
plt.xticks(rotation=90)
plt.show()

# 5 harf ve 3 özellik için sonuçsal olasılık dağılımı
letters_to_plot = ['A', 'B', 'C', 'D', 'E']
features_to_plot = ['F0', 'F1', 'F2']

plt.figure(figsize=(12, 8))

for i, letter in enumerate(letters_to_plot):
    for j, feature in enumerate(features_to_plot):
        ax = plt.subplot(len(letters_to_plot), len(features_to_plot), i * len(features_to_plot) + j + 1)
        values = list(P_F_given_Letter_laplace[letter][feature].values())
        ax.hist(values, bins=10, alpha=0.7, label=letter)
        ax.set_title(f"{letter} - {feature}")
        ax.set_xlabel('Olasılık Değeri')
        ax.set_ylabel('Frekans')

plt.tight_layout()
plt.show()

# Aynı grafikte 5 harf için sonuçsal olasılıkları çizdir
plt.figure(figsize=(10, 6))

for letter in letters_to_plot:
    for feature in features_to_plot:
        plt.plot(P_F_given_Letter_laplace[letter][feature].keys(),
                 P_F_given_Letter_laplace[letter][feature].values(),
                 label=f"{letter} - {feature}")

plt.legend()
plt.title('Sonuçsal Olasılık Dağılımı (5 Harf ve 3 Özellik)')
plt.xlabel('Özellik Değeri')
plt.ylabel('Olasılık')
plt.show()

from sklearn.metrics import confusion_matrix
import seaborn as sns

# Test örneklerini tahmin et
predictions = []
true_labels = test_data['Letter']

for _, row in test_data.iterrows():
    predicted_letter = naive_bayes_predict(row)
    predictions.append(predicted_letter)

# Karmaşa matrisini hesapla
cm = confusion_matrix(true_labels, predictions, labels=P_letter.index)

# Karmaşa matrisini çizdir
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=P_letter.index, yticklabels=P_letter.index)
plt.title("Karmaşa Matrisi")
plt.xlabel("Tahmin Edilen Sınıf")
plt.ylabel("Gerçek Sınıf")
plt.show()

# Doğru tahminleri say
correct_predictions = np.trace(cm)
total_predictions = np.sum(cm)

# Başarı oranı
accuracy = (correct_predictions / total_predictions) * 100
print(f"Model doğruluğu: {accuracy:.2f}%")