"""
@Author: Tianyi Zhang
@Date: 2025/2/23
@Description: 北航电表监控
"""
import requests
from bs4 import BeautifulSoup
import time
import logging
import sys
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file = '/var/log/power_monitor.log'
log_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
log_handler.setFormatter(log_formatter)

logger = logging.getLogger('PowerMonitor')
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)


def get_room_info(id):
    """获取房间信息和电量信息"""
    url = f"http://shsd.buaa.edu.cn/PubBuaa?id={id}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        # 获取电量
        power_text = soup.find('tspan').text.strip()
        power = int(power_text)

        # 获取房间信息
        info_div = soup.find('div', style="float: left; margin-top: 20px;")
        if info_div:
            room_name = info_div.find('p', class_="shadow", style=lambda x: x and "font-size: 20px;" in x)
            room_name = room_name.text.strip() if room_name else "未知房间"
            address = info_div.find_all('p', class_="shadow")[-1]
            address = address.text.replace('地址:', '').strip() if address else "未知地址"
        else:
            room_name = "未知房间"
            address = "未知地址"

        return {
            'power': power,
            'room_name': room_name,
            'address': address
        }
    except Exception as e:
        logger.error(f"获取房间信息失败: {str(e)}")
        return None


def alert_low_power(room_info):
    """
    低电量提醒
    可以通过以下方式实现提醒：
    1. 使用 pushplus 推送
    2. 使用 telegram bot
    3. 发送邮件
    4. 调用其他推送服务
    """

def main():
    room_id = "11111"
    check_interval = 300  # 检查间隔（秒）
    alert_cooldown = 43200  # 提醒冷却时间（秒）
    last_alert_time = 0

    logger.info("电量监控服务启动")

    while True:
        try:
            room_info = get_room_info(room_id)
            if room_info is not None:
                logger.info(f"当前电量: {room_info['power']} ({room_info['room_name']})")

                current_time = time.time()
                if room_info['power'] < 5 and (current_time - last_alert_time) >= alert_cooldown:
                    alert_low_power(room_info)
                    last_alert_time = current_time

            time.sleep(check_interval)
        except Exception as e:
            logger.error(f"发生错误: {str(e)}")
            time.sleep(60)


if __name__ == "__main__":
    main()