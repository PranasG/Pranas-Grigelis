import matplotlib.pyplot as plt
import seaborn as sns

def boxplot_pick(X_train, columns, color="lightblue"):
    columns = [col for col in columns if col in X_train.columns]
    
    for col in columns:
        if pd.api.types.is_numeric_dtype(X_train[col]):
            plt.figure(figsize=(6,4))
            sns.boxplot(y=X_train[col], color=color)
            plt.title(f"Boxplot: {col}")
            plt.ylabel(col)
            plt.show()
        else:
            print(f"{col} skiped column.")



import pandas as pd
import numpy as np
from statsmodels.stats.outliers_influence import variance_inflation_factor

def calculate_vif(df):
    # 1. Užkoduojame kategorinius (object / string / bool) stulpelius
    df = pd.get_dummies(df, drop_first=True)

    # 2. Paverčiame viską į float
    df = df.apply(pd.to_numeric, errors="coerce")

    # 3. Pašaliname stulpelius su NaN arba inf
    df = df.replace([np.inf, -np.inf], np.nan).dropna(axis=1)

    # 4. Jei po to nelieka skaitinių stulpelių
    if df.shape[1] == 0:
        print("❌ Nėra nė vieno tinkamo skaitinio stulpelio VIF skaičiavimui!")
        return pd.DataFrame()

    # 5. Skaičiuojame VIF
    vif_data = pd.DataFrame()
    vif_data["feature"] = df.columns
    vif_data["VIF"] = [variance_inflation_factor(df.values, i)
                       for i in range(df.shape[1])]
    return vif_data

import pandas as pd

def create_groups(data: pd.DataFrame) -> pd.DataFrame:
    """
    Prideda grupuotus stulpelius (age_group, bmi_group, avg_glucose_level_group)
    jei originalūs duomenys turi reikalingus stulpelius.
    Grąžina atnaujintą DataFrame.
    """

    # Amžiaus grupės
    if "age" in data.columns:
        data["age_group"] = pd.cut(
            data["age"],
            bins=[0, 18, 35, 50, 65, 120],
            labels=["1", "2", "3", "4", "5"] 
        )
#    """["child", "young", "adult", "middle-aged", "senior"]"""


    # KMI grupės
    if "bmi" in data.columns:
        data["bmi_group"] = pd.cut(
            data["bmi"],
            bins=[0, 18.5, 24.9, 29.9, 40, 100],
            labels=["1", "2", "3", "4", "5"]
        )
# ["underweight", "normal", "overweight", "obese", "extreme"]
    # Glikozės lygio grupės
    if "avg_glucose_level" in data.columns:
        data["avg_glucose_level_group"] = pd.cut(
            data["avg_glucose_level"],
            bins=[0, 100, 140, 200, 300],
            labels=["1", "2", "3", "4"]
        )
# ["low", "normal", "high", "very high"]
    return data


# failas: plot_utils.py
import matplotlib.pyplot as plt
import pandas as pd

def plot_continuous_stroke(data, columns_to_plot, target='stroke', figsize=(12,8)):
    """
    Nubrėžia bar chart tęstiniams kintamiesiems (pvz., age, bmi)
    su pasiskirstymu pagal target (stroke).

    Parametrai:
    -----------
    data : pd.DataFrame
        Duomenų rinkinys, turi target stulpelį.
    columns_to_plot : list
        Sąrašas tęstinių kintamųjų.
    target : str
        Tikslinis kintamasis (default='stroke').
    figsize : tuple
        Grafinio lango dydis.
    """

    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(36, 36))
    axes = axes.flatten()

    for i, col in enumerate(columns_to_plot):
        grouped = data.groupby([col, target]).size().unstack(fill_value=0)
        percent_df = grouped.div(grouped.sum(axis=1), axis=0) * 100

        grouped.plot(kind='bar', ax=axes[i])
        axes[i].set_title(col)
        axes[i].set_ylabel('Count')
        axes[i].legend(title=target, labels=['Yes', 'No'])

        # procentų užrašai
        for bar_container_idx, bar_container in enumerate(axes[i].containers):
            for bar_idx, bar in enumerate(bar_container):
                height = bar.get_height()
                if height > 0:
                    x = bar.get_x() + bar.get_width() / 2
                    percent_val = percent_df.iloc[bar_idx, bar_container_idx]
                    axes[i].text(x, height + 1, f'{percent_val:.1f}%',
                                 ha='center', va='bottom', fontsize=9)

    # pašalinam tuščius axes
    for j in range(len(columns_to_plot), len(axes)):
        fig.delaxes(axes[j])

    plt.subplots_adjust(top=0.85)
    plt.tight_layout()
    plt.show()



from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

def evaluate_model(name, model, X_test, y_test, threshold=0.3):
    """
    Įvertina modelį: spausdina ROC-AUC, confusion matrix, classification report.
    """
    y_proba = model.predict_proba(X_test)[:, 1]
    y_pred = (y_proba >= threshold).astype(int)
    
    print("="*50)
    print(f"📊 Rezultatai modelio: {name}")
    print("ROC-AUC:", roc_auc_score(y_test, y_proba))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("="*50, "\n")
    
    return {
        "name": name,
        "roc_auc": roc_auc_score(y_test, y_proba),
        "confusion_matrix": confusion_matrix(y_test, y_pred),
        "classification_report": classification_report(y_test, y_pred, output_dict=True)
    }
