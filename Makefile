install:
	pip install -r requirements.txt

run:
	uvicorn main:app --reload

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down