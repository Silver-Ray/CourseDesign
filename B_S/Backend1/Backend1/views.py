# from django.http import JsonResponse
# from random import random

# def emotion_analyze(request):
#   if request.method == 'POST':
#     pScore = random()
#     result = {'status': 'success', 'positive': pScore, 'negative': 1 - pScore}
#     return JsonResponse(result)
#   else:
#     return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
  
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from django.http import JsonResponse
import json
import subprocess
import pandas as pd
import csv
import random

provinces_and_regions = [
    "北京",
    "天津",
    "河北",
    "山西",
    "内蒙古",
    "辽宁",
    "吉林",
    "黑龙江",
    "上海",
    "江苏",
    "浙江",
    "安徽",
    "福建",
    "江西",
    "山东",
    "河南",
    "湖北",
    "湖南",
    "广东",
    "广西",
    "海南",
    "重庆",
    "四川",
    "贵州",
    "云南",
    "西藏",
    "陕西",
    "甘肃",
    "青海",
    "宁夏",
    "新疆",
    "台湾",
    "香港",
    "澳门"
]
 
@api_view(['POST'])
def singleEmoAnalyze(request):
    print(request.data)
    textNeedAnalyze = request.data['text']
    print(textNeedAnalyze)

    runresult = subprocess.run(['python', 'runAnalyze.py', textNeedAnalyze], capture_output=True, text=True)
    if runresult.returncode == 0:
        data = json.loads(runresult.stdout)
        print(data)
    else:
        print("An error occured:", runresult.stderr)
    return Response(data)


@api_view(['GET'])
def wholeEmotionBar(request):
    try:
        with open('province.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        return Response({"error": "File not found"}, status=404)
    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON format"}, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

    print("OK")
    return Response(data, status=200)

@api_view(['POST'])
def fileUpload(request):
    if request.FILES:
        file = request.FILES['file']
        with open('comment.csv', 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        return Response({"message": "文件上传成功"}, status=200)
    else:
        return Response({"error": "没有文件被上传"}, status=400)
    
@api_view(['GET'])
def getComment(request):
    try:
        data = pd.read_csv('comment.csv')
        csv_data = data.to_csv(index=False)
        return Response(csv_data, content_type='text/csv')
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
@api_view(['POST'])
def getURL(request):
    print(request.data)
    return Response({"message": "URL获取成功"}, status=200)

@api_view(['GET'])
def getWholeEmoAnalyze(request):
    provincedata = []
    pSum = 0
    nSum = 0
    for items in provinces_and_regions:
        p = random.random()
        n = 1-p
        pSum = pSum + p
        nSum = nSum + n
        provincedata.append({"province": items, "positive": p, "negative": n})
    print(provincedata)
    data = {"provinceResult": provincedata, "Wpositive": pSum, "Wnegative": nSum}
    print(data)

    return Response(data)

@api_view(['GET'])
def getFileEmoAnalyze(request):
    return Response({"message": "文件分析成功"}, status=200)