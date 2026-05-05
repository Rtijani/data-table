import matplotlib.pyplot as plt
from load_csv import load


def convert_population(value):
    """Convert population strings like '880k', '1.01M' to numbers."""

    value = str(value)
    if value.endswith('k'):
        return float(value[:-1]) * 1_000
    elif value.endswith('M'):
        return float(value[:-1]) * 1_000_000
    else:
        return float(value)


def main():
    """Load population dataset and display population comparison."""

    try:
        dataset = load("population_total.csv")
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    if dataset is None or 'country' not in dataset.columns:
        print("Invalid dataset")
        print("country not listed")
        return

    """ Use country as index for easier access"""
    dataset = dataset.set_index('country')
    country1 = "France"
    country2 = "Belgium"

    if country1 not in dataset.index or country2 not in dataset.index:
        print("Country not found")
        return

    """ Convert years to integers"""
    try:
        years = [int(year) for year in dataset.columns]
    except Exception as e:
        print(f"Invalid year format: {e}")
        return

    """ Keep only years between 1800 and 2050 using filter """
    years_filtered = [y for y in years if 1800 <= y <= 2040]

    population1 = dataset.loc[
        country1,
        [str(y) for y in years_filtered]].apply(convert_population)
    population2 = dataset.loc[
        country2,
        [str(y) for y in years_filtered]].apply(convert_population)

    plt.figure(figsize=(10, 6))
    plt.plot(years_filtered, population1, label=country1, color='green')
    plt.plot(years_filtered, population2, label=country2, color='blue')

    plt.title("Population projections")
    plt.xlabel("Year")
    plt.xlim(1800, 2050)
    plt.ylabel("Population")
    plt.legend()
    plt.xticks([x for x in years_filtered if x % 40 == 0])
    plt.legend(loc="lower right")
    plt.yticks([20_000_000, 40_000_000, 60_000_000], ["20M", "40M", "60M"])
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
