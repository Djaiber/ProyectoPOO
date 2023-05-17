-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 11, 2023 at 12:45 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user`
--

-- --------------------------------------------------------

--
-- Table structure for table `bonication`
--

CREATE TABLE `bonication` (
  `bonoCode` int(8) NOT NULL,
  `consumerId` int(6) NOT NULL,
  `date` date NOT NULL,
  `redeemPoints` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `consumer`
--

CREATE TABLE `consumer` (
  `idConsumer` int(6) NOT NULL,
  `nameConsumer` varchar(50) NOT NULL,
  `emailConsumer` varchar(50) NOT NULL,
  `password` varchar(30) NOT NULL,
  `registeredDate` date NOT NULL DEFAULT current_timestamp(),
  `telefono` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `consumer`
--

INSERT INTO `consumer` (`idConsumer`, `nameConsumer`, `emailConsumer`, `password`, `registeredDate`, `telefono`) VALUES
(1, 'Jaiber Vamos', 'djaiver9@gmail.com', '12345', '2023-05-09', '3173074159'),
(2, 'Jhonantan', 'jhonathan@gmail.com', '12345678', '2023-05-09', '3215646311');

-- --------------------------------------------------------

--
-- Table structure for table `registershopping`
--

CREATE TABLE `registershopping` (
  `idConsumer` int(6) NOT NULL,
  `nameConsumer` varchar(50) NOT NULL,
  `shoppingCode` int(10) NOT NULL,
  `shoppingDate` date NOT NULL DEFAULT current_timestamp(),
  `value` int(8) NOT NULL,
  `bono` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `consumer`
--
ALTER TABLE `consumer`
  ADD PRIMARY KEY (`idConsumer`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `consumer`
--
ALTER TABLE `consumer`
  MODIFY `idConsumer` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
