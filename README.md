# SQLAddressBook
To better understand SQL and how to make a GUI in python, I created a virtual address book. My SQL based address book  provides a GUI to perform CRUD operations as well as visually traverse the entries within the address book. This was hosted on a Raspberry Pi, but the general workflow is replicable on other playforms and operating systems.

## Steps:
1. Download MariaDB
2. Open Terminal
3. Enter this to download MariaDB:
```properties
sudo apt-get update
sudo apt-get install mariadb-server
```  
4. When prompted, enter ```Y```   (yes) to continue
5. Enter:
```properties
sudo mysqld --console
```  
6. Open up a new terminal
7. Enter this to become a super/root user with all permissions:
```properties
sudo mysql
```  
8. Enter:
```properties
create user ‘jake’@’localhost’ identified by ‘xxxx’;
grant all on *.* to ‘jake’@’localhost’;
quit
mysql -u jake -p
xxxx
```
9. To download python driver, enter:
```properties
sudo apt-get install python3-pymysql
```

## Example commands to create and manipulate data in a database
1. To show databases, enter:
```properties
show databases;
```
2. To enter database, enter:
```properties
use [DATABASE NAME];
```
Now that we are in a database, we will create and change data of a table. In this example, we will use the table entitled, "addressBook".
3. To show tables, enter: (this may be empty if no tables have been made)
```properties
show tables;
```
4. To create a table to store data for an address book, enter:
```properties
create table addressBook (name varchar(50), street varchar(50), city varchar(50), state varchar(50), state varchar(50), zip int(5));
```
5. To describe a table's structure and parameters for each attribute and its datatype, enter:
```properties
describe addressBook;
```
6. To insert values to the addressBook table, enter:
```properties
insert into addressBook values (‘Jake Walker’, 123 Old Town Road’, ‘San Jose’, ‘CA’, 95120);
```
7. To delete entries from the addressBook with a specified string assigned to an attribute of the table, enter:
```properties
Delete from addressBook where [TABLE ATTRIBUTE NAME] = [STRING]
```
