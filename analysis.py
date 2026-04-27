import pandas as pd
import matplotlib.pyplot as plt


# ----------------------------
# 1. Daten laden & bereinigen
# ----------------------------
def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    # fehlende Werte
    df["population"] = df["population"].fillna(0)
    df["beruf"] = df["beruf"].fillna("Unbekannt")

    # Duplikate entfernen
    df = df.drop_duplicates()

    # Strings säubern
    df["city"] = df["city"].str.strip()

    # Datentypen
    df["population"] = df["population"].astype(int)

    return df


# ----------------------------
# 2. Bar Chart (alle Städte)
# ----------------------------
def plot_all_cities(df):
    df.plot(x="city", y="population", kind="bar")

    plt.title("Population by City")
    plt.xlabel("City")
    plt.ylabel("Population")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig("chart1.png")
    plt.show()


# ----------------------------
# 3. Bar Chart (große Städte)
# ----------------------------
def plot_big_cities(df):
    big_cities = df[df["population"] > 1000000]

    big_cities.plot(x="city", y="population", kind="bar")

    plt.title("Big Cities Population")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig("chart2.png")
    plt.show()


# ----------------------------
# 4. Pie Chart
# ----------------------------
def plot_pie_chart(df):
    top = df.sort_values(by="population", ascending=False).head(5)
    top.set_index("city")["population"].plot(kind="pie")
    
    plt.title("Population Distribution")
    plt.ylabel("")

    plt.savefig("chart3.png")
    plt.show()


# ----------------------------
# 5. Main
# ----------------------------
def main():
    df = load_and_clean_data("data.csv")

    print("Datenübersicht:")
    print(df.head())

    plot_all_cities(df)
    plot_big_cities(df)
    plot_pie_chart(df)


if __name__ == "__main__":
    main()