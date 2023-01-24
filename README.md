# To set up the project
1. Clone repository to local directory
2. Install [docker](https://docs.docker.com/engine/install/ubuntu/)
3. Install [docker-compose](https://docs.docker.com/compose/install/)
4. Run `cp .env.example .env` to create environments
5. Run `make build` to create images and build containers
6. Run `make beautiful` to collect staticfiles
7. Run `make migrations` to set up db dependencies
8. Run `make superuser` to create superuser and fill the data interactively


# To clean up the services
1. Run `make stop` to stop containers
2. Run `make kill` to delete images and volumes


__endpoints:__<br>
http://localhost/admin - to create posts and comments<br>
http://localhost/posts - to get the list of posts <br>
http://localhost/posts/id - where id is a pk of the exact post, to get the post with all the comments

