# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("토하 섭과 도킹"))

@client.event
async def on_message(message):
    if message.content == "안녕 토하봇!": # 메세지 감지
        await message.channel.send ("{} | {}, 안녕하세요".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, 님, 안뇽하세요. 레멜봇입니다아~~".format(message.author, message.author.mention))
    elif message.content == "마마!": # 메세지 감지
        await message.channel.send ("{} | {}, 후야님 여기요!!! @후야".format(message.author, message.author.mention))
    elif message.content == "파파!": # 메세지 감지
        await message.channel.send ("{} | {}, 꼬물님 여기요!!! @꼬물님||아니 잠시만 예아님인가?|| @예아님".format(message.author, message.author.mention))
    elif message.content == "토하봇 명령어": # 메세지 감지
        await message.channel.send ("{} | {}, 명령어 목록 : `\n 토하봇 명령어\n 안녕 토하봇! \n 마마! \n 파파! \n 토하봇! \n 심심하다.. \n 토하님! \n 마왕이다! \n 마망..`".format(message.author, message.author.mention))
    elif message.content == "토하봇!": # 메세지 감지
        await message.channel.send ("{} | {}, 네!".format(message.author, message.author.mention))
    elif message.content == "심심하다..": # 메세지 감지
        await message.channel.send ("{} | {}, 저도 심심하네요".format(message.author, message.author.mention))
    elif message.content == "토하님!": # 메세지 감지
        await message.channel.send ("{} | {}, 토하님 여기요!!! @토하님!!!".format(message.author, message.author.mention))
    elif message.content == "마왕이다!": # 메세지 감지
        await message.channel.send ("{} | {}, 마왕 잘생겨써요..헤헷".format(message.author, message.author.mention))
    elif message.content == "마망..": # 메세지 감지
        await message.channel.send ("{} | {}, 힘을 내요!!".format(message.author, message.author.mention))

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('OTAzODY2NzE4ODE5MDg2Mzg2.YXzNeg.E_0i8sWwgX89Fzo-RvYzW8DG3ts')