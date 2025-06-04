import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder


# function for preprocessing
def preprocessDataIP(csv):
    # loading the CSV file into a DataFrame
    df = pd.read_csv(csv)


    # adding a new column for a label
    df['is_suspicious'] = (
        (df['is_proxy'] == True) |
        (df['is_hosting'] == True) |
        (df['isp'].fillna("").astype(str).str.lower().str.contains("vpn|tor|mullvad|proton|exit"))
    ).astype(int)


    # encoding categorical features
    countryLabel = LabelEncoder()
    df['country_encoded'] = countryLabel.fit_transform(df['country'])


    # encoding 'isp' feature
    ispLabel = LabelEncoder()
    df['isp_encoded'] = ispLabel.fit_transform(df['isp'])


    # saving the file
    df[['country_encoded', 'isp_encoded', 'is_proxy', 'is_hosting', 'is_suspicious']].to_csv('data\preprocessed_data.csv')

    #
    countryPath = "models/countryLabels.pkl"
    ipsPath = "models/ispLabels.pkl"
    joblib.dump(countryLabel, countryPath)
    joblib.dump(ispLabel, ipsPath)
    print(f"Labels saved to {countryPath}")