-- MySQL dump 10.16  Distrib 10.1.20-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: localhost
-- ------------------------------------------------------
-- Server version	10.1.20-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add group',4,'add_group'),(11,'Can change group',4,'change_group'),(12,'Can delete group',4,'delete_group'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add db log',7,'add_dblog'),(20,'Can change db log',7,'change_dblog'),(21,'Can delete db log',7,'delete_dblog'),(22,'Can add db command',8,'add_dbcommand'),(23,'Can change db command',8,'change_dbcommand'),(24,'Can delete db command',8,'delete_dbcommand'),(25,'Can add db client',9,'add_dbclient'),(26,'Can change db client',9,'change_dbclient'),(27,'Can delete db client',9,'delete_dbclient'),(28,'Can add db system',10,'add_dbsystem'),(29,'Can change db system',10,'change_dbsystem'),(30,'Can delete db system',10,'delete_dbsystem'),(31,'Can add db server',11,'add_dbserver'),(32,'Can change db server',11,'change_dbserver'),(33,'Can delete db server',11,'delete_dbserver'),(34,'Can add db ldap',12,'add_dbldap'),(35,'Can change db ldap',12,'change_dbldap'),(36,'Can delete db ldap',12,'delete_dbldap');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(4,'auth','group'),(2,'auth','permission'),(3,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(9,'webapp','dbclient'),(8,'webapp','dbcommand'),(12,'webapp','dbldap'),(7,'webapp','dblog'),(11,'webapp','dbserver'),(10,'webapp','dbsystem');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-01-24 10:54:44.725363'),(2,'auth','0001_initial','2017-01-24 10:54:45.351802'),(3,'admin','0001_initial','2017-01-24 10:54:45.518600'),(4,'admin','0002_logentry_remove_auto_add','2017-01-24 10:54:45.548183'),(5,'contenttypes','0002_remove_content_type_name','2017-01-24 10:54:45.663643'),(6,'auth','0002_alter_permission_name_max_length','2017-01-24 10:54:45.744056'),(7,'auth','0003_alter_user_email_max_length','2017-01-24 10:54:45.821829'),(8,'auth','0004_alter_user_username_opts','2017-01-24 10:54:45.837619'),(9,'auth','0005_alter_user_last_login_null','2017-01-24 10:54:45.880093'),(10,'auth','0006_require_contenttypes_0002','2017-01-24 10:54:45.883536'),(11,'auth','0007_alter_validators_add_error_messages','2017-01-24 10:54:45.896806'),(12,'auth','0008_alter_user_username_max_length','2017-01-24 10:54:45.980364'),(13,'sessions','0001_initial','2017-01-24 10:54:46.051576'),(14,'webapp','0001_initial','2017-01-24 10:54:46.572705'),(15,'webapp','0002_dbldap','2017-01-24 10:54:46.617070'),(16,'webapp','0003_auto_20161216_1204','2017-01-24 10:54:46.674527'),(17,'webapp','0004_dbldap_is_active','2017-01-24 10:54:46.712866'),(18,'webapp','0005_dbldap_date','2017-01-24 10:54:46.763948'),(19,'webapp','0006_auto_20161216_1327','2017-01-24 10:54:46.775408'),(20,'webapp','0007_auto_20161216_1329','2017-01-24 10:54:46.784420'),(21,'webapp','0008_remove_dbldap_last_login','2017-01-24 10:54:46.821933'),(22,'webapp','0009_dbldap_last_login','2017-01-24 10:54:46.885990'),(23,'webapp','0010_dbldap_is_staff','2017-01-24 10:54:46.935699'),(24,'webapp','0011_dbldap_is_authenticated','2017-01-24 10:54:46.997308'),(25,'webapp','0012_dbldap_is_anonymous','2017-01-24 10:54:47.052333'),(26,'webapp','0013_auto_20161220_1025','2017-01-24 10:54:47.067256'),(27,'webapp','0014_auto_20161220_1111','2017-01-24 10:54:47.088249'),(28,'webapp','0015_auto_20161220_1320','2017-01-24 10:54:47.311235');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `webapp_dbclient`
--

DROP TABLE IF EXISTS `webapp_dbclient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webapp_dbclient` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webapp_dbclient`
--

LOCK TABLES `webapp_dbclient` WRITE;
/*!40000 ALTER TABLE `webapp_dbclient` DISABLE KEYS */;
INSERT INTO `webapp_dbclient` VALUES (1,'vagrant'),(2,'docker'),(3,'chef');
/*!40000 ALTER TABLE `webapp_dbclient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `webapp_dbcommand`
--

DROP TABLE IF EXISTS `webapp_dbcommand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webapp_dbcommand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cmd` varchar(60) NOT NULL,
  `id_os_platform_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `webapp_dbcommand_2b69a2cf` (`id_os_platform_id`),
  CONSTRAINT `webapp_dbcomman_id_os_platform_id_07747a68_fk_webapp_dbsystem_id` FOREIGN KEY (`id_os_platform_id`) REFERENCES `webapp_dbsystem` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webapp_dbcommand`
--

LOCK TABLES `webapp_dbcommand` WRITE;
/*!40000 ALTER TABLE `webapp_dbcommand` DISABLE KEYS */;
INSERT INTO `webapp_dbcommand` VALUES (1,'free -mh',2),(2,'free -mh',3),(3,'uptime',2),(4,'uptime',3),(5,'uptime',1),(6,'lparstat -i',1),(7,'vmstat',2),(8,'netstat -rn',3),(9,'oslevel -sq',1);
/*!40000 ALTER TABLE `webapp_dbcommand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `webapp_dbldap`
--

DROP TABLE IF EXISTS `webapp_dbldap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webapp_dbldap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_email` varchar(40) NOT NULL,
  `userdn` varchar(80) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webapp_dbldap`
--

LOCK TABLES `webapp_dbldap` WRITE;
/*!40000 ALTER TABLE `webapp_dbldap` DISABLE KEYS */;
/*!40000 ALTER TABLE `webapp_dbldap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `webapp_dblog`
--

DROP TABLE IF EXISTS `webapp_dblog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webapp_dblog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `client_name` varchar(30) NOT NULL,
  `server_name` varchar(30) NOT NULL,
  `server_ip` varchar(15) NOT NULL,
  `cmd` varchar(60) NOT NULL,
  `cmd_output` longtext NOT NULL,
  `run_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webapp_dblog`
--

LOCK TABLES `webapp_dblog` WRITE;
/*!40000 ALTER TABLE `webapp_dblog` DISABLE KEYS */;
/*!40000 ALTER TABLE `webapp_dblog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `webapp_dbserver`
--

DROP TABLE IF EXISTS `webapp_dbserver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webapp_dbserver` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_name` varchar(30) NOT NULL,
  `server_ip` varchar(15) NOT NULL,
  `id_client_name_id` int(11) NOT NULL,
  `id_os_platform_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `webapp_dbserver_id_client_name_id_248907fa_fk_webapp_dbclient_id` (`id_client_name_id`),
  KEY `webapp_dbserver_2b69a2cf` (`id_os_platform_id`),
  CONSTRAINT `webapp_dbserver_id_client_name_id_248907fa_fk_webapp_dbclient_id` FOREIGN KEY (`id_client_name_id`) REFERENCES `webapp_dbclient` (`id`),
  CONSTRAINT `webapp_dbserver_id_os_platform_id_8d16af17_fk_webapp_dbsystem_id` FOREIGN KEY (`id_os_platform_id`) REFERENCES `webapp_dbsystem` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webapp_dbserver`
--

LOCK TABLES `webapp_dbserver` WRITE;
/*!40000 ALTER TABLE `webapp_dbserver` DISABLE KEYS */;
INSERT INTO `webapp_dbserver` VALUES (1,'ans_host1','',2,2),(2,'ans_host2','',2,2),(3,'vag_host3','192.168.66.6',1,2);
/*!40000 ALTER TABLE `webapp_dbserver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `webapp_dbsystem`
--

DROP TABLE IF EXISTS `webapp_dbsystem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `webapp_dbsystem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `os_platform` varchar(16) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `webapp_dbsystem`
--

LOCK TABLES `webapp_dbsystem` WRITE;
/*!40000 ALTER TABLE `webapp_dbsystem` DISABLE KEYS */;
INSERT INTO `webapp_dbsystem` VALUES (1,'aix'),(2,'linux'),(3,'debian');
/*!40000 ALTER TABLE `webapp_dbsystem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-24 14:20:42
