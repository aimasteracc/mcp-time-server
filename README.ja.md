<!-- 言語切替 -->
[English](README.md) | [日本語](README.ja.md) | [中文](README.zh.md)

# 🕐 MCPタイムサーバー

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)

Model Context Protocol (MCP) 向けに構築された、プロフェッショナルかつ本番運用可能なタイムゾーン対応時刻サービスです。全世界のタイムゾーンに対応し、包括的な時刻情報を提供します。

## ✨ 特徴

- 🌍 **グローバルタイムゾーン対応** - 世界中の任意のタイムゾーンの時刻情報を取得
- 📊 **豊富な時刻データ** - フォーマット済み時刻、ISO形式、タイムスタンプなど
- 🔍 **タイムゾーン検索** - リージョンでフィルタ可能
- 📝 **詳細なロギング** - プロフェッショナルな監視・デバッグ用ログ
- ⚡ **非同期パフォーマンス** - async/awaitによる最適化
- 🛡️ **堅牢なエラーハンドリング** - 詳細なエラーメッセージ
- 🔧 **環境設定** - 環境変数を使用した柔軟な設定

## 🚀 クイックスタート

### インストール

```bash
# リポジトリをクローン
git clone https://github.com/your-username/mcp-time-server.git
cd mcp-time-server

# uvで依存パッケージをインストール（推奨）
uv sync

# またはpipで
pip install -e .
```

### サーバの起動

```bash
# MCPサーバを起動
python get_time.py

# またはインストール済みスクリプトで
mcp-time-server
```

### 設定

環境変数で希望のタイムゾーンを設定できます：

```bash
export LOCAL_TIMEZONE="Asia/Shanghai"
python get_time.py
```

## 🛠️ 利用可能なツール

### `get_current_time`

任意のタイムゾーンの詳細な時刻情報を取得します。

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

リージョン指定でフィルタ可能な、利用可能タイムゾーン一覧を取得します。

**パラメータ:**
- `region` (任意): リージョンでフィルタ（例: 'Asia', 'America', 'Europe'）

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

## 🏗️ アーキテクチャ

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

本プロジェクトは最新のPython開発ツールを利用しています：

- **Ruff** - 高速なPythonリンター・フォーマッター
- **MyPy** - 静的型チェック
- **Python 3.12+** - 最新Python機能

### テスト実行

```bash
# コード整形
ruff format .

# コードチェック
ruff check .

# 型チェック
mypy get_time.py
```

## 📋 必要要件

- Python 3.12以上
- MCPフレームワーク（mcp[cli] >= 1.9.4）
- pytz（タイムゾーン用）

## 🤝 コントリビュート

1. リポジトリをフォーク
2. フィーチャーブランチを作成（`git checkout -b feature/amazing-feature`）
3. 変更をコミット（`git commit -m 'Add amazing feature'`）
4. ブランチをプッシュ（`git push origin feature/amazing-feature`）
5. プルリクエストを作成

## 📄 ライセンス

本プロジェクトはMITライセンスです。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 🙏 謝辞

- [Model Context Protocol](https://modelcontextprotocol.io/) を利用
- タイムゾーンデータは [pytz](https://pythonhosted.org/pytz/) 提供
- 信頼性の高いAI向け時刻サービスのニーズから着想

---

<div align="center">
  <strong>MCPエコシステムのために❤️で作成</strong>
</div> 