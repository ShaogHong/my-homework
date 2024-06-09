import pandas as pd
from matplotlib import pyplot as plt

"""
重复造车轮,没用到也没什么好看的，单纯凑代码量完成作业罢了
真正的处理逻辑在tools2.py和Log_format_csv.py中

"""


def cont_count(csv_file):
    df = pd.read_csv(csv_file)
    continent_counts = df['大洲'].value_counts().reset_index()
    continent_counts.columns = ['大洲', '数量']
    total_continents = continent_counts['数量'].sum()
    continent_counts['百分比'] = continent_counts['数量'].apply(lambda x: round((x / total_continents) * 100, 2))
    continent_counts.sort_values(by='数量', ascending=False, inplace=True)
    continent_counts = continent_counts[['大洲', '数量', '百分比']]
    continent_counts.to_csv(f"{csv_file} 大洲统计.csv", index=False)
    print(f"统计完成，结果已保存至{csv_file} 大洲统计.csv")


def ip_count(csv_file):
    df = pd.read_csv(csv_file)
    ip_counts = df['ip'].value_counts().reset_index()
    ip_counts.columns = ['ip', '数量']
    merged_df = df.merge(ip_counts, on='ip', how='left')
    grouped_df = merged_df.groupby(['ip', '大洲', '国家', '城市', '所有者'])[['数量']].sum().reset_index()
    total_count = grouped_df['数量'].sum()
    grouped_df['百分比'] = grouped_df['数量'].apply(lambda x: round((x / total_count) * 100, 2))
    grouped_df.sort_values(by='数量', ascending=False, inplace=True)
    grouped_df.reset_index(drop=True, inplace=True)
    grouped_df['排名'] = grouped_df.index + 1
    grouped_df = grouped_df[['排名', 'ip', '国家', '城市', '所有者', '数量', '百分比']]
    grouped_df.to_csv(f'{csv_file} IP统计.csv', index=False)
    print(f"统计完成，结果已保存至{csv_file} IP统计.csv")


def country_count(csv_file):
    df = pd.read_csv(csv_file)
    country_counts = df['国家'].value_counts().reset_index()
    country_counts.columns = ['国家', '数量']
    total_countries = country_counts['数量'].sum()
    country_counts['百分比'] = country_counts['数量'].apply(lambda x: round((x / total_countries) * 100, 2))
    country_counts['排名'] = country_counts.index + 1
    country_counts.sort_values(by='数量', ascending=False, inplace=True)
    country_counts = country_counts[['排名', '国家', '数量', '百分比']]
    country_counts.to_csv(f"{csv_file} 国家统计.csv", index=False)
    print(f"统计完成，结果已保存至{csv_file} 国家统计.csv")


def city_count(csv_file):
    df = pd.read_csv(csv_file)
    city_counts = df['城市'].value_counts().reset_index()
    city_counts.columns = ['城市', '数量']
    total_city = city_counts['数量'].sum()
    city_counts['百分比'] = city_counts['数量'].apply(lambda x: round((x / total_city) * 100, 2))
    city_counts['排名'] = range(1, len(city_counts) + 1)
    city_counts.sort_values(by='数量', ascending=False, inplace=True)
    city_counts = city_counts[['排名', '城市', '数量', '百分比']]
    city_counts.to_csv(f"{csv_file}_城市统计.csv", index=False)
    print(f"统计完成，结果已保存至{csv_file} 城市统计.csv")


def owner_count(csv_file):
    df = pd.read_csv(csv_file)
    owner_counts = df['所有者'].value_counts().reset_index()
    owner_counts.columns = ['所有者', '数量']
    total_owners = owner_counts['数量'].sum()
    owner_counts['百分比'] = owner_counts['数量'].apply(lambda x: round((x / total_owners) * 100, 2))
    owner_counts['排名'] = range(1, len(owner_counts) + 1)
    owner_counts.sort_values(by='数量', ascending=False, inplace=True)
    owner_counts = owner_counts[['排名', '所有者', '数量', '百分比']]
    owner_counts.to_csv(f"{csv_file}_所有者统计.csv", index=False)
    print(f"统计完成，结果已保存至{csv_file} 所有者统计.csv")


def request_lint_count(csv_file):
    df = pd.read_csv(csv_file)
    request_counts = df['请求行'].value_counts().reset_index()
    request_counts.columns = ['请求行', '数量']
    total_request = request_counts['数量'].sum()
    request_counts['百分比'] = request_counts['数量'].apply(lambda x: round((x / total_request) * 100, 2))
    request_counts['排名'] = range(1, len(request_counts) + 1)
    request_counts.sort_values(by='数量', ascending=False, inplace=True)
    request_counts = request_counts[['排名', '请求行', '数量', '百分比']]
    request_counts.to_csv(f"{csv_file}_请求行统计.csv", index=False)
    print(f"统计完成，结果已保存至{csv_file} 请求行统计.csv")


def user_agent_bot_count(csv_file):
    robots = [
        "Googlebot", "Bingbot", "Yahoo", "Slurp", "Baiduspider", "YandexBot", "DuckDuckBot",
        "Sogou web spider", "Exabot", "FacebookBot", "Twitterbot", "LinkedInBot", "Pinterestbot",
        "Applebot", "MJ12bot", "AhrefsBot", "SemrushBot", "RamblerBot", "DotBot", "BingPreview",
        "YandexImages", "Screaming Frog SEO Spider", "SeznamBot", "Embedly", "Slackbot", "TelegramBot",
        "WhatsApp", "Discordbot", "360Spider", "MSNBOT", "NaverBot", "Gigabot", "YandexMobileBot",
        "FacebookExternalHit", "Pinterest", "Ask Jeeves/Teoma", "Alexa Crawler",
        "YodaoBot", "ia_archiver",
        "CoccocBot", "Vsekorakhiver", "voilabot", "mail.ru_bot", "NZZ3", "TurnitinBot",
        "ScopeusBot", "GrapeshotCrawler", "Curalab", "SiteBot", "SitebeamBot", "SEOstats Crawler",
        "Butterfly Collector", "Genieo Web filter",
        "InfoSeek Robot 1.0", "W3 SiteSearch Crawler", "ZoomSpider.net", "Ezooms", "Teoma",
        "Scooter", "WebAlta Crawler", "Gigabot", "Alexa Media Crawler",
        "MojeekBot", "BLEXBot", "YandexSomething", "CrawllyBot",
        "Wotbox", "SiteExplorer.com",
        "sogou spider", "sogou news spider", "sogou orion spider", "sogou pic spider", "sogou video spider"
    ]
    bot_counts = {robot: 0 for robot in robots}
    df = pd.read_csv(csv_file)
    for user_agent in df['用户代理信息']:
        for robot in robots:
            if robot.lower() in str(user_agent).lower():
                bot_counts[robot] += 1
    total_entries = len(df)
    ranked_bots_with_percent = [
        (i + 1, bot, count, round(count / total_entries * 100, 4))
        for i, (bot, count) in enumerate(sorted(bot_counts.items(), key=lambda x: x[1], reverse=True))
    ]
    results_df = pd.DataFrame(ranked_bots_with_percent, columns=['排名', '机器人', '数量', '百分比'])
    results_df.to_csv(f"{csv_file}_机器人统计.csv", index=False)
    print(f"统计结果已保存至：{csv_file}_机器人统计.csv")


def user_agent_browser_count(csv_file):
    browsers = [
        "Chrome", "Safari", "Firefox", "Internet Explorer", "Edge", "Edg", "Opera", "Brave", "BIDUBrowser",
        "UCBrowser", "SamsungBrowser", "Maxthon", "Netscape", "Konqueror", "SeaMonkey", "Camino", "MSIE",
        "PaleMoon", "Waterfox", "Vivaldi", "Avant Browser", "Yandex", "Epic Privacy Browser", "Torch",
        "SlimBrowser", "Midori", "Dolphin", "Puffin", "Silk", "BlackBerry", "IE Mobile", "Android Browser",
        "Chrome Mobile", "Opera Mini", "UCWEB", "QQBrowser", "QQ", "Tor Browser",
        "Comodo Dragon", "Sogou Explorer", "360 Browser", "Baidu Browser", "Samsung Internet", "Opera Coast",
        "Opera GX", "Brave Mobile", "Firefox Focus", "Firefox Reality", "Microsoft Internet Explorer",
        "Microsoft Edge Mobile", "Chromium", "Seamonkey", "K-Meleon", "Avast Secure Browser", "Bitwarden Authenticator",
        "Brave Shields", "Brave Rewards", "CentBrowser", "Coc Coc", "Comodo IceDragon", "Disruptor Browser",
        "GreenBrowser", "Iridium Browser", "K-Ninja", "Kiwi Browser", "Lunascape", "Maxthon Cloud Browser",
        "Orbitum", "QupZilla", "Slimjet", "SRWare Iron", "Torch Browser", "UCWeb Browser", "Vivaldi Snapshot",
        "Xombrero", "Opera GX Gaming Browser", "Opera Touch", "Brave Browser for Android", "Firefox for Android",
        "Chrome for Android", "Edge for Android", "Samsung Internet for Android", "UC Browser for Android",
        "QQ Browser for Android", "Brave Browser for iOS", "Firefox for iOS", "Safari for iOS", "Opera for iOS",
        "Opera Coast for iOS", "Puffin Browser", "Dolphin Browser", "CM Browser", "Flynx Browser", "Ghostery Browser",
        "Maxthon Browser", "Opera Mini for Windows", "Perfect Browser", "Photon Browser"
    ]
    browser_counts = {browser: 0 for browser in browsers}
    df = pd.read_csv(csv_file)
    for user_agent in df['用户代理信息']:
        for browser in browsers:
            if browser.lower() in str(user_agent).lower():
                browser_counts[browser] += 1
    total_browsers = len(browsers)
    ranked_browsers_with_percent = [
        (i + 1, browser, count, round(count / total_browsers * 100, 4))
        for i, (browser, count) in enumerate(sorted(browser_counts.items(), key=lambda x: x[1], reverse=True))
    ]
    results_df = pd.DataFrame(ranked_browsers_with_percent, columns=['排名', '浏览器', '数量', '百分比'])
    results_df.to_csv(f"{csv_file}_浏览器统计.csv", index=False)
    print(f"统计结果已保存至：{csv_file}_浏览器统计.csv")


def user_agent_system_count(csv_file):
    systems = ['AIX', 'Alpine Linux', 'AmigaOS', 'Android', 'Android Auto', 'Android Go',
               'Android Pie', 'Android Q', 'Android R', 'Android S', 'Android TV', 'Android Wear',
               'Arch Linux', 'Bada', 'BeOS', 'BlackBerry', 'BlackBerry OS', 'Bodhi Linux', 'CentOS',
               'Chrome OS', 'Debian', 'Elementary OS', 'Fedora', 'Firefox OS', 'FreeBSD', 'Gentoo',
               'HP-UX', 'Haiku', 'IRIX', 'KDE neon', 'KaOS', 'KaiOS', 'KaiOSWindows', 'Kali Linux',
               'Kindle', 'Kubuntu', 'Linux', 'Lubuntu', 'MX Linux', 'Mac OS X', 'Mac Os',
               'Macintosh', 'Manjaro', 'Mint', 'MorphOS', 'NetBSD', 'Nintendo', 'Nintendo Wii',
               'Nokia', 'OS/2', 'OpenBSD', 'Palm OS', 'Parrot OS', 'PlayStation', 'Q4OS', 'QNX',
               'RISC OS', 'Raspberry Pi OS', 'Red Hat', 'Roku', 'SUSE', 'Sailfish OS', 'SmartTV',
               'Solaris', 'Solus', 'SolusOS', 'SteamOS', 'SunOS', 'Symbian', 'Tails', 'Tizen',
               'Trisquel', 'Ubuntu', 'Unix', 'Void Linux', 'WebTV', 'Windows 10 Mobile',
               'Windows 11', 'Windows 2000', 'Windows 3.11', 'Windows 7', 'Windows 8', 'Windows 8.1',
               'Windows 95', 'Windows 98', 'Windows CE', 'Windows ME', 'Windows Millennium',
               'Windows Mobile', 'Windows NT 10.0', 'Windows NT 3.1', 'Windows NT 3.5',
               'Windows NT 3.51', 'Windows NT 4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2',
               'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Windows NT 6.3', 'Windows Phone',
               'Windows RT', 'Windows Server', 'Windows Vista', 'Windows XP', 'Xbox', 'Xubuntu', 'Zorin OS',
               'iOS', 'iPadOS', 'macOS', 'macOS Big Sur', 'macOS Catalina', 'macOS High Sierra', 'macOS Mojave',
               'macOS Monterey', 'macOS Sierra', 'macOS Ventura', 'openSUSE', 'tvOS', 'watchOS', 'webOS']

    system_counts = {system: 0 for system in systems}
    df = pd.read_csv(csv_file)
    for user_agent in df['用户代理信息']:
        for system in systems:
            if system.lower() in str(user_agent).lower():
                system_counts[system] += 1
    total_count = sum(system_counts.values())
    ranked_systems_with_percent = [
        (i + 1, system, count, round(count / total_count * 100, 4))
        for i, (system, count) in enumerate(sorted(system_counts.items(), key=lambda x: x[1], reverse=True))
    ]
    results_df = pd.DataFrame(ranked_systems_with_percent, columns=['排名', '系统', '数量', '百分比'])
    results_df.to_csv(f"{csv_file}_系统统计.csv", index=False)
    print(f"统计结果已保存至：{csv_file}_系统统计.csv")


def status_code_count(csv_file):
    data = pd.read_csv(csv_file)
    status_counts = data['状态码'].value_counts()
    total_count = status_counts.sum()
    percentage_threshold = 0.01
    filtered_counts = status_counts[status_counts / total_count >= percentage_threshold]
    other_count = status_counts[status_counts / total_count < percentage_threshold].sum()
    if other_count > 0:
        filtered_counts['其他'] = other_count
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(8, 6))
    plt.pie(filtered_counts, labels=filtered_counts.index,
            autopct=lambda p: f'{p:.2f}% ({int(p * total_count) / 100})')
    plt.title('响应状态码统计')
    code_peg = f'{csv_file}的响应状态统计.png'
    plt.savefig(code_peg)
    plt.close()
    print(f"图表已保存至: {code_peg}")

# if __name__ == '__main__':
# csv_file_path = input("把csv文件拖过来:")
# ip_count(csv_file_path)
# cont_count(csv_file_path)
# country_count(csv_file_path)
# city_count("../text_log.log已处理.csv")
# owner_count("../text_log.log已处理.csv")
# request_lint_count("../text_log.log已处理.csv")
# user_agent_bot_count("../text_log.log已处理.csv")
# user_agent_browser_count("../text_log.log已处理.csv")
# user_agent_system_count("../text_log.log已处理.csv")
# status_code_count("../text_log.log已处理.csv")
