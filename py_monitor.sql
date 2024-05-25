/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80012
 Source Host           : localhost:3306
 Source Schema         : py_monitor

 Target Server Type    : MySQL
 Target Server Version : 80012
 File Encoding         : 65001

 Date: 26/05/2024 01:31:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissions_group_id_b120cbf9`(`group_id`) USING BTREE,
  INDEX `auth_group_permissions_permission_id_84c5c92e`(`permission_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  INDEX `auth_permission_content_type_id_2f476e4b`(`content_type_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 65 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add log', 7, 'add_log');
INSERT INTO `auth_permission` VALUES (26, 'Can change log', 7, 'change_log');
INSERT INTO `auth_permission` VALUES (27, 'Can delete log', 7, 'delete_log');
INSERT INTO `auth_permission` VALUES (28, 'Can view log', 7, 'view_log');
INSERT INTO `auth_permission` VALUES (29, 'Can add logo', 8, 'add_logo');
INSERT INTO `auth_permission` VALUES (30, 'Can change logo', 8, 'change_logo');
INSERT INTO `auth_permission` VALUES (31, 'Can delete logo', 8, 'delete_logo');
INSERT INTO `auth_permission` VALUES (32, 'Can view logo', 8, 'view_logo');
INSERT INTO `auth_permission` VALUES (33, 'Can add handle', 9, 'add_handle');
INSERT INTO `auth_permission` VALUES (34, 'Can change handle', 9, 'change_handle');
INSERT INTO `auth_permission` VALUES (35, 'Can delete handle', 9, 'delete_handle');
INSERT INTO `auth_permission` VALUES (36, 'Can view handle', 9, 'view_handle');
INSERT INTO `auth_permission` VALUES (37, 'Can add monitor', 10, 'add_monitor');
INSERT INTO `auth_permission` VALUES (38, 'Can change monitor', 10, 'change_monitor');
INSERT INTO `auth_permission` VALUES (39, 'Can delete monitor', 10, 'delete_monitor');
INSERT INTO `auth_permission` VALUES (40, 'Can view monitor', 10, 'view_monitor');
INSERT INTO `auth_permission` VALUES (41, 'Can add notify', 11, 'add_notify');
INSERT INTO `auth_permission` VALUES (42, 'Can change notify', 11, 'change_notify');
INSERT INTO `auth_permission` VALUES (43, 'Can delete notify', 11, 'delete_notify');
INSERT INTO `auth_permission` VALUES (44, 'Can view notify', 11, 'view_notify');
INSERT INTO `auth_permission` VALUES (45, 'Can add sub email', 12, 'add_subemail');
INSERT INTO `auth_permission` VALUES (46, 'Can change sub email', 12, 'change_subemail');
INSERT INTO `auth_permission` VALUES (47, 'Can delete sub email', 12, 'delete_subemail');
INSERT INTO `auth_permission` VALUES (48, 'Can view sub email', 12, 'view_subemail');
INSERT INTO `auth_permission` VALUES (49, 'Can add power', 13, 'add_power');
INSERT INTO `auth_permission` VALUES (50, 'Can change power', 13, 'change_power');
INSERT INTO `auth_permission` VALUES (51, 'Can delete power', 13, 'delete_power');
INSERT INTO `auth_permission` VALUES (52, 'Can view power', 13, 'view_power');
INSERT INTO `auth_permission` VALUES (53, 'Can add role', 14, 'add_role');
INSERT INTO `auth_permission` VALUES (54, 'Can change role', 14, 'change_role');
INSERT INTO `auth_permission` VALUES (55, 'Can delete role', 14, 'delete_role');
INSERT INTO `auth_permission` VALUES (56, 'Can view role', 14, 'view_role');
INSERT INTO `auth_permission` VALUES (57, 'Can add role power', 15, 'add_rolepower');
INSERT INTO `auth_permission` VALUES (58, 'Can change role power', 15, 'change_rolepower');
INSERT INTO `auth_permission` VALUES (59, 'Can delete role power', 15, 'delete_rolepower');
INSERT INTO `auth_permission` VALUES (60, 'Can view role power', 15, 'view_rolepower');
INSERT INTO `auth_permission` VALUES (61, 'Can add user', 16, 'add_user');
INSERT INTO `auth_permission` VALUES (62, 'Can change user', 16, 'change_user');
INSERT INTO `auth_permission` VALUES (63, 'Can delete user', 16, 'delete_user');
INSERT INTO `auth_permission` VALUES (64, 'Can view user', 16, 'view_user');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_user_id_6a12ed8b`(`user_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544`(`group_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permissions_user_id_a95ead1b`(`user_id`) USING BTREE,
  INDEX `auth_user_user_permissions_permission_id_1fbb5f2c`(`permission_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6`(`user_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (7, 'login', 'log');
INSERT INTO `django_content_type` VALUES (8, 'login', 'logo');
INSERT INTO `django_content_type` VALUES (9, 'monitor', 'handle');
INSERT INTO `django_content_type` VALUES (10, 'monitor', 'monitor');
INSERT INTO `django_content_type` VALUES (11, 'monitor', 'notify');
INSERT INTO `django_content_type` VALUES (12, 'monitor', 'subemail');
INSERT INTO `django_content_type` VALUES (13, 'manage', 'power');
INSERT INTO `django_content_type` VALUES (14, 'manage', 'role');
INSERT INTO `django_content_type` VALUES (15, 'manage', 'rolepower');
INSERT INTO `django_content_type` VALUES (16, 'manage', 'user');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 22 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2024-05-26 01:30:18.547679');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2024-05-26 01:30:19.248206');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2024-05-26 01:30:19.398745');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2024-05-26 01:30:19.405307');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2024-05-26 01:30:19.411745');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2024-05-26 01:30:19.479953');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2024-05-26 01:30:19.526731');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2024-05-26 01:30:19.585533');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2024-05-26 01:30:19.592595');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2024-05-26 01:30:19.648219');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2024-05-26 01:30:19.651091');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2024-05-26 01:30:19.685747');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2024-05-26 01:30:19.730856');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2024-05-26 01:30:19.778255');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2024-05-26 01:30:19.834627');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2024-05-26 01:30:19.842041');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2024-05-26 01:30:19.897523');
INSERT INTO `django_migrations` VALUES (18, 'login', '0001_initial', '2024-05-26 01:30:19.929898');
INSERT INTO `django_migrations` VALUES (19, 'manage', '0001_initial', '2024-05-26 01:30:19.991091');
INSERT INTO `django_migrations` VALUES (20, 'monitor', '0001_initial', '2024-05-26 01:30:20.052472');
INSERT INTO `django_migrations` VALUES (21, 'sessions', '0001_initial', '2024-05-26 01:30:20.102564');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('z41ked98vf2rq3h2wipnug6x09otaqdi', '.eJx1UEtOwzAQvYvXAUJpKcqq96AomnSGYskeu_6IVoi7M3GcpBs20ft6nvKjTg5JdZyNaVQfKUbtuKer1-Gmuv2mbRuVI4Veo-oUoNWsqsJg6U4LzlBJbSpGimIf836AZ_lu29dj3m13b5IdYy-NQvIQkiVO_wW9izrJIvGFkQVt5pOHy-Xx5OwYomB1GS4H38u4BwsMZ6qzVubd971p3HklY68DxBkiGUqLUd7JHmGViGEw843aLHBpFlZuzmTpFLWWJry0JrokZeTqsUv68ybAOtbJhSfNSFfhX8A4jaEo-ohiHvrpl338_gHFRKMq:1sAvEZ:ib9DN9zSC38w-gSgf_SQlyQZOh7VLSH9J-I1tZ9OsAE', '2024-05-26 03:31:07.978229');

-- ----------------------------
-- Table structure for monitor_handle
-- ----------------------------
DROP TABLE IF EXISTS `monitor_handle`;
CREATE TABLE `monitor_handle`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `request_time` datetime(6) NOT NULL,
  `request_method` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `request_path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `response_status` int(11) NOT NULL,
  `response_time` double NOT NULL,
  `disposal_time` datetime(6) NOT NULL,
  `source_ip` char(39) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `attack_type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `details` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `auto_handled` tinyint(1) NOT NULL,
  `handled_status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `handled_action` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `handled_details` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `filename` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `status` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_restore` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of monitor_handle
-- ----------------------------
INSERT INTO `monitor_handle` VALUES (12, '0000-00-00 00:00:00.000000', '12', '', 12, 0, '0000-00-00 00:00:00.000000', '12', '12', '12', 0, '12', '', '', '', '0000-00-00 00:00:00.000000', '', 0);
INSERT INTO `monitor_handle` VALUES (13, '2024-05-25 16:24:56.000000', '23', '23', 0, 0, '0000-00-00 00:00:00.000000', '', '', '', 0, '', '', '', '', '0000-00-00 00:00:00.000000', '', 0);
INSERT INTO `monitor_handle` VALUES (14, '0000-00-00 00:00:00.000000', '23', '23', 0, 0, '0000-00-00 00:00:00.000000', '', '', '', 0, '', '', '', '', '0000-00-00 00:00:00.000000', '', 0);

-- ----------------------------
-- Table structure for monitor_monitor
-- ----------------------------
DROP TABLE IF EXISTS `monitor_monitor`;
CREATE TABLE `monitor_monitor`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `request_url` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `request_method` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `request_data` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `request_ip` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `attack_type` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `attack_time` datetime(6) NOT NULL,
  `description` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of monitor_monitor
-- ----------------------------

-- ----------------------------
-- Table structure for monitor_notify
-- ----------------------------
DROP TABLE IF EXISTS `monitor_notify`;
CREATE TABLE `monitor_notify`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `notify_type` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `notify_mail` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `notify_subject` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `notify_content` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `notify_time` datetime(6) NOT NULL,
  `notify_status` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of monitor_notify
-- ----------------------------
INSERT INTO `monitor_notify` VALUES (11, '2', '12', '12', '1', '1024-05-25 15:12:24.000000', '');
INSERT INTO `monitor_notify` VALUES (12, '12', '12', '12', '12', '0000-00-00 00:00:00.000000', '');

-- ----------------------------
-- Table structure for monitor_subemail
-- ----------------------------
DROP TABLE IF EXISTS `monitor_subemail`;
CREATE TABLE `monitor_subemail`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `sub_email` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `sub_status` int(11) NOT NULL,
  `sub_date` date NOT NULL,
  `sub_name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_id` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of monitor_subemail
-- ----------------------------
INSERT INTO `monitor_subemail` VALUES (1, '1212', 1, '2024-05-25', 'admin', '');
INSERT INTO `monitor_subemail` VALUES (2, '1212', 1, '2024-05-25', 'admin', '1');
INSERT INTO `monitor_subemail` VALUES (3, '3173484026@qq.com', 1, '2024-05-25', '张三', '1');
INSERT INTO `monitor_subemail` VALUES (5, '323', 1, '2024-05-25', '1212', '1');
INSERT INTO `monitor_subemail` VALUES (6, '1212', 1, '2024-05-25', 'admin', '1');

-- ----------------------------
-- Table structure for role_power
-- ----------------------------
DROP TABLE IF EXISTS `role_power`;
CREATE TABLE `role_power`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `power_id` int(11) NOT NULL,
  `power_type` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Fixed;

-- ----------------------------
-- Records of role_power
-- ----------------------------
INSERT INTO `role_power` VALUES (2, 2, 7, 0);
INSERT INTO `role_power` VALUES (3, 2, 8, 1);
INSERT INTO `role_power` VALUES (4, 2, 9, 1);
INSERT INTO `role_power` VALUES (5, 2, 10, 1);
INSERT INTO `role_power` VALUES (7, 2, 12, 1);
INSERT INTO `role_power` VALUES (8, 2, 13, 2);
INSERT INTO `role_power` VALUES (9, 2, 14, 2);
INSERT INTO `role_power` VALUES (10, 2, 15, 2);
INSERT INTO `role_power` VALUES (12, 2, 17, 3);
INSERT INTO `role_power` VALUES (13, 2, 18, 2);
INSERT INTO `role_power` VALUES (14, 2, 19, 2);
INSERT INTO `role_power` VALUES (15, 2, 20, 2);
INSERT INTO `role_power` VALUES (16, 2, 21, 2);
INSERT INTO `role_power` VALUES (17, 2, 22, 2);
INSERT INTO `role_power` VALUES (18, 2, 23, 2);
INSERT INTO `role_power` VALUES (19, 2, 24, 3);
INSERT INTO `role_power` VALUES (50, 2, 25, 2);
INSERT INTO `role_power` VALUES (62, 1, 7, 0);
INSERT INTO `role_power` VALUES (63, 1, 8, 1);
INSERT INTO `role_power` VALUES (64, 1, 9, 1);
INSERT INTO `role_power` VALUES (65, 1, 13, 2);
INSERT INTO `role_power` VALUES (66, 1, 17, 2);
INSERT INTO `role_power` VALUES (67, 1, 18, 2);
INSERT INTO `role_power` VALUES (68, 1, 21, 2);
INSERT INTO `role_power` VALUES (213, 2, 49, 0);
INSERT INTO `role_power` VALUES (214, 2, 50, 0);
INSERT INTO `role_power` VALUES (215, 2, 51, 0);
INSERT INTO `role_power` VALUES (216, 2, 52, 0);
INSERT INTO `role_power` VALUES (217, 2, 53, 1);
INSERT INTO `role_power` VALUES (218, 2, 54, 1);
INSERT INTO `role_power` VALUES (219, 2, 55, 1);
INSERT INTO `role_power` VALUES (221, 2, 57, 1);
INSERT INTO `role_power` VALUES (222, 2, 58, 1);

-- ----------------------------
-- Table structure for sys_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_log`;
CREATE TABLE `sys_log`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `method` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `uid` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `url` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `desc` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL,
  `ip` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `success` int(11) NULL DEFAULT NULL,
  `user_agent` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_log
-- ----------------------------
INSERT INTO `sys_log` VALUES (1, 'POST', 'admin', '/login', '登录成功', '127.0.0.1', 1, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0', '2024-05-26 01:31:07.966509');

-- ----------------------------
-- Table structure for sys_power
-- ----------------------------
DROP TABLE IF EXISTS `sys_power`;
CREATE TABLE `sys_power`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `type` int(11) NOT NULL,
  `code` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `url` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `open_type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `parent_id` int(11) NULL DEFAULT NULL,
  `icon` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `sort` int(11) NULL DEFAULT NULL,
  `enable` int(11) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_power
-- ----------------------------
INSERT INTO `sys_power` VALUES (7, '系统管理', 0, '', NULL, '目录', 0, 'fa fa-gears', 1, 1, '2022-08-21 13:40:46.984340', '2022-08-21 13:40:46.984340');
INSERT INTO `sys_power` VALUES (8, '用户管理', 1, 'user-manage', NULL, '菜单', 7, 'fa fa-user', 1, 1, '2022-08-21 13:41:42.752289', '2022-08-21 13:41:42.753292');
INSERT INTO `sys_power` VALUES (9, '角色管理', 1, 'role-manage', NULL, '菜单', 7, 'fa fa-user-plus', 2, 1, '2022-08-21 13:42:15.823357', '2022-08-21 13:42:15.823357');
INSERT INTO `sys_power` VALUES (10, '权限管理', 1, 'power-manage', NULL, '菜单', 7, 'fa fa-key', 3, 1, '2022-08-21 13:42:49.405794', '2022-08-21 13:42:49.405794');
INSERT INTO `sys_power` VALUES (12, '日志管理', 1, 'log-manage', NULL, '菜单', 7, 'fa fa-bars', 4, 1, '2022-08-21 13:47:53.760215', '2022-08-21 13:47:53.760215');
INSERT INTO `sys_power` VALUES (13, '用户新增', 2, 'user:add', NULL, '按钮', 8, '', 1, 1, '2022-08-21 14:21:40.243014', '2022-08-21 14:21:40.243014');
INSERT INTO `sys_power` VALUES (14, '用户删除', 2, 'user:delete', NULL, '按钮', 8, '', 2, 1, '2022-08-22 00:02:22.548888', '2022-08-22 00:02:22.548888');
INSERT INTO `sys_power` VALUES (15, '角色更新', 2, 'user:role-update', NULL, '按钮', 8, '', 3, 1, '2022-08-22 00:03:44.909199', '2022-08-22 00:03:44.909199');
INSERT INTO `sys_power` VALUES (17, '禁用启用', 3, 'user:enable', NULL, '其他', 8, '', 4, 1, '2022-08-22 00:15:49.725357', '2022-08-22 00:15:49.725357');
INSERT INTO `sys_power` VALUES (18, '角色新增', 2, 'role:add', NULL, '按钮', 9, '', 1, 1, '2022-08-22 00:23:52.949521', '2022-08-22 00:23:52.949521');
INSERT INTO `sys_power` VALUES (19, '角色删除', 2, 'role:delete', NULL, '按钮', 9, '', 2, 1, '2022-08-22 00:24:32.076893', '2022-08-22 00:24:32.076893');
INSERT INTO `sys_power` VALUES (20, '角色权限', 2, 'role:power', NULL, '按钮', 9, '', 3, 1, '2022-08-22 00:25:05.360926', '2022-08-22 00:25:05.361931');
INSERT INTO `sys_power` VALUES (21, '禁用启用', 2, 'role:enable', NULL, '按钮', 9, '', 4, 1, '2022-08-22 00:25:31.890194', '2022-08-22 00:25:31.890194');
INSERT INTO `sys_power` VALUES (22, '权限新增', 2, 'power:add', NULL, '按钮', 10, '', 1, 1, '2022-08-22 00:26:06.919411', '2022-08-22 00:26:06.919411');
INSERT INTO `sys_power` VALUES (23, '权限删除', 2, 'power:delete', NULL, '按钮', 10, '', 2, 1, '2022-08-22 00:26:37.276269', '2022-08-22 00:26:37.276269');
INSERT INTO `sys_power` VALUES (24, '禁用启用', 3, 'power:enable', NULL, '其他', 10, '', 3, 1, '2022-08-22 00:27:07.237696', '2022-08-22 00:27:07.237696');
INSERT INTO `sys_power` VALUES (25, '日志删除', 2, 'log:delete', NULL, '按钮', 12, '', 1, 1, '2022-08-24 11:33:45.484369', '2022-08-24 11:33:45.484369');
INSERT INTO `sys_power` VALUES (49, '事件监控预警', 0, '', NULL, '目录', 0, 'fa fa-gears', 0, 1, '2024-05-23 00:18:51.627776', '2024-05-23 00:18:51.627776');
INSERT INTO `sys_power` VALUES (50, '安全事件通报', 0, '', NULL, '目录', 0, 'fa fa-gears', 0, 1, '2024-05-23 00:18:51.998288', '2024-05-23 00:18:51.998288');
INSERT INTO `sys_power` VALUES (51, '应急响应处置', 0, '', NULL, '目录', 0, 'fa fa-gears', 0, 1, '2024-05-23 00:19:48.832055', '2024-05-23 00:19:48.832055');
INSERT INTO `sys_power` VALUES (52, '数据业务恢复', 0, '', NULL, '目录', 0, 'fa fa-gears', 0, 1, '2024-05-23 00:20:02.743667', '2024-05-23 00:20:02.744663');
INSERT INTO `sys_power` VALUES (53, '事件通报', 1, 'notify', NULL, '菜单', 50, 'fa fa-key', 0, 1, '2024-05-23 00:23:20.760048', '2024-05-23 00:23:20.760048');
INSERT INTO `sys_power` VALUES (54, '监控预警', 1, 'monitor/index', NULL, '菜单', 49, 'fa fa-key', 0, 1, '2024-05-23 00:24:13.562931', '2024-05-23 00:24:13.562931');
INSERT INTO `sys_power` VALUES (55, '应急处置', 1, 'handle', NULL, '菜单', 51, 'fa fa-key', 0, 1, '2024-05-23 00:24:31.286547', '2024-05-23 00:24:31.286547');
INSERT INTO `sys_power` VALUES (57, '业务恢复', 1, 'restore', NULL, '菜单', 52, 'fa fa-key', 0, 1, '2024-05-23 00:25:17.859708', '2024-05-23 00:25:17.859708');
INSERT INTO `sys_power` VALUES (58, '订阅列表', 1, 'sub_email', NULL, '菜单', 50, 'fa fa-key', 0, 1, '2024-05-25 00:11:16.112418', '2024-05-25 00:11:16.112418');

-- ----------------------------
-- Table structure for sys_role
-- ----------------------------
DROP TABLE IF EXISTS `sys_role`;
CREATE TABLE `sys_role`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `role_value` int(11) NOT NULL,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `code` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `enable` int(11) NOT NULL,
  `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `details` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `sort` int(11) NULL DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  `update_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_role
-- ----------------------------
INSERT INTO `sys_role` VALUES (1, 1, '普通用户', 'user', 1, '普通用户权限', NULL, NULL, '2022-08-16 23:14:27.974460', '2022-08-16 23:14:27.974460');
INSERT INTO `sys_role` VALUES (2, 2, '管理员', 'admin', 1, '系统所有权限', NULL, NULL, '2022-08-16 23:15:44.201017', '2022-08-16 23:15:44.201017');

-- ----------------------------
-- Table structure for sys_user
-- ----------------------------
DROP TABLE IF EXISTS `sys_user`;
CREATE TABLE `sys_user`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_number` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `id_password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `user_name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `department` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `position` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `role_id` int(11) NULL DEFAULT NULL,
  `role_des` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `user_status` int(11) NOT NULL,
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sys_user
-- ----------------------------
INSERT INTO `sys_user` VALUES (3, 'admin', 'pbkdf2_sha256$390000$GJVtb3oqScLoOCEk0UQq3v$QECN33IghfBLwPuCZiv7AidqRIaFa6NsQCXRN9nthi0=', 'admin', '管理员', '', 2, '管理员', 1, 'admin@qq.com', '2022-08-21 06:07:55.145119');

-- ----------------------------
-- Table structure for web_logo
-- ----------------------------
DROP TABLE IF EXISTS `web_logo`;
CREATE TABLE `web_logo`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `desc` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `type` int(11) NULL DEFAULT NULL,
  `url` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `parent_id` int(11) NULL DEFAULT NULL,
  `icon` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `sort` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of web_logo
-- ----------------------------
INSERT INTO `web_logo` VALUES (1, '首页', 'homeInfo-title', 0, '/home', 1, NULL, 1);
INSERT INTO `web_logo` VALUES (2, '网络安全事件应急响应与处置系统', 'logoInfo-title', 1, '', 2, 'static/images/logo1.png', 1);
INSERT INTO `web_logo` VALUES (3, '网络安全事件应急响应与处置系统', 'menuInfo-title', 2, '', 3, 'fa fa-address-book', 1);

SET FOREIGN_KEY_CHECKS = 1;
