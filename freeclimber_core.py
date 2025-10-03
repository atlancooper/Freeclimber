import time

# 这里放 FreeClimber 核心逻辑，暂时用示例
def analyze_video(local_path, param1=0.5, param2=10):
    # 模拟分析耗时
    time.sleep(2)
    results = {
        "video": local_path,
        "param1": param1,
        "param2": param2,
        "jumps": 5,
        "positions": [10, 20, 30, 40, 50]
    }
    return results
