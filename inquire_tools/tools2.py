import pandas as pd
from matplotlib import pyplot as plt


class BaseAnalyzer:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = pd.read_csv(csv_file)

    def _count_and_save(self, column_name, output_filename):
        counts = self.df[column_name].value_counts().reset_index()
        counts.columns = [column_name, '数量']
        total = counts['数量'].sum()
        counts['百分比'] = counts['数量'].apply(lambda x: round((x / total) * 100, 2))
        counts['排名'] = counts.index + 1
        counts.sort_values(by='数量', ascending=False, inplace=True)
        self._save_to_csv(counts[['排名', column_name, '数量', '百分比']], output_filename)

    def _save_to_csv(self, df, filename):
        df.to_csv(f"{self.csv_file}_{filename}.csv", index=False)
        print(f"统计完成，结果已保存至{self.csv_file}_{filename}.csv")

    def _user_agent_analysis(self, keyword_list, output_filename, column="用户代理信息"):
        keyword_counts = {keyword: 0 for keyword in keyword_list}
        for user_agent in self.df[column]:
            for keyword in keyword_list:
                if keyword.lower() in str(user_agent).lower():
                    keyword_counts[keyword] += 1
        total = len(self.df)
        ranked_data = [(i + 1, keyword, count, round(count / total * 100, 4))
                       for i, (keyword, count) in
                       enumerate(sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True))]
        df = pd.DataFrame(ranked_data, columns=['排名', '关键词', '数量', '百分比'])
        self._save_to_csv(df, output_filename)

    def plot_status_codes(self, column="状态码"):
        status_counts = self.df[column].value_counts()
        total_count = status_counts.sum()
        percentage_threshold = 0.01
        filtered_counts = status_counts[status_counts / total_count >= percentage_threshold]
        other_count = status_counts[status_counts / total_count < percentage_threshold].sum()
        if other_count > 0:
            filtered_counts['其他'] = other_count
        plt.figure(figsize=(8, 6))
        plt.pie(filtered_counts, labels=filtered_counts.index,
                autopct=lambda p: f'{p:.2f}% ({int(p * total_count) / 100})')
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.title('响应状态码统计')
        code_pie = f'{self.csv_file}_响应状态统计.png'
        plt.savefig(code_pie)
        plt.close()
        print(f"图表已保存至: {code_pie}")

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

# analyzer = BaseAnalyzer("../text_log.log已处理.csv")
# analyzer._count_and_save('大洲', '大洲统计')
# analyzer._count_and_save('ip', 'IP统计')
# analyzer._count_and_save('国家', '国家统计')
# analyzer._count_and_save('城市', '城市统计')
# analyzer._count_and_save('所有者', '所有者统计')
# analyzer._count_and_save('请求行', '请求行统计')
# analyzer._user_agent_analysis(robots, '机器人统计')
# analyzer._user_agent_analysis(browsers, '浏览器统计')
# analyzer._user_agent_analysis(systems, '系统统计')
# analyzer.plot_status_codes()
