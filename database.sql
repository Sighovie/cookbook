
/*******************************************************************************
   Database Name: recipe
   Description: This is a database for online cookbook/recipe.
   DB Server: MySql
   Author: S. Ighovie
********************************************************************************/

/*******************************************************************************
   Drop database if it exists
********************************************************************************/
DROP DATABASE IF EXISTS `recipe`;


/*******************************************************************************
   Create database
********************************************************************************/
CREATE DATABASE `recipe`;


USE `recipe`;


/*******************************************************************************
   Create Tables
********************************************************************************/
--
-- Table structure for table `authors`
--

CREATE TABLE IF NOT EXISTS `authors` (
  `author_id` smallint NOT NULL AUTO_INCREMENT,
  `email` varchar(150) DEFAULT NULL,
  `password` varchar(80) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(100) DEFAULT NULL,
  `gender` varchar(8) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `address` text,
  `city` varchar(150) DEFAULT NULL,
  `state` varchar(150) DEFAULT NULL,
  `country` varchar(150) DEFAULT NULL,
  `postcode` varchar(15) DEFAULT NULL,
  `reg_date`  date DEFAULT NULL,
  `contact_number` varchar(40) DEFAULT NULL,
  `public_status` char(1) DEFAULT '1',   
  `status` char(1) DEFAULT '1',
  PRIMARY KEY (`author_id`)
) ;



--
-- Table structure for table `recipe`
--

CREATE TABLE IF NOT EXISTS `recipe` (
  `recipe_id` smallint NOT NULL AUTO_INCREMENT,
  `author_id`  smallint NOT NULL,
  `category_id`  smallint NOT NULL,  
  `recipe_name` varchar(100) DEFAULT NULL,
  `ingredients` text,
  `preparation_description` text,
  `known_allergies` text,
  `nutrition` text,     
  `preparation_time`  smallint NOT NULL,  
  `cooking_time`  smallint NOT NULL,  
  `cuisine` varchar(100) DEFAULT NULL,  
  `votes`  smallint NOT NULL DEFAULT 0,
  `likes`  smallint NOT NULL DEFAULT 0,  
  `dislikes`  smallint NOT NULL DEFAULT 0,
  `views`  smallint NOT NULL DEFAULT 0,  
  `post_date` date DEFAULT NULL,
  `image_link` varchar(100) DEFAULT NULL, 
  `public_status` char(1) DEFAULT '1',   
  `status` char(1) DEFAULT '1',
  PRIMARY KEY (`recipe_id`)
) ;

    
--
-- Table structure for table `categories`
--

CREATE TABLE IF NOT EXISTS `categories` (
  `category_id` smallint NOT NULL AUTO_INCREMENT,
  `category_name` varchar(60) DEFAULT NULL,
  `status` char(1) DEFAULT '1',
  PRIMARY KEY (`category_id`)
) ;
INSERT INTO categories (category_name,status) VALUES
('Breakfast', '1'),
('Lunch', '1'),
('Beverages', '1'),
('Appetizers', '1'),
('Soups', '1'),
('Salads', '1'),
('Main dishes: Beef', '1'),
('Main dishes: Poultry', '1'),
('Main dishes: Pork', '1'),
('Main dishes: Seafood', '1'),
('Main dishes: Vegetarian', '1'),
('Side dishes: Vegetables', '1'),
('Side dishes: Other', '1'),
('Desserts', '1'),
('Canning / Freezing', '1'),
('Breads', '1'),
('Holidays', '1'),
('Entertaining', '1');


--
-- Table structure for table `reviews`
--

CREATE TABLE IF NOT EXISTS `reviews` (
  `reviews_id` smallint NOT NULL AUTO_INCREMENT,
  `recipe_id`  smallint NOT NULL,    
  `review` text,
  `status` char(1) DEFAULT '1',
  PRIMARY KEY (`reviews_id`)
) ;