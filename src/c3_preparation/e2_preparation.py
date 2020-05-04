# -*- coding: utf-8 -*-
"""Episode: 3-2.買い物なう
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
def sc_visitmarcket(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    candy, doyle = W(w.candy), W(w.doyle)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("市場を見て回る",
            hero.come(),
            sol.come(),
            mako.come(),
            hero.do("三人で市場へとやってきた"),
            outside.look("市場の情景",
                "城下町の中央部の広場に露店がたくさん出て賑わっている",
                "ただ以前に比べて半分の数になり、寂しい"),
            hero.talk("魔王が現れてから、色々と物が入ってこなくなったりして、困ってるみたいなんだ"),
            sol.talk("これでもまだマシな方だ",
                "一度立ち寄った街なんか、誰も家に閉じこもって出てこないんだよ",
                "なんでも一度魔物が大量に街に入ってきて沢山死者が出て、",
                "それ以来買い物すら配達頼りだって"),
            mako.do("花屋を見て、それを買ってとねだる"),
            hero.talk("花なんて冒険に必要ないだろう？"),
            mako.talk("でも綺麗ですよ？"),
            hero.talk("そりゃ、昔は花の街って言われてたくらいだからね",
                "$meもよく……"),
            w.eventPoint("$heroの過去", "小さい頃に花畑で誰かと会った記憶"),
            mako.talk("どうかしました？"),
            hero.talk("いや、なんでも"),
            hero.do("見て歩くが、露店には欲しいものはあまりない"),
            hero.do("それでも食い物を買ってやる$S"),
            mako.talk("ありがとうございます"),
            hero.talk("$hotdogは庶民の食い物だからな！"),
            )

def sc_visitmarcket_herbshop(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    candy, doyle = W(w.candy), W(w.doyle)
    return w.scene("薬草屋にて",
            hero.do("薬草屋に立ち寄る"),
            w.eventPoint("人物紹介", "$candy紹介"),
            w.eventPoint("人物紹介", "$doyle紹介"),
            candy.be(),
            doyle.be(),
            hero.do("薬草を見ている"),
            doyle.do("店の奥で薬草をせんじながら、娘が相手するのをあまりよく思ってない"),
            candy.talk("へー！　$heroさんたち冒険に出るんですか！"),
            candy.look("$makoと同じくらいの背丈だが、二十歳を超えていて合法"),
            hero.talk("そうなんだよ", "$herbならここのが一番ってことで"),
            candy.talk("そうね。うちのはこの国一って言ってもいいくらいだと思う",
                "ね、お父さん"),
            doyle.talk("買うのか買わねえのか、はっきりしろ"),
            hero.talk("は、はい。買いますって"),
            hero.talk("$doyleさんいつも怖いんだよ"),
            sol.talk("そういえば$k_makoは？"),
            hero.talk("なんか好きなもの見てくるって"),
            hero.do("$candyと親しげに話している$S"),
            )

def sc_expensive(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    return w.scene("みんな高額",
            hero.do("その後、装備品やキャンプ用品を見て回るが"),
            hero.talk("なんだこの値段……"),
            sol.talk("いいのはこんくらいすんのよ",
                "まあ$meらの持ち合わせだとこっちだな"),
            sol.do("$Sが見ていたのは一番しょぼい寝袋だ",
                "ただの布を縫い合わせただけに見える"),
            hero.talk("これで寒さ防げるの？"),
            sol.talk("お前な、何もない野原で寝ると思ってたのか？",
                "洞窟とか、そういう場所を探して、地べたに寝なくていいように、",
                "これを使うだけだぞ？"),
            hero.talk("え？"),
            sol.talk("野宿の何もしらないみたいだから、冒険に出たら$meがみっちり教え込んでやるよ",
                "如何にこの世界が人間の暮らす環境になっていないか",
                "如何に屋根がある、壁があるってことが幸せかな"),
            hero.do("震え上がる$S"),
            )

def sc_pickedmoney(w: World):
    hero, mako, sol, yula = W(w.hero), W(w.mako), W(w.sol), W(w.yula)
    mam = W(w.mam)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("金を失った",
            hero.do("結局散財して帰ってきた$Sたち"),
            mako.talk("あ、おかえりなさいませ", "どうでしたか？"),
            hero.talk("先に帰ってたんだね"),
            mako.talk("せっかくなのでベッドメイクしておきました"),
            inside.look("部屋の様子が一変している"),
            hero.talk("これどうしたの？"),
            mako.talk("だから$meが色々と飾っておきました",
                "いいでしょう？"),
            inside.look("花柄の壁紙とかすごいメルヘンチックになっている"),
            hero.talk("これも？"),
            hero.do("サイドテーブルの上のドクロの置物を見て"),
            mako.talk("それは$meの趣味です", "あまりこういうの置かないようにしたんですけど"),
            hero.talk("いや、そういう問題じゃなくて"),
            mako.talk("だって魔王退治したら結婚してここが新居になる訳でしょう？",
                "ね"),
            inside.look("狭い部屋には不釣り合いなキングサイズのダブルベッド"),
            hero.talk("いや、あの、あれはね"),
            sol.talk("まあいいじゃねえか",
                "一度は口から出した言葉だ、男なら引っ込めないだろう？"),
            hero.talk("$solまで！"),
            hero.do("なんとか準備を整えた$Sたちは、明日の朝ここを発つことに決めて、わかれた"),
            )

## episode
def ep_shopping(w: World):
    return w.episode("3-2.買い物なう",
            sc_visitmarcket(w),
            sc_visitmarcket_herbshop(w),
            sc_expensive(w),
            sc_pickedmoney(w),
            ## NOTE
            ##  - 市場にやってくる
            ##  - 色々と見て回るがみんな高い
            ##  - 財布をだましとられ、大事な金を失う
            )
