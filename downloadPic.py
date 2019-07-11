import requests
import json
import urllib
import time

# length		资源数量
# category	资源主题
# path		资源本地存放路径


def getSogouImag(category, length, path):
    n = length
    cate = category
    imgs = requests.get('http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category=' +
                        cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n)+'&height=1920&width=1080')
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []  # 空列表
    for j in jd:
                # 'bthumbUrl' 缩略小图
        # imgs_url.append(j['bthumbUrl'])
                # 'pic_url' 大图片路径
        imgs_url.append(j['pic_url'])  # 使用 append() 添加元素
    m = 0
    # 当前时间，时间格式：yyyyMMddhhmmss——(20190701210155)
    localTimes = time.strftime("%Y%m%d%H%M%S", time.localtime())
    for img_url in imgs_url:
        print('***** '+localTimes+str(m)+'.jpg *****'+'   Downloading...')
        urllib.request.urlretrieve(img_url, path+localTimes+str(m)+'.jpg')
        m = m + 1
    print('Download complete!')


getSogouImag('壁纸', 30, 'D:/Download/Image/')
