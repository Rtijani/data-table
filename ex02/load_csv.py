import pandas as pd

# For clarity: in this project, Dataset == pandas.DataFrame
Dataset = pd.DataFrame


def load(path: str) -> Dataset | None:
    """
    Loads a CSV file as a Dataset (pandas.DataFrame).
    Args:path (str): Path to the CSV file.
    Print the dataset dimensions (rows, columns)
    Return:Dataset (pandas.DataFrame) if successful,
    None if file is missing or invalid.the relevance of this
    project is understanding what
    DataFrame does so for this project i made my
    Dataset = pd.DataFrame then """
    try:
        dataset = pd.read_csv(path)

        print(f"Loading dataset of dimensions {dataset.shape}")

        return dataset

    except FileNotFoundError:
        print("File not found")
        return None

    except pd.errors.EmptyDataError:
        print("File is empty")
        return None

    except pd.errors.ParserError:
        print("Invalid CSV format")
        return None


def main():
    """
    Main function for testing the load function.
    """
    paths = [
        "population_total.csv"
    ]

    for path in paths:
        print(f"\nTesting path: {path}")
        dataset = load(path)
        if dataset is not None:
            print(dataset.head())
        else:
            print("Failed to load dataset.")


if __name__ == "__main__":
    main()
