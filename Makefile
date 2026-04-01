# 長いコマンドを省略して打てるようにするための設定
# PHONYはMakefileで独自コマンドを設定するための宣言
.PHONY: up down build logs sh migrate mm csu db test pup pdown pbuild pdb ptest

up:        ## 起動
	docker compose up
down:      ## 停止
	docker compose down
build:     ## ビルド
	docker compose up --build
logs:      ## Flaskのログ確認
	docker compose logs -f app
sh:        ## Flaskコンテナのシェルに入る
	docker compose exec -it app /bin/bash
migrate:   ## マイグレーション実行
	docker compose exec app flask db migrate
db:		   ## MySQLコンテナに入る
	docker compose exec -it db mysql -u appuser -p
test:	   ## テスト用のMySQLデータベースに入る
	docker compose exec -it db mysql -u testuser -p

# prod用
pup:
	docker compose -f compose.prod.yaml --env-file .env.prod up
pdown:
	docker compose -f compose.prod.yaml down -v
pbuild:
	docker compose -f compose.prod.yaml --env-file .env.prod up --build
pdb:
	docker compose exec -it db psql -U appuser -d VSLog_db
ptest:
	docker compose exec -it db psql -U testuser -d app_test