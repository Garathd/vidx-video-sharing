-- MySQL dump 10.13  Distrib 5.5.57, for debian-linux-gnu (x86_64)
--
-- Host: 0.0.0.0    Database: milestoneProject4
-- ------------------------------------------------------
-- Server version	5.5.57-0ubuntu0.14.04.1

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
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Music'),(2,'Movie'),(3,'Sport'),(4,'Comedy'),(5,'Documentary'),(6,'Tutorial'),(7,'Anime'),(8,'Live'),(9,'Biography');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Garath','access'),(2,'Sean','0000'),(3,'Mike','0000'),(4,'Dave','0000'),(5,'Billy','0000'),(6,'Tony','0000');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `videos`
--

DROP TABLE IF EXISTS `videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `videos` (
  `video_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `description` varchar(255) NOT NULL,
  `img_source` varchar(255) NOT NULL,
  `video_source` varchar(255) NOT NULL,
  `category_id` int(11) NOT NULL,
  `origin` char(5) NOT NULL,
  PRIMARY KEY (`video_id`),
  KEY `user_id` (`user_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `videos_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `videos_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `categories` (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `videos`
--

LOCK TABLES `videos` WRITE;
/*!40000 ALTER TABLE `videos` DISABLE KEYS */;
INSERT INTO `videos` VALUES (1,1,'Simple Man','Simple Man by Lynyrd (2003) Live at Amsouth Amphitheatre, TN','https://i.pinimg.com/originals/03/1a/48/031a485f25d9ff077190676c30c2cd71.png','https://www.youtube.com/watch?v=sHQ_aTjXObs',1,'true'),(2,1,'Through the Grapevine','Creedence Clearwater Revival performing I Heard It Through The Grapevine','http://www.chattanoogapulse.com/downloads/5127/download/between%20the%20sleeves.png?cb=6a376c9d663b3886f2f894f19b004f5a&w=400&h=','https://www.youtube.com/watch?v=wCCfc2vAuDU',1,'true'),(5,1,'Dragon Ball Z','Random Bull Shit','http://4.bp.blogspot.com/-Rikzkpxtcxk/TfW-kudsnhI/AAAAAAAABYs/HOM2udytZzk/s400/dragon+ball+z+wallpapers+16.jpg','https://www.youtube.com/watch?v=xbhCPt6PZIU',2,'true'),(6,2,'Jackass','Best of Jackass Clips','https://www.wykop.pl/cdn/c3201142/comment_tdKvtwvekzTCGtkq5MOVTntjyZ2U53ti,w400.jpg','https://www.youtube.com/watch?v=3_3VrHLuqG4',4,'true'),(7,2,'Jones vs Gustafsson','Epic classic of their first encounter ','https://static.adweek.com/adweek.com-prod/wp-content/uploads/sites/8/2016/03/ufc400.jpg','https://www.youtube.com/watch?v=1TWKgnGaE9U',3,'true'),(8,3,'Fleetwood Mac','Documentary about the band Fleetwood Mac. The band talks candidly about the good times and bad times and the whole story of what went on in the Rumors album','https://i.ebayimg.com/00/s/MTIwMFgxNjAw/z/pI8AAOSwhnlb9MQz/$_1.JPG','https://www.youtube.com/watch?v=2SbuqzGYJyc',5,'true'),(9,3,'Learn Python','An extensive tutorial on learning python for beginners','http://www.letsrundigital.com/assets/images/services/python.png','https://www.youtube.com/watch?v=rfscVS0vtbw',6,'true'),(11,3,'Jones VS Gustafsson 1','Epic classic of their first encounter ','https://static.adweek.com/adweek.com-prod/wp-content/uploads/sites/8/2016/03/ufc400.jpg','https://www.youtube.com/watch?v=1TWKgnGaE9U',3,'false'),(13,3,'Through the Grapevine','Creedence Clearwater Revival performing I Heard It Through The Grapevine','http://www.chattanoogapulse.com/downloads/5127/download/between%20the%20sleeves.png?cb=6a376c9d663b3886f2f894f19b004f5a&w=400&h=','https://www.youtube.com/watch?v=wCCfc2vAuDU',1,'false'),(14,2,'Dragon Ball Z','Cool scenes from Dragon Ball Z','http://4.bp.blogspot.com/-Rikzkpxtcxk/TfW-kudsnhI/AAAAAAAABYs/HOM2udytZzk/s400/dragon+ball+z+wallpapers+16.jpg','https://www.youtube.com/watch?v=xbhCPt6PZIU',2,'false'),(15,1,'Fleetwood Mac','Documentary about the band Fleetwood Mac. The band talks candidly about the good times and bad times and the whole story of what went on in the Rumors album','https://i.ebayimg.com/00/s/MTIwMFgxNjAw/z/pI8AAOSwhnlb9MQz/$_1.JPG','https://www.youtube.com/watch?v=2SbuqzGYJyc',5,'false');
/*!40000 ALTER TABLE `videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `votes`
--

DROP TABLE IF EXISTS `votes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `votes` (
  `vote_id` int(11) NOT NULL AUTO_INCREMENT,
  `video_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `vote` int(5) NOT NULL,
  PRIMARY KEY (`vote_id`),
  KEY `video_id` (`video_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `votes_ibfk_1` FOREIGN KEY (`video_id`) REFERENCES `videos` (`video_id`) ON DELETE CASCADE,
  CONSTRAINT `votes_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `votes`
--

LOCK TABLES `votes` WRITE;
/*!40000 ALTER TABLE `votes` DISABLE KEYS */;
INSERT INTO `votes` VALUES (1,6,1,-1),(2,7,1,1),(3,6,3,-1),(4,8,1,1),(5,9,2,-1),(6,5,2,1);
/*!40000 ALTER TABLE `votes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-24 14:08:18
