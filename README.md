# 従業員管理システム

このシステムは、従業員の基本情報、スキル、トレーニング履歴を管理するためのWebアプリケーションです。Djangoフレームワークを使用して構築されており、従業員の情報を登録、更新、削除する機能を提供します。また、ユーザー登録とログインの機能も含まれています。
<p align="right">(<a href="#top">トップへ</a>)</p>


## 主な機能
- **管理者ユーザの作成**: 全てのDBに対してCRUD操作を行える権限を持つユーザの作成および管理
- **ユーザー登録とログイン**: 新規ユーザーの登録と、既存ユーザーのログイン/ログアウト機能  
※一般ユーザができることは以下
- **従業員情報の一覧表示**: 登録されている全従業員の情報を一覧表示
- **従業員情報の詳細表示**: 各従業員の詳細情報（基本情報、スキル、トレーニング履歴）を表示
- **従業員情報の追加**: 新たな従業員の基本情報を追加
- **従業員情報の更新**: 既存のある従業員に対して，基本情報を更新
- **スキル情報の追加と更新**: 既存のある従業員に対して，新たなスキルを追加または更新
<p align="right">(<a href="#top">トップへ</a>)</p>

## 使用技術一覧

- **フロントエンド**: HTML, CSS
- **バックエンド**: Django (Python)
- **データベース**: SQLite (開発用)
<p align="right">(<a href="#top">トップへ</a>)</p>


## 開発環境セットアップ手順

1. 本リポジトリのクローン

```bash
git clone <リポジトリURL>
```
2. Pythonの環境構築  
Python：3.10.2  
Django：3.2  
```bash
# venv仮想環境を構築（任意）
python3 -m venv venv
source venv/bin/activate
```
※仮想環境内に移動．ターミナルの先頭が(venv)となる．
```bash
# 必要なパッケージをインストール
pip install -r requirements.txt
```
```bash
# requirements.txtの作成は以下（ここでは不要）
python3 -m pip freeze > requirements.txt
```
3. アプリの起動
```bash
# DB変更を管理するmigrationsディレクトリの作成（初回のみ）
python manage.py makemigrations employee
# DBのマイグレーション実行（DB変更時のみ）
python manage.py migrate
```
```bash
# 開発サーバーを起動
python manage.py runserver
```
<p align="right">(<a href="#top">トップへ</a>)</p>

## 使用方法
アプリケーションを起動後、ブラウザでhttp://127.0.0.1:8000/にアクセスすることで、従業員管理システムを使用できます。最初にユーザー登録を行い、その後ログインして各種機能を利用してください。
### 管理者の登録方法
```bash
# 管理者権限ユーザーを作成
python3 manage.py createsuperuser
```
<p align="right">(<a href="#top">トップへ</a>)</p>

## 設計詳細
### モデル  
Employee: 従業員の基本情報を表すモデル  
Skill: 従業員のスキル情報を表すモデル   
Training: 従業員のトレーニング履歴を表すモデル  

### ビュー
ビュークラスは、主に従業員情報のCRUD操作とユーザーの登録・ログイン機能を実装しています。ビューの実装では、Djangoのジェネリックビューを拡張し、カスタマイズを加えています。

### テンプレート
テンプレートでは、Bootstrapフレームワークを使用してUIを構築しています。各ページのレイアウトは、再利用可能なコンポーネントを用いて構成されています。
<p align="right">(<a href="#top">トップへ</a>)</p>


## ディレクトリ構成
<pre>
.
├── README.md  
├── db.sqlite3   
├── employee  
│   ├── admin.py  
│   ├── apps.py  
│   ├── forms.py  
│   ├── migrations  
│   │   ├── 0001_initial.py  
│   │  
│   ├── models.py  
│   ├── templates  
│   │   ├── employee  
│   │   │   ├── employee_detail.html  
│   │   │   ├── employee_form.html  
│   │   │   ├── employee_list.html  
│   │   │   └── skill_form.html  
│   │   ├── format  
│   │   │   ├── base.html  
│   │   │   ├── page4.html  
│   │   │   └── page5.html  
│   │   └── registration  
│   │       ├── login.html  
│   │       └── register.html  
│   ├── templatetags  
│   │   └── mytag.py  
│   ├── tests.py  
│   ├── urls.py  
│   ├── views.py  
│   └── views_common.py  
├── empsys  
│   ├── settings.py  
│   ├── urls.py  
│   └── wsgi.py  
├── manage.py  
├── requiremnts.txt  
</pre>
<p align="right">(<a href="#top">トップへ</a>)</p>