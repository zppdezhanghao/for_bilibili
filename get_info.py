import os,requests,re,datetime,os

datenum = datetime.datetime.now()
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

    if pattern_title.findall(response.text)[0] == []:
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



first_level_folders = []
second_level_folders = []
for i in os.listdir():
    if not "." in i:
        first_level_folders.append(i)

        media_folders = []
        for ii in os.listdir(i):
            if not "." in ii:
                media_folders.append(ii)
        second_level_folders.append(media_folders)

second_level_folders[0]

os.listdir(first_level_folders[0]+"/"+second_level_folders[0][0])
cc = []
for i,ii in enumerate(first_level_folders):
    for j in second_level_folders[i]:
        txt_name = []
        info_txt_name = []
        for jj in os.listdir(first_level_folders[i]+ "/" + j):
            if not "info_" in jj:
                txt_name.append(first_level_folders[i]+ "/" + j + "/" + jj)
                info_txt_name.append(first_level_folders[i]+ "/" + j + "/info_" + jj)

        with open(txt_name[0],"r+") as f:
             media_bv = f.readlines()
        f.close()

        ccc = []
        for k in media_bv:
            ccc.append(get_info_by_bv(k.replace("\n","")))

        with open(info_txt_name[0],"w+",encoding='utf-8') as f:
            for kk in ccc:
                f.write(kk + "\n")

        print("已完成" +  info_txt_name[0])

        cc.append(ccc)

get_info_by_bv(k.replace("\n",""))
k
all_url ="https://api.bilibili.com/x/web-interface/view?bvid=" + k.replace("\n","")
response = requests.get(all_url)
response.text
