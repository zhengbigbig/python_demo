-- 数据表

CREATE TABLE `pagers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) NOT NULL DEFAULT '' COMMENT '论文标题',
  `url` varchar(200) NOT NULL DEFAULT '' COMMENT '论文URL',
  `authors` varchar(1000) NOT NULL DEFAULT '' COMMENT '论文作者',
  `create_time` int(11) NOT NULL DEFAULT 0 COMMENT '创建时间',
  `update_time` int(11) NOT NULL DEFAULT 0 COMMENT '更新时间',
  `is_deleted` tinyint(4) NOT NULL DEFAULT 0 COMMENT '是否已删除',
  PRIMARY KEY (`id`),
  KEY `title_IDX` (`title`) USING BTREE,
  KEY `authors_IDX` ('authors') USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='论文表'