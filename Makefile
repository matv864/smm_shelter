delete_compose:
	docker container prune -f

dev:
	make delete_compose
	docker compose -f dev.yml up  
server:
	make delete_compose
	docker compose -f server.yml up

database:
	make delete_compose
	docker compose -f database.yml up

full_clean:
	docker container prune -f
	docker builder prune -af
	docker volume prune -af