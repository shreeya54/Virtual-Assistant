import wikipedia
import re

def tell_me_about(topic):
    try:
        # info = str(ny.content[:500].encode('utf-8'))
        # res = re.sub('[^a-zA-Z.\d\s]', '', info)[1:]
        res = wikipedia.summary(topic, sentences=1)
        final_res=re.sub(r'\([^)]*\)', '', res)
        return final_res
    except Exception as e:
        print(e)
        return "Failed to Search on Wikipedia"
