# -*- coding: utf-8 -*-
"""Episode: 6-1.クエストなう
"""
## path
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
## local libs
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer


## define alias
W = Writer
_ = W.getWho()


## scenes
def sc_money_quest(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    rucca = W(w.rucca)
    return w.scene("クエストで金稼ぎ",
            hero.do("チャンネル配信で儲からないことが分かった$Sたちは、何とか地道に稼ごうと街のギルド本部に来ていた"),
            rucca.be("受付に子どもみたいな女性が座っている"),
            hero.talk("あのー、クエスト受けたいんですけど、受付の人いる？"),
            rucca.talk("こほん", "$meが受付ですが"),
            hero.talk("え？"),
            hero.do("思わず$makoを見る"),
            mako.talk("何なんですか、$hero様？"),
            hero.talk("いや", "それよりお嬢ちゃん",
                "受付ごっこはいいから、ちゃんとした人を"),
            rucca.talk("受付ですって！"),
            rucca.do("大量の書類をさばいている"),
            sol.do("掲示板を見ている"),
            rucca.do("ベテランの冒険者がぺこぺこしている"),
            hero.talk("あれ？　ほんとに受付なの？"),
            rucca.talk("だからそう言ってるでしょ？",
                "それで何のクエストを受けられるんですか？"),
            hero.talk("えーと、これとか"),
            hero.do("いくつか選んだ高額クエストを全部否定される"),
            rucca.talk("あなたたち何考えてるんですか？",
                "どう見ても$goblinと戦うのがやっとに見えるんですが"),
            rucca.do("魔道具を使って何かを測っている"),
            rucca.talk("まあそちらの小さい魔法使いの方は大丈夫そうですが、",
                "一人で受けるクエストはこの中にありませんからね",
                "もっと自分たちに適したものを選んで下さい",
                "そうでないと受理できません"),
            hero.talk("だってさ", "どうする？"),
            hero.do("相談しあい、結局手短なクエストからやることにした"),
            camera=w.hero,
            stage=w.on_castletown1,
            day=w.in_current, time=w.at_afternoon,
            )

def sc_lessmoney(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("稼ぎが少ない",
            hero.do("結局$Sたちが受けたのは家の補修工事や棚作り、",
                "畑を耕したり、野生の獣を追い払ったりという、",
                "雑用ばかりだった"),
            hero.do("ほうぼう終えて、戻ってくる"),
            mako.talk("あ、おかえりなさいませ、$hero様"),
            mako.do("テーブルの上に美味しそうなお菓子を置いて、寛いでいる$S"),
            hero.talk("あー、ちっとも儲からない！"),
            sol.come("戻ってきて"),
            sol.talk("何倒れてんだ？"),
            sol.look("日に焼けていい顔", "筋肉質になっている"),
            sol.talk("やっぱ$me、冒険者よりこっちの方が合ってんのかな"),
            hero.talk("$meは農民にはなりたくなーい！"),
            )

def sc_quest_goblin(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    rucca = W(w.rucca)
    return w.scene("$goblin討伐クエスト",
            hero.do("再度、ギルド本部にやってきてクエストを探す$Sたち"),
            hero.talk("やっぱこれじゃないかな"),
            hero.do("$Sが気に入ったのは$goblinの巣退治だ",
                "街道外れの森に$goblinたちが巣を構えてしまい、街道を通りかかる商人や旅人の荷物が奪われる事件が多発していて困っているらしい"),
            hero.talk("やっぱこういうのをしてこそ$w_Yだよ"),
            sol.talk("ん？　何か言ったか？"),
            hero.talk("あー、いや、冒険者っぽいなって"),
            hero.think("危なく$w_Yとバラすところだったとひやひやする"),
            w.eventPoint("勇者バレ", "思わず勇者らしいクエストと発言"),
            rucca.talk("またあなたたちですか",
                "いい加減にわかったでしょう？",
                "高額クエスト受ければ簡単にお金が稼げるっていう幻想はもたずに、",
                "自分たちの身の丈にあったものを選んで地道に続けるのが大事だって"),
            rucca.do("持ってきた申請書を見て"),
            rucca.talk("確かに$goblin退治くらいならって言いましたが、これは別です",
                "あなたたちに教えてあげましょう",
                "$goblinというのは一体では大したことありません",
                "最弱クラスといってもいいでしょう",
                "しかし奴らは群れを作ります",
                "それはさしずめ我が国の軍隊のようで、",
                "統率するボスが有能であれば$orgaにも匹敵すると言われています"),
            hero.talk("まあでもここらでそんな強いのいないでしょ？"),
            rucca.do("かぶりを振る"),
            rucca.talk("あなたたちは何も分かってません",
                "これ、最近一番挑戦されて誰も達成できなかったクエストなんです"),
            hero.do("そこには逃げ帰った人や中には殺された人の結果が記載されていた"),
            hero.talk("な、何とかなるよ", "これでも$meは$w_Yだからな"),
            rucca.talk("何を言ってるんですか？", "どう見たってあなたが$w_Yなはずないです"),
            mako.talk("$meも一緒に行くから$goblin程度は大丈夫ですよ",
                "それなら許可してくれますか？"),
            rucca.talk("まあ、あなたが一緒というなら戦力的には充分だと認めますが"),
            hero.do("何とか受諾して、$goblin討伐クエストに挑戦することになった"),
            )

## episode
def ep_quest_goblin(w: World):
    return w.episode("6-1.クエストなう",
            sc_money_quest(w),
            sc_lessmoney(w),
            sc_quest_goblin(w),
            ## NOTE
            ##  - 金稼ぎの為にクエストを探す勇者たち
            ##  - おつかいをこなすも微々たる金
            ##  - ゴブリン退治を見つけ、それをこなすことにする
            )
