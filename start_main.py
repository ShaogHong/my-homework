from inquire_tools import Log_format_csv
from inquire_tools.tools2 import BaseAnalyzer, systems, browsers, robots


def safe_input(prompt):
    while True:
        try:
            return input(prompt)
        except Exception as e:
            print(f"错误: {e}")


def print_menu():
    print("[1]  格式化日志为csv(以下操作的前提)")
    print("[2]  ip统计排行")
    print("[3]  大洲统计排行")
    print("[4]  国家统计排行")
    print("[5]  城市统计排行")
    print("[6]  ip所有者统计排行")
    print("[7]  请求行统计排行")
    print("[8]  用户代理信息机器人统计")
    print("[9]  用户代理信息浏览器统计")
    print("[10] 用户代理信息系统统计")
    print("[11] 状态码统计")
    print("[a]  2-11全部统计")
    print("[q]退出")


def initialize_analyzer(log_filename):
    """按需初始化BaseAnalyzer实例"""
    return BaseAnalyzer(f"{log_filename}已处理.csv")


def process_choice(analyzer, choice):
    """根据用户选择执行相应操作"""
    actions = {
        "2": lambda: analyzer._count_and_save('ip', 'IP统计'),
        "3": lambda: analyzer._count_and_save('大洲', '大洲统计'),
        "4": lambda: analyzer._count_and_save('国家', '国家统计'),
        "5": lambda: analyzer._count_and_save('城市', '城市统计'),
        "6": lambda: analyzer._count_and_save('所有者', '所有者统计'),
        "7": lambda: analyzer._count_and_save('请求行', '请求行统计'),
        "8": lambda: analyzer._user_agent_analysis(robots, '机器人统计'),
        "9": lambda: analyzer._user_agent_analysis(browsers, '浏览器统计'),
        "10": lambda: analyzer._user_agent_analysis(systems, '系统统计'),
        "11": lambda: analyzer.plot_status_codes()
    }

    # if choice == "1":
    #     Log_format_csv.main(log_filename)
    if choice == "a":
        for act in actions.values():
            act()
    elif choice in actions:
        actions[choice]()
    else:
        print("无效选择")


print("""响应日志处理工具,感谢您的使用,希望能够帮到您!\n网址：https://zzhanzhang.top 作者：娄南湘先生""")
log_filename = safe_input("把日志文件拖过来:")

analyzer = None

while True:
    print_menu()
    choice = safe_input("选项编号：").lower()

    if choice == "q":
        break

    if choice == "1":
        Log_format_csv.main(log_filename)
        continue

    if analyzer is None:
        analyzer = initialize_analyzer(log_filename)

    try:
        process_choice(analyzer, choice)
    except Exception as e:
        print(f"错误: {e}")
        continue
