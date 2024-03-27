-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_recipes
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_recipes` ;

-- -----------------------------------------------------
-- Schema esquema_recipes
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_recipes` DEFAULT CHARACTER SET utf8 ;
USE `esquema_recipes` ;

-- -----------------------------------------------------
-- Table `esquema_recipes`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_recipes`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_recipes`.`recipes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_recipes`.`recipes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `date_made` DATETIME NULL,
  `under_30` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recipes_users_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_recipes_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `esquema_recipes`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
