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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=654 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
-- Table structure for table `suffix`
--

DROP TABLE IF EXISTS `suffix`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suffix` (
  `SuffixID` int NOT NULL AUTO_INCREMENT,
  `Suffix` varchar(45) NOT NULL,
  PRIMARY KEY (`SuffixID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=99 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-08 17:18:17
