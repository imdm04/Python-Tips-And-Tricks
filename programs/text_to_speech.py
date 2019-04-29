import pyttsx3
# engine = pyttsx3.init()
# engine.say('HEllo friends, how are you?')
# # engine.runAndWait()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
# engine.runAndWait()

# # windows in-built library
# import win32com.client as wincl
# speak = wincl.Dispatch("SAPI.SpVoice")
# speak.Speak("Hello World, How are you")
from gtts import gTTS
import os
tts = gTTS(text="""
hello, good moning

let me introduce my self 
My name is Darshan Makadiya and i am from rajkot. i am 22 years old and i am purcuing my B. Tech. degree in computer engineer from UTU.

i father is a farmer and my mother is housemaker. 
my younger sister is persuing her BCA in Rajkot.
my hobbies are travelling, playing cricket, watching movies.
i have basic skills in web development technologies and colud services on aws.
in web technologies like HTML, php, javascript, nodejs, AJAX, jquery and bootstrap and also used both sql and no sql databases like MYSQL, MSSQL SERVER, mongodb and  ElasticSearch.

I want to improve my AWS skills so i tried to learn about some cloud services on aws like EC2, Lambda, DynamoDB, Cognito, elastic beanstalk, api gateway. 

My strengths are i am a  good team member, working hard and positive attitude towards my life.
My best ambition is to increase my skills and knowledge for cloud technologies by working in good company.

experiences:
i have 2 month experience as web development intern at Infinity infoway.(2018)
i have 6 month experience as web development intern at Om Infotech. Rajkot. 

its all about me


As per my knowledge,
coditas step up in this industry just befor 4 years.
coditas is fast growing, 
a well-reputed company in the market and
also provides lots of opportunity in future and well defined adaptable atmosphere.
coditas recently craeted cloud team with certified people.
Company has may client all around the world.
Company uses many latest growing technologies like Node.js, React native, Cloud computing, DevOps.
One big thing many companies are asking about experience.
How can a fresher get experience? But your company gave an opportunity to the fresher.


my opinion on effects of smartphone, the smartphone is good and it makes our tasks easy but overuse of it makes bad effects on our work productivity, behaviour and health. 

We waste our time in social media not for any intentional work but only for just a time pass purpose then it affects our productivity for doing work. When we overuse smartphones then it's becames our bad habit and we check our phone in every few minutes, it will distract us to concentrate and we can't focus on our work. It may cause anxiety, stress and depression.it makes us unconscious and affect our thinking ability. We also miss the creativity that comes in idle moments, when our mind is free to wander.

But at the end i think smartphone is not so much harmfull if you control on use it.If we can control our self then not a single technology our other things can distract our thinking and productivity. 
That is why I often try to remind myself not to depend on smartphones too much because my attention matters more than productivity.
I think it is time to reclaim your attention and thereby, reclaim your productivty. It is worth it.

I think I am capable to join Coditas technologies to excel my career and contribute to the growth of organisation.
I got to know about this opportunity from one of your aws engineer Varun elavia.

Thank u for giving me this great chance to share my knowlegde and thoughts with your uprising active company i am grateful for listening me.
""", lang='en')
tts.save("good.mp3")
os.system("start good.mp3")