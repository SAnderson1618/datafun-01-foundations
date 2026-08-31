import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("Fetching historical tornado data...")
    url = "https://www.spc.noaa.gov/wcm/data/1950-2022_actual_tornadoes.csv"
    df = pd.read_csv(url)

    # Filter for Colorado tornadoes
    co_data = df[df['st'] == 'CO'].copy()
    print(f"Total historical tornadoes in Colorado: {len(co_data)}")

    # Create a quick summary of tornadoes by magnitude
    mag_counts = co_data['mag'].value_counts().sort_index()
    print("\nTornadoes by Magnitude in CO:\n", mag_counts)

if __name__ == "__main__":
    main()
