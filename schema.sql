-- --------------------------------------------------------
-- Host:                         192.168.0.101
-- Server version:               5.5.32-0ubuntu0.13.04.1 - (Ubuntu)
-- Server OS:                    debian-linux-gnu
-- HeidiSQL Version:             8.0.0.4396
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping structure for table dhcp.groups
CREATE TABLE IF NOT EXISTS `groups` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `domain` tinytext,
  `description` tinytext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table dhcp.leases
CREATE TABLE IF NOT EXISTS `leases` (
  `mac` char(17) NOT NULL,
  `ip` varchar(15) NOT NULL,
  `hostname` tinytext,
  `subnet` int(10) unsigned NOT NULL,
  PRIMARY KEY (`mac`),
  KEY `subnet` (`subnet`),
  CONSTRAINT `leases_subnets_id` FOREIGN KEY (`subnet`) REFERENCES `subnets` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table dhcp.options
CREATE TABLE IF NOT EXISTS `options` (
  `group` int(10) unsigned NOT NULL,
  `number` int(10) unsigned NOT NULL,
  `value` tinytext NOT NULL,
  `description` tinytext,
  KEY `group` (`group`),
  KEY `group_number` (`group`,`number`),
  CONSTRAINT `options_groups_id` FOREIGN KEY (`group`) REFERENCES `groups` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table dhcp.reservations
CREATE TABLE IF NOT EXISTS `reservations` (
  `subnet` int(10) unsigned NOT NULL,
  `mac` varchar(17) NOT NULL,
  `hostname` varchar(50) DEFAULT NULL,
  `ip` varchar(15) NOT NULL,
  KEY `mac` (`mac`),
  KEY `subnet` (`subnet`),
  CONSTRAINT `reservations_subnets_id` FOREIGN KEY (`subnet`) REFERENCES `subnets` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.


-- Dumping structure for table dhcp.subnets
CREATE TABLE IF NOT EXISTS `subnets` (
  `id` int(10) unsigned NOT NULL,
  `network_address` varchar(15) NOT NULL,
  `subnet_mask` varchar(15) NOT NULL,
  `gateway` varchar(15) NOT NULL,
  `lease_time` int(10) NOT NULL DEFAULT '86400',
  `group` int(11) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `group` (`group`),
  CONSTRAINT `subnets_groups_id` FOREIGN KEY (`group`) REFERENCES `groups` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
