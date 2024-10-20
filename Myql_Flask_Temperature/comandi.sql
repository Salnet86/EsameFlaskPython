mysql -u another_user -p

SELECT User, Host, plugin FROM mysql.user WHERE User = 'root';

SELECT User, Host, plugin FROM mysql.user WHERE User = 'root';

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
FLUSH PRIVILEGES;

sudo systemctl status mysql

sudo systemctl restart mysql

sudo mysql -u root -p


GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'your_password' WITH GRANT OPTION;
FLUSH PRIVILEGES;


sudo systemctl stop mysql


sudo mysqld_safe --skip-grant-tables &


mysql -u root


USE mysql;
UPDATE user SET authentication_string=PASSWORD('new_password') WHERE User='root';
FLUSH PRIVILEGES;



ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';
FLUSH PRIVILEGES;



sudo systemctl stop mysql
sudo systemctl start mysql


mysql -u root -p
