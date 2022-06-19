-- --------------------------------------------------------
-- Hôte:                         C:\Users\totor\Documents\db.sqlite3
-- Version du serveur:           3.38.0
-- SE du serveur:                
-- HeidiSQL Version:             12.0.0.6468
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour db
CREATE DATABASE IF NOT EXISTS "db";
;

-- Listage de la structure de table db. auth_group
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. auth_group_permissions
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. auth_permission
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. auth_user
CREATE TABLE IF NOT EXISTS "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. auth_user_groups
CREATE TABLE IF NOT EXISTS "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. auth_user_user_permissions
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. django_admin_log
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0));

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. django_content_type
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. django_migrations
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. django_session
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. webapp_act
CREATE TABLE IF NOT EXISTS "webapp_act" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Nom" varchar(50) NOT NULL);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. webapp_cat
CREATE TABLE IF NOT EXISTS "webapp_cat" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Nom" varchar(50) NOT NULL, "Description" varchar(100000) NOT NULL);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. webapp_film
CREATE TABLE IF NOT EXISTS "webapp_film" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "titre" varchar(50) NOT NULL, "annee" integer NOT NULL, "genre_id" bigint NOT NULL REFERENCES "webapp_cat" ("id") DEFERRABLE INITIALLY DEFERRED, "realisateur_id" bigint NOT NULL REFERENCES "webapp_realisateur" ("id") DEFERRABLE INITIALLY DEFERRED, "acteur_principal_id" bigint NOT NULL REFERENCES "webapp_act" ("id") DEFERRABLE INITIALLY DEFERRED, "synopsis" varchar(100000) NOT NULL, "note" integer NOT NULL, "avis" varchar(100000) NOT NULL, "pseudo" varchar(50) NOT NULL);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. webapp_personne
CREATE TABLE IF NOT EXISTS "webapp_personne" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Nom" varchar(50) NOT NULL, "Prenom" varchar(50) NOT NULL, "Age" integer NOT NULL, "mail" varchar(254) NOT NULL, "password" varchar(50) NOT NULL, "type_id" bigint NOT NULL REFERENCES "webapp_type" ("id") DEFERRABLE INITIALLY DEFERRED, "pseudo" varchar(50) NOT NULL);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. webapp_realisateur
CREATE TABLE IF NOT EXISTS "webapp_realisateur" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "Nom" varchar(50) NOT NULL);

-- Les données exportées n'étaient pas sélectionnées.

-- Listage de la structure de table db. webapp_type
CREATE TABLE IF NOT EXISTS "webapp_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "type" varchar(50) NOT NULL);

-- Les données exportées n'étaient pas sélectionnées.

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
