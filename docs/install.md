# install.md

## 安装指南

### OpenWRT 环境安装

1. 安装必要的包
```bash
opkg update
opkg install python3 python3-pip
pip3 install requests beautifulsoup4
```

2. 下载项目
```bash
cd /root
git clone https://github.com/colorfulshadow/buaa-power-monitor.git
cd buaa-power-monitor
```

3. 复制服务文件和程序
```bash
# 复制服务启动脚本
cp service/power_monitor /etc/init.d/power_monitor
chmod +x /etc/init.d/power_monitor

# 复制主程序
mkdir -p /usr/bin/power_monitor
cp src/monitor.py /usr/bin/power_monitor/
chmod +x /usr/bin/power_monitor/monitor.py
```

4. 启用服务
```bash
# 启用开机自启
/etc/init.d/power_monitor enable

# 启动服务
/etc/init.d/power_monitor start
```

### Windows 环境安装（用于开发测试）

1. 安装 Python 3.8+
2. 克隆项目
```bash
git clone https://github.com/your-username/buaa-power-monitor.git
cd buaa-power-monitor
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 运行测试
```bash
python src/monitor.py
```

## 服务管理

### OpenWRT 服务命令
```bash
# 启动服务
/etc/init.d/power_monitor start

# 停止服务
/etc/init.d/power_monitor stop

# 重启服务
/etc/init.d/power_monitor restart

# 查看服务状态
service power_monitor status
```

### 日志查看
```bash
# 查看实时日志
tail -f /var/log/power_monitor.log

# 查看最近100行日志
tail -n 100 /var/log/power_monitor.log
```
