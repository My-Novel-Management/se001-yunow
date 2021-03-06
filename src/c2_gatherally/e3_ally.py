# -*- coding: utf-8 -*-
"""Episode: 2-3.捨て戦士なう
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
def sc_noracat(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    bcat = W(w.blacat)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("野良猫",
            hero.come("失意の中、歩いていた"),
            outside.look("徐々に日が陰ってきて、影が長く伸びている",
                "石畳から土の地道になり、周囲の家も粗末なものが目立つ",
                "住宅街"),
            hero.explain("色々なところで魔王退治の仲間になってくれないかと聞いて回るが、",
                "ガキだと全く相手にしてもらえなかった",
                "そもそも英雄の息子"),
            hero.do("$aidaたちに教わった仲間集め$w_apliに登録してみたが、何もない"),
            hero.talk("登録してみたんだけどなあ", "何もない"),
            hero.talk("はあ、どうすればいいんだろう"),
            w.eventPoint("迷子猫", "迷子の猫を見つけた"),
            hero.do("と、目の前を魚をくわえた黒猫が歩いていく"),
            bcat.come(),
            bcat.look("一部だけ白い毛がまざっている小さな黒猫"),
            hero.talk("あれ？　お前ってひょっとして？"),
            hero.do("$smaphに出ていた迷子猫探してくださいによく似ている"),
            hero.do("追いかけていく"),
            stage=w.on_street,
            time=w.at_evening,
            )

def sc_falldownman(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    bcat = W(w.blacat)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("行き倒れの戦士",
            sol.be("黒猫を追い詰めていた"),
            bcat.be(),
            outside.look("袋小路になった場所",
                "家の煙突から煙が伸びている"),
            sol.talk("おい待て", "そいつは$meの晩飯だぞ！"),
            outside.look("周囲には魚を焼くいい匂いが漂う"),
            bcat.do("睨んでいる"),
            sol.talk("こいつぅ！"),
            sol.do("背中の$bladeを抜いて、構える"),
            sol.look("大柄な男",
                "筋肉質で薄い革の鎧をまとっている",
                "髪は赤くて立っている",
                "頭髪をバンダナで結んでいる"),
            hero.talk("危ない！"),
            sol.talk("へ？"),
            hero.do("剣を振り上げたままの$solの前に出て、黒猫を逃す"),
            sol.talk("お前何してくれてんだよ！"),
            hero.talk("いや、迷子の猫みたいで"),
            sol.talk("あいつが咥えてたのは$meの晩飯なんだよ！"),
            bcat.go("二人でもめているうちにどこかに消えてしまう"),
            sol.talk("おい！　$meの晩飯どうしてくれるんだ！"),
            stage=w.on_street,
            )

def sc_myhome(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    mam = W(w.mam)
    return w.scene("家でご飯を",
            hero.come("家に戻ってくる$S"),
            inside.look("$heroの家の内装",
                "テーブルの上には手編みの小物がある",
                "母親の内職だった"),
            sol.come(),
            sol.talk("ちわーす"),
            hero.talk("帰ったよー"),
            mam.come(),
            mam.talk("どうだった、お城は？"),
            hero.talk("あー、えっと、その……"),
            mam.talk("そちらの方は？"),
            hero.talk("道で拾った戦士です"),
            sol.talk("どうも", "$solです", "晩飯ごちになります"),
            mam.talk("え？"),
            mam.do("唖然"),
            w.br(),
            mam.talk("へえ、$on_zabanから！", "遠いところから"),
            sol.talk("こっちで兵士募集してたから、それできたんですよ"),
            hero.do("何故か二人で打ち解けている"),
            inside.look("目の前のテーブルには普段よりも多いおかずが並ぶ"),
            hero.talk("あのさ、これいつもより沢山ある気がするんだけど"),
            mam.talk("何言ってんの", "いつもと変わらないでしょ？　ね？"),
            hero.do("食べてさっさと自分の部屋に行こうとする"),
            stage=w.on_herohome_int,
            time=w.at_night,
            )

def sc_stalkinggirl(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("ストーカーの少女",
            hero.do("フォローしたと通知がある"),
            hero.talk("へえ。こんな機能があるんだ",
                "名前は$makoだった"),
            mako.come("突然知らない少女が現れる"),
            mako.talk("$k_heroと結婚をしにきました"),
            mako.do("何故か彼女は笑っている"),
            )

## episode
def ep_ally(w: World):
    return w.episode("2-3.捨て戦士なう",
            sc_noracat(w),
            sc_falldownman(w),
            sc_myhome(w),
            sc_stalkinggirl(w),
            ## NOTE
            ##  - 帰り道、野良猫を見つける
            ##  - 戦士が行き倒れていて拾った
            ##  - ストーカーの少女が現れた
            )
