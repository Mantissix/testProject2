have_gift = False


def send_gift():
    #global have_gift
    have_gift = True
    print("发礼物啦！")
    return have_gift


def show_gift(have_gift=send_gift()):
    if have_gift:
        print("收到礼物啦！好开心！")
    else:
        print("等待礼物中。。。但是我没有收到。。。")


send_gift()
show_gift()