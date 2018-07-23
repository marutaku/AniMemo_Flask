BEGIN;
create table `users` (
    `id` int(11) unsigned not null auto_increment primary key,
    `name` varchar(255) not null,
    `image_path` varchar(255) null,
    `email` varchar(255) not null,
    `password` varchar(255) not null,
    `created_at` timestamp DEFAULT CURRENT_TIMESTAMP
);

alter table `users` add unique `users_email_unique`(`email`);

create table `works` (
    `id` int(11) unsigned not null auto_increment primary key,
    `title` varchar(255) not null,
    `image_path` varchar(255) null,
    `title_short1` varchar(255) null,
    `title_short2` varchar(255) null,
    `title_short3` varchar(255) null,
    `year` int not null,
    `cours` int not null,
    `public_url` varchar(255) not null,
    `twitter_account` varchar(255) not null,
    `twitter_hash_tag` varchar(255) not null,
    `created_at` timestamp DEFAULT CURRENT_TIMESTAMP
);

create table `follows` (
    `id` int(11) unsigned not null auto_increment primary key,
    `user_id` int(11) unsigned not null,
    `followed_user_id` int(11) unsigned not null,
    `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (followed_user_id) REFERENCES users(id)
);

create table `reviews` (
    `id` int(11) unsigned not null auto_increment primary key,
    `user_id` int(11) unsigned not null,
    `work_id` int(11) unsigned not null,
    `text` varchar(255) not null,
    `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (work_id) REFERENCES works(id)
);

create table `states` (
    `id` int(11) unsigned not null auto_increment primary key,
    `state` int not null,
    `user_id` int(11) unsigned not null,
    `work_id` int(11) unsigned not null,
    `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (work_id) REFERENCES works(id)
);
COMMIT;
