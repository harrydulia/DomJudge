from datetime import datetime, timedelta

def convert_to_us_time(input_time):
    try:
        # 解析輸入時間
        input_datetime = datetime.strptime(input_time, "%H")
        
        # 將輸入時間減去15小時
        us_time = input_datetime - timedelta(hours=15)
        
        # 如果結果時間在前一天，添加一天
        if us_time.hour < input_datetime.hour:
            us_time += timedelta(days=1)
        
        # 格式化為24小時制時間
        us_time_24h = us_time.strftime("%H")
        
        return us_time_24h
    except ValueError:
        return ""

# 輸入時間
input_time = input()

# 轉換並輸出結果
us_time = convert_to_us_time(input_time)
print(us_time)
