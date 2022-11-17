CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ADMIN TABLES

CREATE TABLE domains (
  uuid UUID NOT NULL PRIMARY KEY,
  name VARCHAR(80) NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP DEFAULT NULL,
  deleted TIMESTAMP DEFAULT NULL
);

CREATE TABLE fronts (
	uuid UUID NOT NULL PRIMARY KEY,
	name VARCHAR(80) NOT NULL
);

CREATE TABLE apps (
	uuid UUID NOT NULL PRIMARY KEY,
	name VARCHAR(80) NOT NULL,
	front_uuid UUID NOT NULL,
	domain_uuid UUID NOT NULL,
	created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	updated TIMESTAMP DEFAULT NULL,
	deleted TIMESTAMP DEFAULT NULL,
	FOREIGN KEY (front_uuid) REFERENCES fronts (uuid),
	FOREIGN KEY (domain_uuid) REFERENCES domains (uuid)
);

CREATE TABLE permissions (
  uuid UUID NOT NULL PRIMARY KEY,
  name VARCHAR(80) NOT NULL UNIQUE,
  description TEXT NOT NULL,
  config TEXT DEFAULT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP DEFAULT NULL,
  deleted TIMESTAMP DEFAULT NULL
);

CREATE TABLE menus (
  uuid UUID NOT NULL PRIMARY KEY,
  name VARCHAR(80) NOT NULL UNIQUE,
  icon VARCHAR(20) DEFAULT NULL,
  route VARCHAR(20) DEFAULT NULL,
  config TEXT DEFAULT NULL,
  menu_uuid UUID DEFAULT NULL,
  FOREIGN KEY (menu_uuid) REFERENCES menus (uuid)
);

CREATE TABLE roles (
  uuid UUID NOT NULL PRIMARY KEY,
  name VARCHAR(80) NOT NULL,
  identifier VARCHAR(80) NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP DEFAULT NULL,
  deleted TIMESTAMP DEFAULT NULL,
  domain_uuid UUID NOT NULL,
  FOREIGN KEY (domain_uuid) REFERENCES domains (uuid)
);

CREATE TABLE role_permission (
  role_uuid UUID NOT NULL,
  permission_uuid UUID NOT NULL,
  FOREIGN KEY (role_uuid) REFERENCES roles (uuid),
  FOREIGN KEY (permission_uuid) REFERENCES permissions (uuid)
);

CREATE TABLE users (
  uuid UUID NOT NULL PRIMARY KEY,
  name VARCHAR(80) NOT NULL,
  phone VARCHAR(20) DEFAULT NULL UNIQUE,
  email VARCHAR(20) DEFAULT NULL UNIQUE,
  username VARCHAR(80) NOT NULL UNIQUE,
  password VARCHAR(200) NOT NULL,
  salt VARCHAR(200) NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated TIMESTAMP DEFAULT NULL,
  deleted TIMESTAMP DEFAULT NULL
);

CREATE TABLE user_role (
  user_uuid UUID NOT NULL,
  role_uuid UUID NOT NULL,
  FOREIGN KEY (user_uuid) REFERENCES users (uuid),
  FOREIGN KEY (role_uuid) REFERENCES roles (uuid)
);

-- FIRST LOAD

INSERT INTO fronts (uuid, name) VALUES
(uuid_generate_v4(), 'Desktop Windows'),
(uuid_generate_v4(), 'Mobile Android'),
(uuid_generate_v4(), 'Mobile iOS'),
(uuid_generate_v4(), 'Web React'),
(uuid_generate_v4(), 'Web Vue');

-- PROJECT TABLES
