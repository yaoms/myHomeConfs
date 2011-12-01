#!/bin/sh
#mencoder "$1" -o "$2" \
#  -vf dsize=480:320:2,scale=-8:-8,harddup \
#  -oac mp3lame -lameopts abr:br=128 \
#  -ovc x264 \
#  -x264encopts bitrate=512

#  HTC Hero内置播放器的视频编解码测试 收藏
#　　Android没有比较好的视频播放器，这一点是令人难受的。不过对于嵌入式设备能够播放到什么程度的视频我还是正好需要研究一下的。于是就干脆的在机器上试了试。
#
#　　首先，肯定是首选的测试了h264编码，结果发现，这个破播放器更本解不动main profile的h264，于是只能使用baseline的水平来测试了。可是我这里的ffmpeg居然不认vpre baseline于是只能自己研究去了。
#
#view plaincopy to clipboardprint?
#./ffmpeg -i /media/disk-2/MTV/Air.wmv  -f mp4 -acodec libfaac -ab 94k -vcodec libx264 -crf 24 -coder 0 -refs 1 -deblockalpha 1 -deblockbeta -1 -me_method umh -subq 9 -me_range 32  -bf 0 -g 300 -i_qfactor 1.3 -b_qfactor 1.4 -flags2 -wpred-8x8dct -s 480x320  /home/Videos/airavcbasecrf.mp4
#
#
#　　编码一段动画，480x320，视频流码率820Kbps
#
#　　这里存在的问题是，mencoder的lavf似乎有问题，编出来的mp4封装别人不认，而只能用ffmpeg了，自行编baseline的时候必须要禁用掉8x8dct CABAC  refs 也必须设置为1 b帧设置为0。此外，还禁止interlace和wpred
#
#　　如果不这么做会有什么后果呢？呵呵，我是测试了，开了CABAC以后，HTC HERO就把它当成一张绿色的图片了。而开了B帧以后就类似于在一张固定的背景上变化了。
#
#关于Profile的配置参考，下面这一段说的比较不错。
#
#Baseline Profile
#I/P slices
#Multiple reference frames (–refs <int>, >1 in the x264 CLI)
#In-loop deblocking
#CAVLC entropy coding (–no-cabac in the x264 CLI)
#Main Profile
#Baseline Profile features mentioned above
#B slices
#CABAC entropy coding
#Interlaced coding – PAFF/MBAFF
#Weighted prediction
#High Profile
#Main Profile features mentioned above
#8×8 transform option (–8×8dct in the x264 CLI)
#Custom quantisation matrices
#　　但是，baseline的h264实在是太可怜了，于是，我又试着去用ffmpeg的mpeg4来编码
#
#view plaincopy to clipboardprint?
#./ffmpeg -i /media/disk-2/MTV/Air.wmv  -f mp4 -acodec libfaac -ab 96k -vcodec mpeg4 -aspect 16:9 -qscale 6 -mbd 2 -bf 16 -s 480x320 /home/Videos/airmp4v.mp4
#
#
#  这个编码完码率在1000kbps左右，但是和上面那个比起来质量查太多了。充满了明显的马赛克，我只能说，这个mpeg4不敢恭维。
#
#　　最后确定还是用h264，于是再优化以下参数，最后用这个：


# ./ffmpeg -i /media/disk-2/MTV/Air.wmv  -f mp4 -acodec libfaac -ab 94k -vcodec libx264 -crf 24 -coder 0 -refs 6 -flags +loop -deblockalpha 0 -deblockbeta 0 -me_method umh -subq 9 -me_range 32  -bf 0 -g 300 -i_qfactor 1.3 -b_qfactor 1.4 -flags2 -wpred-8x8dct -ss 100 -s 480x320  /home/ulysess/Videos/airavcref4.mp4
# 可以比较不错的调整的是crf 和refs的值，普通的就用refs 6就好了，动画可以用到12以上，注意的是，refs越高解码负载越高质量会好一点，crf越小质量越好。
# 最后，如果你一定要压榨以下剩余价值，我实际机器测试结果是refs最大可以是4，还可以开8x8dct。于是就变成这样了。
# /ffmpeg -i /media/disk-2/MTV/Air.wmv  -f mp4 -acodec libfaac -ab 94k -vcodec libx264 -crf 24 -coder 0 -refs 6 -flags +loop -deblockalpha 0 -deblockbeta 0 -me_method umh -subq 9 -me_range 32  -bf 0 -g 300 -i_qfactor 1.3 -b_qfactor 1.4 -flags2 -wpred+8x8dct -ss 100 -s 480x320  /home/Videos/airavcref4.mp4
# -----裁边：：：：
# ffmpeg -i /media/动心DVDRip/Crystal/EVA-死与新生－魂之轮回.vob   -f mp4 -acodec libfaac -ab 94k -vcodec libx264 -crf 24 -coder 0 -refs 4 -flags +loop -deblockalpha 0 -deblockbeta 0 -me_method umh -subq 9 -me_range 32  -bf 0 -g 300 -i_qfactor 1.3 -b_qfactor 1.4 -flags2 -wpred+8x8dct -cropleft 39 -cropright 26 -croptop 50 -aspect 4:3 -s 480x320 /home/OP.mp4
ffmpeg -i "$1" -f mp4 -acodec libfaac -ab 94k -vcodec max -crf 24 \
 -coder 0 -refs 4 -flags +loop -deblockalpha 0 -deblockbeta 0 -me_method umh \
 -subq 9 -me_range 32  -bf 0 -g 300 -i_qfactor 1.3 -b_qfactor 1.4 -flags2 \
 -wpred+8x8dct \
 -aspect 4:3 -s 480x320 \
 "$2"

