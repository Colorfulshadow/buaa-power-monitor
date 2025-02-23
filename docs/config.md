## 配置说明

### 基本配置项

在 `/usr/bin/power_monitor/monitor.py` 中可以修改以下配置：

```python
# 房间ID
room_id = "11111"  # 修改为你的房间ID

# 检查间隔（秒）
check_interval = 300  # 默认5分钟

# 提醒冷却时间（秒）
alert_cooldown = 3600  # 默认1小时

# 低电量阈值
LOW_POWER_THRESHOLD = 5  # 当电量低于该值时触发提醒
```

### 消息推送配置

在 `alert_low_power` 函数中配置推送方式，支持以下几种推送方式：

1. Server酱
```python
def alert_low_power(room_info):
    # Server酱推送
    send_key = "YOUR_SEND_KEY"
    url = f"https://sctapi.ftqq.com/{send_key}.send"
    title = f"电量低警告 - {room_info['room_name']}"
    desp = f"房间: {room_info['room_name']}\n地址: {room_info['address']}\n当前电量: {room_info['power']}度"
    requests.post(url, data={"title": title, "desp": desp})
```

2. Telegram Bot
```python
def alert_low_power(room_info):
    # Telegram Bot推送
    bot_token = "YOUR_BOT_TOKEN"
    chat_id = "YOUR_CHAT_ID"
    message = f"电量低警告\n房间: {room_info['room_name']}\n地址: {room_info['address']}\n当前电量: {room_info['power']}度"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": message})
```

3. 邮件推送
```python
def alert_low_power(room_info):
    # 邮件推送配置
    smtp_server = "smtp.example.com"
    smtp_port = 587
    sender_email = "your_email@example.com"
    receiver_email = "receiver@example.com"
    password = "your_password"
    
    message = f"""Subject: 电量低警告 - {room_info['room_name']}
    
    房间: {room_info['room_name']}
    地址: {room_info['address']}
    当前电量: {room_info['power']}度
    """
    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.encode('utf-8'))
```

4. Bark推送
```python
def alert_low_power(room_info,send_keys):
    # Bark推送配置
    message = (
        f"⚡ 电量低警告 ⚡\n"
        f"房间: {room_info['room_name']}\n"
        f"地址: {room_info['address']}\n"
        f"当前电量: {room_info['power']}度"
        f"自主购电: http://shsd.buaa.edu.cn/BuaaPay"
    )
    logger.warning(message)
    send_keys = ['']  # bark中的sendkey

    for send_key in send_keys:
        server_url = f'https://your_bark_server/{send_key}'
        payload = {
            'title': '低电量警告',
            'body': message,
            'icon': 'https://api.zty.ink/api/v2/objects/icon/icm5tt8b0caqz2hl4y.png',
            'group': '房间低电量提醒'
        }
        requests.post(server_url, data=payload)
```

### 日志配置

日志配置可以在脚本开头部分修改：

```python
# 日志文件路径
log_file = '/var/log/power_monitor.log'

# 日志级别设置
logger.setLevel(logging.INFO)  # 可选: DEBUG, INFO, WARNING, ERROR, CRITICAL

# 日志文件大小和保留数量
maxBytes = 1024*1024  # 单个日志文件最大1MB
backupCount = 5       # 保留5个备份文件
```

### 故障排除

1. 如果服务无法启动，检查：
   - Python和依赖包是否正确安装
   - 服务脚本权限是否正确
   - 日志文件权限是否正确

2. 如果无法获取电量信息，检查：
   - 网络连接是否正常
   - 房间ID是否正确
   - 查看错误日志获取详细信息

3. 如果推送消息失败，检查：
   - 推送服务配置是否正确
   - 网络连接是否正常
   - 相关token/key是否过期

如有其他问题，请查看日志文件或提交Issue获取帮助。