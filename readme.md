# PIRI Python Tools

## capture.py
GDK로 화면을 갈무리하고 넘파이 늘넣이(배열)로 바꿉니다.
Captures screenshots of a window with GDK and converts them to numpy arrays.

## cutaud
동영상 사이사이의 소리를 없앱니다.
Mutes multiple sections of a video.

## dateshare
하루에 사진을 얼마나 찍었는지 보여줍니다.
Shows how many photos were taken in each day.

## dunaol 두나올
두나올(이진법)을 그림으로 보여줍니다. 검정하양(흑백) 막(무작위)그림을 만드는 데 쓸 수도 있습니다.
Illustrates how binary works. Can also be used to generate random black-and-white images.

## iremgari 이름갈이
여러 파일을 한벌에 고치고 이름바꿉니다.
Bulk rename and/or edit files.

쓰임새 보기(예시):

```python
def eligible(name):
	# Example use: move all files in immediate subdirectories to the given root..
	return name.count('/') == 1

def process(name):
	# ..prefixing the new filename with the subdirectory name.
	spl = name.split('/')
	return spl[0] + '_' + spl[1]
```

`./iremgari -r /target/dir`

## nurijach 누리자취
traceroute를 돌려서 나온 IP의 땅위자리(좌표)를 kml에 씁니다.
Writes geolocations of IPs from traceroute to kml.

## randomImage.py
무지갯빛 막그림을 만듭니다.
Creates beautiful random images.

## renameSeq.py
파일이름을 모두 셀글(숫자)로 바꿉니다.
Renames a sequence of files so they all have integers as names.

## sirxegier 섞새겨
Sirxegier is a barebones commandline music player script for one specific purpose: **shuffle** all audio files under a directory, and **remember** the shuffled order. Written because out of 4 music players I tried, 1 didn't have this functionality, 1 kept hanging after each file and 2 tried to scan my entire home folder without any prompts.

Features:

- Shuffle all audio files from one or more directories into one list.
- Play files from that list(using mpv).
- Remember the shuffled order and current track.
- No changes to any directory except the one sirxegier's run in.

Does **not** feature:

- Playlists.
- Reading or fetching metadata.
- Remembering the current second within a file.

Dependency: mpv in a Path.

May have some encoding issues on Windows.

## spaceout
글 씨 사 이 에 빈 자 리 를 넣 습 니 다 .
I n s e r t s s p a c e s b e t w e e n c h a r a c t e r s .

## 풀라
모아쓴 한글을 [CMUO 글꼴](https://github.com/Tzetachi/Computer-Modern-Unicode-Oesol)의 매김(인코딩)으로 풀어씁니다. 보기: `풀라 ㅇ 들아롬 | 풀크게 ㄸ > 날아롬`

## 풀크게
풀어쓴 한글에서 글월 첫글씨를 큰글씨로 바꿉니다.
