# Ignition / Postgres Project Template

___

## Prerequisite

Understand the process of creating docker containers using the [docker-image](https://github.com/design-group/ignition-docker).

This project assumes you have a local DG Traefik reverse proxy running, if not, the script will set one up or you can set one up using this repository [dg-traefik-proxy](https://github.com/design-group/dg-traefik-proxy)

All Design Group project repositories use the following automation tools:

- [pre-commit](https://pre-commit.com/)
- [pylint](https://pylint.org/)
- [markdownlint](https://github.com/markdownlint/markdownlint)
- [shellcheck](https://github.com/koalaman/shellcheck)
- [yamllint](https://github.com/adrienverge/yamllint)

Please confirm they are present in your environment before continuing.

___

## Setup

1. Follow [this guide from Github](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) to create a new repository from the template.
1. Go the repository page on GitHub you created in the previous step and copy the clone link under Code-->HTTPS. Navigate to the folder where you want to have the code.

    ```sh
   git clone <clone link for HTTPS>
    ``` 

1. Run the initialization script from the root directory within a bash terminal in VS Code.

    ```sh
   ./scripts/initialize.sh
    ```

___

## Database Versioning

This project uses [liquibase](https://www.liquibase.org/) to manage database versioning.

In order to keep the use of liquibase as simple as possible, the following conventions are used:

1. The liquibase changelog file is located at `database/liquibase/main.yaml`
2. All liquibase changesets are stored as `.sql` files in the `database/tables` directory
3. Any simulated data changesets are stored as `.sql` files in the `database/simulated-data` directory

In order to update the database schema with a new feature, do the following:

1. Add a new changeset to the `database/tables` directory. 
	-	All liquibase changesets must start with a comment that contains the following information:

```sql
-- liquibase formatted sql
-- changeset <my-username>:init-<my-changeset-description>
```

1. Add an `includes` tag to the `database/liquibase/main.yaml` file that points to the new changeset.
1. Start the liquibase container. It will automatically stop when it is done. 

___

## Pre-Configured Database

The template is pre-configured with a postgres database, that can be setup with an `init.sql` script to create the database and tables.

To setup the database, add your `init.sql` script to the `ddl` directory, and uncomment the volume mount in the database. The script will be run when the container is first created, and not as it is stopped and started.

___

## Code Linting

The following tools are used to lint the code:

1. Python: [pylint](https://pylint.org/) 
   - The configuration file is located at `linting/.pylintrc`
1. Markdown: [markdownlint](https://github.com/igorshubovych/markdownlint-cli) 
   - The configuration file is located at `linting/.markdownlint.json` 

The linting is performed using the [pre-commit](https://pre-commit.com/) framework. 
The configuration file is located at `linting/.pre-commit-config.yaml`. 
The linting is performed on all files that are staged for commit. 

To run the linting manually, use the following command:

```sh
pre-commit run --all-files
```

___

## Gateway Config

The gateway configuration is stored in stripped gateway backups, that have all projects removed. In order to get these backups run the following command:

```sh
bash download-gateway-backups.sh
```

The backups are stored in the `backups` directory, and if configured in the compose file will automatically restore when the container is initially created. 

If you are preparing this repository for another user, after configuration of the gateway is complete, run the above backup command, and then uncomment the volume and command listed in the `docker-compose.yml` file.
