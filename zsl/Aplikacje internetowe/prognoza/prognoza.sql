-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Czas generowania: 28 Lis 2022, 15:11
-- Wersja serwera: 10.1.8-MariaDB
-- Wersja PHP: 5.6.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `prognoza`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `miasta`
--

CREATE TABLE `miasta` (
  `id` int(11) NOT NULL,
  `nazwa` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `miasta`
--

INSERT INTO `miasta` (`id`, `nazwa`) VALUES
(1, 'Warszawa'),
(2, 'Poznań'),
(3, 'Łódź'),
(4, 'Kraków');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pogoda`
--

CREATE TABLE `pogoda` (
  `id` int(11) NOT NULL,
  `miasta_id` int(11) NOT NULL,
  `data_prognozy` date NOT NULL,
  `temperatura_noc` int(11) NOT NULL,
  `temperatura_dzien` int(11) NOT NULL,
  `opady` int(11) NOT NULL,
  `cisnienie` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pogoda`
--

INSERT INTO `pogoda` (`id`, `miasta_id`, `data_prognozy`, `temperatura_noc`, `temperatura_dzien`, `opady`, `cisnienie`) VALUES
(1, 2, '2019-05-18', 12, 15, 30, 996),
(2, 2, '2019-05-17', 11, 15, 30, 995),
(3, 2, '2019-05-16', 11, 17, 30, 995),
(4, 2, '2019-05-15', 8, 19, 4, 1000),
(5, 2, '2019-05-14', 8, 23, 4, 1000),
(6, 2, '2019-05-13', 5, 20, 0, 1020),
(7, 2, '2019-05-12', 5, 20, 0, 1020);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indexes for table `miasta`
--
ALTER TABLE `miasta`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pogoda`
--
ALTER TABLE `pogoda`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `miasta`
--
ALTER TABLE `miasta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT dla tabeli `pogoda`
--
ALTER TABLE `pogoda`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
