import time
import requests
from lxml import etree

if __name__ == '__main__':
    # todo login
    print('欢迎使用高校考试网 www.gaoxiaokaoshi.com 自动刷课脚本')
    print('此脚本不参与任何交易，如果侵权的话，请联系我删库跑路。')
    print('项目地址https://github.com/AlwaysLazy21/GXKSscript')
    print('如果你感觉此脚本对你有帮助的话，可以给我一个★star')
    username = input('请输入你的账号：')
    password = input('请输入账号密码：')
    session = requests.session()
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    data = {
        'screenType': '1440',
        'name': username,
        'pw': password
    }
    loginUrl = 'http://www.gaoxiaokaoshi.com/HidLogin.aspx'
    loginResp = session.post(loginUrl, headers=head, data=data)
    # print(loginResp.content.decode())
    if loginResp.status_code == 200:
        print("Login successfull", end=' ')
    else:
        print("Login failed", end=' ')
    loginResp.close()
    time.sleep(1)  # 等待一秒钟


    class mess:
        def __init__(self, course, isFinished, courseId, lookTime):
            self.course = course
            self.isFinished = isFinished
            self.courseId = courseId
            self.lookTime = lookTime

        def setIsFinished(self, isFinished):
            self.isFinished = isFinished

        def setCourseId(self, courseId):
            self.courseId = courseId

        def setLookTime(self, lookTime):
            self.lookTime = lookTime

        def show(self):
            print(self.course, self.isFinished, '课程ID:', self.courseId, ' 已观看 ', self.lookTime, '分钟')


    course_list = []
    # todo 获取课程
    for page in range(100):
        print('.', end=' ')
        data_course = {
            '__VIEWSTATE': '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',
            '__EVENTVALIDATION': 'pSk4P35UquECGSKpdgM9n23Key7Mc7Zk/lp8/4ubIgiJzsDwaLQ8WhCL0NvBbMqT4IwD5bnZGxq++D76H2S2EONohcczJXwlEMKZdACZi7smPenf5PpMc4Bab/TE1bVGuqzRjXKS5O0yKhHwv5OTWDRNlIQlHHjFToiqShOxh3V08c2HI72WEhRmbYDFi18AAo0UMq/71KEyg6SV3+SBFBa21dOodTl0ZoaIAwRd7XDqsBIQwsyefJfAjWS6ccGjyMqUXOa1415irGoHBUHOvWlHN5HN+401/FddXxh7xL+WhaTFxCfuUa+GEosdMJYOsgZc5nS1h0kP9CrG',
            'PageSplit1$ddlPage': page + 1
        }
        time.sleep(1)
        mainUrl = 'http://www.gaoxiaokaoshi.com/Study/LibraryStudyList.aspx'
        mainResp = session.post(mainUrl, headers=head, data=data_course)
        # print(mainResp.content.decode())
        # print(mainResp.status_code)
        if mainResp.status_code != 200:
            break
        mainResp.close()
        # print(mainResp.content.decode())
        time.sleep(1)
        # todo xpath解析
        et = etree.HTML(mainResp.text)
        # print(mainResp.text)
        # 课程名称

        course = et.xpath('//td[@class="pleft30"]/text()')
        # 是否完成
        isFinished = et.xpath('//td/span/text()')
        # 课程id
        courseId = et.xpath('//tr/td[6]/a/@onclick')
        # 观看时长
        lookTime = et.xpath('//tr//td[4]/text()')

        for i in course:
            if i == '课程名称': continue
            temp = mess(i, '不知道', '000', '-1')
            course_list.append(temp)
        index = 0
        for i in isFinished:
            course_list.__getitem__(index + page * 9).setIsFinished(i)
            index += 1
        index = 0
        for i in courseId:
            course_list.__getitem__(index + page * 9).setCourseId(i.split(',')[-1][0:-1])
            index += 1
        index = 0
        for i in lookTime:
            if i == '已完成学时': continue
            course_list.__getitem__(index + page * 9).setLookTime(i[0:-2])
            index += 1
            # print(i)

        del index
    print()
    # for i in course_list:
    #     i.show()
    # todo 获取frame表单信息
    frameDemoUrl = "http://www.gaoxiaokaoshi.com/Study/LibraryStudy.aspx?tmp=1&Id={}&PlanId=11"
    for i in course_list:
        i.show()
        # print(i.lookTime)
        lookTime = int(i.lookTime)
        if i.isFinished == '已完成': continue
        frameUrl = f"http://www.gaoxiaokaoshi.com/Study/LibraryStudy.aspx?tmp=1&Id={i.courseId}&PlanId=11"
        # print(frameUrl)
        time.sleep(1)
        frameResp = session.get(frameUrl, headers=head)
        frameResp.close()
        et = etree.HTML(frameResp.text)
        id = ''
        refId = ''
        Mins = ''
        StudentId = ''
        SessionID = ''
        hidNewId = et.xpath('//input[@id="hidNewId"]/@value')
        for i in hidNewId: id = i
        hidRefId = et.xpath('//input[@id="hidRefId"]/@value')
        for i in hidRefId: refId = i
        hidPassLine = et.xpath('//input[@id="hidPassLine"]/@value')
        for i in hidPassLine: Mins = i
        hidStudentId = et.xpath('//input[@id="hidStudentId"]/@value')
        for i in hidStudentId: StudentId = i
        hidSessionID = et.xpath('//input[@id="hidSessionID"]/@value')
        for i in hidSessionID: SessionID = i
        index = 1

        domainURl = 'http://www.gaoxiaokaoshi.com/Study/updateTime.ashx?'
        head = {
            'Host': 'www.gaoxiaokaoshi.com',
            'Referer': frameUrl,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        # print(frameUrl)
        print('正在学习中，需要', int(Mins) - lookTime, '分钟，每60秒报备下信息')
        for i in range(int(Mins)-lookTime):
            index = i + 1
            time.sleep(60)
            print('现已累计观看', index, '分钟,进度会自己保存。可随时退出本程序')
            param_from = {
                'Id': id,
                'pTime': 60 * index,
                'Mins': Mins,
                'refId': refId,
                'StudentId': StudentId,
                'StydyTime': 0,
                'SessionId': SessionID
            }
            domainResp = session.get(domainURl, headers=head, params=param_from)
            # print(domainResp.url)
            # print(domainResp.status_code)
    print('一分钟后自动退出，也可现在手动退出')
    time.sleep(60)

        # print(frameResp.text)
        # break
        # todo 2022年7月4日18点17分 今天就先写到这里
        # todo 伪造数据发送到服务器
