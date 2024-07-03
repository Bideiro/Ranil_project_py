-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: ranil_proj
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `UID` int NOT NULL AUTO_INCREMENT,
  `LevelID` int NOT NULL,
  `RUID` varchar(45) DEFAULT NULL,
  `Uname` varchar(45) NOT NULL,
  `Passcode` varchar(6) NOT NULL,
  `Fname` varchar(45) NOT NULL,
  `Lname` varchar(45) NOT NULL,
  `SexID` int NOT NULL,
  `Phono` varchar(12) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Position` varchar(50) DEFAULT NULL,
  `HireDate` date NOT NULL,
  `BirthDate` date NOT NULL,
  `Address` varchar(45) NOT NULL,
  PRIMARY KEY (`UID`),
  UNIQUE KEY `UID_UNIQUE` (`UID`),
  UNIQUE KEY `RUID_UNIQUE` (`RUID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,1,'EMP-001','che','222222','Franchesca Jane','Macam',1,'639493075834','qfnmacam@tip.edu.ph','Sobrang Maganda','2023-01-15','2001-09-22','san mateo rizal'),(2,0,'AD-002','Dei','222222','Deighro','De Ocampo',0,'639876543214','qd-deocampo@tip.edu.ph','stock man','2023-01-15','2002-06-19','taytay rizal'),(3,0,'AD-003','Rheiniel','999999','Rheiniel Jerard','Damasco',1,'123456789','qrjfdamasco@tip.edu.ph','taga measure','2023-01-15','2002-06-19','montalban rizal'),(4,0,'AD-004','Rachel','111111','JCc','Manuel',1,'639999999999','rachel@gmai.com','admin','2000-01-01','2024-06-07','');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `actions`
--

DROP TABLE IF EXISTS `actions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actions` (
  `ActionTypeID` varchar(12) NOT NULL,
  `ActionType` varchar(25) NOT NULL,
  PRIMARY KEY (`ActionTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actions`
--

LOCK TABLES `actions` WRITE;
/*!40000 ALTER TABLE `actions` DISABLE KEYS */;
/*!40000 ALTER TABLE `actions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `algoproddb`
--

DROP TABLE IF EXISTS `algoproddb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `algoproddb` (
  `ProductID` varchar(45) NOT NULL,
  `ProductName` varchar(45) DEFAULT NULL,
  `MonthlyDemand` int DEFAULT NULL,
  `UnitPrice` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ProductID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `algoproddb`
--

LOCK TABLES `algoproddb` WRITE;
/*!40000 ALTER TABLE `algoproddb` DISABLE KEYS */;
INSERT INTO `algoproddb` VALUES ('00-0001','Beef Pro Adult Dog Food',50,140.00),('00-0002','Beef Pro Puppy Dog Food',63,155.00),('01-0001','Aozi Cat Food',50,175.00),('02-0001','African Mix',120,80.00),('02-0002','Apollo Economix Grains',300,37.00),('02-0003','Breeder Mix',290,45.00),('12-0001','Baby Stag Booster',29,80.00),('15-0001','Amtyl 500 Tablet',37,17.00),('15-0002','Amoxicillin 500 Capsule',29,5.00),('15-0003','Agmectin Powder Granules',13,28.00),('15-0004','Astig Dewormer Tablet',37,9.00),('15-0005','Ambroxol Powder',24,38.00),('15-0006','B12 Capsule (50\'s)',59,45.00);
/*!40000 ALTER TABLE `algoproddb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `CategoryID` int NOT NULL AUTO_INCREMENT,
  `Category` varchar(45) NOT NULL,
  PRIMARY KEY (`CategoryID`),
  UNIQUE KEY `ProductTypeID_UNIQUE` (`CategoryID`),
  UNIQUE KEY `ProductType_UNIQUE` (`Category`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (9,'a'),(8,'aso'),(10,'b'),(1,'Cat Food'),(0,'Dog Food'),(2,'Feeds'),(3,'Fertilizers'),(6,'Live Stock'),(5,'Medicine'),(7,'Others'),(4,'Pet Essentials');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `levels`
--

DROP TABLE IF EXISTS `levels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `levels` (
  `LevelID` varchar(12) NOT NULL,
  `Level` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`LevelID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `levels`
--

LOCK TABLES `levels` WRITE;
/*!40000 ALTER TABLE `levels` DISABLE KEYS */;
INSERT INTO `levels` VALUES ('0','Admin'),('1','Employee');
/*!40000 ALTER TABLE `levels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `logs`
--

DROP TABLE IF EXISTS `logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `logs` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `UserID` varchar(45) NOT NULL,
  `UserLevel` varchar(45) DEFAULT NULL,
  `User` varchar(45) DEFAULT NULL,
  `Activity` varchar(45) DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=281 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logs`
--

LOCK TABLES `logs` WRITE;
/*!40000 ALTER TABLE `logs` DISABLE KEYS */;
INSERT INTO `logs` VALUES (1,'EMP-001','Employee','Che','Logged in','2024-07-01 10:01:33'),(2,'1','1','Che','Logged Out','2024-07-01 10:01:40'),(3,'EMP-001','Employee','Che','Logged in','2024-07-01 10:01:53'),(4,'EMP-001','Employee','Che','Logged in','2024-07-01 10:02:49'),(5,'AD-001','Admin','Che','Logged in','2024-07-01 10:26:23'),(6,'AD-001','Admin','Che','Logged in','2024-07-01 10:35:11'),(7,'AD-002','Admin','Dei','Logged in','2024-07-01 10:39:53'),(8,'2','Admin','Dei','Logged Out','2024-07-01 10:48:30'),(9,'AD-001','Admin','Che','Logged in','2024-07-01 10:48:44'),(10,'AD-001','Admin','Che','Logged in','2024-07-01 10:50:04'),(11,'AD-001','Admin','Che','Logged Out','2024-07-01 10:50:13'),(12,'AD-002','Admin','Dei','Logged in','2024-07-01 10:50:43'),(13,'AD-002','Admin','Dei','Logged Out','2024-07-01 10:53:20'),(14,'AD-003','Admin','Rheiniel','Logged in','2024-07-01 10:53:49'),(15,'AD-001','Admin','Che','Logged in','2024-07-01 10:59:43'),(16,'AD-001','Admin','Che','Logged in','2024-07-01 11:02:02'),(17,'AD-001','Admin','Che','Logged in','2024-07-01 11:05:14'),(18,'AD-001','Admin','Che','Logged in','2024-07-01 11:06:04'),(19,'AD-001','Admin','Che','Logged in','2024-07-01 11:08:32'),(20,'AD-001','Admin','Che','Logged in','2024-07-01 11:10:04'),(21,'AD-001','Admin','Che','Logged in','2024-07-01 11:11:21'),(22,'AD-001','Admin','Che','Logged in','2024-07-01 11:12:08'),(23,'AD-001','Admin','Che','Logged in','2024-07-01 11:12:39'),(24,'AD-002','Admin','Dei','Logged in','2024-07-01 11:22:13'),(25,'AD-002','Admin','Dei','Logged in','2024-07-01 11:27:59'),(26,'AD-002','Admin','Dei','Logged in','2024-07-01 11:29:45'),(27,'AD-002','Admin','Dei','Logged in','2024-07-01 11:33:33'),(28,'AD-002','Admin','Dei','Logged in','2024-07-01 11:36:14'),(29,'AD-002','Admin','Dei','Logged in','2024-07-01 11:38:51'),(30,'AD-002','Admin','Dei','Logged in','2024-07-01 11:57:51'),(31,'AD-002','Admin','Dei','Logged in','2024-07-01 11:59:30'),(32,'AD-002','Admin','Dei','Logged in','2024-07-01 12:02:07'),(33,'AD-002','Admin','Dei','Logged in','2024-07-01 12:05:27'),(34,'AD-002','Admin','Dei','Logged in','2024-07-01 12:07:17'),(35,'AD-002','Admin','Dei','Logged in','2024-07-01 12:12:17'),(36,'AD-002','Admin','Dei','Logged in','2024-07-01 12:14:32'),(37,'AD-002','Admin','Dei','Logged in','2024-07-01 12:17:37'),(38,'AD-001','Admin','Che','Logged in','2024-07-01 12:30:11'),(39,'AD-001','Admin','Che','Logged Out','2024-07-01 12:31:06'),(40,'AD-001','Admin','Che','Logged in','2024-07-01 12:31:47'),(41,'AD-001','Admin','Che','Logged Out','2024-07-01 12:48:03'),(42,'AD-001','Admin','Che','Logged in','2024-07-01 13:14:10'),(43,'AD-001','Admin','Che','Logged Out','2024-07-01 13:15:55'),(44,'AD-001','Admin','Che','Logged in','2024-07-01 13:16:09'),(45,'AD-002','Admin','Dei','Logged in','2024-07-01 13:27:17'),(46,'AD-002','Admin','Dei','Logged in','2024-07-01 13:48:36'),(47,'AD-002','Admin','Dei','Logged in','2024-07-01 14:00:01'),(48,'AD-002','Admin','Dei','Logged in','2024-07-01 14:05:36'),(49,'AD-002','Admin','Dei','Logged in','2024-07-01 14:08:19'),(50,'AD-001','Admin','Che','Logged in','2024-07-01 14:20:31'),(51,'AD-001','Admin','Che','Logged Out','2024-07-01 14:20:35'),(52,'AD-001','Admin','Che','Logged in','2024-07-01 14:21:04'),(53,'AD-001','Admin','Che','Logged in','2024-07-01 14:25:51'),(54,'AD-001','Admin','Che','Logged in','2024-07-01 14:29:56'),(55,'AD-001','Admin','Che','Logged in','2024-07-01 14:31:19'),(56,'AD-001','Admin','Che','Logged in','2024-07-01 14:34:54'),(57,'AD-001','Admin','Che','Logged in','2024-07-01 14:36:21'),(58,'AD-001','Admin','Che','Logged in','2024-07-01 14:37:53'),(59,'AD-001','Admin','Che','Logged in','2024-07-01 14:39:12'),(60,'AD-001','Admin','Che','Logged in','2024-07-01 14:41:44'),(61,'AD-001','Admin','Che','Logged in','2024-07-01 14:43:17'),(62,'AD-001','Admin','Che','Logged in','2024-07-01 14:45:04'),(63,'AD-002','Admin','Dei','Logged in','2024-07-01 15:26:01'),(64,'AD-002','Admin','Dei','Logged in','2024-07-01 17:16:49'),(65,'AD-002','Admin','Dei','Logged in','2024-07-01 17:20:40'),(66,'AD-002','Admin','Dei','Logged in','2024-07-01 17:53:38'),(67,'AD-002','Admin','Dei','Logged in','2024-07-01 17:54:21'),(68,'AD-002','Admin','Dei','Logged in','2024-07-01 17:55:16'),(69,'AD-002','Admin','Dei','Logged in','2024-07-01 17:56:37'),(70,'AD-002','Admin','Dei','Logged in','2024-07-01 17:59:05'),(71,'AD-002','Admin','Dei','Logged in','2024-07-01 18:00:13'),(72,'AD-002','Admin','Dei','Logged in','2024-07-01 18:00:54'),(73,'AD-002','Admin','Dei','Logged in','2024-07-01 18:02:48'),(74,'AD-002','Admin','Dei','Logged in','2024-07-01 18:06:07'),(75,'AD-002','Admin','Dei','Logged in','2024-07-01 18:06:47'),(76,'AD-002','Admin','Dei','Logged in','2024-07-01 22:25:05'),(77,'AD-002','Admin','Dei','Logged in','2024-07-01 22:31:49'),(78,'AD-002','Admin','Dei','Logged in','2024-07-02 05:12:11'),(79,'AD-002','Admin','Dei','Logged in','2024-07-02 05:25:38'),(80,'AD-002','Admin','Dei','Logged in','2024-07-02 05:26:36'),(81,'AD-002','Admin','Dei','Logged in','2024-07-02 05:27:46'),(82,'AD-002','Admin','Dei','Logged in','2024-07-02 05:28:38'),(83,'AD-002','Admin','Dei','Logged in','2024-07-02 05:29:37'),(84,'AD-002','Admin','Dei','Logged in','2024-07-02 05:30:40'),(85,'AD-002','Admin','Dei','Logged in','2024-07-02 05:33:15'),(86,'AD-002','Admin','Dei','Logged in','2024-07-02 05:41:47'),(87,'AD-002','Admin','Dei','Logged in','2024-07-02 05:45:21'),(88,'AD-002','Admin','Dei','Logged in','2024-07-02 05:45:53'),(89,'AD-002','Admin','Dei','Logged in','2024-07-02 05:53:02'),(90,'AD-002','Admin','Dei','Logged in','2024-07-02 06:02:12'),(91,'AD-002','Admin','Dei','Logged in','2024-07-02 06:03:09'),(92,'AD-002','Admin','Dei','Logged in','2024-07-02 06:04:21'),(93,'AD-002','Admin','Dei','Logged in','2024-07-02 06:05:20'),(94,'AD-002','Admin','Dei','Logged in','2024-07-02 06:06:31'),(95,'AD-002','Admin','Dei','Logged in','2024-07-02 06:07:24'),(96,'AD-002','Admin','Dei','Logged in','2024-07-02 06:11:09'),(97,'AD-002','Admin','Dei','Logged in','2024-07-02 06:13:34'),(98,'AD-002','Admin','Dei','Logged in','2024-07-02 06:51:10'),(99,'AD-002','Admin','Dei','Logged in','2024-07-02 06:53:05'),(100,'AD-002','Admin','Dei','Logged in','2024-07-02 06:55:26'),(101,'AD-002','Admin','Dei','Logged in','2024-07-02 06:58:02'),(102,'AD-002','Admin','Dei','Logged in','2024-07-02 06:58:40'),(103,'AD-002','Admin','Dei','Logged in','2024-07-02 06:59:28'),(104,'AD-002','Admin','Dei','Logged in','2024-07-02 07:00:51'),(105,'AD-002','Admin','Dei','Logged in','2024-07-02 07:01:25'),(106,'AD-002','Admin','Dei','Logged in','2024-07-02 07:01:59'),(107,'AD-002','Admin','Dei','Logged in','2024-07-02 07:11:03'),(108,'AD-002','Admin','Dei','Logged in','2024-07-02 07:12:42'),(109,'AD-002','Admin','Dei','Logged in','2024-07-02 07:16:44'),(110,'AD-002','Admin','Dei','Logged in','2024-07-02 07:20:14'),(111,'AD-002','Admin','Dei','Logged in','2024-07-02 07:20:39'),(112,'AD-002','Admin','Dei','Logged in','2024-07-02 07:22:22'),(113,'AD-002','Admin','Dei','Logged in','2024-07-02 07:22:39'),(114,'AD-002','Admin','Dei','Logged in','2024-07-02 07:23:00'),(115,'AD-002','Admin','Dei','Logged in','2024-07-02 07:46:47'),(116,'AD-002','Admin','Dei','Logged in','2024-07-02 07:48:26'),(117,'AD-002','Admin','Dei','Logged in','2024-07-02 07:50:23'),(118,'AD-002','Admin','Dei','Logged in','2024-07-02 07:50:47'),(119,'AD-002','Admin','Dei','Logged in','2024-07-02 07:51:12'),(120,'AD-002','Admin','Dei','Logged in','2024-07-02 07:55:25'),(121,'AD-002','Admin','Dei','Logged in','2024-07-02 07:55:49'),(122,'AD-002','Admin','Dei','Logged in','2024-07-02 07:57:03'),(123,'AD-002','Admin','Dei','Logged in','2024-07-02 08:00:23'),(124,'AD-002','Admin','Dei','Logged in','2024-07-02 08:05:35'),(125,'AD-002','Admin','Dei','Logged in','2024-07-02 08:06:17'),(126,'AD-002','Admin','Dei','Logged in','2024-07-02 08:07:32'),(127,'AD-002','Admin','Dei','Logged in','2024-07-02 08:18:19'),(128,'AD-002','Admin','Dei','Logged in','2024-07-02 08:19:22'),(129,'AD-002','Admin','Dei','Logged in','2024-07-02 08:21:26'),(130,'AD-002','Admin','Dei','Logged in','2024-07-02 08:45:03'),(131,'AD-002','Admin','Dei','Logged in','2024-07-02 08:49:30'),(132,'AD-002','Admin','Dei','Logged in','2024-07-02 08:54:58'),(133,'AD-002','Admin','Dei','Logged in','2024-07-02 11:57:47'),(134,'AD-002','Admin','Dei','Logged in','2024-07-02 11:59:31'),(135,'AD-002','Admin','Dei','Logged in','2024-07-02 12:01:46'),(136,'AD-002','Admin','Dei','Logged in','2024-07-02 12:08:15'),(137,'AD-002','Admin','Dei','Logged in','2024-07-02 12:09:11'),(138,'AD-002','Admin','Dei','Logged in','2024-07-02 12:09:45'),(139,'AD-002','Admin','Dei','Logged in','2024-07-02 12:11:56'),(140,'AD-002','Admin','Dei','Logged in','2024-07-02 12:13:20'),(141,'AD-002','Admin','Dei','Logged in','2024-07-02 12:16:22'),(142,'AD-002','Admin','Dei','Logged in','2024-07-02 12:17:55'),(143,'AD-002','Admin','Dei','Logged in','2024-07-02 12:19:44'),(144,'AD-002','Admin','Dei','Logged in','2024-07-02 12:24:04'),(145,'AD-002','Admin','Dei','Logged in','2024-07-02 12:24:54'),(146,'AD-002','Admin','Dei','Logged in','2024-07-02 12:53:40'),(147,'AD-002','Admin','Dei','Logged in','2024-07-02 13:05:19'),(148,'AD-002','Admin','Dei','Logged in','2024-07-02 13:07:42'),(149,'AD-002','Admin','Dei','Logged in','2024-07-02 13:10:07'),(150,'AD-002','Admin','Dei','Logged in','2024-07-02 13:11:15'),(151,'AD-002','Admin','Dei','Logged in','2024-07-02 13:11:59'),(152,'AD-002','Admin','Dei','Logged in','2024-07-02 13:12:39'),(153,'AD-002','Admin','Dei','Logged in','2024-07-02 13:26:52'),(154,'AD-002','Admin','Dei','Logged in','2024-07-02 13:27:46'),(155,'AD-002','Admin','Dei','Logged in','2024-07-02 13:29:09'),(156,'AD-002','Admin','Dei','Logged in','2024-07-02 13:43:57'),(157,'AD-002','Admin','Dei','Logged in','2024-07-02 13:46:25'),(158,'AD-002','Admin','Dei','Logged in','2024-07-02 13:48:13'),(159,'AD-002','Admin','Dei','Logged in','2024-07-02 13:48:47'),(160,'AD-002','Admin','Dei','Logged in','2024-07-02 13:50:33'),(161,'AD-002','Admin','Dei','Logged in','2024-07-02 13:51:27'),(162,'AD-002','Admin','Dei','Logged in','2024-07-02 13:52:39'),(163,'AD-002','Admin','Dei','Logged in','2024-07-02 13:53:57'),(164,'AD-002','Admin','Dei','Logged in','2024-07-02 13:54:57'),(165,'AD-002','Admin','Dei','Logged in','2024-07-02 13:55:20'),(166,'AD-002','Admin','Dei','Logged in','2024-07-02 13:55:44'),(167,'AD-002','Admin','Dei','Logged in','2024-07-02 13:58:04'),(168,'AD-002','Admin','Dei','Logged in','2024-07-02 14:00:38'),(169,'AD-001','Admin','Che','Logged in','2024-07-02 14:05:07'),(170,'AD-001','Admin','Che','Logged in','2024-07-02 14:13:28'),(171,'AD-001','Admin','Che','Logged in','2024-07-02 14:16:26'),(172,'AD-001','Admin','Che','Logged in','2024-07-02 14:19:19'),(173,'AD-001','Admin','Che','Logged in','2024-07-02 14:27:01'),(174,'EMP-001','Employee','che','Logged in','2024-07-02 14:30:33'),(175,'EMP-001','Employee','che','Logged in','2024-07-02 14:33:23'),(176,'EMP-001','Employee','che','Logged in','2024-07-02 14:42:33'),(177,'EMP-001','Employee','che','Logged in','2024-07-02 14:47:05'),(178,'EMP-001','Employee','che','Logged in','2024-07-02 15:00:53'),(179,'EMP-001','Employee','che','Logged in','2024-07-02 15:04:52'),(180,'EMP-001','Employee','che','Logged in','2024-07-02 15:05:16'),(181,'EMP-001','Employee','che','Logged in','2024-07-02 15:06:08'),(182,'EMP-001','Employee','che','Logged in','2024-07-02 15:06:39'),(183,'EMP-001','Employee','che','Logged in','2024-07-02 15:07:05'),(184,'EMP-001','Employee','che','Logged in','2024-07-02 15:08:15'),(185,'EMP-001','Employee','che','Logged in','2024-07-02 15:09:12'),(186,'EMP-001','Employee','che','Logged in','2024-07-02 15:10:15'),(187,'EMP-001','Employee','che','Logged in','2024-07-02 15:11:49'),(188,'EMP-001','Employee','che','Logged Out','2024-07-02 15:13:36'),(189,'EMP-001','Employee','che','Logged in','2024-07-02 15:14:15'),(190,'EMP-001','Employee','che','Logged Out','2024-07-02 15:26:56'),(191,'EMP-001','Employee','che','Logged in','2024-07-02 15:30:01'),(192,'EMP-001','Employee','che','Logged in','2024-07-02 15:34:36'),(193,'EMP-001','Employee','che','Logged Out','2024-07-02 15:36:13'),(194,'EMP-001','Employee','che','Logged in','2024-07-02 15:36:24'),(195,'EMP-001','Employee','che','Logged in','2024-07-02 15:37:09'),(196,'EMP-001','Employee','che','Logged in','2024-07-02 15:38:51'),(197,'EMP-001','Employee','che','Logged in','2024-07-02 15:42:51'),(198,'EMP-001','Employee','che','Logged in','2024-07-02 15:48:07'),(199,'EMP-001','Employee','che','Logged in','2024-07-02 15:49:06'),(200,'EMP-001','Employee','che','Logged in','2024-07-02 15:50:25'),(201,'EMP-001','Employee','che','Logged in','2024-07-02 16:03:56'),(202,'EMP-001','Employee','che','Logged in','2024-07-02 16:10:42'),(203,'EMP-001','Employee','che','Logged in','2024-07-02 16:11:54'),(204,'EMP-001','Employee','che','Logged in','2024-07-02 16:14:18'),(205,'EMP-001','Employee','che','Logged in','2024-07-02 16:16:39'),(206,'EMP-001','Employee','che','Logged in','2024-07-02 16:17:57'),(207,'EMP-001','Employee','che','Logged Out','2024-07-02 16:18:06'),(208,'EMP-001','Employee','che','Logged in','2024-07-02 16:18:10'),(209,'EMP-001','Employee','che','Logged in','2024-07-02 16:19:42'),(210,'EMP-001','Employee','che','Logged Out','2024-07-02 16:19:54'),(211,'EMP-001','Employee','che','Logged in','2024-07-02 16:22:45'),(212,'EMP-001','Employee','che','Logged Out','2024-07-02 16:22:48'),(213,'EMP-001','Employee','che','Logged in','2024-07-02 16:37:21'),(214,'EMP-001','Employee','che','Logged in','2024-07-02 16:40:39'),(215,'EMP-001','Employee','che','Logged in','2024-07-02 16:47:38'),(216,'EMP-001','Employee','che','Logged in','2024-07-02 16:49:13'),(217,'EMP-001','Employee','che','Logged in','2024-07-02 16:49:54'),(218,'EMP-001','Employee','che','Logged in','2024-07-02 16:51:09'),(219,'EMP-001','Employee','che','Logged in','2024-07-02 16:58:18'),(220,'EMP-001','Employee','che','Logged in','2024-07-02 17:02:32'),(221,'EMP-001','Employee','che','Logged in','2024-07-02 17:03:54'),(222,'EMP-001','Employee','che','Logged in','2024-07-02 17:09:44'),(223,'EMP-001','Employee','che','Logged in','2024-07-02 17:15:24'),(224,'EMP-001','Employee','che','Logged in','2024-07-02 17:24:47'),(225,'EMP-001','Employee','che','Logged in','2024-07-02 17:25:44'),(226,'EMP-001','Employee','che','Logged in','2024-07-02 17:27:44'),(227,'EMP-001','Employee','che','Logged in','2024-07-02 17:33:15'),(228,'EMP-001','Employee','che','Logged in','2024-07-02 17:35:53'),(229,'EMP-001','Employee','che','Logged in','2024-07-02 17:48:17'),(230,'EMP-001','Employee','che','Logged in','2024-07-02 17:50:09'),(231,'EMP-001','Employee','che','Logged in','2024-07-02 17:53:31'),(232,'EMP-001','Employee','che','Logged in','2024-07-02 17:54:01'),(233,'EMP-001','Employee','che','Logged in','2024-07-02 17:54:30'),(234,'AD-002','Admin','Dei','Logged in','2024-07-02 19:55:37'),(235,'AD-002','Admin','Dei','Logged in','2024-07-02 19:58:43'),(236,'AD-002','Admin','Dei','Logged in','2024-07-03 05:06:22'),(237,'AD-002','Admin','Dei','Logged Out','2024-07-03 05:16:08'),(238,'EMP-001','Employee','che','Logged in','2024-07-03 05:16:21'),(239,'EMP-001','Employee','che','Logged Out','2024-07-03 05:16:33'),(240,'EMP-001','Employee','che','Logged Out','2024-07-03 05:16:34'),(241,'EMP-001','Employee','che','Logged Out','2024-07-03 05:16:35'),(242,'EMP-001','Employee','che','Logged Out','2024-07-03 05:16:35'),(243,'EMP-001','Employee','che','Logged Out','2024-07-03 05:16:35'),(244,'EMP-001','Employee','che','Logged Out','2024-07-03 05:16:36'),(245,'EMP-001','Employee','che','Logged Out','2024-07-03 05:16:36'),(246,'AD-002','Admin','Dei','Logged in','2024-07-03 05:17:42'),(247,'AD-002','Admin','Dei','Logged Out','2024-07-03 05:17:45'),(248,'EMP-001','Employee','che','Logged in','2024-07-03 05:17:48'),(249,'EMP-001','Employee','che','Logged Out','2024-07-03 05:17:51'),(250,'EMP-001','Employee','che','Logged Out','2024-07-03 05:17:51'),(251,'EMP-001','Employee','che','Logged Out','2024-07-03 05:17:51'),(252,'AD-002','Admin','Dei','Logged in','2024-07-03 05:18:56'),(253,'AD-002','Admin','Dei','Logged Out','2024-07-03 05:18:58'),(254,'EMP-001','Employee','che','Logged in','2024-07-03 05:19:04'),(255,'EMP-001','Employee','che','Logged Out','2024-07-03 05:19:14'),(256,'AD-002','Admin','Dei','Logged in','2024-07-03 05:25:06'),(257,'AD-002','Admin','Dei','Logged in','2024-07-03 05:26:16'),(258,'AD-002','Admin','Dei','Logged in','2024-07-03 05:29:40'),(259,'AD-002','Admin','Dei','Logged in','2024-07-03 05:30:02'),(260,'AD-002','Admin','Dei','Logged in','2024-07-03 05:32:05'),(261,'AD-002','Admin','Dei','Logged in','2024-07-03 05:33:00'),(262,'AD-002','Admin','Dei','Logged in','2024-07-03 05:35:21'),(263,'AD-002','Admin','Dei','Logged in','2024-07-03 05:36:02'),(264,'AD-002','Admin','Dei','Logged in','2024-07-03 05:36:32'),(265,'AD-002','Admin','Dei','Logged in','2024-07-03 05:38:02'),(266,'AD-002','Admin','Dei','Logged in','2024-07-03 05:41:57'),(267,'AD-002','Admin','Dei','Logged in','2024-07-03 05:50:10'),(268,'AD-002','Admin','Dei','Logged in','2024-07-03 05:51:42'),(269,'AD-002','Admin','Dei','Logged in','2024-07-03 05:56:00'),(270,'AD-002','Admin','Dei','Logged in','2024-07-03 05:59:10'),(271,'AD-002','Admin','Dei','Logged in','2024-07-03 06:00:07'),(272,'AD-002','Admin','Dei','Logged in','2024-07-03 06:07:02'),(273,'AD-002','Admin','Dei','Logged in','2024-07-03 06:08:05'),(274,'AD-002','Admin','Dei','Logged in','2024-07-03 06:09:14'),(275,'AD-002','Admin','Dei','Logged in','2024-07-03 08:58:28'),(276,'AD-002','Admin','Dei','Logged Out','2024-07-03 08:58:30'),(277,'AD-002','Admin','Dei','Logged in','2024-07-03 08:58:37'),(278,'AD-002','Admin','Dei','Logged in','2024-07-03 09:01:58'),(279,'AD-002','Admin','Dei','Logged in','2024-07-03 09:08:07'),(280,'AD-002','Admin','Dei','Logged in','2024-07-03 09:10:18');
/*!40000 ALTER TABLE `logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_method`
--

DROP TABLE IF EXISTS `payment_method`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_method` (
  `PaymentTypeID` int NOT NULL,
  `PaymentType` varchar(45) NOT NULL,
  PRIMARY KEY (`PaymentTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_method`
--

LOCK TABLES `payment_method` WRITE;
/*!40000 ALTER TABLE `payment_method` DISABLE KEYS */;
INSERT INTO `payment_method` VALUES (0,'Cash'),(1,'GCash'),(2,'Split');
/*!40000 ALTER TABLE `payment_method` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_type`
--

DROP TABLE IF EXISTS `payment_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_type` (
  `PaymentTypeID` int NOT NULL,
  `PaymentType` varchar(45) NOT NULL,
  PRIMARY KEY (`PaymentTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_type`
--

LOCK TABLES `payment_type` WRITE;
/*!40000 ALTER TABLE `payment_type` DISABLE KEYS */;
INSERT INTO `payment_type` VALUES (0,'Cash'),(1,'GCash'),(2,'Split');
/*!40000 ALTER TABLE `payment_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `ProductID` int NOT NULL AUTO_INCREMENT,
  `RPID` varchar(45) DEFAULT NULL,
  `ProductName` varchar(45) NOT NULL,
  `SellingPrice` int NOT NULL DEFAULT '0',
  `TotalStock` int NOT NULL,
  `ExpirationDate` date DEFAULT NULL,
  `Description` varchar(100) DEFAULT 'No Description.',
  `UnitTypeID` int NOT NULL,
  `CategoryID` int NOT NULL,
  `Active` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`ProductID`),
  UNIQUE KEY `ProductID_UNIQUE` (`ProductID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'00-0001','Vitality',100,14,'2000-01-01','dogfood',0,0,0),(2,'01-0002','Whiskas',150,0,'2000-01-01','',0,1,1),(3,'00-0003','Pedigree',100,21,'2000-01-01','',0,0,0),(4,'00-0004','Royal Canin',200,21,'2000-01-01','',0,0,1),(5,'01-0005','Aozi cat',170,24,'2000-01-01','',0,1,1);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_sold`
--

DROP TABLE IF EXISTS `products_sold`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_sold` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ReceiptID` varchar(45) NOT NULL,
  `ProductID` varchar(45) NOT NULL,
  `Quantity` int NOT NULL,
  `Price` decimal(10,2) DEFAULT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `idproducts_sold_UNIQUE` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_sold`
--

LOCK TABLES `products_sold` WRITE;
/*!40000 ALTER TABLE `products_sold` DISABLE KEYS */;
INSERT INTO `products_sold` VALUES (12,'24070100037','00-0001',1,100.00,'2024-07-01'),(13,'24070100038','00-0003',1,100.00,'2024-07-02'),(14,'24070100039','00-0004',1,200.00,'2024-07-03'),(15,'24070100040','00-0001',1,100.00,'2024-07-04'),(16,'24070100040','01-0002',1,150.00,'2024-08-01'),(17,'24070100040','00-0003',1,100.00,'2024-09-01'),(18,'24070100040','00-0004',1,200.00,'2024-10-01'),(19,'24070100040','01-0005',1,170.00,'2022-07-01'),(20,'24070100041','01-0002',1,150.00,'2022-07-01'),(21,'24070100042','00-0003',1,100.00,'2023-07-01'),(22,'24070100042','00-0004',1,200.00,'2023-07-01'),(23,'24070100042','01-0005',1,170.00,'2024-07-01'),(24,'24070100043','01-0002',1,150.00,'2024-07-01'),(25,'24070100043','00-0001',1,100.00,'2024-07-01'),(26,'24070100043','00-0003',1,100.00,'2024-07-01'),(27,'24070100043','00-0004',1,200.00,'2024-07-01'),(28,'24070100043','01-0005',1,170.00,'2024-07-01'),(29,'24070100044','00-0001',1,100.00,'2024-07-01'),(30,'24070100044','01-0002',1,150.00,'2024-07-01'),(31,'24070100044','00-0003',1,100.00,'2024-07-01'),(32,'24070100044','00-0004',1,200.00,'2024-07-01'),(33,'24070100044','01-0005',1,170.00,'2024-07-01'),(34,'24070100045','00-0001',1,100.00,'2024-07-01'),(35,'24070100047','00-0001',1,100.00,'2024-07-01'),(36,'24070100048','00-0001',1,100.00,'2024-07-01'),(37,'24070100049','00-0001',1,100.00,'2024-07-01'),(38,'24070100049','01-0002',1,150.00,'2024-07-01'),(39,'24070100050','00-0001',1,100.00,'2024-07-01'),(40,'24070100050','01-0002',1,150.00,'2024-07-01'),(41,'24070100051','01-0002',1,150.00,'2024-07-01'),(42,'24070100051','00-0001',1,100.00,'2024-07-01'),(43,'24070100052','00-0001',1,100.00,'2024-07-01'),(44,'24070100052','00-0003',1,100.00,'2024-07-01'),(45,'24070100053','01-0002',1,150.00,'2024-07-01'),(46,'24070100053','00-0001',1,100.00,'2024-07-01'),(47,'24070100054','00-0001',1,100.00,'2024-07-01'),(48,'24070100054','01-0002',1,150.00,'2024-07-01'),(49,'24070100055','00-0001',1,100.00,'2024-07-01'),(50,'24070100055','01-0002',1,150.00,'2024-07-01'),(51,'24070100056','01-0002',1,150.00,'2024-07-01'),(52,'24070100056','00-0001',1,100.00,'2024-07-01'),(53,'24070100057','00-0001',1,100.00,'2024-07-01'),(54,'24070100057','00-0004',1,200.00,'2024-07-01'),(55,'24070100058','01-0002',1,150.00,'2024-07-01'),(56,'24070100058','00-0001',1,100.00,'2024-07-01'),(57,'24070200059','00-0001',1,100.00,'2024-07-02'),(58,'24070200059','01-0002',1,150.00,'2024-07-02'),(59,'24070200060','01-0002',1,150.00,'2024-07-02'),(60,'24070200060','00-0001',1,100.00,'2024-07-02'),(61,'24070200061','00-0001',1,100.00,'2024-07-02'),(62,'24070200061','01-0002',1,150.00,'2024-07-02'),(63,'24070200062','00-0001',1,100.00,'2024-07-02'),(64,'24070200062','01-0002',1,150.00,'2024-07-02'),(65,'24070200063','00-0001',1,100.00,'2024-07-02'),(66,'24070200063','01-0002',1,150.00,'2024-07-02'),(67,'24070200064','00-0001',1,100.00,'2024-07-02'),(68,'24070200064','01-0002',1,150.00,'2024-07-02'),(69,'24070200065','01-0002',1,150.00,'2024-07-02'),(70,'24070200065','00-0001',1,100.00,'2024-07-02'),(71,'24070200066','00-0001',1,100.00,'2024-07-02'),(72,'24070200066','01-0002',1,150.00,'2024-07-02'),(73,'24070200067','00-0001',1,100.00,'2024-07-02'),(74,'24070200067','01-0002',1,150.00,'2024-07-02'),(75,'24070200068','00-0001',1,100.00,'2024-07-02'),(76,'24070200068','01-0002',1,150.00,'2024-07-02'),(77,'24070200069','00-0001',1,100.00,'2024-07-02'),(78,'24070200070','00-0001',1,100.00,'2024-07-02'),(79,'24070200070','01-0002',1,150.00,'2024-07-02'),(80,'24070200071','00-0001',1,100.00,'2024-07-02'),(81,'24070200071','01-0002',1,150.00,'2024-07-02'),(82,'24070200072','00-0001',1,100.00,'2024-07-02'),(83,'24070200072','01-0002',1,150.00,'2024-07-02'),(84,'24070200073','00-0001',1,100.00,'2024-07-02'),(85,'24070200073','01-0002',1,150.00,'2024-07-02'),(86,'24070200074','00-0001',1,100.00,'2024-07-02'),(87,'24070200074','01-0002',1,150.00,'2024-07-02'),(88,'24070200075','00-0001',1,100.00,'2024-07-02'),(89,'24070200075','01-0002',1,150.00,'2024-07-02'),(90,'24070200076','00-0001',1,100.00,'2024-07-02'),(91,'24070200077','00-0001',1,100.00,'2024-07-02'),(92,'24070200078','00-0001',1,100.00,'2024-07-02'),(93,'24070200079','00-0001',1,100.00,'2024-07-02'),(94,'24070200080','00-0001',1,100.00,'2024-07-02'),(95,'24070200081','00-0001',1,100.00,'2024-07-02'),(96,'24070200082','00-0001',1,100.00,'2024-07-02'),(97,'24070200083','00-0003',1,100.00,'2024-07-02'),(98,'24070200084','00-0003',1,100.00,'2024-07-02'),(99,'24070200085','00-0004',1,200.00,'2024-07-02'),(100,'24070200086','00-0004',1,200.00,'2024-07-02');
/*!40000 ALTER TABLE `products_sold` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_supplied`
--

DROP TABLE IF EXISTS `products_supplied`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_supplied` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `RPID` varchar(45) NOT NULL,
  `SupplierReceiptID` varchar(45) NOT NULL,
  `BoughtQuantity` int NOT NULL,
  `CurrentQuantity` int NOT NULL,
  `Date` date DEFAULT NULL,
  `CostPrice` decimal(10,2) NOT NULL,
  `ExpirationDate` date DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID_UNIQUE` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_supplied`
--

LOCK TABLES `products_supplied` WRITE;
/*!40000 ALTER TABLE `products_supplied` DISABLE KEYS */;
INSERT INTO `products_supplied` VALUES (1,'00-0001','hrkkj45i4u5i4',25,25,'2000-01-01',90.00,'2000-01-01'),(2,'00-0001','gdad343',25,25,'2000-01-01',100.00,'2000-01-01'),(3,'01-0002','gdad343',25,25,'2000-01-01',100.00,'2000-01-01'),(4,'00-0003','gdad343',25,25,'2000-01-01',100.00,'2000-01-01'),(5,'00-0004','gdad343',25,25,'2000-01-01',100.00,'2000-01-01'),(6,'01-0005','gdad343',25,25,'2000-01-01',100.00,'2000-01-01'),(7,'00-0001','22222',1,1,'2000-01-01',100.00,'2000-01-01'),(8,'00-0003','22222',1,1,'2000-01-01',100.00,'2000-01-01'),(9,'00-0004','22222',1,1,'2000-01-01',100.00,'2000-01-01'),(10,'00-0001','hello',2,2,'2000-01-01',100.00,'2000-01-01'),(11,'01-0002','hello',3,3,'2000-01-01',100.00,'2000-01-01'),(12,'00-0003','hello',3,3,'2000-01-01',100.00,'2000-01-01'),(13,'00-0004','hello',3,3,'2000-01-01',100.00,'2000-01-01'),(14,'01-0005','hello',3,3,'2000-01-01',100.00,'2000-01-01'),(15,'00-0001','bago',1,1,'2000-01-01',100.00,'2000-01-01'),(16,'00-0001','11111',1,1,'2000-01-01',100.00,'2000-01-01');
/*!40000 ALTER TABLE `products_supplied` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sex`
--

DROP TABLE IF EXISTS `sex`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sex` (
  `SexID` int NOT NULL AUTO_INCREMENT,
  `Sex` varchar(45) NOT NULL,
  PRIMARY KEY (`SexID`),
  UNIQUE KEY `SexID_UNIQUE` (`SexID`),
  UNIQUE KEY `Sex_UNIQUE` (`Sex`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sex`
--

LOCK TABLES `sex` WRITE;
/*!40000 ALTER TABLE `sex` DISABLE KEYS */;
INSERT INTO `sex` VALUES (1,'Female'),(0,'Male');
/*!40000 ALTER TABLE `sex` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier_receipts`
--

DROP TABLE IF EXISTS `supplier_receipts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier_receipts` (
  `SupplierReceiptID` int unsigned NOT NULL AUTO_INCREMENT,
  `RUID` varchar(45) DEFAULT NULL,
  `ReceiptRef` varchar(45) DEFAULT NULL,
  `TotalPrice` varchar(10) NOT NULL,
  `PaymentTypeID` varchar(10) DEFAULT '0',
  `OrderDate` date NOT NULL,
  `DeliveryDate` date NOT NULL,
  `GCashRef` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`SupplierReceiptID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier_receipts`
--

LOCK TABLES `supplier_receipts` WRITE;
/*!40000 ALTER TABLE `supplier_receipts` DISABLE KEYS */;
INSERT INTO `supplier_receipts` VALUES (1,'1','hrkkj45i4u5i4','2250','0','2000-01-01','2000-01-01',NULL),(2,'1','gdad343','12500','0','2000-01-01','2000-01-01',NULL),(3,'2','22222','300','0','2000-01-01','2000-01-01',NULL),(4,'1','hello','1400','0','2000-02-01','2000-01-01',NULL),(5,'1','bago','100','0','2000-02-01','2000-01-01',NULL),(6,'1','11111','100','0','2000-01-01','2000-01-01',NULL);
/*!40000 ALTER TABLE `supplier_receipts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction_receipts`
--

DROP TABLE IF EXISTS `transaction_receipts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction_receipts` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `RUID` varchar(45) NOT NULL,
  `TransactionReceiptID` varchar(45) DEFAULT NULL,
  `Price` decimal(10,2) NOT NULL,
  `PaidPrice` decimal(10,2) NOT NULL,
  `PurchaseDate` datetime NOT NULL,
  `GCashReference` varchar(25) DEFAULT 'None',
  `PaymentTypeID` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_receipts`
--

LOCK TABLES `transaction_receipts` WRITE;
/*!40000 ALTER TABLE `transaction_receipts` DISABLE KEYS */;
INSERT INTO `transaction_receipts` VALUES (37,'AD-001','24070100037',100.00,200.00,'2024-07-01 00:00:00',NULL,0),(38,'AD-002','24070100038',100.00,1000.00,'2024-07-01 00:00:00',NULL,0),(39,'AD-002','24070100039',200.00,200.00,'2024-07-02 00:00:00','2020',1),(40,'AD-002','24070100040',720.00,1000.00,'2024-07-03 00:00:00','2020',0),(41,'AD-002','24070100041',150.00,150.00,'2024-08-04 00:00:00','45234fdf',2),(42,'AD-003','24070100042',470.00,500.00,'2024-07-05 00:00:00','433453454',2),(43,'AD-001','24070100043',720.00,1000.00,'2024-07-06 00:00:00',NULL,0),(44,'AD-001','24070100044',720.00,1000.00,'2024-09-07 00:00:00',NULL,0),(45,'AD-001','24070100045',100.00,100.00,'2023-07-08 00:00:00',NULL,0),(46,'AD-003','24070100046',100.00,500.00,'2022-07-09 00:00:00','None',NULL),(47,'AD-001','24070100047',100.00,100.00,'2024-07-01 00:00:00',NULL,0),(48,'AD-002','24070100048',100.00,100.00,'2024-07-01 00:00:00',NULL,0),(49,'AD-002','24070100049',250.00,250.00,'2024-07-01 00:00:00',NULL,0),(50,'AD-002','24070100050',250.00,250.00,'2024-07-01 00:00:00',NULL,0),(51,'AD-002','24070100051',250.00,250.00,'2024-07-01 00:00:00',NULL,0),(52,'AD-002','24070100052',200.00,250.00,'2024-07-01 00:00:00',NULL,0),(53,'AD-002','24070100053',250.00,250.00,'2024-07-01 00:00:00',NULL,0),(54,'AD-002','24070100054',250.00,250.00,'2024-07-01 00:00:00',NULL,0),(55,'AD-002','24070100055',250.00,250.00,'2024-07-01 00:00:00',NULL,0),(56,'AD-002','24070100056',250.00,250.00,'2024-07-01 00:00:00',NULL,0),(57,'AD-002','24070100057',300.00,300.00,'2024-07-01 00:00:00',NULL,0),(58,'AD-002','24070100058',250.00,250.00,'2024-07-01 00:00:00',NULL,0),(59,'AD-002','24070200059',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(60,'AD-002','24070200060',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(61,'AD-002','24070200061',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(62,'AD-002','24070200062',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(63,'AD-002','24070200063',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(64,'AD-002','24070200064',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(65,'AD-002','24070200065',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(66,'AD-002','24070200066',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(67,'AD-002','24070200067',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(68,'AD-002','24070200068',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(69,'AD-002','24070200069',100.00,250.00,'2024-07-02 00:00:00',NULL,0),(70,'AD-002','24070200070',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(71,'AD-002','24070200071',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(72,'AD-002','24070200072',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(73,'AD-002','24070200073',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(74,'AD-002','24070200074',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(75,'AD-002','24070200075',250.00,250.00,'2024-07-02 00:00:00',NULL,0),(76,'AD-002','24070200076',100.00,100.00,'2024-07-02 00:00:00',NULL,0),(77,'AD-002','24070200077',100.00,100.00,'2024-07-02 00:00:00',NULL,0),(78,'AD-002','24070200078',100.00,100.00,'2024-07-02 00:00:00',NULL,0),(79,'AD-002','24070200079',100.00,100.00,'2024-07-02 00:00:00',NULL,0),(80,'AD-002','24070200080',100.00,250.00,'2024-07-02 00:00:00',NULL,0),(81,'AD-002','24070200081',100.00,250.00,'2024-07-02 00:00:00',NULL,0),(82,'EMP-001','24070200082',100.00,100.00,'2024-07-02 14:54:40',NULL,0),(83,'EMP-001','24070200083',100.00,100.00,'2024-07-02 15:32:57',NULL,0),(84,'EMP-001','24070200084',100.00,100.00,'2024-07-02 15:33:19',NULL,0),(85,'EMP-001','24070200085',200.00,300.00,'2024-07-02 15:34:56',NULL,0),(86,'AD-002','24070200086',200.00,200.00,'2024-07-02 20:02:38',NULL,0);
/*!40000 ALTER TABLE `transaction_receipts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unit_type`
--

DROP TABLE IF EXISTS `unit_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unit_type` (
  `UnitTypeID` int unsigned NOT NULL AUTO_INCREMENT,
  `UnitType` varchar(45) NOT NULL,
  PRIMARY KEY (`UnitTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unit_type`
--

LOCK TABLES `unit_type` WRITE;
/*!40000 ALTER TABLE `unit_type` DISABLE KEYS */;
INSERT INTO `unit_type` VALUES (0,'Kilograms'),(1,'Piece'),(2,'Liters'),(3,'ML'),(5,'piece');
/*!40000 ALTER TABLE `unit_type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-03  9:44:21
