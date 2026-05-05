import matplotlib.pyplot as plt
from load_csv import load


"""first i load both file as instructed in the subject
if there was any error return nothing
then i checked if the files is none
or country is none it should print an error message
then i made gdp and life expectancy to set to index country
its in the file if you open it
i also made the year to be = 1900
i also set country as index this is very neccessry
i used insertion to give me only the country that existed in both files
some data might be missing so i used not.na to remove
then i also converted he data to numeric using lambda
because here we are working with python and a large file"""


def main():
    """Load income and life expectancy datasets and display 1900 projections.
    Load datasets"""
    try:
        gdp_dataset = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_expectancy_dataset = load(
            "life_expectancy_years.csv")
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return

    """ Check country column """
    if gdp_dataset is None or 'country' not in gdp_dataset.columns:
        print("GDP dataset invalid or missing 'country'")
        return
    if life_expectancy_dataset is None:
        print("Life expectancy dataset invalid ")
        return
    if 'country' not in life_expectancy_dataset.columns:
        print("missing 'country'")
        return

    """ Set index to 'country' """
    gdp_dataset = gdp_dataset.set_index('country')
    life_expectancy_dataset = life_expectancy_dataset.set_index('country')

    year = '1900'

    """ Filter countries with data for 1900 """
    common_countries = gdp_dataset.index.intersection(
        life_expectancy_dataset.index)
    gdp_1900 = gdp_dataset.loc[common_countries, year]
    life_1900 = life_expectancy_dataset.loc[common_countries, year]

    """ Some data may be missing (NaN), remove them """
    valid = gdp_1900.notna() & life_1900.notna()
    gdp_1900 = gdp_1900[valid]
    life_1900 = life_1900[valid]

    """ Convert data to numeric if necessary"""
    gdp_1900 = gdp_1900.astype(float)
    life_1900 = life_1900.astype(float)

    """ Plot life expectancy vs GDP """
    plt.figure(figsize=(10, 6))
    plt.scatter(gdp_1900, life_1900, color='blue', label='Countries')
    plt.title("1900")
    plt.xlabel("Gross Domestic Product ")
    plt.ylabel("Life Expectancy")
    plt.xticks([300, 1000, 10000], [300, "1k", "10k"])
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
