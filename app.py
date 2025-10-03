import streamlit as st
from freeclimber_core import analyze_video
import tempfile
import os
import json

st.set_page_config(page_title="FreeClimber Web", layout="wide")
st.title("FreeClimber — Web 版")

uploaded = st.file_uploader("上传视频 (.mp4/.avi/.mov)", type=["mp4","avi","mov"])

param1 = st.slider("灵敏度 param1", 0.0, 1.0, 0.5)
param2 = st.number_input("阈值 param2", min_value=1, max_value=200, value=10)

if uploaded is not None:
    st.video(uploaded)

    if st.button("开始分析"):
        with st.spinner("正在分析（可能需要一会儿）..."):
            # 保存到临时文件
            tfile = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
            tfile.write(uploaded.getbuffer())
            tfile.flush()
            tfile.close()

            # 调用核心函数
            try:
                results = analyze_video(tfile.name, param1=param1, param2=int(param2))
            except Exception as e:
                st.error(f"分析出错：{e}")
                raise
            finally:
                try:
                    os.remove(tfile.name)
                except:
                    pass

            st.success("分析完成 ✅")
            st.json(results)

            st.download_button("下载结果 (JSON)", data=json.dumps(results, ensure_ascii=False, indent=2), file_name="freeclimber_result.json", mime="application/json")
