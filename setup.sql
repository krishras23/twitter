create DATABASE twitter

create TABLE twitter.users (
    userID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(20) UNIQUE,
	userPassword VARCHAR(20),
	email VARCHAR(200),
	createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from twitter.users


INSERT INTO twitter.users (username, userPassword, email) values ();

UPDATE twitter.users

ALTER TABLE twitter.users MODIFY COLUMN username VARCHAR(200);
ALTER TABLE twitter.users MODIFY COLUMN userPassword VARCHAR(200);

create TABLE twitter.tweet (
    tweetID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(20) NOT NULL,
	message VARCHAR (100),
	createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


create TABLE twitter.followers (
    follower VARCHAR(20),
	following VARCHAR(20),
);

SELECT *
FROM tweets
INNER JOIN followers
ON tweets.username = followers.following;

SELECT *
FROM tweets
RIGHT JOIN followers
ON tweets.username = followers.following;

SELECT *
FROM tweets
LEFT JOIN followers
ON tweets.username = followers.following;