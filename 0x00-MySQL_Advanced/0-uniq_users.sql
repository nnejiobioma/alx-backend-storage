-- Check if the 'users' table already exists
CREATE TABLE IF NOT EXISTS `users` (
    --If it doesn't exist, create the 'users' table
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   `email` VARCHAR(255) NOT NULL UNIQUE,
   `name` VARCHAR(255)
);