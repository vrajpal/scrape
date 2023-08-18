DROP DATABASE IF EXISTS scrape_mlb;

CREATE DATABASE scrape_mlb;

USE scrape_mlb;

CREATE TABLE player(
  player_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name varchar(255),
  last_name varchar(255),
  age INT,
  team_id INT,
  position INT
); 

CREATE TABLE team(
  team_id INT AUTO_INCREMENT PRIMARY KEY,
  name varchar(255),
  location varchar(255)
);

CREATE TABLE stat(
  stat_id INT AUTO_INCREMENT PRIMARY KEY,
  value double(16,4) DEFAULT NULL,
  player_id INT,
  team_id INT,
  stat_name varchar(255),
  stat_abbrev varchar(255)
);
