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
  `Passcode` varchar(64) NOT NULL,
  `Fname` varchar(45) NOT NULL,
  `Lname` varchar(45) NOT NULL,
  `Mname` varchar(45) DEFAULT NULL,
  `SuffixID` int DEFAULT NULL,
  `SexID` int NOT NULL,
  `Phono` varchar(12) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Position` varchar(50) NOT NULL DEFAULT 'None',
  `HireDate` date NOT NULL,
  `BirthDate` date NOT NULL,
  `Address` varchar(45) NOT NULL,
  `Status` int NOT NULL DEFAULT '1',
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
INSERT INTO `accounts` VALUES (1,0,'AD-001','Rheiniel','af41e68e1309fa29a5044cbdc36b90a3821d8807e68c7675a6c495112bc8a55f','Rheiniel Jerard','Damasco','Frigillana',NULL,1,'639154974346','rheiniel.j@gmail.com','Admin','2021-07-04','2001-10-03','Philippines',1),(2,0,'AD-002','Che','937377f056160fc4b15e0b770c67136a5f03c15205b4d3bf918268fefa2c6d0a','Franchesca Jane','Macam','',0,1,'639999999999','chesca@gmail.com','Cashier','2023-06-12','2001-09-22','Phil',1),(3,0,'AD-003','Dei','ec4c88ca7f69534f10c0611c1ecd13e7c2cdf73e1b915e9fd0cf27ac10da43fa','Deighro','De Ocampo','',0,0,'639999999999','qd-deocampo@tip.edu.ph','Kargador','2023-06-12','2003-06-19','Phil',1),(4,1,'EMP-004','Rach','91b4d142823f7d20c5f08df69122de43f35f057a988d9619f6d3138485c9a203','Rachel','Manuel','',0,1,'639999999999','rachelmanuel@gmail.com','Owner','2023-06-12','1987-06-17','Phil',1);
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Cat Food'),(0,'Dog Food'),(2,'Feeds'),(3,'Fertilizers'),(6,'Live Stock'),(5,'Medicine'),(7,'Others'),(4,'Pet Essentials');
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logs`
--

LOCK TABLES `logs` WRITE;
/*!40000 ALTER TABLE `logs` DISABLE KEYS */;
INSERT INTO `logs` VALUES (1,'AD-002','Admin','Che','Logged In','2024-07-10 14:24:43'),(2,'AD-002','Admin','Che','Viewed User List','2024-07-10 14:24:46'),(3,'AD-002','Admin','Che','Viewed User List','2024-07-10 14:24:46'),(4,'AD-002','Admin','Che','Viewed Sales List','2024-07-10 14:24:48'),(5,'AD-002','Admin','Che','Viewed Sales List','2024-07-10 14:24:48'),(6,'AD-002','Admin','Che','Logged In','2024-07-10 14:29:08');
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
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'02-0001','African Mix',80,25,'2024-07-22','',5,2,1),(2,'02-0002','Apollo Economix Grains',37,10,'2024-07-22','',5,2,1),(3,'01-0003','Aozi Cat Food',175,15,'2024-07-23','',5,1,1),(4,'05-0004','Amityl 500 tablet',17,20,'2024-07-23','',3,5,1),(5,'05-0005','Amoxicillin Powder/Granules',5,25,'2024-07-23','',4,5,1),(6,'05-0006','Agmectin Powder/Granules',28,15,'2024-07-24','',4,5,1),(7,'05-0007','Astig Dewormer Tablet',9,15,'2024-07-24','',3,5,1),(8,'05-0008','Ambroxitil Powder',38,40,'2024-07-24','',4,5,1),(9,'02-0009','Breeder Mix',45,15,'2024-07-20','',5,2,1),(10,'00-0010','Beef Pro Adult Dog Food',140,35,'2024-07-21','',5,0,1),(11,'00-0011','Beef Pro Puppy Dog Food',155,20,'2024-07-21','',5,0,1),(12,'02-0012','Baby Stag Booster (1kg Pack)',51,15,'2024-07-20','',1,2,1),(13,'00-0013','Beef Teriyaki Dog Food',80,15,'2024-07-20','',5,0,1),(14,'05-0014','B12 Caplet',45,25,'2024-07-15','',0,5,1),(15,'05-0015','Cecical 200g',80,25,'2024-07-16','',7,5,1),(16,'05-0016','Clear Out 500ml',300,10,'2024-07-15','',0,5,1),(17,'05-0017','Clear Out 1L',545,20,'2024-07-15','',0,5,1),(18,'02-0018','Duck Layer Pellet',36,20,'2024-07-16','',5,2,1),(19,'05-0019','Dextrose Powder 300g',80,40,'2024-07-19','',0,5,1),(20,'05-0020','Dextrose Powder 100g',45,55,'2024-07-19','',0,5,1),(21,'05-0021','Doxylar Forte Tablet',70,15,'2024-07-18','',3,5,1),(22,'07-0022','Disposable Syringe 1mL',7,40,'2024-07-18','',2,7,1),(23,'07-0023','Disposabale Syringe 3mL',8,30,'2024-07-18','',2,7,1),(24,'07-0024','Disposabale Syringe 5mL',9,25,'2024-07-17','',2,7,1),(25,'02-0025','Enertone (pack 1kg)',44,25,'2024-07-17','',1,2,1),(26,'02-0026','Enertone (per kilo)',42,25,'2024-07-17','',5,2,1),(27,'05-0027','Electrogen',19,25,'2024-07-17','',1,5,1),(28,'05-0028','El Toro Tablet',12,50,'2024-07-17','',3,5,1);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_sold`
--

LOCK TABLES `products_sold` WRITE;
/*!40000 ALTER TABLE `products_sold` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_supplied`
--

LOCK TABLES `products_supplied` WRITE;
/*!40000 ALTER TABLE `products_supplied` DISABLE KEYS */;
INSERT INTO `products_supplied` VALUES (1,'07-0024','8019017806595',25,25,'2024-07-07',5.00,'2024-07-17'),(2,'02-0025','8019017806595',25,25,'2024-07-07',40.00,'2024-07-17'),(3,'02-0026','8019017806595',25,25,'2024-07-07',40.00,'2024-07-17'),(4,'05-0027','8019017806595',25,25,'2024-07-07',15.00,'2024-07-17'),(5,'05-0028','8019017806595',50,50,'2024-07-07',10.00,'2024-07-17'),(6,'05-0021','5018984152021',15,15,'2024-07-08',60.00,'2024-07-18'),(7,'07-0022','5018984152021',40,40,'2024-07-08',5.00,'2024-07-18'),(8,'07-0023','5018984152021',30,30,'2024-07-08',5.00,'2024-07-18'),(9,'05-0019','5018984152021',40,40,'2024-07-08',70.00,'2024-07-19'),(10,'05-0020','5018984152021',55,55,'2024-07-08',30.00,'2024-07-19'),(11,'05-0014','832167626',25,25,'2024-07-09',40.00,'2024-07-15'),(12,'05-0016','832167626',10,10,'2024-07-09',275.00,'2024-07-15'),(13,'05-0017','832167626',20,20,'2024-07-09',500.00,'2024-07-15'),(14,'05-0015','832167626',25,25,'2024-07-09',70.00,'2024-07-16'),(15,'02-0018','832167626',20,20,'2024-07-09',30.00,'2024-07-16'),(16,'02-0009','8018964517713',15,15,'2024-07-10',40.00,'2024-07-20'),(17,'02-0012','8018964517713',15,15,'2024-07-10',45.00,'2024-07-20'),(18,'00-0013','8018964517713',15,15,'2024-07-10',70.00,'2024-07-20'),(19,'00-0010','8018964517713',35,35,'2024-07-10',130.00,'2024-07-21'),(20,'00-0011','8018964517713',20,20,'2024-07-10',145.00,'2024-07-21'),(21,'02-0002','8018882617204',10,10,'2024-07-10',30.00,'2024-07-22'),(22,'02-0001','8018882617204',25,25,'2024-07-10',70.00,'2024-07-22'),(23,'05-0005','8018882617204',25,25,'2024-07-10',3.00,'2024-07-23'),(24,'05-0004','8018882617204',20,20,'2024-07-10',15.00,'2024-07-23'),(25,'01-0003','8018882617204',15,15,'2024-07-10',165.00,'2024-07-23'),(26,'05-0008','8018882571962',40,40,'2024-07-10',35.00,'2024-07-24'),(27,'05-0007','8018882571962',15,15,'2024-07-10',5.00,'2024-07-24'),(28,'05-0006','8018882571962',15,15,'2024-07-10',25.00,'2024-07-24');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
-- Table structure for table `suffix`
--

DROP TABLE IF EXISTS `suffix`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suffix` (
  `SuffixID` int NOT NULL AUTO_INCREMENT,
  `Suffix` varchar(45) NOT NULL,
  PRIMARY KEY (`SuffixID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suffix`
--

LOCK TABLES `suffix` WRITE;
/*!40000 ALTER TABLE `suffix` DISABLE KEYS */;
INSERT INTO `suffix` VALUES (0,'N/A'),(1,'Jr.'),(2,'Sr.'),(3,'II'),(4,'III'),(5,'IV');
/*!40000 ALTER TABLE `suffix` ENABLE KEYS */;
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
INSERT INTO `supplier_receipts` VALUES (1,'AD-002','8019017806595','3000','0','2025-07-06','2024-07-07',NULL),(2,'AD-002','5018984152021','5700','0','2025-07-07','2024-07-08',NULL),(3,'AD-002','832167626','16100','0','2025-07-08','2024-07-09',NULL),(4,'AD-002','8018964517713','9775','0','2025-07-09','2024-07-10',NULL),(5,'AD-002','8018882617204','4900','0','2025-07-10','2024-07-10',NULL),(6,'AD-002','8018882571962','1850','0','2025-07-10','2024-07-10',NULL);
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
  `GCashReference` varchar(30) DEFAULT 'None',
  `PaymentTypeID` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_receipts`
--

LOCK TABLES `transaction_receipts` WRITE;
/*!40000 ALTER TABLE `transaction_receipts` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unit_type`
--

LOCK TABLES `unit_type` WRITE;
/*!40000 ALTER TABLE `unit_type` DISABLE KEYS */;
INSERT INTO `unit_type` VALUES (0,'Bottle'),(1,'Pack'),(2,'Piece'),(3,'Tablet'),(4,'Sachet'),(5,'Kilogram'),(6,'Capsule'),(7,'Box');
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

-- Dump completed on 2024-07-10 14:50:09
