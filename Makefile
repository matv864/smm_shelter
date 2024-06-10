delete_compose:
	docker container prune -f

dev:
	make delete_compose
	docker compose -f dev.yml up  
server:
	make delete_compose
	docker compose -f server.yml up

full_clean:
	docker container prune -f
	docker rmi smm_shelter-frontend
	docker builder  prune -a