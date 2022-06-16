# FastBerry (FastApi + Strawberry)

FastBerry is blueprint to quickly start a web project with following attribute

1. FastApi, SqlModel, Strawberry as api layer
2. ReactJs as UI layer
3. Stack built and distributed with docker.
4. Minimal env setup required on developer host.

## QuickStart

1. Build and Deploy
   1. `./cenv build`
   2. `./cenv deploy`
   3. Notice the url and explore, passwords should be printed as well
   4. Other configs can reviewed by looking at .env file
2. Auto lint and format api code `./cenv lint`
3. Create new schema migration ` ./cenv alembic revision --autogenerate -m "<Add your Comment>" `
4. Add new python package ` ./cenv poetry add <pip names> `
5. Tail logs of running stack `./cenv logs`
6. Add new npm module `./cenv npm install <module name>`

## TODO

1. Add auth to api
2. Add pagination to api
3. Integrate UI to api
4. Add linter for UI codebase
5. Add k8 deployment configs
6. Add image version and push/pull support
