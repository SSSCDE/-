# ==================== 1. 自定义模糊效果 ====================
init python:
    def blur(amount=20):
        return Transform(blur=amount)

# ==================== 2. 定义说话时的轻微晃动 ====================
define tiny_vpunch = vpunch
define tiny_hpunch = hpunch

# ==================== 2. 声明角色 ====================
define a = Character("{b}麻辣{/b}", color="#305080")
define b = Character("{b}蒋成瀚{/b}", color="#601818")
define p = Character("{b}我{/b}", color="#000000")
define w = Character("{b}神秘内个{/b}", color="#c06060")
define q = Character("{b}???{/b}", color="#000000cc")

# ==================== 3. 定义背景 ====================
image bg_building = "bg_building.jpg"
image bg_classroom = "bg_classroom.jpg"
image bg_street = "bg_street.jpg"
image bg_lib = "bg_lib.jpg"
image bg_lib2 = "bg_lib2.jpg"
image bg_lib3 = "bg_lib3.jpg"
image csgo = "csgo.jpg"

# ==================== 4. 定义立绘 ====================
image a normal = Transform("a/normal.png", zoom=0.7)
image a strike = Transform("a/strike.png", zoom=0.45)

image b serious = Transform("b/serious.png", zoom=0.7)
image b joke = Transform("b/joke.png", zoom=0.7)
image b ws = Transform("b/ws.png", zoom=0.7)

# 初始化好感度
default ml_favor = 0
default jch_favor = 0
default nn = 0

init python:
    renpy.music.register_channel("bgm2", mixer="music", loop=True)

image dark_overlay = "#00000088"

# ==================== 5. 游戏开始 ====================
label start:

    scene black
    play bgm2 "BGM.mp3" fadein 2.0

    "我的第一个故事开始了。"

    "你在一间奇怪的教室里醒来，记忆一片模糊。"
    play music "walking_on_night_streets.mp3" noloop volume 0.5

    scene bg_classroom with fade

    show bg_classroom at blur(20) with Dissolve(1.5)

    w "别怕。"
    w "你能听见我说话，对吧？"

    show bg_classroom with Dissolve(1.5)

    menu:
        "【你是谁？】":
            jump who_are_you
        "【我在哪？】":
            jump where_am_i
    stop music fadeout 2.0

# ==================== 6. 分支剧情 ====================
label who_are_you:
    "你颤抖着问出这个问题。"

    w "我是谁不重要。重要的是，你是谁。"
    w "你现在...或许该叫你【西安內个大学的学生】。"
    jump e1

label where_am_i:
    "你挣扎着环顾四周。"
    w "一个你无法逃脱的地方。"
    w "或者说，你只有內才能出去。"
    jump e1

# ==================== 7. 剧情汇合 ====================
label e1:
    p "这到底是怎么回事..."
    p "不管了，往外走走试试看。"

    scene bg_building with fade

    "忽然，一个声音叫住了你。"
    "学弟，你是刚来的吧！"

    p "?!"

    show a normal at left with dissolve
    show a normal with tiny_vpunch
    a "学弟你好，我是西安交通大学电气学院的麻辣！"

    show a strike with Dissolve(0.2)
    show a strike with tiny_hpunch
    a "欢迎你呀！以后叫我麻学长就行了。"

    p "..."
    p "你，你好。。。"

    show a normal with Dissolve(0.2)
    show a normal with tiny_hpunch
    a "学弟初来乍到，应该不知道什么叫內吧？"

    menu:
        "【內？】":
            jump l1
        "【我知道】":
            $ ml_favor += 1
            jump l2

# ==================== 分支剧情2 ====================
label l1:
    "这是什么奇怪的东西"
    show a normal with tiny_hpunch
    a "【內】，是这个学校的灵魂，是所有人生存的所在"
    p "这样吗。"
    show a normal with tiny_hpunch
    a "那当然，我就是去年的西交內王"
    show a strike with Dissolve(0.1)
    show a strike with tiny_hpunch
    a "你所不知，今年的西交內王争霸赛马上就要开幕了！！"
    "！！"
    show a strike with tiny_vpunch
    a "学弟好好准备吧！祝你好运啊，再见！"
    p "。。。"
    jump e2

label l2:
    "我早有耳闻！"
    show a strike with Dissolve(0.1)
    show a strike with tiny_vpunch
    a "学弟好厉害！！"
    show a strike with tiny_vpunch
    a "你所不知，今年的西交內王争霸赛马上就要开幕了！！"
    "！！"
    show a strike with tiny_vpunch
    a "学弟好好准备吧！祝你好运啊，再见！"
    p "。。。"
    jump e2

# ==================== 剧情汇合2 ====================
label e2:
    hide a with moveoutleft
    "麻辣离开了"
    p "好奇怪但是热情的学长"
    scene black with Dissolve(2.0)
    p "內王争霸赛吗？记下吧，感觉是很重要的事。。。"
    show screen favor_hud
    play sound "correct_answer3.mp3"
    "【现在开始，可以查看內內度了！！！】"

    "第一章 完"

    p "现在该去哪呢？"

    menu:
        "【图书馆】":
            jump l21
        "【未解锁】":
            jump l22

label l22:
    scene black with fade
    "更多精彩正在开发中"
    "敬请期待"
    "SSSCDE 开发"
    "空格返回主页"
    return

label l21:
    scene bg_lib2 with fade
    "交大并不是一个很大的学校。"
    "很快就到了一个叫【四大发明广场】的地方"
    "再往前一点就到了吧"
    scene bg_lib with Dissolve(2.0)
    "【钱学森图书馆】————内个的圣地，卷鬼的殿堂。"
    "深吸一口气"
    scene black with Dissolve(2.0)
    "入馆吧"
    "这个学校藏着太多秘密。"

    scene bg_lib3 with Dissolve(2.0)

    p "图书馆里真安静"
    p "旁边似乎坐着一个认真学习的学长呢"
    p "可以向他打听內王争霸赛的事吗？"
    p "试试吧"

    menu:
        "【向认真的学长打听】":
            jump s1

label s1:
    p "...学长...你好..."
    show dark_overlay with Dissolve(1.5)

    show b ws at Transform(xalign=0.98, yalign=0.8) with moveinright
    show b ws with tiny_vpunch
    q "!?"
    q "学弟，你好，我叫蒋成瀚，你有什么事吗？"

    show b serious at Transform(xalign=0.98, yalign=0.8) with Dissolve(0.2)
    b ""
    p "呃，抱歉打扰学长了，我想问一下那个。。內王争霸赛的事。"
    show b serious with tiny_hpunch
    b "內王争霸赛！！"
    b "我正在为此准备呢"

    b "去年，我败给了同学院的麻辣同学"
    show b serious with tiny_vpunch
    b "这次，我必须拿到冠军。"
    "蒋成瀚的脸上露出激动的神情"

    p "(什么？他竟然跟刚刚的麻辣学长认识?太巧了吧)"
    p "(要不要告诉他刚刚跟麻辣学长遇见的事呢？）"

    menu:
        "【要】":
            jump l31
        "【不要】":
            jump l32

label l31:
    p "麻辣学长？是个戴着眼镜很热情的学长吗？"
    show b serious with tiny_hpunch
    b "啊，你怎么会认识他？"
    p "我，我刚刚在教学楼下遇见了。。。"
    show b serious with tiny_hpunch
    b "居然背着我偷偷去做迎新志愿者！！真的是太內了！"
    "蒋成瀚学长的脸上出现了一种奇怪的表情"
    "不过很快就消失了"
    p "..."
    show b serious with tiny_hpunch
    b "没什么没什么，他跟我同学院，也是个熟人了。"
    b "既然已经遇上了他，那你也想必知道了，什么是內"
    b "內王争霸赛，简而言之就是在整个学校范围内评选出最內的学生。获得內王的称号是所有交大学生追求的无上荣誉。"
    "蒋成瀚顿了顿，凑过来小声说："
    b "而且据校园的传说...获奖者可以得到一些特殊的奖励。"
    show b serious with tiny_hpunch
    b "但是每一届內王都对此守口如瓶，没有人知道奖励到底是什么。"
    b "连麻辣都不肯告诉我。"
    "蒋成瀚脸上露出无奈的表情，耸了耸肩"
    show b joke at Transform(xalign=0.98, yalign=0.8) with Dissolve(0.2)
    b "內王争霸赛也欢迎你啦，学弟！！！"
    jump s2

label l32:

    b "话说回来————"
    b "內王争霸赛，简而言之就是在整个学校范围内评选出最內的学生。获得內王的称号是所有交大学生追求的无上荣誉。"
    "蒋成瀚顿了顿，凑过来小声说："
    b "而且据校园的传说...获奖者可以得到一些特殊的奖励。"
    show b serious with tiny_hpunch
    b "但是每一届內王都对此守口如瓶，没有人知道奖励到底是什么。"
    b "麻辣是跟我同学院的，甚至可以说是我的好朋友"
    b "但是甚至连麻辣都不肯告诉我。"
    "蒋成瀚脸上露出无奈的表情，耸了耸肩"
    show b joke at Transform(xalign=0.98, yalign=0.8) with Dissolve(0.2)
    b "內王争霸赛也欢迎你啦，学弟！！！"
    jump s2

label s2:
    hide b with moveoutright
    scene bg_lib3 with Dissolve(2.0)
    "蒋成瀚回到位置，继续沉默的学习起来，似乎非常的认真"

    p "这个学校的学长都有些奇怪呢"
    p "不过好歹知道了什么是內王争霸赛。"
    p "大概就是比谁更努力的比赛吧。"
    p "至于那个神秘大奖...也许对逃离这里有帮助。"
    p "那个神秘的声音...会是谁呢？"

    "V1.2 未完待续！！"
    "继续以返回主页"

    return