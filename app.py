import gradio as gr

from tab import tab1


# 创建带有标签页的接口
interface = gr.TabbedInterface(
    [tab1],  # 标签页
    ["角色设计"],  # 每个标签页的标题
    title="通用角色扮演"  # 整个接口的标题为
)

# 启动接口
interface.launch()
