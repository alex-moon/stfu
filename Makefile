build:
	scripts/build.sh

run:
	scripts/run.sh

serve: webpack
	npm run dev

deploy:
	scripts/deploy.sh

db:
	scripts/db.sh

dump:
	scripts/dump.sh

migrate:
	scripts/migrate.sh

restore:
	scripts/restore.sh
