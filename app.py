import gradio as gr

from tab import tab1
from tab2 import tab2


# 创建带有标签页的接口
interface = gr.TabbedInterface(
    [tab1, tab2],  # 标签页
    ["单一角色对话", "AI自发结对讨论"],  # 每个标签页的标题
    title="通用角色扮演"  # 整个接口的标题为
)

# 启动接口
interface.launch()
