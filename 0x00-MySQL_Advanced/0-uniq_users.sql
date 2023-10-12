-- Check if the 'users' table already exists
IF NOT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'users') THEN
    -- If it doesn't exist, create the 'users' table
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255)
    );
END IF;

-- Creates table users with variables id, email and name
--CREATE TABLE IF NOT EXISTS `users` (
    --`id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   -- `email` VARCHAR(255) NOT NULL UNIQUE,
   -- `name` VARCHAR(255)
--);
