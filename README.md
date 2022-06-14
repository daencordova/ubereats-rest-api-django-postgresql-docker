## Ubereats Rest API built with Django, Django Rest Framwork, PostgreSQL and Docker

Uses the default Django development server.

1. Rename *.env.example* to *.env*.
2. Update the environment variables in the *.env* file.
3. Prepare Django environment to start up

```bash
$ make makemigrations
$ make migrate
$ make createsuperuser
$ make collectstatic
```

4. Build the images and run the containers:

```bash
$ make up-development
```
Test it out at [http://localhost:8000](http://localhost:8000).