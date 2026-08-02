# ==================== 1. 自定义模糊效果 ====================
init python:
    def blur(amount=20):
        return Transform(blur=amount)

# ==================== 2. 定义说话时的轻微晃动 ====================
define tiny_vpunch = vpunch
define tiny_hpunch = hpunch

# ==================== 2. 声明角色 ====================
define a = Character("{b}麻辣{/b}", color="#305080")      # 更深的海军蓝
define b = Character("{b}蒋成瀚{/b}", color="#601818")    # 更深的暗红
define p = Character("{b}我{/b}", color="#000000")        # 稍亮的中灰（纯黑看不清）
define w = Character("{b}神秘内个{/b}", color="#c06060")  # 更深的玫瑰红

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
default ml_favor = 0       # 麻辣的好感度
default jch_favor = 0      # 蒋成瀚的好感度
default nn = 0  #内度

# ==================== 5. 游戏开始 ====================
label start:

    scene black
    play music "BGM.mp3" fadein 2.0

    "我的第一个故事开始了。"

    "你在一间奇怪的教室里醒来，记忆一片模糊。"

    scene bg_classroom with fade

    # 背景慢慢变模糊
    show bg_classroom at blur(20) with Dissolve(1.5)

    w "别怕。"
    w "你能听见我说话，对吧？"

    # 背景慢慢恢复清晰
    show bg_classroom with Dissolve(1.5)

    # 第一个选项菜单
    menu:
        "【你是谁？】":
            jump who_are_you
        "【我在哪？】":
            jump where_am_i

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

    # 慢速淡出到黑屏，再淡入新场景
  

    scene bg_building with fade

    "忽然，一个声音叫住了你。"

    "学弟，你是刚来的吧！"

    p "?!" 

    # 麻辣学长登场
    show a normal at left with dissolve

    a "学弟你好，我是西安交通大学电气学院的麻辣！" with tiny_vpunch

    show a strike with Dissolve(0.2)

    a "欢迎你呀！以后叫我麻学长就行了。" with tiny_hpunch

    p "..." with tiny_vpunch
    p "你，你好。。。" with tiny_vpunch

    show a normal with Dissolve(0.2)

    a "学弟初来乍到，应该不知道什么叫內吧？" with tiny_hpunch

    menu:
        "【內？】":
            jump l1
        "【我知道】":
            $ ml_favor += 1
            jump l2

# ==================== 分支剧情2 ====================
label l1:
    "这是什么奇怪的东西" 

    a "【內】，是这个学校的灵魂，是所有人生存的所在" with tiny_vpunch
    p "这样吗。"
    a "那当然，我就是去年的西交內王" with tiny_hpunch
    show a strike with Dissolve(0.1)
    a "你所不知，今年的西交內王争霸赛马上就要开幕了！！" with tiny_vpunch
    "！！"
    a "学弟好好准备吧！祝你好运啊，再见！" with tiny_vpunch
    p "。。。"
    jump e2

label l2:
    "我早有耳闻！" 
    show a strike with Dissolve(0.1)
    a "学弟好厉害！！" with tiny_vpunch 
    a "你所不知，今年的西交內王争霸赛马上就要开幕了！！" with tiny_vpunch
    "！！"
    a "学弟好好准备吧！祝你好运啊，再见！" with tiny_vpunch
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
    "【现在开始，可以查看內內度了！！！】"
    
    "第一章 完"

    p "现在该去哪呢？"

    menu:
        "【图书馆】":
            jump l21
        "【未解锁】":
            jump l22

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
    "未完待续 感谢游玩 V1.1"

label l22:
    return


    # 故事结束，返回主菜单
    return