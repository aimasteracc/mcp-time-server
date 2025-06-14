<!-- 言語切替 -->
[English](README.md) | [日本語](README.ja.md) | [中文](README.zh.md)

# 🕐 MCPタイムサーバー

プロフェッショナルなタイムゾーン対応の時刻サービス（Model Context Protocol対応）。全世界のタイムゾーンに対応し、詳細な時刻情報を提供します。

## ✨ 特徴

- 🌍 **グローバルタイムゾーン対応** - 世界中の任意のタイムゾーンの時刻情報を取得
- 📊 **豊富な時刻データ** - フォーマット済み時刻、ISO形式、タイムスタンプなど
- 🔍 **タイムゾーン検索** - リージョンでフィルタ可能
- 📝 **詳細なロギング** - プロフェッショナルなログ出力
- ⚡ **非同期対応** - async/awaitによる高パフォーマンス
- 🛡️ **堅牢なエラーハンドリング**
- 🔧 **環境変数による柔軟な設定**

## 🚀 クイックスタート

### インストール

```bash
# リポジトリをクローン
git clone https://github.com/your-username/mcp-time-server.git
cd mcp-time-server

# 依存パッケージをuvでインストール（推奨）
uv sync

# またはpipで
pip install -e .
```

### サーバ起動

```bash
python get_time.py
# または
mcp-time-server
```

### 設定

```bash
export LOCAL_TIMEZONE="Asia/Shanghai"
python get_time.py
```

## 🛠️ 利用可能なツール

### `get_current_time`
任意のタイムゾーンの詳細な時刻情報（JSON形式）を取得します。

**パラメータ:**
- `timezone` (任意): 対象タイムゾーンID（例: 'UTC', 'Asia/Shanghai'）

**戻り値例:**
```json
{
  "timezone": "Asia/Shanghai",
  "formatted_time": "2025-06-14 15:43:37 CST+0800",
  "iso_format": "2025-06-14T15:43:37.123456+08:00",
  "timestamp": 1718349817.123456,
  "weekday": "Friday",
  "month": "June"
}
```

### `list_available_timezones`
利用可能なタイムゾーンを、リージョンでフィルタして取得できます。

**パラメータ:**
- `region` (任意): リージョン（例: 'Asia', 'America', 'Europe'）

**戻り値例:**
```json
["Asia/Shanghai", "Asia/Tokyo", "Asia/Seoul", "..."]
```

### `get_server_info`
サーバのメタデータと機能情報を取得します。

**戻り値例:**
```json
{
  "name": "Professional Time Server",
  "version": "1.0.0",
  "description": "Professional timezone-aware time service",
  "supported_operations": ["get_current_time", "list_available_timezones", "get_server_info"],
  "default_timezone": "UTC",
  "total_timezones": 594
}
```

## 🏗️ ディレクトリ構成

```
./
├── get_time.py          # メインサーバ実装
├── pyproject.toml       # プロジェクト設定
├── README.md            # 英語ドキュメント
├── README.ja.md         # 日本語ドキュメント
├── README.zh.md         # 中国語ドキュメント
├── .gitignore           # Git無視設定
├── .python-version      # Pythonバージョン指定
├── uv.lock              # 依存ロックファイル
```

## 🔧 開発

### コード品質
- **Ruff** - 高速なPythonリンター・フォーマッター
- **MyPy** - 静的型チェック
- **Python 3.12+** - 最新Python機能

### テスト実行
```bash
ruff format .
ruff check .
mypy get_time.py
```

## 📋 必要要件
- Python 3.12以上
- MCPフレームワーク（mcp[cli] >= 1.9.4）
- pytz（タイムゾーン用）

## 🤝 コントリビュート
1. リポジトリをフォーク
2. フィーチャーブランチ作成
3. 変更をコミット
4. プッシュ
5. プルリクエスト作成

## 📄 ライセンス
MITライセンス

## 🙏 謝辞
- Model Context Protocol
- pytz
- AIアプリケーション向け信頼性の高い時刻サービスにインスパイア

---

<div align="center">
  <strong>MCPエコシステムのために❤️で作成</strong>
</div> 