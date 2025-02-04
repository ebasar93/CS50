CREATE TABLE users (
    `id` INT AUTO_INCREMENT,
    `first_name` VARCHAR (32) NOT NULL,
    `last_name` VARCHAR (32) NOT NULL,
    `user_name` VARCHAR (16) NOT NULL UNIQUE,
    `password` VARCHAR (16) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE schools (
    `id` INT AUTO_INCREMENT ,
    `name` VARCHAR (32) NOT NULL,
    `type` ENUM ('Primary', 'Secondary', 'Higher Education') NOT NULL,
    `location` VARCHAR (32) NOT NULL,
    `year` SMALLINT NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE companies (
    `id` INT AUTO_INCREMENT ,
    `name` VARCHAR (32) NOT NULL,
    `location` VARCHAR (32) NOT NULL,
    PRIMARY KEY(`id`)
);
CREATE TABLE connections_users (
    `id` INT AUTO_INCREMENT ,
    `user1_id` INT NOT NULL,
    `user2_id` INT NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY(`user1_id`) REFERENCES `users`(`id`),
    FOREIGN KEY(`user2_id`) REFERENCES `users`(`id`)
);
CREATE TABLE connections_schools (
    `id` INT AUTO_INCREMENT ,
    `user_id` INT NOT NULL,
    `school_id` INT NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    `type` VARCHAR (32) NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY (`school_id`) REFERENCES `schools`(`id`)
);
CREATE TABLE connections_companies (
    `id` INT AUTO_INCREMENT ,
    `user_id` INT NOT NULL,
    `company_id` INT NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE,
    `type` VARCHAR (32) NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`),
    FOREIGN KEY (`company_id`) REFERENCES `companies`(`id`)
);
