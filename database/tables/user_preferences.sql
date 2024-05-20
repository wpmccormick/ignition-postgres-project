-- liquibase formatted sql
-- changeset kgamble:init-ExampleTable
CREATE TABLE ignition.user_preferences (
	id SERIAL PRIMARY KEY,
	user_id INTEGER NOT NULL,
	preference_json JSONB NOT NULL
);
