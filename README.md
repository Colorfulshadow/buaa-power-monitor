# BUAA Power Monitor

![License](https://img.shields.io/github/license/colorfulshadow/buaa-power-monitor)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

北航电费监控工具，支持低电量提醒，可在 OpenWRT 路由器上运行。

## 功能特点

- 🔌 实时监控电量变化
- 📊 支持多种推送方式（Server酱、Telegram、邮件等）
- 🔄 系统服务化运行，自动重启
- 📝 完整的日志记录
- 💡 低电量智能提醒（可配置阈值和提醒间隔）

## 快速开始

### OpenWRT 环境

```bash
# 安装依赖
opkg update
opkg install python3 python3-pip
pip3 install requests beautifulsoup4

# 下载项目
cd /root
git clone https://github.com/colorfulshadow/buaa-power-monitor.git
cd buaa-power-monitor

# 安装服务
cp service/power_monitor /etc/init.d/power_monitor
chmod +x /etc/init.d/power_monitor
cp src/monitor.py /usr/bin/power_monitor.py
chmod +x /usr/bin/monitor.py

# 启动服务
/etc/init.d/power_monitor enable
/etc/init.d/power_monitor start
```

详细安装说明请参考 [install.md](docs/install.md)。

## 配置说明

主要配置项：
- 房间ID设置
- 检查间隔时间
- 提醒阈值
- 推送方式配置

详细配置说明请参考 [config.md](docs/config.md)。

## 推送示例

低电量提醒消息格式：
```
[电量低警告]
房间: 3公寓南楼-3-316
地址: 3公寓南楼-3-316[空调]
当前电量: 4度
```

## 项目结构

```
buaa-power-monitor/
├── README.md           # 项目说明
├── requirements.txt    # Python依赖
├── src/               # 源代码
│   └── monitor.py     # 主程序
├── service/           # 服务相关文件
│   └── power_monitor  # OpenWRT服务脚本
└── docs/             # 文档
    ├── install.md    # 安装指南
    └── config.md     # 配置说明
```

## 环境要求

- Python 3.8+
- OpenWRT 或其他 Linux 系统
- 必要的 Python 包（见 requirements.txt）

## 常见问题

1. 服务无法启动
   - 检查 Python 和依赖包是否正确安装
   - 检查服务脚本权限
   - 查看系统日志

2. 无法获取电量信息
   - 确认网络连接正常
   - 验证房间ID是否正确
   - 查看错误日志

更多问题请参考 [config.md](docs/config.md) 的故障排除部分。

## TODO

> TODO 是不可能to do的
- [ ] 添加更多推送渠道支持
- [ ] 添加电量使用统计功能
- [ ] 添加 Web 管理界面
- [ ] 支持多房间监控
- [ ] 添加电费消耗预测

## 贡献指南

欢迎提交 Issue 和 Pull Request。在提交 PR 之前，请确保：

1. 代码风格符合项目规范
2. 添加了必要的测试
3. 更新了相关文档

## 许可证

本项目使用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 致谢

感谢所有贡献者的帮助。

## 免责声明

本项目仅供学习交流使用，请勿用于任何商业用途。使用本项目造成的任何问题，开发者不承担任何责任。
