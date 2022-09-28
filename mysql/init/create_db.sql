DROP DATABASE IF EXISTS flipflap;
CREATE DATABASE flipflap;
USE flipflap;

CREATE TABLE IF NOT EXISTS `manga` (
    `manga_id` varchar(36) PRIMARY KEY NOT NULL,
    `title` varchar(255) NOT NULL,
    `author` varchar(255) NOT NULL,
    `page_num` int NOT NULL,
    `is_completed` boolean NOT NULL,
    `created_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `manga_service` (
    `manga_service_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `manga_id` varchar(36) NOT NULL,
    `service_name` varchar(255) NOT NULL,
    `url` text,
    INDEX `manga_idx` (`manga_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `history` (
    `history_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `manga_id` varchar(36) NOT NULL,
    `user_id` varchar(36) NOT NULL,
    `page_ratio` float NOT NULL,
    `created_at` datetime NOT NULL,
    INDEX `user_idx` (`user_id`, `created_at`),
    INDEX `manga_idx` (`manga_id`, `created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `faves` (
    `faves_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `manga_id` varchar(36) NOT NULL,
    `user_id` varchar(36) NOT NULL,
    `created_at` datetime NOT NULL,
    INDEX `user_idx` (`user_id`),
    INDEX `manga_idx` (`manga_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `bookmark` (
    `bookmark_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `manga_id` varchar(36) NOT NULL,
    `user_id` varchar(36) NOT NULL,
    `created_at` datetime NOT NULL,
    INDEX `user_idx` (`user_id`),
    INDEX `manga_idx` (`manga_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tag_manga` (
    `tag_manga_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `manga_id` varchar(36) NOT NULL,
    `tag` varchar(100) NOT NULL,
    INDEX `tag_idx` (`tag`),
    INDEX `manga_idx` (`manga_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE IF NOT EXISTS `tag_user` (
    `tag_user_id` int(11) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    `user_id` varchar(36) NOT NULL,
    `tag` varchar(100) NOT NULL,
    INDEX `tag_idx` (`tag`),
    INDEX `user_idx` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
