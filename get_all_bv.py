import os,requests,re,datetime,os
datenum = datetime.datetime.now()

def get_region_url(url,days):
    response = requests.get(url)
    pattern = re.compile(r'"tid":(.*?)}')
    pattern_name = re.compile(r'"name":"(.*?)","tid"')
    tid = pattern.findall(response.text)
    region_name = pattern_name.findall(response.text)


    final_url = []
    for i in tid:
        if days == 1:
            final_url.append("https://www.bilibili.com/ranking/all/"+ i +"/0/1")
        elif days == 3:
            final_url.append("https://www.bilibili.com/ranking/all/"+ i +"/0/3")
        elif days == 7:
            final_url.append("https://www.bilibili.com/ranking/all/"+ i +"/0/7")
        elif days == 30:
            final_url.append("https://www.bilibili.com/ranking/all/"+ i +"/0/30")
        else:
            print("请输入1(单日排行),3(三日排行),7(周排行)或30(月排行)")
            return

    return region_name,final_url


def get_bv_fun(url):
    response = requests.get(url)
    pattern = re.compile(r'(?<="bvid":")\w{12}')
    pattern2 = re.compile(r'"bvid":"(.*?)","author"')
    get_bv_raw = pattern2.findall(response.text)

    get_bv_final = []
    others = []
    for i,ii in enumerate(get_bv_raw):
        if len(ii) != 12:
            others.append(i)
            get_bv_final.append(pattern.findall(ii)[-1])
        else:
            get_bv_final.append(ii)
    return get_bv_final


def get_info_by_bv(bvnum):
    all_url ="https://api.bilibili.com/x/web-interface/view?bvid=" + bvnum
    response = requests.get(all_url)
    pattern_title = re.compile(r'"title":"(.*?)","')
    pattern_name = re.compile(r'"name":"(.*?)","face":')
    pattern_view = re.compile(r'"view":(.*?),"danmaku"')
    pattern_danmaku = re.compile(r'"danmaku":(.*?),"reply"')
    pattern_reply = re.compile(r'"reply":(.*?),"favorite"')
    pattern_favorite = re.compile(r'"favorite":(.*?),"coin"')
    pattern_coin = re.compile(r'"coin":(.*?),"share"')
    pattern_share = re.compile(r'"share":(.*?),"now_rank"')
    pattern_like = re.compile(r'"like":(.*?),"dislike"')
    pattern_dislike = re.compile(r'"dislike":(.*?),"evaluation"')

    if pattern_title.findall(response.text) == []:
        return "/NA"
    else:
        title = "title=" + pattern_title.findall(response.text)[0]
        name = ",upname=" + pattern_name.findall(response.text)[0]
        view = ",view=" + pattern_view.findall(response.text)[0]
        danmaku = ",danmaku=" + pattern_danmaku.findall(response.text)[0]
        reply = ",reply=" + pattern_reply.findall(response.text)[0]
        favorite = ",favorite=" + pattern_favorite.findall(response.text)[0]
        coin = ",coin=" + pattern_coin.findall(response.text)[0]
        share = ",share=" + pattern_share.findall(response.text)[0]
        like = ",like=" + pattern_like.findall(response.text)[0]
        dislike = ",dislike=" + pattern_dislike.findall(response.text)[0]
        return title + name + view + danmaku + reply + favorite + coin + share + like + dislike



for j in [1,3,7,30]:
    all_regions_name,all_regions_url = get_region_url('https://www.bilibili.com/ranking/all/3/0/' + str(j),j)
    for ii,i in enumerate(all_regions_name):
        if not i in os.listdir():
            os.mkdir(i)
        for jj in ["日排行","三日排行","周排行","月排行"]:
            if not jj in os.listdir(i):
                os.mkdir(i + "/" + jj)

        if j == 1:
            all_path = i + "/" + "日排行" + "/" + i + "_" + datenum.strftime("%m-%d-%Y-%H_%M")  + '.txt'
            all_new_path =  i + "/" + "日排行" + "/info_" + i + "_" + datenum.strftime("%m-%d-%Y-%H_%M")  + '.txt'
        elif j == 3:
            all_path = i + "/" + "三日排行" + "/" + i + "_" + datenum.strftime("%m-%d-%Y-%H_%M")  + '.txt'
            all_new_path =  i + "/" + "三日排行" + "/info_" + i + "_" + datenum.strftime("%m-%d-%Y-%H_%M")  + '.txt'
        elif j == 7:
            all_path = i + "/" + "周排行" + "/" + i + "_" + datenum.strftime("%m-%d-%Y-%H_%M")  + '.txt'
            all_new_path =  i + "/" + "周排行" + "/info_" + i + "_" + datenum.strftime("%m-%d-%Y-%H_%M")  + '.txt'
        elif j == 30:
            all_path = i + "/" + "月排行" + "/" + i + "_" + datenum.strftime("%m-%d-%Y-%H_%M")  + '.txt'
            all_new_path =  i + "/" + "月排行" + "/info_" + i + "_" + datenum.strftime("%m-%d-%Y-%H_%M")  + '.txt'

        bv_num = get_bv_fun(all_regions_url[ii])
        with open(all_path,'w') as f:
            for iii in bv_num:
                f.write(iii + '\n')
        f.close()

        with open(all_new_path,'w+',encoding='utf-8') as f:
            for iii in bv_num:
                f.write(get_info_by_bv(iii) + '\n')
        f.close()
