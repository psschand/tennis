

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tennis_DB`
--

-- --------------------------------------------------------

--
-- Table structure for table `tennis_book`
--


CREATE TABLE IF NOT EXISTS `tennis_book`  (
    id int NOT NULL AUTO_INCREMENT,
    ATP varchar(255) ,
    Location varchar(255),
    Tournament varchar(255),
    Date varchar(255),
    Series varchar(255),
	Court varchar(255) ,
    Surface varchar(255),
    Round varchar(255),
	Winner varchar(255) ,
    Loser varchar(255),
    PRIMARY KEY (id)
);



--
-- Dumping data for table `tennis_book`
--
INSERT INTO `tennis_book` (`id`, `ATP`, `Location`, `Tournament`, `Date`, `Series`, `Court`, `Surface`, `Round`, `Winner`, `Loser`) VALUES
(16, '1', 'Brisbane', 'Brisbane International','02-01-2011', 'ATP250','Outdoor','Hard', '1st Round','Lopez F.','Petzschner P');


