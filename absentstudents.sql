-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 11, 2021 at 06:24 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `absentstudents`
--

-- --------------------------------------------------------

--
-- Table structure for table `absents_phones`
--

DROP TABLE IF EXISTS `absents_phones`;
CREATE TABLE IF NOT EXISTS `absents_phones` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `std_id` varchar(11) NOT NULL,
  `parent_phone` varchar(11) NOT NULL,
  `dt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=140 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `absents_phones`
--

INSERT INTO `absents_phones` (`id`, `std_id`, `parent_phone`, `dt`) VALUES
(1, '5900035883', '9193838705', '2021-06-11 05:18:14'),
(2, '4311851650', '9192816887', '2021-06-11 05:18:14'),
(139, '150604319', '919498245', '2021-06-11 05:18:14');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
