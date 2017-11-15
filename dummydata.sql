BEGIN TRANSACTION;
DROP TABLE IF EXISTS `store_products`;
CREATE TABLE IF NOT EXISTS `store_products` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	varchar ( 256 ) NOT NULL,
	`description`	varchar ( 512 ) NOT NULL,
	`image_id`	integer,
	FOREIGN KEY(`image_id`) REFERENCES `store_image`(`id`)
);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (1,'Sea Cucumber','The cutest sea cucumber you will ever see',1);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (2,'Fight for the heavens','Just beautiful',2);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (3,'Tiger','Wild tiger',3);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (4,'Barney','Purple dinosaur',4);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (5,'Teletubbies','Teletubbies with snowman',5);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (6,'Abstract','Triangles in different colours',6);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (7,'Black and White','Scary teletubbies',7);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (8,'Christmas','Decorated tree',8);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (9,'Heart of Stone','Wow many stones',9);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (10,'Entertainment','Angelina Jolie',10);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (11,'Macro','Flower heart',11);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (12,'Orangutan','Orange monkey',12);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (13,'Portrait','Man who forgot his umbrella',13);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (14,'Railroad','railroad through a forest',14);
INSERT INTO `store_products` (id,name,description,image_id) VALUES (15,'Still life','Fruit',15);
DROP TABLE IF EXISTS `store_productimages`;
CREATE TABLE IF NOT EXISTS `store_productimages` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`image_id`	integer,
	`product_id`	integer,
	FOREIGN KEY(`image_id`) REFERENCES `store_image`(`id`),
	FOREIGN KEY(`product_id`) REFERENCES `store_products`(`id`)
);
DROP TABLE IF EXISTS `store_productcategories`;
CREATE TABLE IF NOT EXISTS `store_productcategories` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`category_id`	integer,
	`product_id`	integer,
	FOREIGN KEY(`category_id`) REFERENCES `store_category`(`id`),
	FOREIGN KEY(`product_id`) REFERENCES `store_products`(`id`)
);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (1,6,1);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (2,5,2);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (3,13,3);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (4,13,4);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (5,3,5);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (6,7,6);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (7,11,7);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (8,12,8);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (9,3,9);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (10,11,10);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (11,9,11);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (12,13,12);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (13,4,13);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (14,3,14);
INSERT INTO `store_productcategories` (id,category_id,product_id) VALUES (15,10,15);
DROP TABLE IF EXISTS `store_orders`;
CREATE TABLE IF NOT EXISTS `store_orders` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`	date NOT NULL,
	`amount`	integer NOT NULL,
	`customer_id`	integer,
	`product_id`	integer,
	FOREIGN KEY(`customer_id`) REFERENCES `store_accounts`(`id`),
	FOREIGN KEY(`product_id`) REFERENCES `store_products`(`id`)
);
DROP TABLE IF EXISTS `store_image`;
CREATE TABLE IF NOT EXISTS `store_image` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`caption`	varchar ( 64 ) NOT NULL,
	`url`	varchar ( 200 ) NOT NULL
);
INSERT INTO `store_image` (id,caption,url) VALUES (1,'Sea Cucumber','sea-cucumber.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (2,'Purple Space','space1.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (3,'Tiger','tiger.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (4,'Barney','barney.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (5,'Teletubbies','ttsnow.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (6,'Abstract','abstract.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (7,'Black and White','bandw.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (8,'Christmas','christmas.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (9,'Heart of Stone','heartofstone.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (10,'Entertainment','entertainment.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (11,'Macro','macro.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (12,'Orangutan','orangutan.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (13,'Portrait','portrait.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (14,'Railroad','railroad.jpg');
INSERT INTO `store_image` (id,caption,url) VALUES (15,'Still Life','stilllife.jpg');
DROP TABLE IF EXISTS `store_category`;
CREATE TABLE IF NOT EXISTS `store_category` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	varchar ( 64 ) NOT NULL,
	`url`	varchar ( 200 ) NOT NULL
);
INSERT INTO `store_category` (id,name,url) VALUES (1,'All products','all');
INSERT INTO `store_category` (id,name,url) VALUES (2,'Landscape','landscape');
INSERT INTO `store_category` (id,name,url) VALUES (3,'Nature','nature');
INSERT INTO `store_category` (id,name,url) VALUES (4,'Portrait','portrait');
INSERT INTO `store_category` (id,name,url) VALUES (5,'Space','space');
INSERT INTO `store_category` (id,name,url) VALUES (6,'Underwater','underwater');
INSERT INTO `store_category` (id,name,url) VALUES (7,'Abstract','abstract');
INSERT INTO `store_category` (id,name,url) VALUES (8,'Architecture','architecture');
INSERT INTO `store_category` (id,name,url) VALUES (9,'Macro','macro');
INSERT INTO `store_category` (id,name,url) VALUES (10,'Still Life','stilllife');
INSERT INTO `store_category` (id,name,url) VALUES (11,'Black and White','blackandwhite');
INSERT INTO `store_category` (id,name,url) VALUES (12,'Holidays','holidays');
INSERT INTO `store_category` (id,name,url) VALUES (13,'Animals','animals');
INSERT INTO `store_category` (id,name,url) VALUES (14,'Customizable','customizable');
DROP TABLE IF EXISTS `store_address`;
CREATE TABLE IF NOT EXISTS `store_address` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`street`	varchar ( 128 ) NOT NULL,
	`streetnumber`	integer NOT NULL,
	`zipcode`	varchar ( 10 ) NOT NULL,
	`city`	varchar ( 64 ) NOT NULL
);
DROP TABLE IF EXISTS `store_accounts`;
CREATE TABLE IF NOT EXISTS `store_accounts` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`fullname`	varchar ( 64 ) NOT NULL,
	`email`	varchar ( 254 ) NOT NULL UNIQUE,
	`password`	varchar ( 128 ) NOT NULL,
	`birthday`	date NOT NULL,
	`gender`	varchar ( 1 ) NOT NULL,
	`billingaddress_id`	integer,
	`shippingaddress_id`	integer,
	FOREIGN KEY(`billingaddress_id`) REFERENCES `store_address`(`id`),
	FOREIGN KEY(`shippingaddress_id`) REFERENCES `store_address`(`id`)
);
INSERT INTO `store_accounts` (id,fullname,email,password,birthday,gender,billingaddress_id,shippingaddress_id) VALUES (1,'test','test@test.com','ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff','2017-10-30','',NULL,NULL);
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
	`session_key`	varchar ( 40 ) NOT NULL,
	`session_data`	text NOT NULL,
	`expire_date`	datetime NOT NULL,
	PRIMARY KEY(`session_key`)
);
INSERT INTO `django_session` (session_key,session_data,expire_date) VALUES ('qykhlyc83vsej1rwdbcn6wtl5eryxae5','NjYxNjFlZjQ0NmEzNDcwODUzYjY2NzE0ZTIyYzk0ZWRmZWU1N2IwMTp7IkZ1bGxuYW1lIjoidGVzdCIsIkVtYWlsIjoidGVzdEB0ZXN0LmNvbSIsIklzTG9nZ2VkSW4iOnRydWUsIlVJRCI6MH0=','2017-11-13 14:08:49.087630');
INSERT INTO `django_session` (session_key,session_data,expire_date) VALUES ('7vj9y8llxfn5fkei4oq4f1vy7bc8o0ro','NjYxNjFlZjQ0NmEzNDcwODUzYjY2NzE0ZTIyYzk0ZWRmZWU1N2IwMTp7IkZ1bGxuYW1lIjoidGVzdCIsIkVtYWlsIjoidGVzdEB0ZXN0LmNvbSIsIklzTG9nZ2VkSW4iOnRydWUsIlVJRCI6MH0=','2017-11-29 09:24:16.382144');
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`app`	varchar ( 255 ) NOT NULL,
	`name`	varchar ( 255 ) NOT NULL,
	`applied`	datetime NOT NULL
);
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (1,'contenttypes','0001_initial','2017-09-29 09:06:57.668315');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (2,'auth','0001_initial','2017-09-29 09:06:57.699341');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (3,'admin','0001_initial','2017-09-29 09:06:57.724406');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (4,'admin','0002_logentry_remove_auto_add','2017-09-29 09:06:57.749472');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (5,'contenttypes','0002_remove_content_type_name','2017-09-29 09:06:57.795598');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (6,'auth','0002_alter_permission_name_max_length','2017-09-29 09:06:57.814645');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (7,'auth','0003_alter_user_email_max_length','2017-09-29 09:06:57.834700');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (8,'auth','0004_alter_user_username_opts','2017-09-29 09:06:57.856757');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (9,'auth','0005_alter_user_last_login_null','2017-09-29 09:06:57.877900');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (10,'auth','0006_require_contenttypes_0002','2017-09-29 09:06:57.884671');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (11,'auth','0007_alter_validators_add_error_messages','2017-09-29 09:06:57.905024');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (12,'auth','0008_alter_user_username_max_length','2017-09-29 09:06:57.926704');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (13,'sessions','0001_initial','2017-09-29 09:06:57.942812');
INSERT INTO `django_migrations` (id,app,name,applied) VALUES (14,'store','0001_initial','2017-10-30 11:52:05.449912');
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`app_label`	varchar ( 100 ) NOT NULL,
	`model`	varchar ( 100 ) NOT NULL
);
INSERT INTO `django_content_type` (id,app_label,model) VALUES (1,'admin','logentry');
INSERT INTO `django_content_type` (id,app_label,model) VALUES (2,'auth','permission');
INSERT INTO `django_content_type` (id,app_label,model) VALUES (3,'auth','group');
INSERT INTO `django_content_type` (id,app_label,model) VALUES (4,'auth','user');
INSERT INTO `django_content_type` (id,app_label,model) VALUES (5,'contenttypes','contenttype');
INSERT INTO `django_content_type` (id,app_label,model) VALUES (6,'sessions','session');
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`object_id`	text,
	`object_repr`	varchar ( 200 ) NOT NULL,
	`action_flag`	smallint unsigned NOT NULL,
	`change_message`	text NOT NULL,
	`content_type_id`	integer,
	`user_id`	integer NOT NULL,
	`action_time`	datetime NOT NULL,
	FOREIGN KEY(`user_id`) REFERENCES `auth_user`(`id`),
	FOREIGN KEY(`content_type_id`) REFERENCES `django_content_type`(`id`)
);
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`user_id`	integer NOT NULL,
	`permission_id`	integer NOT NULL,
	FOREIGN KEY(`user_id`) REFERENCES `auth_user`(`id`),
	FOREIGN KEY(`permission_id`) REFERENCES `auth_permission`(`id`)
);
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`user_id`	integer NOT NULL,
	`group_id`	integer NOT NULL,
	FOREIGN KEY(`user_id`) REFERENCES `auth_user`(`id`),
	FOREIGN KEY(`group_id`) REFERENCES `auth_group`(`id`)
);
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`password`	varchar ( 128 ) NOT NULL,
	`last_login`	datetime,
	`is_superuser`	bool NOT NULL,
	`first_name`	varchar ( 30 ) NOT NULL,
	`last_name`	varchar ( 30 ) NOT NULL,
	`email`	varchar ( 254 ) NOT NULL,
	`is_staff`	bool NOT NULL,
	`is_active`	bool NOT NULL,
	`date_joined`	datetime NOT NULL,
	`username`	varchar ( 150 ) NOT NULL UNIQUE
);
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`content_type_id`	integer NOT NULL,
	`codename`	varchar ( 100 ) NOT NULL,
	`name`	varchar ( 255 ) NOT NULL,
	FOREIGN KEY(`content_type_id`) REFERENCES `django_content_type`(`id`)
);
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (4,2,'add_permission','Can add permission');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (5,2,'change_permission','Can change permission');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (6,2,'delete_permission','Can delete permission');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (7,3,'add_group','Can add group');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (8,3,'change_group','Can change group');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (9,3,'delete_group','Can delete group');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (10,4,'add_user','Can add user');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (11,4,'change_user','Can change user');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (12,4,'delete_user','Can delete user');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (13,5,'add_contenttype','Can add content type');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (14,5,'change_contenttype','Can change content type');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (15,5,'delete_contenttype','Can delete content type');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (16,6,'add_session','Can add session');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (17,6,'change_session','Can change session');
INSERT INTO `auth_permission` (id,content_type_id,codename,name) VALUES (18,6,'delete_session','Can delete session');
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`group_id`	integer NOT NULL,
	`permission_id`	integer NOT NULL,
	FOREIGN KEY(`permission_id`) REFERENCES `auth_permission`(`id`),
	FOREIGN KEY(`group_id`) REFERENCES `auth_group`(`id`)
);
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	varchar ( 80 ) NOT NULL UNIQUE
);
DROP INDEX IF EXISTS `store_products_image_id_721ea100`;
CREATE INDEX IF NOT EXISTS `store_products_image_id_721ea100` ON `store_products` (
	`image_id`
);
DROP INDEX IF EXISTS `store_productimages_product_id_1b6521cd`;
CREATE INDEX IF NOT EXISTS `store_productimages_product_id_1b6521cd` ON `store_productimages` (
	`product_id`
);
DROP INDEX IF EXISTS `store_productimages_image_id_022dbc20`;
CREATE INDEX IF NOT EXISTS `store_productimages_image_id_022dbc20` ON `store_productimages` (
	`image_id`
);
DROP INDEX IF EXISTS `store_productcategories_product_id_2326777f`;
CREATE INDEX IF NOT EXISTS `store_productcategories_product_id_2326777f` ON `store_productcategories` (
	`product_id`
);
DROP INDEX IF EXISTS `store_productcategories_category_id_9266ac02`;
CREATE INDEX IF NOT EXISTS `store_productcategories_category_id_9266ac02` ON `store_productcategories` (
	`category_id`
);
DROP INDEX IF EXISTS `store_orders_product_id_c1c24d19`;
CREATE INDEX IF NOT EXISTS `store_orders_product_id_c1c24d19` ON `store_orders` (
	`product_id`
);
DROP INDEX IF EXISTS `store_orders_customer_id_0db3dd86`;
CREATE INDEX IF NOT EXISTS `store_orders_customer_id_0db3dd86` ON `store_orders` (
	`customer_id`
);
DROP INDEX IF EXISTS `store_accounts_shippingaddress_id_3efd2cf5`;
CREATE INDEX IF NOT EXISTS `store_accounts_shippingaddress_id_3efd2cf5` ON `store_accounts` (
	`shippingaddress_id`
);
DROP INDEX IF EXISTS `store_accounts_billingaddress_id_c879e903`;
CREATE INDEX IF NOT EXISTS `store_accounts_billingaddress_id_c879e903` ON `store_accounts` (
	`billingaddress_id`
);
DROP INDEX IF EXISTS `django_session_expire_date_a5c62663`;
CREATE INDEX IF NOT EXISTS `django_session_expire_date_a5c62663` ON `django_session` (
	`expire_date`
);
DROP INDEX IF EXISTS `django_content_type_app_label_model_76bd3d3b_uniq`;
CREATE UNIQUE INDEX IF NOT EXISTS `django_content_type_app_label_model_76bd3d3b_uniq` ON `django_content_type` (
	`app_label`,
	`model`
);
DROP INDEX IF EXISTS `django_admin_log_user_id_c564eba6`;
CREATE INDEX IF NOT EXISTS `django_admin_log_user_id_c564eba6` ON `django_admin_log` (
	`user_id`
);
DROP INDEX IF EXISTS `django_admin_log_content_type_id_c4bce8eb`;
CREATE INDEX IF NOT EXISTS `django_admin_log_content_type_id_c4bce8eb` ON `django_admin_log` (
	`content_type_id`
);
DROP INDEX IF EXISTS `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`;
CREATE UNIQUE INDEX IF NOT EXISTS `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` ON `auth_user_user_permissions` (
	`user_id`,
	`permission_id`
);
DROP INDEX IF EXISTS `auth_user_user_permissions_user_id_a95ead1b`;
CREATE INDEX IF NOT EXISTS `auth_user_user_permissions_user_id_a95ead1b` ON `auth_user_user_permissions` (
	`user_id`
);
DROP INDEX IF EXISTS `auth_user_user_permissions_permission_id_1fbb5f2c`;
CREATE INDEX IF NOT EXISTS `auth_user_user_permissions_permission_id_1fbb5f2c` ON `auth_user_user_permissions` (
	`permission_id`
);
DROP INDEX IF EXISTS `auth_user_groups_user_id_group_id_94350c0c_uniq`;
CREATE UNIQUE INDEX IF NOT EXISTS `auth_user_groups_user_id_group_id_94350c0c_uniq` ON `auth_user_groups` (
	`user_id`,
	`group_id`
);
DROP INDEX IF EXISTS `auth_user_groups_user_id_6a12ed8b`;
CREATE INDEX IF NOT EXISTS `auth_user_groups_user_id_6a12ed8b` ON `auth_user_groups` (
	`user_id`
);
DROP INDEX IF EXISTS `auth_user_groups_group_id_97559544`;
CREATE INDEX IF NOT EXISTS `auth_user_groups_group_id_97559544` ON `auth_user_groups` (
	`group_id`
);
DROP INDEX IF EXISTS `auth_permission_content_type_id_codename_01ab375a_uniq`;
CREATE UNIQUE INDEX IF NOT EXISTS `auth_permission_content_type_id_codename_01ab375a_uniq` ON `auth_permission` (
	`content_type_id`,
	`codename`
);
DROP INDEX IF EXISTS `auth_permission_content_type_id_2f476e4b`;
CREATE INDEX IF NOT EXISTS `auth_permission_content_type_id_2f476e4b` ON `auth_permission` (
	`content_type_id`
);
DROP INDEX IF EXISTS `auth_group_permissions_permission_id_84c5c92e`;
CREATE INDEX IF NOT EXISTS `auth_group_permissions_permission_id_84c5c92e` ON `auth_group_permissions` (
	`permission_id`
);
DROP INDEX IF EXISTS `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`;
CREATE UNIQUE INDEX IF NOT EXISTS `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` ON `auth_group_permissions` (
	`group_id`,
	`permission_id`
);
DROP INDEX IF EXISTS `auth_group_permissions_group_id_b120cbf9`;
CREATE INDEX IF NOT EXISTS `auth_group_permissions_group_id_b120cbf9` ON `auth_group_permissions` (
	`group_id`
);
COMMIT;
