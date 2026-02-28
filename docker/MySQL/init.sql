-- コンテナ初回起動時のテスト用DB、DBユーザーの作成
CREATE DATABASE IF NOT EXISTS app_test;
CREATE USER IF NOT EXISTS 'testuser'@'%' IDENTIFIED BY 'test1234';
GRANT ALL PRIVILEGES ON app_test.* TO 'testuser'@'%';
FLUSH PRIVILEGES;