-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  sam. 31 août 2024 à 21:28
-- Version du serveur :  10.4.10-MariaDB
-- Version de PHP :  7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `tahyee`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add affectation', 1, 'add_affectation'),
(2, 'Can change affectation', 1, 'change_affectation'),
(3, 'Can delete affectation', 1, 'delete_affectation'),
(4, 'Can view affectation', 1, 'view_affectation'),
(5, 'Can add candidats', 2, 'add_candidats'),
(6, 'Can change candidats', 2, 'change_candidats'),
(7, 'Can delete candidats', 2, 'delete_candidats'),
(8, 'Can view candidats', 2, 'view_candidats'),
(9, 'Can add room', 3, 'add_room'),
(10, 'Can change room', 3, 'change_room'),
(11, 'Can delete room', 3, 'delete_room'),
(12, 'Can view room', 3, 'view_room'),
(13, 'Can add service', 4, 'add_service'),
(14, 'Can change service', 4, 'change_service'),
(15, 'Can delete service', 4, 'delete_service'),
(16, 'Can view service', 4, 'view_service'),
(17, 'Can add utilisateur', 5, 'add_utilisateur'),
(18, 'Can change utilisateur', 5, 'change_utilisateur'),
(19, 'Can delete utilisateur', 5, 'delete_utilisateur'),
(20, 'Can view utilisateur', 5, 'view_utilisateur'),
(21, 'Can add attestation', 6, 'add_attestation'),
(22, 'Can change attestation', 6, 'change_attestation'),
(23, 'Can delete attestation', 6, 'delete_attestation'),
(24, 'Can view attestation', 6, 'view_attestation'),
(25, 'Can add demandes', 7, 'add_demandes'),
(26, 'Can change demandes', 7, 'change_demandes'),
(27, 'Can delete demandes', 7, 'delete_demandes'),
(28, 'Can view demandes', 7, 'view_demandes'),
(29, 'Can add document', 8, 'add_document'),
(30, 'Can change document', 8, 'change_document'),
(31, 'Can delete document', 8, 'delete_document'),
(32, 'Can view document', 8, 'view_document'),
(33, 'Can add evaluation', 9, 'add_evaluation'),
(34, 'Can change evaluation', 9, 'change_evaluation'),
(35, 'Can delete evaluation', 9, 'delete_evaluation'),
(36, 'Can view evaluation', 9, 'view_evaluation'),
(37, 'Can add sujet_stage', 10, 'add_sujet_stage'),
(38, 'Can change sujet_stage', 10, 'change_sujet_stage'),
(39, 'Can delete sujet_stage', 10, 'delete_sujet_stage'),
(40, 'Can view sujet_stage', 10, 'view_sujet_stage'),
(41, 'Can add notification', 11, 'add_notification'),
(42, 'Can change notification', 11, 'change_notification'),
(43, 'Can delete notification', 11, 'delete_notification'),
(44, 'Can view notification', 11, 'view_notification'),
(45, 'Can add log entry', 12, 'add_logentry'),
(46, 'Can change log entry', 12, 'change_logentry'),
(47, 'Can delete log entry', 12, 'delete_logentry'),
(48, 'Can view log entry', 12, 'view_logentry'),
(49, 'Can add permission', 13, 'add_permission'),
(50, 'Can change permission', 13, 'change_permission'),
(51, 'Can delete permission', 13, 'delete_permission'),
(52, 'Can view permission', 13, 'view_permission'),
(53, 'Can add group', 14, 'add_group'),
(54, 'Can change group', 14, 'change_group'),
(55, 'Can delete group', 14, 'delete_group'),
(56, 'Can view group', 14, 'view_group'),
(57, 'Can add user', 15, 'add_user'),
(58, 'Can change user', 15, 'change_user'),
(59, 'Can delete user', 15, 'delete_user'),
(60, 'Can view user', 15, 'view_user'),
(61, 'Can add content type', 16, 'add_contenttype'),
(62, 'Can change content type', 16, 'change_contenttype'),
(63, 'Can delete content type', 16, 'delete_contenttype'),
(64, 'Can view content type', 16, 'view_contenttype'),
(65, 'Can add session', 17, 'add_session'),
(66, 'Can change session', 17, 'change_session'),
(67, 'Can delete session', 17, 'delete_session'),
(68, 'Can view session', 17, 'view_session');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$aXYVDAP7BlbOOL36xbFVxs$XgOYi0+Y8oUihDbuO1jkTclxctcpHbqFfy9CJxSEVcs=', '2024-08-31 14:23:05.822041', 1, 'tahya', '', '', '', 1, 1, '2024-08-31 14:22:49.245539');

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-08-31 15:50:40.456126', '1', '1', 2, '[]', 7, 1);

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'stage_moov', 'affectation'),
(2, 'stage_moov', 'candidats'),
(3, 'stage_moov', 'room'),
(4, 'stage_moov', 'service'),
(5, 'stage_moov', 'utilisateur'),
(6, 'stage_moov', 'attestation'),
(7, 'stage_moov', 'demandes'),
(8, 'stage_moov', 'document'),
(9, 'stage_moov', 'evaluation'),
(10, 'stage_moov', 'sujet_stage'),
(11, 'stage_moov', 'notification'),
(12, 'admin', 'logentry'),
(13, 'auth', 'permission'),
(14, 'auth', 'group'),
(15, 'auth', 'user'),
(16, 'contenttypes', 'contenttype'),
(17, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-08-31 14:20:54.847158'),
(2, 'auth', '0001_initial', '2024-08-31 14:20:54.994819'),
(3, 'admin', '0001_initial', '2024-08-31 14:20:55.039338'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-08-31 14:20:55.049305'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-31 14:20:55.059273'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-08-31 14:20:55.101352'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-08-31 14:20:55.125599'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-08-31 14:20:55.142393'),
(9, 'auth', '0004_alter_user_username_opts', '2024-08-31 14:20:55.148546'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-08-31 14:20:55.166561'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-08-31 14:20:55.169989'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-08-31 14:20:55.180183'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-08-31 14:20:55.198695'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-08-31 14:20:55.217961'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-08-31 14:20:55.235425'),
(16, 'auth', '0011_update_proxy_permissions', '2024-08-31 14:20:55.243467'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-08-31 14:20:55.260181'),
(18, 'sessions', '0001_initial', '2024-08-31 14:20:55.277292'),
(19, 'stage_moov', '0001_initial', '2024-08-31 14:20:55.680620'),
(20, 'stage_moov', '0002_remove_demandes_id_sujet_candidats_password_and_more', '2024-08-31 14:20:56.092868'),
(21, 'stage_moov', '0003_alter_candidats_password', '2024-08-31 14:21:03.605001'),
(22, 'stage_moov', '0004_rename_id_candidat_demandes_nom_candidat', '2024-08-31 16:13:59.008809');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('4237l8qy2gz6l4k9ewd13rw5c0vfqb7q', '.eJxVjDEOAiEQRe9CbcgADoKlvWcgAwyyaiBZdivj3XWTLbT9773_EoHWpYZ18BymLM5CicPvFik9uG0g36nduky9LfMU5abInQ557Zmfl939O6g06rdmJufoBFZ50AikwWSw4G3yjn0hRG-LcSWyMaQ0Fi5aGSSGGI9KoXh_AM0yN2Y:1skP0L:UHzMi2WVIK9ssNqreAgqx3vF9m8Z5AupnGQNv-lLqHg', '2024-09-14 14:23:05.822783');

-- --------------------------------------------------------

--
-- Structure de la table `stage_moov_affectation`
--

DROP TABLE IF EXISTS `stage_moov_affectation`;
CREATE TABLE IF NOT EXISTS `stage_moov_affectation` (
  `Id_affectation` int(11) NOT NULL AUTO_INCREMENT,
  `date_affectaion` datetime(6) NOT NULL,
  `Id_demande_id` int(11) NOT NULL,
  `Id_sujet_id` int(11) NOT NULL,
  PRIMARY KEY (`Id_affectation`),
  KEY `stage_moov_affectation_Id_demande_id_615aafa5` (`Id_demande_id`),
  KEY `stage_moov_affectation_Id_sujet_id_06b22bce` (`Id_sujet_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `stage_moov_attestation`
--

DROP TABLE IF EXISTS `stage_moov_attestation`;
CREATE TABLE IF NOT EXISTS `stage_moov_attestation` (
  `Id_attestation` int(11) NOT NULL AUTO_INCREMENT,
  `Date_emission` datetime(6) NOT NULL,
  `chemin_attestation` varchar(100) NOT NULL,
  `Id_affectation_id` int(11) NOT NULL,
  `stagaire_id` int(11) NOT NULL,
  PRIMARY KEY (`Id_attestation`),
  KEY `stage_moov_attestation_Id_affectation_id_69b735b7` (`Id_affectation_id`),
  KEY `stage_moov_attestation_stagaire_id_db1b09ae` (`stagaire_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `stage_moov_candidats`
--

DROP TABLE IF EXISTS `stage_moov_candidats`;
CREATE TABLE IF NOT EXISTS `stage_moov_candidats` (
  `Id_candidat` int(11) NOT NULL AUTO_INCREMENT,
  `Nom_complet` varchar(50) NOT NULL,
  `universite` varchar(50) NOT NULL,
  `niveau_academique` varchar(50) NOT NULL,
  `specialite` varchar(50) NOT NULL,
  `Date_Naissance` date NOT NULL,
  `email` varchar(50) NOT NULL,
  `telephone` varchar(8) NOT NULL,
  `Date_demande` datetime(6) NOT NULL,
  `cv` varchar(100) DEFAULT NULL,
  `lettre_motivation` varchar(100) DEFAULT NULL,
  `demande` varchar(100) NOT NULL,
  `periode` varchar(50) NOT NULL,
  `Id_utilisateur_id` int(11) DEFAULT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`Id_candidat`),
  UNIQUE KEY `email` (`email`),
  KEY `stage_moov_candidats_Id_utilisateur_id_b75f7fd3` (`Id_utilisateur_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `stage_moov_candidats`
--

INSERT INTO `stage_moov_candidats` (`Id_candidat`, `Nom_complet`, `universite`, `niveau_academique`, `specialite`, `Date_Naissance`, `email`, `telephone`, `Date_demande`, `cv`, `lettre_motivation`, `demande`, `periode`, `Id_utilisateur_id`, `password`) VALUES
(2, 'tahya', 'supnum', 'l2', 'dsi', '2011-05-04', 'tahya@gmail.com', '45678412', '2024-08-31 14:27:38.885570', '', '', 'Documents/demandes/Rapport_Stage_1_mN9z9jU.docx', 'deux moi', NULL, 'tahya'),
(3, 'lolo', 'sup', 'l1', 'dsi', '2001-07-06', 'lolo@gmail.com', '45678412', '2024-08-31 15:51:27.813342', '', '', 'Documents/demandes/Rapport_Stage_1_BuZ4SPT.docx', 'un moi', NULL, 'lolo'),
(4, 'chiva', 'institut', 'l1', 'dsi', '2001-07-06', 'chiva@gmail.com', '45678412', '2024-08-31 15:54:23.369404', '', '', 'Documents/demandes/Rapport_Stage_1_MKeje0q.docx', '2 moi', NULL, 'chiva');

-- --------------------------------------------------------

--
-- Structure de la table `stage_moov_demandes`
--

DROP TABLE IF EXISTS `stage_moov_demandes`;
CREATE TABLE IF NOT EXISTS `stage_moov_demandes` (
  `Id_demande` int(11) NOT NULL AUTO_INCREMENT,
  `Date_soumission` datetime(6) NOT NULL,
  `statut` varchar(50) NOT NULL,
  `Nom_candidat_id` int(11) NOT NULL,
  PRIMARY KEY (`Id_demande`),
  KEY `stage_moov_demandes_Id_candidat_id_25e41d56` (`Nom_candidat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `stage_moov_demandes`
--

INSERT INTO `stage_moov_demandes` (`Id_demande`, `Date_soumission`, `statut`, `Nom_candidat_id`) VALUES
(2, '2024-08-31 15:54:23.369404', 'rejete', 4);

-- --------------------------------------------------------

--
-- Structure de la table `stage_moov_document`
--

DROP TABLE IF EXISTS `stage_moov_document`;
CREATE TABLE IF NOT EXISTS `stage_moov_document` (
  `Id_document` int(11) NOT NULL AUTO_INCREMENT,
  `type_document` varchar(50) DEFAULT NULL,
  `chemin_document` varchar(50) NOT NULL,
  `Id_demande_id` int(11) NOT NULL,
  `candidat_id` int(11) NOT NULL,
  PRIMARY KEY (`Id_document`),
  KEY `stage_moov_document_Id_demande_id_df8e8df2` (`Id_demande_id`),
  KEY `stage_moov_document_candidat_id_22846470` (`candidat_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `stage_moov_evaluation`
--

DROP TABLE IF EXISTS `stage_moov_evaluation`;
CREATE TABLE IF NOT EXISTS `stage_moov_evaluation` (
  `Id_evaluation` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(50) NOT NULL,
  `user` varchar(20) NOT NULL,
  `files` varchar(100) NOT NULL,
  `date` datetime(6) NOT NULL,
  `room_id` int(11) NOT NULL,
  PRIMARY KEY (`Id_evaluation`),
  KEY `stage_moov_evaluation_room_id_43f2916e` (`room_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `stage_moov_notification`
--

DROP TABLE IF EXISTS `stage_moov_notification`;
CREATE TABLE IF NOT EXISTS `stage_moov_notification` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `message` longtext NOT NULL,
  `date_envoi` datetime(6) NOT NULL,
  `lu` tinyint(1) NOT NULL,
  `candidat_id` int(11) NOT NULL,
  `utilisateur_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `stage_moov_notification_candidat_id_29434c69` (`candidat_id`),
  KEY `stage_moov_notification_utilisateur_id_89f318dd` (`utilisateur_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `stage_moov_room`
--

DROP TABLE IF EXISTS `stage_moov_room`;
CREATE TABLE IF NOT EXISTS `stage_moov_room` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `stage_moov_service`
--

DROP TABLE IF EXISTS `stage_moov_service`;
CREATE TABLE IF NOT EXISTS `stage_moov_service` (
  `Id_service` int(11) NOT NULL AUTO_INCREMENT,
  `Nom_service` varchar(50) NOT NULL,
  `description` longtext DEFAULT NULL,
  PRIMARY KEY (`Id_service`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `stage_moov_sujet_stage`
--

DROP TABLE IF EXISTS `stage_moov_sujet_stage`;
CREATE TABLE IF NOT EXISTS `stage_moov_sujet_stage` (
  `Id_sujet` int(11) NOT NULL AUTO_INCREMENT,
  `titre` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  `Date_creation` datetime(6) NOT NULL,
  `Date_mise_a_jour` datetime(6) NOT NULL,
  `Id_service_id` int(11) NOT NULL,
  PRIMARY KEY (`Id_sujet`),
  KEY `stage_moov_sujet_stage_Id_service_id_542f8ecc` (`Id_service_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Structure de la table `stage_moov_utilisateur`
--

DROP TABLE IF EXISTS `stage_moov_utilisateur`;
CREATE TABLE IF NOT EXISTS `stage_moov_utilisateur` (
  `Id_utilisateur` int(11) NOT NULL AUTO_INCREMENT,
  `Nom_complet` varchar(50) NOT NULL,
  `Email` varchar(191) NOT NULL,
  `password` varchar(100) NOT NULL,
  `role` varchar(50) NOT NULL,
  `Date_creation` datetime(6) NOT NULL,
  PRIMARY KEY (`Id_utilisateur`),
  UNIQUE KEY `Email` (`Email`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
