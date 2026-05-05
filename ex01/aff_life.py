import matplotlib.pyplot as plt
from load_csv import load


def plot_country_life_expectancy(country_name: str, path: str):
    """
    Loads the CSV file and plots the life expectancy of the given country
    check the main.

    Args:
        country_name (str): Country to plot
        path (str): Path to the CSV file
    """
    try:
        dataset = load(path)
        if dataset is None:
            print("Failed to load dataset")
            return

        if 'country' not in dataset.columns:
            print("Not the expected CSV file")
            return

        dataset = dataset.set_index('country')

        if country_name not in dataset.index:
            print(f"No data found for {country_name}")
            return

    # Convert columns to integers for plotting

        years = [int(x) for x in dataset.loc[country_name].index]
        values = dataset.loc[country_name].values

        plt.figure(figsize=(10, 6))
        plt.plot(years, values, label=country_name)
        plt.title(f'{country_name} Life Expectancy Projections')
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.xticks([x for x in years if x % 40 == 0], rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"CSV year columns are not valid integers: {e}")
        return


def main():
    """Main function for plotting France life expectancy."""
    plot_country_life_expectancy("France", "life_expectancy_years.csv")


if __name__ == "__main__":
    main()
