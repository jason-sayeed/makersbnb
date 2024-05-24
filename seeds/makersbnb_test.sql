DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;

-- Then, we recreate them
CREATE TABLE spaces (id SERIAL PRIMARY KEY, description VARCHAR(255), price FLOAT, user_id INT, name VARCHAR(255), fromdate VARCHAR(255), todate VARCHAR(255), free_dates TEXT);
CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(255), password VARCHAR(255));
CREATE TABLE requests (id SERIAL PRIMARY KEY,  spaceid INT, date DATE, guestid INT, hostid INT, approved BOOLEAN);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO spaces (description, price, user_id, name, fromdate, todate, free_dates) VALUES ('house with a pool', 99.99, 1,'pool house', '01-01-2024', '31-01-2024', '[01-01-2024, 02-01-2024, 03-01-2024, 03-01-2024, 04-01-2024, 
05-01-2024, 06-01-2024, 07-01-2024, 08-01-2024, 09-01-2024, 
10-01-2024, 11-01-2024, 12-01-2024, 13-01-2024, 14-01-2024, 
15-01-2024, 16-01-2024, 17-01-2024, 18-01-2024, 19-01-2024, 
20-01-2024, 21-01-2024, 22-01-2024, 23-01-2024, 24-01-2024, 
25-01-2024, 26-01-2024, 27-01-2024, 28-01-2024, 29-01-2024, 
30-01-2024]');
INSERT INTO spaces (description, price, user_id, name, fromdate, todate, free_dates) VALUES ('house on a lake', 99.99, 2, 'lake house', '02-01-2024', '03-01-2024', '[02-01-2024,03-01-2024]');
INSERT INTO spaces (description, price, user_id, name, fromdate, todate, free_dates) VALUES ('house on a hill', 99.99, 3, 'hill house', '01-02-2024', '02-02-2024', '[01-02-2024,02-02-2024]');
INSERT INTO users (username, password) VALUES ('user1@test.com', 'password123');
INSERT INTO users (username, password) VALUES ('user2@test.com', 'password000');
INSERT INTO requests (spaceid, date, guestid, hostid, approved) VALUES (1, '2024-01-01', 1, 2, False);