# fast_api_movie_search
source venv/bin/activate

export PYTHONDONTWRITEBYTECODE=1

pip3 install -r requirements.txt

creating migration file: alembic revision --autogenerate -m "message"

migrate: alembic upgrade head

python3 main.py
