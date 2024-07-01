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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,1,'EMP-001','Che','220901','Franchesca Jane','Macam',1,'639493075834','qfnmacam@tip.edu.ph','cashier','2023-01-15','2001-09-22','san mateo rizal'),(2,0,'AD-002','Dei','222222','Deighro','De Ocampo',0,'639876543214','qd-deocampo@tip.edu.ph','stock man','2023-01-15','2002-06-19','taytay rizal'),(3,0,'AD-003','Rheiniel','999999','Rheiniel Jerard','Damasco',1,'123456789','qrjfdamasco@tip.edu.ph','taga measure','2023-01-15','2002-06-19','montalban rizal');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `logs`
--

LOCK TABLES `logs` WRITE;
/*!40000 ALTER TABLE `logs` DISABLE KEYS */;
/*!40000 ALTER TABLE `logs` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
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
  `Quantity` varchar(45) NOT NULL,
  `Price` varchar(45) DEFAULT NULL,
  `Date` varchar(45) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `idproducts_sold_UNIQUE` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
  `Date` datetime DEFAULT NULL,
  `CostPrice` decimal(10,2) NOT NULL,
  `ExpirationDate` date DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID_UNIQUE` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_supplied`
--

LOCK TABLES `products_supplied` WRITE;
/*!40000 ALTER TABLE `products_supplied` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier_receipts`
--

LOCK TABLES `supplier_receipts` WRITE;
/*!40000 ALTER TABLE `supplier_receipts` DISABLE KEYS */;
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
  `PurchaseDate` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `GCashReference` varchar(25) DEFAULT 'None',
  `PaymentTypeID` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unit_type`
--

LOCK TABLES `unit_type` WRITE;
/*!40000 ALTER TABLE `unit_type` DISABLE KEYS */;
INSERT INTO `unit_type` VALUES (0,'Kilograms'),(1,'Piece'),(2,'Liters'),(3,'ML');
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

-- Dump completed on 2024-07-01  9:53:44
