-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 10, 2020 at 05:32 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tedlaweb`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add search history model', 7, 'add_searchhistorymodel'),
(26, 'Can change search history model', 7, 'change_searchhistorymodel'),
(27, 'Can delete search history model', 7, 'delete_searchhistorymodel'),
(28, 'Can view search history model', 7, 'view_searchhistorymodel'),
(29, 'Can add handle model', 8, 'add_handlemodel'),
(30, 'Can change handle model', 8, 'change_handlemodel'),
(31, 'Can delete handle model', 8, 'delete_handlemodel'),
(32, 'Can view handle model', 8, 'view_handlemodel'),
(33, 'Can add save item model', 9, 'add_saveitemmodel'),
(34, 'Can change save item model', 9, 'change_saveitemmodel'),
(35, 'Can delete save item model', 9, 'delete_saveitemmodel'),
(36, 'Can view save item model', 9, 'view_saveitemmodel'),
(37, 'Can add like item model', 10, 'add_likeitemmodel'),
(38, 'Can change like item model', 10, 'change_likeitemmodel'),
(39, 'Can delete like item model', 10, 'delete_likeitemmodel'),
(40, 'Can view like item model', 10, 'view_likeitemmodel');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-11-15 20:44:11.550497', '44', 'History <tedla001@odu.edu, machine learning>', 3, '', 7, 5);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(8, 'users', 'handlemodel'),
(10, 'users', 'likeitemmodel'),
(9, 'users', 'saveitemmodel'),
(7, 'users', 'searchhistorymodel'),
(6, 'users', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-11-15 00:43:23.036437'),
(2, 'contenttypes', '0002_remove_content_type_name', '2020-11-15 00:43:23.880347'),
(3, 'auth', '0001_initial', '2020-11-15 00:43:24.932990'),
(4, 'auth', '0002_alter_permission_name_max_length', '2020-11-15 00:43:28.401219'),
(5, 'auth', '0003_alter_user_email_max_length', '2020-11-15 00:43:28.490745'),
(6, 'auth', '0004_alter_user_username_opts', '2020-11-15 00:43:28.544419'),
(7, 'auth', '0005_alter_user_last_login_null', '2020-11-15 00:43:28.573939'),
(8, 'auth', '0006_require_contenttypes_0002', '2020-11-15 00:43:28.601454'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2020-11-15 00:43:28.635505'),
(10, 'auth', '0008_alter_user_username_max_length', '2020-11-15 00:43:28.666219'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2020-11-15 00:43:28.696472'),
(12, 'auth', '0010_alter_group_name_max_length', '2020-11-15 00:43:28.791027'),
(13, 'auth', '0011_update_proxy_permissions', '2020-11-15 00:43:28.827110'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2020-11-15 00:43:28.881346'),
(15, 'users', '0001_initial', '2020-11-15 00:43:29.660056'),
(16, 'admin', '0001_initial', '2020-11-15 00:43:33.471328'),
(17, 'admin', '0002_logentry_remove_auto_add', '2020-11-15 00:43:35.000230'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2020-11-15 00:43:35.084440'),
(19, 'sessions', '0001_initial', '2020-11-15 00:43:35.507317'),
(20, 'users', '0002_searchhistorymodel', '2020-11-15 00:43:35.859352'),
(21, 'users', '0003_handlemodel', '2020-11-15 00:43:36.957876'),
(22, 'users', '0004_auto_20201117_1111', '2020-11-17 11:11:29.379067'),
(23, 'users', '0005_auto_20201117_1112', '2020-11-17 11:12:39.641548'),
(24, 'users', '0006_saveitemmodel', '2020-11-17 16:35:28.873423'),
(25, 'users', '0007_likeitemmodel', '2020-12-06 21:51:36.798867');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('h3o3dsu8tx470jjxnbft7rk4dqm2fd9a', '.eJxVj0EOwiAQRa9iWNtmoFDApXvP0AwwClpp0tK4MN5dmnShyaz-f_8l82YDriUO60LzkAI7Mc6Ov5lD_6C8FeGO-Ta1fsplTq7dkHZvl_YyBRrPO_sniLjEuoaAHhwpsF46Z5UCISXHrjNWUd93jsgoKa-qB3sFaYzUghsKGrXWytgqfUUsZVoIZ1-Nb1ZSGamqn-hjynQYa5NTvlU0YCG-PWMlNMDr7aGooQABDecN1-zz-QLpg0_w:1kfDIp:SFsscBZ_l-Clh41I2M2Y9_iJn6NyaESZ3PessFeSziM', '2020-12-01 21:34:35.166198'),
('md6ha52h96o5i74pioqajzlbt6dmb0op', '.eJxVj0FugzAQRa9SzaqRAhobAzFSN9n3DGhsD4WU2pVt0kWUu9dIbCLN6v33vzQP-Jsp55CYop1heEBe8sowgF0pJfEW_E_YEoc7x48b3SnZuPzmYdq8fT_BGRxlFkUXWmGFotwBZYESJVZCVqjheYaRtjyPZSyOi9sr8MIM2W_2e-Bu5L9CbYPPcTH1rtRHmurP4Hi9Hu7LwEypfACtkNR3xqFzsr_01AjJop10o5RCvrC0tiF0lrrJIPaKGbVQrWk6JNROwPMfZBpYNQ:1knBL4:OjDr-isoQLekXlaEkNG-ewV8g3DKgHj-maJ8aokhut8', '2020-12-23 21:05:50.876899');

-- --------------------------------------------------------

--
-- Table structure for table `users_handlemodel`
--

CREATE TABLE `users_handlemodel` (
  `id` int(11) NOT NULL,
  `handle` varchar(500) NOT NULL,
  `date` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_handlemodel`
--

INSERT INTO `users_handlemodel` (`id`, `handle`, `date`, `user_id`) VALUES
(1, '29581', '2020-11-16 20:01:36.677708', 1),
(2, '29582', '2020-11-17 20:44:06.272683', 1),
(3, '29583', '2020-11-17 20:47:43.866366', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users_likeitemmodel`
--

CREATE TABLE `users_likeitemmodel` (
  `id` int(11) NOT NULL,
  `handle` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_likeitemmodel`
--

INSERT INTO `users_likeitemmodel` (`id`, `handle`, `user_id`) VALUES
(4, '28277', 1),
(5, '29348', 1),
(6, '28277', 1),
(7, '28277', 1),
(8, '28277', 1),
(9, '28277', 1),
(50, '28418', 1),
(51, '27369', 1),
(52, '26103', 1),
(53, '28072', 1),
(54, '27337', 1),
(56, '28980', 1),
(58, '25954', 10),
(59, '27717', 10),
(60, '29287', 10),
(61, '27517', 10),
(62, '26691', 10),
(63, '28645', 10),
(64, '28980', 10),
(65, '26463', 10),
(66, '28387', 11),
(67, '27787', 11),
(68, '28123', 11),
(69, '25954', 11),
(70, '27717', 11),
(71, '28980', 11),
(72, '25954', 12),
(73, '27717', 12),
(74, '29287', 12),
(75, '28387', 12),
(76, '27787', 12),
(77, '26420', 12),
(78, '28819', 12),
(79, '28023', 12),
(80, '29305', 12),
(81, '28902', 12),
(84, '26035', 1),
(85, '26480', 1),
(86, '27787', 1),
(87, '28679', 1),
(89, '27609', 1),
(90, '27900', 1),
(91, '29070', 1),
(94, '26463', 1),
(95, '26599', 1),
(102, '27717', 1),
(103, '29287', 1),
(116, '26972', 1),
(117, '25954', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users_saveitemmodel`
--

CREATE TABLE `users_saveitemmodel` (
  `id` int(11) NOT NULL,
  `handle` varchar(500) NOT NULL,
  `date` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_saveitemmodel`
--

INSERT INTO `users_saveitemmodel` (`id`, `handle`, `date`, `user_id`) VALUES
(80, '26034', '2020-12-08 10:56:59.999182', 1),
(81, '27186', '2020-12-08 10:57:02.399089', 1),
(83, '27717', '2020-12-08 11:14:44.763427', 1),
(85, '26972', '2020-12-08 11:18:22.670816', 1),
(87, '25954', '2020-12-08 12:15:38.382295', 1),
(89, '27337', '2020-12-08 12:48:33.835543', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users_searchhistorymodel`
--

CREATE TABLE `users_searchhistorymodel` (
  `id` int(11) NOT NULL,
  `searchtext` varchar(500) NOT NULL,
  `date` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  `contributor_author` varchar(150) NOT NULL,
  `contributor_committeechair` varchar(150) NOT NULL,
  `contributor_department` varchar(150) NOT NULL,
  `date1` varchar(30) NOT NULL,
  `date2` varchar(30) NOT NULL,
  `description_degree` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_searchhistorymodel`
--

INSERT INTO `users_searchhistorymodel` (`id`, `searchtext`, `date`, `user_id`, `contributor_author`, `contributor_committeechair`, `contributor_department`, `date1`, `date2`, `description_degree`) VALUES
(193, 'power', '2020-11-17 14:26:49.337980', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(194, 'machine learning', '2020-11-17 16:30:47.148050', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(195, 'machine learning', '2020-11-17 16:33:40.964365', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(196, 'machine learning', '2020-11-17 16:36:04.492460', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(197, 'machine learning', '2020-11-17 16:37:16.158777', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(198, 'asd', '2020-11-17 16:37:55.119617', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(199, 'machine learning', '2020-11-17 16:37:59.097308', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(200, 'machine learning ', '2020-11-17 16:39:27.781709', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(201, 'machine learning', '2020-11-17 16:39:55.262289', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(202, 'power', '2020-11-17 16:39:58.626694', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(203, 'machine learning', '2020-11-17 16:47:37.648394', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(204, 'machine learning', '2020-11-17 17:16:53.495479', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(205, 'machine learning ', '2020-11-17 17:16:56.230605', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(206, 'power electronics', '2020-11-17 17:17:02.326303', 9, '', '', '', '1940-01-01', '2020-11-17', ''),
(292, 'machine learning', '2020-12-07 01:22:22.574960', 10, '', '', '', '1940-01-01', '2020-12-07', ''),
(293, 'power', '2020-12-07 01:22:43.570896', 10, '', '', '', '1940-01-01', '2020-12-07', ''),
(294, 'machine learning', '2020-12-07 01:22:50.429637', 10, '', '', '', '1940-01-01', '2020-12-07', ''),
(295, 'powers', '2020-12-07 13:24:45.430082', 11, '', '', '', '1940-01-01', '2020-12-07', ''),
(296, 'David', '2020-12-07 13:24:52.362859', 11, '', '', '', '1940-01-01', '2020-12-07', ''),
(297, 'machine learning', '2020-12-07 13:24:58.155163', 11, '', '', '', '1940-01-01', '2020-12-07', ''),
(298, 'digital', '2020-12-07 13:25:04.155158', 11, '', '', '', '1940-01-01', '2020-12-07', ''),
(299, 'signal', '2020-12-07 13:25:09.872502', 11, '', '', '', '1940-01-01', '2020-12-07', ''),
(300, 'power electronics', '2020-12-07 13:25:33.784641', 11, '', '', '', '1940-01-01', '2020-12-07', ''),
(301, 'power electronics', '2020-12-07 13:25:48.464726', 11, '', '', '', '1940-01-01', '2020-12-07', ''),
(302, 'power electronics', '2020-12-07 13:25:59.582425', 11, '', '', '', '1940-01-01', '2020-12-07', ''),
(303, 'Electronics', '2020-12-07 13:26:43.140099', 11, '', '', '', '1940-01-01', '2020-12-07', ''),
(304, 'machine learning', '2020-12-07 13:26:53.490999', 11, '', '', 'computer science', '1940-01-01', '2020-12-07', ''),
(305, 'machine learning', '2020-12-07 13:28:55.638294', 12, '', '', '', '1940-01-01', '2020-12-07', ''),
(306, 'signal', '2020-12-07 13:29:06.767081', 12, '', '', '', '1940-01-01', '2020-12-07', ''),
(307, 'processor', '2020-12-07 13:29:18.324625', 12, '', '', '', '1940-01-01', '2020-12-07', ''),
(308, 'micro', '2020-12-07 13:29:28.672021', 12, '', '', '', '1940-01-01', '2020-12-07', ''),
(309, 'artificial intelligence', '2020-12-07 13:29:51.591454', 12, '', '', '', '1940-01-01', '2020-12-07', ''),
(376, 'machine learning', '2020-12-08 10:56:22.339765', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(377, 'power', '2020-12-08 10:56:41.947775', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(378, 'machine learning', '2020-12-08 11:13:52.026570', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(379, 'machine learning', '2020-12-08 11:15:19.726879', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(380, 'machine learning', '2020-12-08 11:15:37.435559', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(381, 'Digital Signal processing', '2020-12-08 11:17:43.251273', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(382, 'machine learning', '2020-12-08 11:19:09.706193', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(385, 'machine learning', '2020-12-08 11:55:47.765368', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(387, 'machine learning', '2020-12-08 12:16:15.650126', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(388, 'machine learning', '2020-12-08 12:16:36.324530', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(390, 'machine learning', '2020-12-08 12:48:56.317731', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(391, 'Digital Signal processing', '2020-12-08 12:49:14.735766', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(393, 'machine learning', '2020-12-08 13:08:02.890984', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(394, 'Digital Signal processing', '2020-12-08 13:08:20.895096', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(395, 'machine learning', '2020-12-08 13:08:27.151598', 1, '', '', '', '1940-01-01', '2020-12-08', ''),
(396, 'machine learning', '2020-12-09 10:13:52.224797', 1, '', '', '', '1940-01-01', '2020-12-09', ''),
(397, 'machine learning', '2020-12-09 10:16:39.048971', 1, '', '', '', '1940-01-01', '2020-12-09', ''),
(398, 'machine learning', '2020-12-09 16:32:15.056572', 1, '', '', '', '1940-01-01', '2020-12-09', ''),
(399, 'class1 onmouseover=javascript:func()', '2020-12-09 21:05:44.024384', 1, '', '', '', '1940-01-01', '2020-12-09', ''),
(400, 'class1 onmouseover=javascript:func()', '2020-12-09 21:05:50.843859', 1, '', '', '', '1940-01-01', '2020-12-09', '');

-- --------------------------------------------------------

--
-- Table structure for table `users_user`
--

CREATE TABLE `users_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `email` varchar(254) NOT NULL,
  `username` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users_user`
--

INSERT INTO `users_user` (`id`, `password`, `last_login`, `is_superuser`, `first_name`, `last_name`, `is_staff`, `is_active`, `date_joined`, `email`, `username`) VALUES
(1, 'pbkdf2_sha256$216000$7QbrT7b8SRsB$WLPxJrfMwdIjLZYMu6LmU/UF5NHr+VGBB2BOkj3zq2E=', '2020-12-09 10:02:48.393987', 0, '', '', 0, 1, '2020-11-15 01:20:17.450655', 'saraswathi419@gmail.com', ''),
(5, 'pbkdf2_sha256$216000$vwgZp8v5rP40$PvIHeXN7toTXvOWQ4Ogu4at5Yi9tmvm7DIZCdupv2Vs=', '2020-11-15 20:37:23.449886', 1, '', '', 1, 1, '2020-11-15 20:36:16.578122', 'saras@odu.edu', 'saras'),
(7, 'pbkdf2_sha256$216000$oF0AFChCoiUt$j2w4XUamV3IUNAjTrp/V3/qF4yE6yLEK4T51H+nlD1M=', '2020-11-16 21:20:14.785083', 0, '', '', 0, 1, '2020-11-16 21:19:13.154142', 'dummy@gmail.com', ''),
(8, 'pbkdf2_sha256$216000$NgqCFSisz6dT$1gHaHaR+4zVJ2lyhxDOUKmv6jN9zrKAdO+yy/vlhmuw=', '2020-11-16 21:46:21.865204', 0, '', '', 0, 1, '2020-11-16 21:24:02.371790', 'karthik99.84@gmail.com', ''),
(9, 'pbkdf2_sha256$216000$zsKxarTKkyC9$dO8FmgprwamkJwTmZA/o1O+PzG/26XvQGwZlnJBIXp0=', '2020-11-17 17:16:33.473459', 0, '', '', 0, 1, '2020-11-17 12:01:14.054964', 'tedlawebtest@gmail.com', ''),
(10, 'pbkdf2_sha256$216000$fENpdV3Xk0ZW$CYPTc32TNXnQVPWGHCVgW0f02sNFYUBrrHrOEsDEZEw=', '2020-12-07 01:22:14.518865', 0, '', '', 0, 1, '2020-12-07 01:20:40.764002', 'someone@gmail.com', ''),
(11, 'pbkdf2_sha256$216000$Pck3LVvtyykA$WpKGd+6n0crs/VFUxxYkLYOcWuiS2w+2zsNM25PZk1M=', '2020-12-07 13:24:27.228120', 0, '', '', 0, 1, '2020-12-07 13:23:43.015961', 'someone2@gmail.com', ''),
(12, 'pbkdf2_sha256$216000$Xr4Zkx1tGexh$8WDGzxZf1JwOtoKql21NXVRv8hAhtdPFuR/rsOjmWUU=', '2020-12-07 13:28:47.139091', 0, '', '', 0, 1, '2020-12-07 13:28:01.996469', 'someone3@gmail.com', '');

-- --------------------------------------------------------

--
-- Table structure for table `users_user_groups`
--

CREATE TABLE `users_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users_user_user_permissions`
--

CREATE TABLE `users_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_users_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `users_handlemodel`
--
ALTER TABLE `users_handlemodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_handlemodel_user_id_877727e8_fk_users_user_id` (`user_id`);

--
-- Indexes for table `users_likeitemmodel`
--
ALTER TABLE `users_likeitemmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_likeitemmodel_user_id_42de0c0d_fk_users_user_id` (`user_id`);

--
-- Indexes for table `users_saveitemmodel`
--
ALTER TABLE `users_saveitemmodel`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `handle` (`handle`),
  ADD KEY `users_saveitemmodel_user_id_3a312515_fk_users_user_id` (`user_id`);

--
-- Indexes for table `users_searchhistorymodel`
--
ALTER TABLE `users_searchhistorymodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_searchhistorymodel_user_id_1da2dff1_fk_users_user_id` (`user_id`);

--
-- Indexes for table `users_user`
--
ALTER TABLE `users_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `users_user_groups`
--
ALTER TABLE `users_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_user_groups_user_id_group_id_b88eab82_uniq` (`user_id`,`group_id`),
  ADD KEY `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `users_user_user_permissions`
--
ALTER TABLE `users_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_user_user_permissions_user_id_permission_id_43338c45_uniq` (`user_id`,`permission_id`),
  ADD KEY `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `users_handlemodel`
--
ALTER TABLE `users_handlemodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `users_likeitemmodel`
--
ALTER TABLE `users_likeitemmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=118;

--
-- AUTO_INCREMENT for table `users_saveitemmodel`
--
ALTER TABLE `users_saveitemmodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=91;

--
-- AUTO_INCREMENT for table `users_searchhistorymodel`
--
ALTER TABLE `users_searchhistorymodel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=401;

--
-- AUTO_INCREMENT for table `users_user`
--
ALTER TABLE `users_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `users_user_groups`
--
ALTER TABLE `users_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_user_user_permissions`
--
ALTER TABLE `users_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`);

--
-- Constraints for table `users_handlemodel`
--
ALTER TABLE `users_handlemodel`
  ADD CONSTRAINT `users_handlemodel_user_id_877727e8_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`);

--
-- Constraints for table `users_likeitemmodel`
--
ALTER TABLE `users_likeitemmodel`
  ADD CONSTRAINT `users_likeitemmodel_user_id_42de0c0d_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`);

--
-- Constraints for table `users_saveitemmodel`
--
ALTER TABLE `users_saveitemmodel`
  ADD CONSTRAINT `users_saveitemmodel_user_id_3a312515_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`);

--
-- Constraints for table `users_searchhistorymodel`
--
ALTER TABLE `users_searchhistorymodel`
  ADD CONSTRAINT `users_searchhistorymodel_user_id_1da2dff1_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`);

--
-- Constraints for table `users_user_groups`
--
ALTER TABLE `users_user_groups`
  ADD CONSTRAINT `users_user_groups_group_id_9afc8d0e_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `users_user_groups_user_id_5f6f5a90_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`);

--
-- Constraints for table `users_user_user_permissions`
--
ALTER TABLE `users_user_user_permissions`
  ADD CONSTRAINT `users_user_user_perm_permission_id_0b93982e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `users_user_user_permissions_user_id_20aca447_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
