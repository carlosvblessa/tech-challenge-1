#!/usr/bin/env bash
set -e

# 1) Aguarda o Postgres ficar disponível
echo "🔌 Aguardando o Postgres em $DB_HOST:$DB_PORT..."
until PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$DB_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
  sleep 1
done
echo "✅ Postgres disponível!"

# 2) Executa as migrações Alembic
echo "📦 Aplicando migrações Alembic..."
alembic upgrade head

# define porta padrão se não existir (poderia vir como 8000 em dev)
: "${PORT:=8000}"
exec uvicorn src.main:app --host 0.0.0.0 --port "$PORT"
