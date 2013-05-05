--===============init users======================
CREATE TABLE `banksalerrest`.`users` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `login_name` VARCHAR(64),
  `login_password` VARCHAR(64),
  `real_name` VARCHAR(32),
  `mobile` VARCHAR(16),
  `department` INTEGER UNSIGNED,
  `user_code` VARCHAR(8),
  `is_active` INT(1) UNSIGNED,
  PRIMARY KEY (`id`)
)
--==================================================
--================init auth_key=====================
CREATE TABLE `banksalerrest`.`auth_key` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` INTEGER UNSIGNED,
  `auth_key` VARCHAR(64),
  PRIMARY KEY (`id`)
)
--==================================================
--================init role_permission==============
CREATE TABLE `banksalerrest`.`role_permission` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `role_id` INTEGER UNSIGNED,
  `permission_id` INTEGER UNSIGNED,
  PRIMARY KEY (`id`)
)
--==================================================
--================init permissions==================
CREATE TABLE `banksalerrest`.`permissions` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `permission_name` VARCHAR(64),
  `code_name` VARCHAR(32),
  PRIMARY KEY (`id`)
)
--==================================================
--================init opera========================
CREATE TABLE `banksalerrest`.`opera` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `opera_name` VARCHAR(64),
  PRIMARY KEY (`id`)
)
--==================================================
--================init opera_permission=============
CREATE TABLE `banksalerrest`.`opera_permission` (
  `id` INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  `permission_id` INTEGER UNSIGNED,
  `opera_id` INTEGER UNSIGNED,
  PRIMARY KEY (`id`)
)
--==================================================