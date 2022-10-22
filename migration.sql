DROP DATABASE IF EXISTS `desafio`;

CREATE DATABASE `desafio`;

USE `desafio`;

-- desafio.categories definition

CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`));

-- desafio.products definition

CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(60) NOT NULL,
  `category_id` int NOT NULL,
  `price` float DEFAULT NULL,
  `serie` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`category_id`)
  REFERENCES `categories` (`id`)
  ON DELETE CASCADE);