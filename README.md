# ✨ VSLog
VSLog(Visualized Study Log)という日々の学習記録をグラフ化して「見える化」させるアプリである。  
学習状況の把握、学習へのモチベーション維持・向上を目的とする。

## 🔗 URL
https://vslog.onrender.com/  
Renderというサービスでデプロイ。公開期間2026/4月末までを予定。

## 📚 目次
- [背景](#背景)
- [ターゲット](#ターゲット)
- [使用技術](#使用技術)
- [デモ](#デモ)
- [開発環境の構築](#開発環境の構築)
- [ディレクトリ・ファイル構成](#ディレクトリファイル構成)
- [詳細説明](#詳細説明)

## 背景
未経験からITエンジニアになるためには、「1000時間以上」の勉強時間が必要とされている中、自身の学習時間がどの程度なのか、どのような分野を学習してきたのか等、学習状況が把握しづらいと感じていた。  
日々の学習記録を日報形式で記録し、蓄積した学習履歴を視覚化できるアプリがあれば、自身の学習状況が容易に把握でき、モチベーションの維持・向上にも繋がると考えた。  
さらに、未経験からITエンジニアへ転職する際に、本アプリを通じて企業へ学習状況を公開することで、学習意欲・スキルをアピールできるとともに、IT企業の採用担当者においても、自社が求める人材にマッチしているか否かの判断材料の一助になり得ると考えた。  
よって、日々の学習記録をグラフ化して「見える化」させるアプリを開発することとした。

## ターゲット
本アプリはユーザーが学習する分野を自由に設定できるため、IT関連の従事者に限らず、勉学に励む小中高生・学生および資格取得を目指す社会人もターゲットに含めるものとした。
- 小中高生・学生
- 資格取得を目指す社会人
- IT企業への就職・転職希望者

## 使用技術
主な使用技術は以下のとおりである。

| **カテゴリ** | **技術** |
| --- | --- |
| フロントエンド | HTML / CSS / JavaScript |
| バックエンド | Python / Flask / MySQL / PostgreSQL |
| テスト | Pytest |
| インフラ | Render（Paas）/ Docker |
| その他 | Figma/ Canva / GitHub |

## デモ
以下のデモ動画にて、アプリの内容を示す。  
※音声は出ません。

[![デモ動画](<img width="auto" height="auto" alt="Image" src="https://github.com/user-attachments/assets/30b58de3-b13b-4e44-bb18-2aee5b241f6f" />)](https://github.com/user-attachments/assets/0df36f40-1d37-42a7-8828-cc6ba8cfe0c6)

## 開発環境の構築
### 環境変数ファイルの準備
.env.exampleファイルをコピーし、ファイル名を.envにしてルートディレクトリ直下に保存する。  
.envには以下の内容を記述する。  
FLASKのSECRET_KEYは以下のコマンドの出力結果を設定する。  
```
python -c 'import secrets; print(secrets.token_hex())'
```

```
# MySQL設定
MYSQL_HOST=db
MYSQL_ROOT_PASSWORD=secret
MYSQL_USER=appuser
MYSQL_PASSWORD=pass1234
MYSQL_DATABASE=VSLog_db

# MySQLテスト設定
MYSQL_TEST_USER=testuser
MYSQL_TEST_PASSWORD=test1234
MYSQL_TEST_DATABASE=app_test

# Flask設定
FLASK_PORT=5000
SECRET_KEY=dev-secret-key
FLASK_APP='src:create_app("src.config.DevelopmentConfig")'
FLASK_ENV=development
FLASK_DEBUG=1
```

### Dockerによる起動・終了
本アプリはDockerにて開発環境の構築を行っているため、はじめに、自身のローカルPCにDockerデスクトップをインストールする。  
https://www.docker.com/ja-jp/

Dockerデスクトップをインストール後、GitHubから本アプリをcloneする。その後、ターミナル上で以下のコマンドを打つと本アプリがローカルホストで起動する。  
起動コマンド  
```
docker compose up --build
```

次にブラウザを開き、URLの入力フォームに以下を入力する。  
http://localhost:5000/

本アプリ（Flask）のポート番号は「5000」に設定しており、その後ろにログイン画面のURLを記述している。  
既にローカルPC上でポート番号「5000」が使用されている場合は、.envファイルのFlaskポートの番号を変更する。例）5001, 55000など  

（以下が該当箇所であり、必要に応じて修正する。）
***  
ファイルパス：VSLog/.env  
該当箇所：`FLASK_PORT=5000`  
***

アプリを終了するには、ターミナル上で以下のコマンドを打つ。  
終了コマンド  
```
docker compose down
```

## ディレクトリ・ファイル構成
ディレクトリ・ファイル構成を以下に示す。  

<pre>
.
└── VSLog                                              # 個人開発のプロジェクトルート/
    ├── docker                                         # Docker設定/
    │   ├── Flask/
    │   │   ├── Dockerfile
    │   │   ├── Dockerfile.prod
    │   │   └── wait-for-it.sh
    │   ├── MySQL/
    │   │   ├── Dockerfile
    │   │   ├── init.sql
    │   │   └── my.cnf
    │   └── PostgreSQL/
    │       ├── initdb/
    │       │   └── 01_create_test_user.sh
    │       └── Dockerfile.prod
    ├── migrations                                      # migration管理
    ├── src                                             # ソースコード/
    │   ├── analytics                                   # 統計値・グラフ取得のためのビジネスロジック層
    │   ├── blueprints                                  # HTTPリクエスト／レスポンス、コントローラー層
    │   ├── models                                      # ORM定義、モデル層
    │   ├── presenters                                  # DB取得データの整形
    │   ├── static                                      # 静的ファイル一式
    │   ├── templates                                   # html一式
    │   ├── usecases                                    # 認証、プロフィール変更、統計値・グラフ取得のためのユースケース層
    │   ├── __init__.py                                 # Flaskアプリのファクトリー
    │   ├── config.py                                   # 開発環境、本番環境、テスト環境設定
    │   └── extensions.py                               # SQLAlchemy, migrationの拡張機能設定
    ├── tests                                           # Pytestによるテスト設定/
    │   ├── test_auth                                   # 認証テスト
    │   ├── test_profile                                # プロフィールテスト
    │   ├── test_study                                  # 統計値・グラフテスト
    │   ├── conftest.py                                 # テストの初期設定
    │   ├── test_db_smoke.py                            # DB起動確認テスト
    │   ├── test_error.py                               # エラーステータスコードテスト
    │   └── test_show_endpoints.py                      # エンドポイントテスト
    ├── .dockerignore                                   # Dockerビルド除外ファイル
    ├── .gitignore                                      # Git管理対象外リスト
    ├── compose.prod.yaml                               # 本番環境のDockercompose設定
    ├── compose.yaml                                    # 開発環境のDockercompose設定
    ├── Makefile                                        # コマンド省略のための設定
    ├── pytest.ini                                      # Pytestのルートディレクトリ設定
    ├── README.md                                       # 本プロジェクトの説明ファイル
    ├── requirements.txt                                # Python依存パッケージ一覧
    └── wsgi.py                                         # Flaskアプリ本番環境設定
</pre>

## 詳細説明
以降より、本アプリの詳細説明を示す。

### 使用技術の選定理由
本アプリの主な機能は、「学習日数および学習時間等の統計値の取得」、「年月日別・学習分野別のグラフ取得」である。  
よって、採用するプログラミング言語は、統計やデータ分析に強みがあり、そのためのライブラリが豊富な **「Python」** とする。  
PythonのWebフレームワークとして、軽量フレームワークのFlask、フルスタックフレームワークのDjangoがあるが、本アプリでは **「Flask」** を採用する。  
その理由として、本アプリは「学習記録の可視化」に特化したシンプルな機能であり、DBのテーブル数、画面遷移数が比較的少なく、小規模なアプリであると考える。よって、最小限の機能を有する軽量なFlaskを採用することとし、必要に応じてライブラリを追加する。  
Flaskは、Djangoとは異なり、マイグレーション、ORMが標準搭載されていない。  
保守性・運用性の向上のため、データベースのスキーマを柔軟に変更できるマイグレーションライブラリである **「Flask-Migrate」** を追加する。  
さらに、オブジェクト指向プログラミングとデータベースを結びつけ、RDB製品のSQL文法の違いを吸収できるORMを採用することとし、そのライブラリである **「Flask-SQLAlchemy」** を追加する。  
また、グラフ作成ライブラリである **「matplotlib」** を追加する。  
DBは、軽量で安定性が高く、小規模なアプリに適する **「MySQL」** とする。

### 機能一覧
本アプリではユーザーが学習分野を自由に登録し、その学習分野に関する学習時間・学習内容を日報形式で登録すると自動的にグラフが作成され、積み上げた学習記録が可視化できるようになっている。  
ホーム画面にて、学習日数・学習時間の合計・平均の統計値、グラフ（棒グラフ・円グラフ・折れ線グラフ）が表示される。  
統計値は表示期間によって、動的に変更される。例えば、月間2025年9月の表示形式を選択した場合、その年月の統計値が自動で取得できる。  
グラフは、横軸・縦軸・グラフ種類からユーザーが表示したいものを選択し、表示できる。  
プルダウンメニューの変更があれば、自動でフォームが送信され、統計値・グラフのいずれも非同期通信で内容が変化する。  
以下に機能一覧を示す。  

| **分類** | **URL** | **機能** |
| --- | --- | --- |
| 認証前 | / | スタート画面 |
|  | /login | ログイン機能 |
|  | /signup | 新規登録機能 |
|  | /password-reset | パスワード再設定機能 |
| 認証後 | /logout | ログアウト機能 |
|  | /index/<user_id> | 学習日数・学習時間の合計・学習時間の平均の表示機能 |
|  | /index/<user_id> | 表示期間（今週・先週・月間・年間・全期間）選択機能 |
|  | /index/<user_id> | 横軸表示形式（年月日別・分野別）選択機能 |
|  | /index/<user_id> | 縦軸表示形式（時間・％）選択機能 |
|  | /index/<user_id> | グラフ種類の（棒グラフ・円グラフ・折れ線グラフ）選択機能 |
|  | /study-logs/<user_id> | 学習記録の登録・編集機能 |
|  | /study-logs/<user_id> | 年月日に応じた学習記録の切り替え機能 |
|  | /study-fields/<user_id> | 学習分野の登録・編集機能 |
|  | /study-logs/<user_id>, /study-fields/<user_id> | 新規入力項目追加機能 |
|  | /study-logs/<user_id>, /study-fields/<user_id> | 入力項目削除機能 |
|  | /study-logs-list/<user_id> | 学習履歴一覧の閲覧機能 |
|  | /study-logs-list/<user_id> | 学習履歴一覧のモーダルウインドウ表示機能 |
|  | /study-logs-list/<user_id> | 学習履歴一覧の入力・未入力の色分け機能（青・赤） |
|  | /study-logs-list/<user_id> | 年付きに応じた学習履歴一覧の切り替え機能 |
|  | /profile-edit/<user_id> | プロフィール編集機能 |
|  | /password-update/<user_id> | パスワード変更機能 |
| 共通 |  | レスポンシブデザイン機能 |
|  |  | flashメッセージ（正常・エラー）の色分け表示機能 |

### 画面設計、UI/UX
#### デザインの方向性
- シンプルで誰でも簡単に直感的に使える。
- 目が疲れない。奇抜さよりもシンプルさを重視する。
- グラフのカラーはユーザーが自由に選択できるようにする。グラフがカラフルになりやすいので、グラフ以外の要素は、できる限り白・黒・グレー等の無彩色に抑える。
- 画面遷移が少なく、必要な情報にすぐアクセスできる。
- 学習状況を文字情報だけではなく、数字・図で示せる。
- 学習日が一目でわかるように、学習履歴の記入・未記入を色分けする。

#### 使用する色
- ベースカラー：グレー、白
- メインカラー：青（信頼・誠実）
- 文字色：黒

#### 画面遷移図
画面遷移図を以下に示す。  
<img width="auto" height="auto" alt="Image" src="https://github.com/user-attachments/assets/97efb631-2f62-4119-86d8-9927f8853966" />

#### 画面デザイン（ワイヤーフレーム）
画面デザインを以下に示す。画面デザインはFigmaで作成した。  
<img width="auto" height="auto" alt="Image" src="https://github.com/user-attachments/assets/ed9e1c38-737c-4448-af64-25563f97e90c" />

### DB設計
#### ER図
ER図を以下に示す。  
<img width="auto" height="auto" alt="Image" src="https://github.com/user-attachments/assets/23a77ccf-cb8f-45c2-bd7e-e594a9a033d2" />

#### ER図の考え方
- 学習記録テーブル（study_logs）はuser_idと紐づけることで、userが学習記録を「登録・編集・削除」できるようにする。
また、学習分野テーブル（fields）と紐づけることで、学習分野を削除するとその学習分野に関連する学習記録を削除できるようにする。
- 「年月日別」、「分野別」のグラフを作成するために、study_logsテーブルには学習日（study_date）、学習分野（field_id）を設定し、SQL操作でグラフ取得を行う。
- user_idはURLに表示されるため、第3者が推測できないよう、uuid(4)を使用する。そのため、VARCHAR文字数は、uuid(4)の文字数36文字とする。
- emailは重複が生じないように、UNIQUE設定とする。
- 学習日（study_date)の型は、日付で管理するため、時間を含まないDATEとする。
- 学習時間（hours）の型は、時分までの入力を考慮したDECIMALとし、小数点以下2桁表示までとする。また、数十年分の長期累計時間を表示する場合を考慮しDECIMAL(6,2)とする。最大：99999.99時間（およそ11年分の合計時間）まで表示可能である。
- 分野名（field_name）の文字数は、PC上での視認性確保のため、最大20文字のVARCHAR(20)とする。
- 凡例カラー（color_code）は、RGBで表現することとし、16進カラーコード（#FFFFFF）を表現可能なVARCHAR(7)とする。
- 2038年問題を考慮し、created_atの型は「DATETIME」とする。
