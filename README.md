# sample-repo

S&P500の推移、主要な経済指標、関連ニュースを確認できる簡易ダッシュボードです。

## 使い方

1. 依存パッケージをインストールします。
   ```bash
   pip install -r requirements.txt
   ```
2. [NewsAPI](https://newsapi.org/) のAPIキーを取得し、環境変数 `NEWSAPI_KEY` に設定します。
3. ダッシュボードを起動します。
   ```bash
   streamlit run dashboard.py
   ```

ダッシュボードでは直近1年のS&P500の終値、FREDから取得したCPIと失業率、NewsAPIによる関連ニュースを表示します。
