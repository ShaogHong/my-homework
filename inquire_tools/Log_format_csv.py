import csv
import requests
import re
import time as tm
import sys

DEFAULT_API_URL = "https://qifu.baidu.com/ip/geo/v1/district?ip="


def query_ip_location(ip):
    url = DEFAULT_API_URL + ip
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data.get("code") == "Success":
                tm.sleep(0.07)
                return data["data"]
    except Exception as e:
        print(f"查询 IP 时出错 {ip}: {e}")
    return None


def parse_log_line(line):
    pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?\[(?P<time>.*?)\]\s*"(?P<method>\w+)\s*(?P<path>.*?)\s*(?P<protocol>.*?)"\s*(?P<status>\d+)\s*(?P<size>\d+)\s*"(?P<referrer>.*?)"\s*"(?P<user_agent>.*?)"'
    match = re.match(pattern, line)
    if match:
        groups = match.groupdict()
        ip = groups['ip']
        time = groups['time']
        method = groups['method']
        path = groups['protocol'].split()[0]
        protocol = groups['protocol'].split()[-1]
        status = groups['status']
        size = groups['size']
        referrer = groups['referrer']
        user_agent = groups['user_agent']

        return ip, time, method, path, protocol, status, size, referrer, user_agent
    return None


def write_to_csv(log_data, filename):
    headers = ["ip", "大洲", "国家", "城市", "城市编码", "经度", "纬度", "所有者", "运营商", "请求时间", "请求方法",
               "请求行", "请求的资源路径", "HTTP协议版本", "状态码", "响应大小", "引用页", "用户代理信息"]
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(log_data)


def row_count(file):
    line_count = sum(1 for _ in file)
    choice = input(
        f"该日志共有{line_count}行，任意键全部处理, 或输入数字从指定行开始处理: ")
    if choice.isdigit():
        start_line = int(choice)
        file.seek(0)
        for _ in range(start_line):
            next(file)
    else:
        file.seek(0)


def main(log_filename):
    # log_filename = input("把日志文件拖过来：")
    ip_locations = {}
    log_data = []
    insert_values = []
    query_ip_yesOrno = input("是否启用ip查询?(y/n): ").lower()
    start_time = tm.time()
    if query_ip_yesOrno != 'y':
        with open(log_filename, mode='r', encoding='utf-8') as file:
            row_count(file)
            loading_symbols = ['| ', '- ', '/ ', '\\ ']
            loading_index = 0

            for idx, line in enumerate(file):
                parsed_line = parse_log_line(line)
                if parsed_line:
                    ip, time, method, path, xie_yi, status, size, referrer, user_agent = parsed_line

                    entry = [
                        ip,
                        "null",
                        "null",
                        "null",
                        "null",
                        "null",
                        "null",
                        "null",
                        "null",
                        time,
                        method,
                        f"{method} {path} {xie_yi}",
                        path,
                        xie_yi,
                        status,
                        size,
                        referrer,
                        user_agent
                    ]
                    insert_values.append(entry)

                sys.stdout.write(f"\r格式化中 {loading_symbols[loading_index]}")
                loading_index = (loading_index + 1) % len(loading_symbols)
                sys.stdout.flush()
                if len(insert_values) == 100:
                    log_data.extend(insert_values)
                    insert_values = []

            if len(insert_values) > 0:
                log_data.extend(insert_values)

        write_to_csv(log_data, f"{log_filename}已处理.csv")

    else:
        with open(log_filename, mode='r', encoding='utf-8') as file:
            row_count(file)
            loading_symbols = ['| ', '- ', '/ ', '\\ ']
            loading_index = 0
            for idx, line in enumerate(file):
                parsed_line = parse_log_line(line)
                if parsed_line:
                    ip, time, method, path, xie_yi, status, size, referrer, user_agent = parsed_line
                    if ip not in ip_locations:
                        ip_location = query_ip_location(ip)
                        if ip_location:
                            ip_locations[ip] = ip_location
                    else:
                        ip_location = ip_locations[ip]

                    if ip_location:
                        entry = [
                            ip,
                            ip_location.get("continent", "null"),
                            ip_location.get("country", "null"),
                            ip_location.get("city", "null"),
                            ip_location.get("areacode", "null"),
                            ip_location.get("lng", "null"),
                            ip_location.get("lat", "null"),
                            ip_location.get("owner", "null"),
                            ip_location.get("isp", "null"),
                            time,
                            method,
                            f"{method} {path} {xie_yi}",
                            path,
                            xie_yi,
                            status,
                            size,
                            referrer,
                            user_agent
                        ]
                        insert_values.append(entry)

                sys.stdout.write(f"\r格式化中 {loading_symbols[loading_index]}")
                loading_index = (loading_index + 1) % len(loading_symbols)
                sys.stdout.flush()

                if len(insert_values) == 100:
                    log_data.extend(insert_values)
                    insert_values = []

            if len(insert_values) > 0:
                log_data.extend(insert_values)

    write_to_csv(log_data, f"{log_filename}已处理.csv")
    end_time = tm.time()
    print(f"\nIP属地查询完成，日志格式化完成，TIME: {end_time - start_time:.1f}S，文件保存在{log_filename}已处理.csv")


# if __name__ == "__main__":
#     main()
