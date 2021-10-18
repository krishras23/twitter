create DATABASE twitter

create TABLE twitter.user (
	username VARCHAR(20) PRIMARY KEY,
	userPassword VARCHAR(20),
	email VARCHAR(200),
	createdAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

select * from twitter.user


INSERT INTO twitter.user (username, userPassword, email) values ();

UPDATE twitter.user

ALTER TABLE twitter.user MODIFY COLUMN username VARCHAR(200);
ALTER TABLE twitter.user MODIFY COLUMN userPassword VARCHAR(200);

