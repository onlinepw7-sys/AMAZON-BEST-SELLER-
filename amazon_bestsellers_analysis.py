import pandas as pd
import matplotlib.pyplot as plt

# Change this filename if your CSV has a different name.
CSV_FILE = "amazon_bestsellers.csv"


def load_data(filename):
    """Load Amazon bestseller data from a CSV file."""
    df = pd.read_csv(filename)
    return df


def clean_data(df):
    """Basic cleaning for common Amazon bestseller CSV columns."""
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^a-z0-9_]", "", regex=True)
    )

    # Convert common numeric columns when present.
    for column in ["price", "rating", "reviews", "review_count", "ratings_count"]:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column].astype(str).str.replace(r"[^0-9.]", "", regex=True),
                errors="coerce",
            )

    return df


def analyze(df):
    """Print useful analysis without assuming one exact CSV schema."""
    print("\n===== AMAZON BESTSELLERS ANALYSIS =====")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\n--- Columns ---")
    print(", ".join(df.columns))

    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    numeric_columns = df.select_dtypes(include="number").columns.tolist()

    if numeric_columns:
        print("\n--- Numeric Summary ---")
        print(df[numeric_columns].describe().round(2))

    for column in ["rating", "reviews", "review_count", "ratings_count", "price"]:
        if column in df.columns:
            print(f"\n--- Top 10 by {column} ---")
            print(df.sort_values(column, ascending=False).head(10).to_string(index=False))

    text_candidates = [
        "category",
        "product_category",
        "brand",
        "author",
        "genre",
    ]

    for column in text_candidates:
        if column in df.columns:
            print(f"\n--- Most common {column} ---")
            print(df[column].value_counts(dropna=True).head(10))
            break


def create_charts(df):
    """Create simple charts when suitable columns are available."""
    charts_dir = Path("charts")
    charts_dir.mkdir(exist_ok=True)

    if "rating" in df.columns:
        rating_data = df["rating"].dropna()
        if not rating_data.empty:
            plt.figure(figsize=(8, 5))
            rating_data.plot(kind="hist", bins=10)
            plt.title("Amazon Bestseller Rating Distribution")
            plt.xlabel("Rating")
            plt.ylabel("Number of Products")
            plt.tight_layout()
            plt.savefig(charts_dir / "rating_distribution.png")
            plt.close()

    if "price" in df.columns:
        price_data = df["price"].dropna()
        if not price_data.empty:
            plt.figure(figsize=(8, 5))
            price_data.plot(kind="hist", bins=15)
            plt.title("Amazon Bestseller Price Distribution")
            plt.xlabel("Price")
            plt.ylabel("Number of Products")
            plt.tight_layout()
            plt.savefig(charts_dir / "price_distribution.png")
            plt.close()


def main():
    try:
        df = load_data(CSV_FILE)
    except FileNotFoundError:
        print(
            f"CSV file not found: {CSV_FILE}\n"
            "Place your CSV file in the same folder as this script."
        )
        return

    df = clean_data(df)
    analyze(df)
    create_charts(df)


if __name__ == "__main__":
    main()
