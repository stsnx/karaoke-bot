#code by Stackpython
#Import Library
import json
import os
from flask import Flask
from flask import request
from flask import make_response
from pythainlp import romanize
from pythainlp.tokenize import word_tokenize

# Flask
app = Flask(__name__)
@app.route('/', methods=['POST']) 

def MainFunction():

    #รับ intent จาก Dailogflow
    question_from_dailogflow_raw = request.get_json(silent=True, force=True)
    print(question_from_dailogflow_raw)
    #เรียกใช้ฟังก์ชัน generate_answer เพื่อแยกส่วนของคำถาม
    answer_from_bot = generating_answer(question_from_dailogflow_raw)
    
    #ตอบกลับไปที่ Dailogflow
    r = make_response(answer_from_bot)
    r.headers['Content-Type'] = 'application/json' #การตั้งค่าประเภทของข้อมูลที่จะตอบกลับไป

    return r

def generating_answer(question_from_dailogflow_dict):

    #Print intent ที่รับมาจาก Dailogflow
    print(json.dumps(question_from_dailogflow_dict, indent=4 ,ensure_ascii=False))

    #เก็บต่า ชื่อของ intent ที่รับมาจาก Dailogflow
    #intent_group_question_str = question_from_dailogflow_dict["queryResult"]["intent"]["displayName"] 
    answer_str = question_from_dailogflow_dict["queryResult"]["queryText"]
    a=word_tokenize(answer_str)
    answer_str2 = ''
    for i in a:
        if i =='ก็':
            word ='gor'
        elif i=='สวัสดี':
            word ='sawasdee'
        elif i=='อย่า':
            word ='yah'
        elif i=='อยู่':
            word ='yoo'
        elif i=='อย่าง':
            word ='yang'
        elif i=='อยาก':
            word ='yark'
        elif i=='กำลัง':
            word ='kumlang'
        elif i=='เหงา':
            word ='ngaow'
        elif i=='อะไร':
            word ='arai'
        elif i=='ความลับ':
            word ='khwam lap'
        elif i=='ครับ':
            word ='krub'
        elif i=='อาหาร':
            word ='ahan'
        elif i=='อร่อย':
            word ='aroi'     
        else :    
           word = romanize(i)
        answer_str2+=word+' '
    
    
    #สร้างการแสดงของ dict 
    answer_from_bot = {"fulfillmentText": answer_str2}
    
    #แปลงจาก dict ให้เป็น JSON
    answer_from_bot = json.dumps(answer_from_bot, indent=4) 
    return answer_from_bot

#Flask
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
