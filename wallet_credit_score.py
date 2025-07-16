import pandas as pd
import json
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(filepath):
    with open(filepath, 'r') as f:
        raw_data = json.load(f)

    parsed = []
    for item in raw_data:
        action_data = item.get('actionData', {})
        try:
            parsed.append({
                'user': item.get('userWallet'),
                'action': item.get('action'),
                'timestamp': item.get('timestamp'),
                'amount': float(action_data.get('amount', 0)),
                'asset': action_data.get('assetSymbol', 'UNKNOWN')
            })
        except Exception as e:
            print(f"Error parsing record: {e}")
            continue

    df = pd.DataFrame(parsed)
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df = df.dropna(subset=['user', 'action', 'timestamp'])
    return df

def feature_engineering(df):
    grouped = df.groupby('user')
    features = pd.DataFrame()
    features['total_txns'] = grouped.size()
    features['num_deposit'] = grouped.apply(lambda x: (x['action'].str.lower() == 'deposit').sum())
    features['num_borrow'] = grouped.apply(lambda x: (x['action'].str.lower() == 'borrow').sum())
    features['num_repay'] = grouped.apply(lambda x: (x['action'].str.lower() == 'repay').sum())
    features['num_redeem'] = grouped.apply(lambda x: (x['action'].str.lower() == 'redeemunderlying').sum())
    features['num_liquidation'] = grouped.apply(lambda x: (x['action'].str.lower() == 'liquidationcall').sum())
    features['avg_amount'] = grouped['amount'].mean()
    features['active_days'] = grouped['timestamp'].apply(lambda x: x.dt.date.nunique())
    features['borrow_to_repay_ratio'] = features['num_borrow'] / (features['num_repay'] + 1)
    features['liquidation_ratio'] = features['num_liquidation'] / features['total_txns']
    return features.fillna(0).reset_index()

def score_wallets(features):
    scaler = MinMaxScaler()
    keys = [
        'num_deposit', 'num_repay', 'avg_amount',
        'active_days', 'borrow_to_repay_ratio', 'liquidation_ratio'
    ]
    scaled = pd.DataFrame(scaler.fit_transform(features[keys]), columns=keys)
    scaled['borrow_to_repay_ratio'] = 1 - scaled['borrow_to_repay_ratio']
    scaled['liquidation_ratio'] = 1 - scaled['liquidation_ratio']

    weights = {
        'num_deposit': 0.2,
        'num_repay': 0.2,
        'avg_amount': 0.1,
        'active_days': 0.2,
        'borrow_to_repay_ratio': 0.15,
        'liquidation_ratio': 0.15
    }

    features['score'] = (scaled[list(weights.keys())] * pd.Series(weights)).sum(axis=1) * 1000
    features['score'] = features['score'].clip(0, 1000)
    return features[['user', 'score']]

def plot_distribution(scores_df):
    plt.figure(figsize=(10, 5))
    sns.histplot(scores_df['score'], bins=10, kde=True)
    plt.title("Wallet Score Distribution")
    plt.xlabel("Credit Score (0–1000)")
    plt.ylabel("Number of Wallets")
    plt.grid()
    plt.tight_layout()
    plt.savefig("score_distribution.png")
    plt.show()

if __name__ == "__main__":
    file_path = "user-wallet-transactions.json"
    print("📂 Loading data...")
    df = load_data(file_path)

    print("🔧 Engineering features...")
    features = feature_engineering(df)

    print("💯 Scoring wallets...")
    scored_wallets = score_wallets(features)
    scored_wallets.to_csv("wallet_scores.csv", index=False)

    print("📊 Plotting score distribution...")
    plot_distribution(scored_wallets)

    print("✅ Done! Files saved:")
    print(f"  → wallet_scores.csv")
    print(f"  → score_distribution.png")
