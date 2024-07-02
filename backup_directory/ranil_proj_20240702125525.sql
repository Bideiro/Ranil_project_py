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

INSERT INTO accounts VALUES ('1', '0', 'AD-001', 'Che', '222222', 'Franchesca Jane', 'Macam', '1', '639493075834', 'qfnmacam@tip.edu.ph', 'Maganda', '2023-01-15', '2001-09-22', 'san mateo rizal');
INSERT INTO accounts VALUES ('2', '0', 'AD-002', 'Dei', '222222', 'Deighro', 'De Ocampo', '0', '639876543214', 'qd-deocampo@tip.edu.ph', 'stock man', '2023-01-15', '2002-06-19', 'taytay rizal');
INSERT INTO accounts VALUES ('3', '0', 'AD-003', 'Rheiniel', '999999', 'Rheiniel Jerard', 'Damasco', '1', '123456789', 'qrjfdamasco@tip.edu.ph', 'taga measure', '2023-01-15', '2002-06-19', 'montalban rizal');
INSERT INTO accounts VALUES ('4', '0', 'AD-004', 'Rachel', '111111', 'JCc', 'Manuel', '1', '639999999999', 'rachel@gmai.com', 'admin', '2000-01-01', '2024-06-07', '');

CREATE TABLE `actions` (
  `ActionTypeID` varchar(12) NOT NULL,
  `ActionType` varchar(25) NOT NULL,
  PRIMARY KEY (`ActionTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE `algoproddb` (
  `ProductID` varchar(45) NOT NULL,
  `ProductName` varchar(45) DEFAULT NULL,
  `MonthlyDemand` int DEFAULT NULL,
  `UnitPrice` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`ProductID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO algoproddb VALUES ('00-0001', 'Beef Pro Adult Dog Food', '50', '140.00');
INSERT INTO algoproddb VALUES ('00-0002', 'Beef Pro Puppy Dog Food', '63', '155.00');
INSERT INTO algoproddb VALUES ('01-0001', 'Aozi Cat Food', '50', '175.00');
INSERT INTO algoproddb VALUES ('02-0001', 'African Mix', '120', '80.00');
INSERT INTO algoproddb VALUES ('02-0002', 'Apollo Economix Grains', '300', '37.00');
INSERT INTO algoproddb VALUES ('02-0003', 'Breeder Mix', '290', '45.00');
INSERT INTO algoproddb VALUES ('12-0001', 'Baby Stag Booster', '29', '80.00');
INSERT INTO algoproddb VALUES ('15-0001', 'Amtyl 500 Tablet', '37', '17.00');
INSERT INTO algoproddb VALUES ('15-0002', 'Amoxicillin 500 Capsule', '29', '5.00');
INSERT INTO algoproddb VALUES ('15-0003', 'Agmectin Powder Granules', '13', '28.00');
INSERT INTO algoproddb VALUES ('15-0004', 'Astig Dewormer Tablet', '37', '9.00');
INSERT INTO algoproddb VALUES ('15-0005', 'Ambroxol Powder', '24', '38.00');
INSERT INTO algoproddb VALUES ('15-0006', 'B12 Capsule (50's)', '59', '45.00');

CREATE TABLE `category` (
  `CategoryID` int NOT NULL AUTO_INCREMENT,
  `Category` varchar(45) NOT NULL,
  PRIMARY KEY (`CategoryID`),
  UNIQUE KEY `ProductTypeID_UNIQUE` (`CategoryID`),
  UNIQUE KEY `ProductType_UNIQUE` (`Category`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO category VALUES ('8', 'aso');
INSERT INTO category VALUES ('1', 'Cat Food');
INSERT INTO category VALUES ('0', 'Dog Food');
INSERT INTO category VALUES ('2', 'Feeds');
INSERT INTO category VALUES ('3', 'Fertilizers');
INSERT INTO category VALUES ('6', 'Live Stock');
INSERT INTO category VALUES ('5', 'Medicine');
INSERT INTO category VALUES ('7', 'Others');
INSERT INTO category VALUES ('4', 'Pet Essentials');

CREATE TABLE `levels` (
  `LevelID` varchar(12) NOT NULL,
  `Level` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`LevelID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO levels VALUES ('0', 'Admin');
INSERT INTO levels VALUES ('1', 'Employee');

CREATE TABLE `logs` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `UserID` varchar(45) NOT NULL,
  `UserLevel` varchar(45) DEFAULT NULL,
  `User` varchar(45) DEFAULT NULL,
  `Activity` varchar(45) DEFAULT NULL,
  `DateTime` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO logs VALUES ('1', 'EMP-001', 'Employee', 'Che', 'Logged in', '2024-07-01 10:01:33');
INSERT INTO logs VALUES ('2', '1', '1', 'Che', 'Logged Out', '2024-07-01 10:01:40');
INSERT INTO logs VALUES ('3', 'EMP-001', 'Employee', 'Che', 'Logged in', '2024-07-01 10:01:53');
INSERT INTO logs VALUES ('4', 'EMP-001', 'Employee', 'Che', 'Logged in', '2024-07-01 10:02:49');
INSERT INTO logs VALUES ('5', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 10:26:23');
INSERT INTO logs VALUES ('6', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 10:35:11');
INSERT INTO logs VALUES ('7', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 10:39:53');
INSERT INTO logs VALUES ('8', '2', 'Admin', 'Dei', 'Logged Out', '2024-07-01 10:48:30');
INSERT INTO logs VALUES ('9', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 10:48:44');
INSERT INTO logs VALUES ('10', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 10:50:04');
INSERT INTO logs VALUES ('11', 'AD-001', 'Admin', 'Che', 'Logged Out', '2024-07-01 10:50:13');
INSERT INTO logs VALUES ('12', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 10:50:43');
INSERT INTO logs VALUES ('13', 'AD-002', 'Admin', 'Dei', 'Logged Out', '2024-07-01 10:53:20');
INSERT INTO logs VALUES ('14', 'AD-003', 'Admin', 'Rheiniel', 'Logged in', '2024-07-01 10:53:49');
INSERT INTO logs VALUES ('15', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 10:59:43');
INSERT INTO logs VALUES ('16', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 11:02:02');
INSERT INTO logs VALUES ('17', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 11:05:14');
INSERT INTO logs VALUES ('18', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 11:06:04');
INSERT INTO logs VALUES ('19', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 11:08:32');
INSERT INTO logs VALUES ('20', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 11:10:04');
INSERT INTO logs VALUES ('21', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 11:11:21');
INSERT INTO logs VALUES ('22', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 11:12:08');
INSERT INTO logs VALUES ('23', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 11:12:39');
INSERT INTO logs VALUES ('24', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 11:22:13');
INSERT INTO logs VALUES ('25', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 11:27:59');
INSERT INTO logs VALUES ('26', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 11:29:45');
INSERT INTO logs VALUES ('27', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 11:33:33');
INSERT INTO logs VALUES ('28', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 11:36:14');
INSERT INTO logs VALUES ('29', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 11:38:51');
INSERT INTO logs VALUES ('30', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 11:57:51');
INSERT INTO logs VALUES ('31', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 11:59:30');
INSERT INTO logs VALUES ('32', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 12:02:07');
INSERT INTO logs VALUES ('33', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 12:05:27');
INSERT INTO logs VALUES ('34', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 12:07:17');
INSERT INTO logs VALUES ('35', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 12:12:17');
INSERT INTO logs VALUES ('36', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 12:14:32');
INSERT INTO logs VALUES ('37', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 12:17:37');
INSERT INTO logs VALUES ('38', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 12:30:11');
INSERT INTO logs VALUES ('39', 'AD-001', 'Admin', 'Che', 'Logged Out', '2024-07-01 12:31:06');
INSERT INTO logs VALUES ('40', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 12:31:47');
INSERT INTO logs VALUES ('41', 'AD-001', 'Admin', 'Che', 'Logged Out', '2024-07-01 12:48:03');
INSERT INTO logs VALUES ('42', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 13:14:10');
INSERT INTO logs VALUES ('43', 'AD-001', 'Admin', 'Che', 'Logged Out', '2024-07-01 13:15:55');
INSERT INTO logs VALUES ('44', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 13:16:09');
INSERT INTO logs VALUES ('45', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 13:27:17');
INSERT INTO logs VALUES ('46', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 13:48:36');
INSERT INTO logs VALUES ('47', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 14:00:01');
INSERT INTO logs VALUES ('48', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 14:05:36');
INSERT INTO logs VALUES ('49', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 14:08:19');
INSERT INTO logs VALUES ('50', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:20:31');
INSERT INTO logs VALUES ('51', 'AD-001', 'Admin', 'Che', 'Logged Out', '2024-07-01 14:20:35');
INSERT INTO logs VALUES ('52', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:21:04');
INSERT INTO logs VALUES ('53', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:25:51');
INSERT INTO logs VALUES ('54', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:29:56');
INSERT INTO logs VALUES ('55', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:31:19');
INSERT INTO logs VALUES ('56', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:34:54');
INSERT INTO logs VALUES ('57', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:36:21');
INSERT INTO logs VALUES ('58', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:37:53');
INSERT INTO logs VALUES ('59', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:39:12');
INSERT INTO logs VALUES ('60', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:41:44');
INSERT INTO logs VALUES ('61', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:43:17');
INSERT INTO logs VALUES ('62', 'AD-001', 'Admin', 'Che', 'Logged in', '2024-07-01 14:45:04');
INSERT INTO logs VALUES ('63', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 15:26:01');
INSERT INTO logs VALUES ('64', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 17:16:49');
INSERT INTO logs VALUES ('65', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 17:20:40');
INSERT INTO logs VALUES ('66', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 17:53:38');
INSERT INTO logs VALUES ('67', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 17:54:21');
INSERT INTO logs VALUES ('68', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 17:55:16');
INSERT INTO logs VALUES ('69', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 17:56:37');
INSERT INTO logs VALUES ('70', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 17:59:05');
INSERT INTO logs VALUES ('71', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 18:00:13');
INSERT INTO logs VALUES ('72', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 18:00:54');
INSERT INTO logs VALUES ('73', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 18:02:48');
INSERT INTO logs VALUES ('74', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 18:06:07');
INSERT INTO logs VALUES ('75', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 18:06:47');
INSERT INTO logs VALUES ('76', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 22:25:05');
INSERT INTO logs VALUES ('77', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-01 22:31:49');
INSERT INTO logs VALUES ('78', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:12:11');
INSERT INTO logs VALUES ('79', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:25:38');
INSERT INTO logs VALUES ('80', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:26:36');
INSERT INTO logs VALUES ('81', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:27:46');
INSERT INTO logs VALUES ('82', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:28:38');
INSERT INTO logs VALUES ('83', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:29:37');
INSERT INTO logs VALUES ('84', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:30:40');
INSERT INTO logs VALUES ('85', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:33:15');
INSERT INTO logs VALUES ('86', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:41:47');
INSERT INTO logs VALUES ('87', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:45:21');
INSERT INTO logs VALUES ('88', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:45:53');
INSERT INTO logs VALUES ('89', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 05:53:02');
INSERT INTO logs VALUES ('90', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:02:12');
INSERT INTO logs VALUES ('91', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:03:09');
INSERT INTO logs VALUES ('92', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:04:21');
INSERT INTO logs VALUES ('93', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:05:20');
INSERT INTO logs VALUES ('94', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:06:31');
INSERT INTO logs VALUES ('95', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:07:24');
INSERT INTO logs VALUES ('96', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:11:09');
INSERT INTO logs VALUES ('97', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:13:34');
INSERT INTO logs VALUES ('98', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:51:10');
INSERT INTO logs VALUES ('99', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:53:05');
INSERT INTO logs VALUES ('100', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:55:26');
INSERT INTO logs VALUES ('101', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:58:02');
INSERT INTO logs VALUES ('102', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:58:40');
INSERT INTO logs VALUES ('103', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 06:59:28');
INSERT INTO logs VALUES ('104', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:00:51');
INSERT INTO logs VALUES ('105', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:01:25');
INSERT INTO logs VALUES ('106', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:01:59');
INSERT INTO logs VALUES ('107', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:11:03');
INSERT INTO logs VALUES ('108', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:12:42');
INSERT INTO logs VALUES ('109', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:16:44');
INSERT INTO logs VALUES ('110', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:20:14');
INSERT INTO logs VALUES ('111', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:20:39');
INSERT INTO logs VALUES ('112', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:22:22');
INSERT INTO logs VALUES ('113', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:22:39');
INSERT INTO logs VALUES ('114', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:23:00');
INSERT INTO logs VALUES ('115', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:46:47');
INSERT INTO logs VALUES ('116', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:48:26');
INSERT INTO logs VALUES ('117', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:50:23');
INSERT INTO logs VALUES ('118', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:50:47');
INSERT INTO logs VALUES ('119', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:51:12');
INSERT INTO logs VALUES ('120', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:55:25');
INSERT INTO logs VALUES ('121', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:55:49');
INSERT INTO logs VALUES ('122', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 07:57:03');
INSERT INTO logs VALUES ('123', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 08:00:23');
INSERT INTO logs VALUES ('124', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 08:05:35');
INSERT INTO logs VALUES ('125', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 08:06:17');
INSERT INTO logs VALUES ('126', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 08:07:32');
INSERT INTO logs VALUES ('127', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 08:18:19');
INSERT INTO logs VALUES ('128', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 08:19:22');
INSERT INTO logs VALUES ('129', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 08:21:26');
INSERT INTO logs VALUES ('130', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 08:45:03');
INSERT INTO logs VALUES ('131', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 08:49:30');
INSERT INTO logs VALUES ('132', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 08:54:58');
INSERT INTO logs VALUES ('133', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 11:57:47');
INSERT INTO logs VALUES ('134', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 11:59:31');
INSERT INTO logs VALUES ('135', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:01:46');
INSERT INTO logs VALUES ('136', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:08:15');
INSERT INTO logs VALUES ('137', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:09:11');
INSERT INTO logs VALUES ('138', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:09:45');
INSERT INTO logs VALUES ('139', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:11:56');
INSERT INTO logs VALUES ('140', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:13:20');
INSERT INTO logs VALUES ('141', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:16:22');
INSERT INTO logs VALUES ('142', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:17:55');
INSERT INTO logs VALUES ('143', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:19:44');
INSERT INTO logs VALUES ('144', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:24:04');
INSERT INTO logs VALUES ('145', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:24:54');
INSERT INTO logs VALUES ('146', 'AD-002', 'Admin', 'Dei', 'Logged in', '2024-07-02 12:53:40');

CREATE TABLE `payment_method` (
  `PaymentTypeID` int NOT NULL,
  `PaymentType` varchar(45) NOT NULL,
  PRIMARY KEY (`PaymentTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO payment_method VALUES ('0', 'Cash');
INSERT INTO payment_method VALUES ('1', 'GCash');
INSERT INTO payment_method VALUES ('2', 'Split');

CREATE TABLE `payment_type` (
  `PaymentTypeID` int NOT NULL,
  `PaymentType` varchar(45) NOT NULL,
  PRIMARY KEY (`PaymentTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO payment_type VALUES ('0', 'Cash');
INSERT INTO payment_type VALUES ('1', 'GCash');
INSERT INTO payment_type VALUES ('2', 'Split');

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

INSERT INTO products VALUES ('1', '00-0001', 'Vitality', '100', '15', '2000-01-01', 'dogfood', '0', '0', '1');
INSERT INTO products VALUES ('2', '01-0002', 'Whiskas', '150', '0', '2000-01-01', '', '0', '1', '1');
INSERT INTO products VALUES ('3', '00-0003', 'Pedigree', '100', '23', '2000-01-01', '', '0', '0', '1');
INSERT INTO products VALUES ('4', '00-0004', 'Royal Canin', '200', '23', '2000-01-01', '', '0', '0', '1');
INSERT INTO products VALUES ('5', '01-0005', 'Aozi cat', '170', '24', '2000-01-01', '', '0', '1', '1');

CREATE TABLE `products_sold` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ReceiptID` varchar(45) NOT NULL,
  `ProductID` varchar(45) NOT NULL,
  `Quantity` varchar(45) NOT NULL,
  `Price` varchar(45) DEFAULT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `idproducts_sold_UNIQUE` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO products_sold VALUES ('12', '24070100037', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('13', '24070100038', '00-0003', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('14', '24070100039', '00-0004', '1', '200', '2024-07-03');
INSERT INTO products_sold VALUES ('15', '24070100040', '00-0001', '1', '100', '2024-07-04');
INSERT INTO products_sold VALUES ('16', '24070100040', '01-0002', '1', '150', '2024-08-01');
INSERT INTO products_sold VALUES ('17', '24070100040', '00-0003', '1', '100', '2024-09-01');
INSERT INTO products_sold VALUES ('18', '24070100040', '00-0004', '1', '200', '2024-10-01');
INSERT INTO products_sold VALUES ('19', '24070100040', '01-0005', '1', '170', '2022-07-01');
INSERT INTO products_sold VALUES ('20', '24070100041', '01-0002', '1', '150', '2022-07-01');
INSERT INTO products_sold VALUES ('21', '24070100042', '00-0003', '1', '100', '2023-07-01');
INSERT INTO products_sold VALUES ('22', '24070100042', '00-0004', '1', '200', '2023-07-01');
INSERT INTO products_sold VALUES ('23', '24070100042', '01-0005', '1', '170', '2024-07-01');
INSERT INTO products_sold VALUES ('24', '24070100043', '01-0002', '1', '150', '2024-07-01');
INSERT INTO products_sold VALUES ('25', '24070100043', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('26', '24070100043', '00-0003', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('27', '24070100043', '00-0004', '1', '200', '2024-07-01');
INSERT INTO products_sold VALUES ('28', '24070100043', '01-0005', '1', '170', '2024-07-01');
INSERT INTO products_sold VALUES ('29', '24070100044', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('30', '24070100044', '01-0002', '1', '150', '2024-07-01');
INSERT INTO products_sold VALUES ('31', '24070100044', '00-0003', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('32', '24070100044', '00-0004', '1', '200', '2024-07-01');
INSERT INTO products_sold VALUES ('33', '24070100044', '01-0005', '1', '170', '2024-07-01');
INSERT INTO products_sold VALUES ('34', '24070100045', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('35', '24070100047', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('36', '24070100048', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('37', '24070100049', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('38', '24070100049', '01-0002', '1', '150', '2024-07-01');
INSERT INTO products_sold VALUES ('39', '24070100050', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('40', '24070100050', '01-0002', '1', '150', '2024-07-01');
INSERT INTO products_sold VALUES ('41', '24070100051', '01-0002', '1', '150', '2024-07-01');
INSERT INTO products_sold VALUES ('42', '24070100051', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('43', '24070100052', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('44', '24070100052', '00-0003', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('45', '24070100053', '01-0002', '1', '150', '2024-07-01');
INSERT INTO products_sold VALUES ('46', '24070100053', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('47', '24070100054', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('48', '24070100054', '01-0002', '1', '150', '2024-07-01');
INSERT INTO products_sold VALUES ('49', '24070100055', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('50', '24070100055', '01-0002', '1', '150', '2024-07-01');
INSERT INTO products_sold VALUES ('51', '24070100056', '01-0002', '1', '150', '2024-07-01');
INSERT INTO products_sold VALUES ('52', '24070100056', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('53', '24070100057', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('54', '24070100057', '00-0004', '1', '200', '2024-07-01');
INSERT INTO products_sold VALUES ('55', '24070100058', '01-0002', '1', '150', '2024-07-01');
INSERT INTO products_sold VALUES ('56', '24070100058', '00-0001', '1', '100', '2024-07-01');
INSERT INTO products_sold VALUES ('57', '24070200059', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('58', '24070200059', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('59', '24070200060', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('60', '24070200060', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('61', '24070200061', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('62', '24070200061', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('63', '24070200062', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('64', '24070200062', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('65', '24070200063', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('66', '24070200063', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('67', '24070200064', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('68', '24070200064', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('69', '24070200065', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('70', '24070200065', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('71', '24070200066', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('72', '24070200066', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('73', '24070200067', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('74', '24070200067', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('75', '24070200068', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('76', '24070200068', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('77', '24070200069', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('78', '24070200070', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('79', '24070200070', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('80', '24070200071', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('81', '24070200071', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('82', '24070200072', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('83', '24070200072', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('84', '24070200073', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('85', '24070200073', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('86', '24070200074', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('87', '24070200074', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('88', '24070200075', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('89', '24070200075', '01-0002', '1', '150', '2024-07-02');
INSERT INTO products_sold VALUES ('90', '24070200076', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('91', '24070200077', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('92', '24070200078', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('93', '24070200079', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('94', '24070200080', '00-0001', '1', '100', '2024-07-02');
INSERT INTO products_sold VALUES ('95', '24070200081', '00-0001', '1', '100', '2024-07-02');

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

INSERT INTO products_supplied VALUES ('1', '00-0001', 'hrkkj45i4u5i4', '25', '25', '2000-01-01', '90.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('2', '00-0001', 'gdad343', '25', '25', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('3', '01-0002', 'gdad343', '25', '25', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('4', '00-0003', 'gdad343', '25', '25', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('5', '00-0004', 'gdad343', '25', '25', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('6', '01-0005', 'gdad343', '25', '25', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('7', '00-0001', '22222', '1', '1', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('8', '00-0003', '22222', '1', '1', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('9', '00-0004', '22222', '1', '1', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('10', '00-0001', 'hello', '2', '2', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('11', '01-0002', 'hello', '3', '3', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('12', '00-0003', 'hello', '3', '3', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('13', '00-0004', 'hello', '3', '3', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('14', '01-0005', 'hello', '3', '3', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('15', '00-0001', 'bago', '1', '1', '2000-01-01', '100.00', '2000-01-01');
INSERT INTO products_supplied VALUES ('16', '00-0001', '11111', '1', '1', '2000-01-01', '100.00', '2000-01-01');

CREATE TABLE `sex` (
  `SexID` int NOT NULL AUTO_INCREMENT,
  `Sex` varchar(45) NOT NULL,
  PRIMARY KEY (`SexID`),
  UNIQUE KEY `SexID_UNIQUE` (`SexID`),
  UNIQUE KEY `Sex_UNIQUE` (`Sex`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO sex VALUES ('1', 'Female');
INSERT INTO sex VALUES ('0', 'Male');

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

INSERT INTO supplier_receipts VALUES ('1', '1', 'hrkkj45i4u5i4', '2250', '0', '2000-01-01', '2000-01-01', NULL);
INSERT INTO supplier_receipts VALUES ('2', '1', 'gdad343', '12500', '0', '2000-01-01', '2000-01-01', NULL);
INSERT INTO supplier_receipts VALUES ('3', '2', '22222', '300', '0', '2000-01-01', '2000-01-01', NULL);
INSERT INTO supplier_receipts VALUES ('4', '1', 'hello', '1400', '0', '2000-02-01', '2000-01-01', NULL);
INSERT INTO supplier_receipts VALUES ('5', '1', 'bago', '100', '0', '2000-02-01', '2000-01-01', NULL);
INSERT INTO supplier_receipts VALUES ('6', '1', '11111', '100', '0', '2000-01-01', '2000-01-01', NULL);

CREATE TABLE `transaction_receipts` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `RUID` varchar(45) NOT NULL,
  `TransactionReceiptID` varchar(45) DEFAULT NULL,
  `Price` decimal(10,2) NOT NULL,
  `PaidPrice` decimal(10,2) NOT NULL,
  `PurchaseDate` date NOT NULL,
  `GCashReference` varchar(25) DEFAULT 'None',
  `PaymentTypeID` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO transaction_receipts VALUES ('37', 'AD-001', '24070100037', '100.00', '200.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('38', 'AD-002', '24070100038', '100.00', '1000.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('39', 'AD-002', '24070100039', '200.00', '200.00', '2024-07-02', '2020', '1');
INSERT INTO transaction_receipts VALUES ('40', 'AD-002', '24070100040', '720.00', '1000.00', '2024-07-03', '2020', '0');
INSERT INTO transaction_receipts VALUES ('41', 'AD-002', '24070100041', '150.00', '150.00', '2024-08-04', '45234fdf', '2');
INSERT INTO transaction_receipts VALUES ('42', 'AD-003', '24070100042', '470.00', '500.00', '2024-07-05', '433453454', '2');
INSERT INTO transaction_receipts VALUES ('43', 'AD-001', '24070100043', '720.00', '1000.00', '2024-07-06', NULL, '0');
INSERT INTO transaction_receipts VALUES ('44', 'AD-001', '24070100044', '720.00', '1000.00', '2024-09-07', NULL, '0');
INSERT INTO transaction_receipts VALUES ('45', 'AD-001', '24070100045', '100.00', '100.00', '2023-07-08', NULL, '0');
INSERT INTO transaction_receipts VALUES ('46', 'AD-003', '24070100046', '100.00', '500.00', '2022-07-09', 'None', NULL);
INSERT INTO transaction_receipts VALUES ('47', 'AD-001', '24070100047', '100.00', '100.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('48', 'AD-002', '24070100048', '100.00', '100.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('49', 'AD-002', '24070100049', '250.00', '250.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('50', 'AD-002', '24070100050', '250.00', '250.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('51', 'AD-002', '24070100051', '250.00', '250.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('52', 'AD-002', '24070100052', '200.00', '250.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('53', 'AD-002', '24070100053', '250.00', '250.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('54', 'AD-002', '24070100054', '250.00', '250.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('55', 'AD-002', '24070100055', '250.00', '250.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('56', 'AD-002', '24070100056', '250.00', '250.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('57', 'AD-002', '24070100057', '300.00', '300.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('58', 'AD-002', '24070100058', '250.00', '250.00', '2024-07-01', NULL, '0');
INSERT INTO transaction_receipts VALUES ('59', 'AD-002', '24070200059', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('60', 'AD-002', '24070200060', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('61', 'AD-002', '24070200061', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('62', 'AD-002', '24070200062', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('63', 'AD-002', '24070200063', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('64', 'AD-002', '24070200064', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('65', 'AD-002', '24070200065', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('66', 'AD-002', '24070200066', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('67', 'AD-002', '24070200067', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('68', 'AD-002', '24070200068', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('69', 'AD-002', '24070200069', '100.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('70', 'AD-002', '24070200070', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('71', 'AD-002', '24070200071', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('72', 'AD-002', '24070200072', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('73', 'AD-002', '24070200073', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('74', 'AD-002', '24070200074', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('75', 'AD-002', '24070200075', '250.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('76', 'AD-002', '24070200076', '100.00', '100.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('77', 'AD-002', '24070200077', '100.00', '100.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('78', 'AD-002', '24070200078', '100.00', '100.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('79', 'AD-002', '24070200079', '100.00', '100.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('80', 'AD-002', '24070200080', '100.00', '250.00', '2024-07-02', NULL, '0');
INSERT INTO transaction_receipts VALUES ('81', 'AD-002', '24070200081', '100.00', '250.00', '2024-07-02', NULL, '0');

CREATE TABLE `unit_type` (
  `UnitTypeID` int unsigned NOT NULL AUTO_INCREMENT,
  `UnitType` varchar(45) NOT NULL,
  PRIMARY KEY (`UnitTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO unit_type VALUES ('0', 'Kilograms');
INSERT INTO unit_type VALUES ('1', 'Piece');
INSERT INTO unit_type VALUES ('2', 'Liters');
INSERT INTO unit_type VALUES ('3', 'ML');
INSERT INTO unit_type VALUES ('5', 'piece');

