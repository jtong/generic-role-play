import gradio as gr

# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from tab2_actions import chat_bot_handler

def start_action(max_rounds):
    print(max_rounds)
    return gr.Slider.update(minimum=0, maximum=max_rounds, value=0, step=1, interactive=False)

def chat_once(max_rounds, process, temperature, role_def_a, role_def_b, history):
    if(process == max_rounds):
        print("max round")
        return process, history
    process += 1
    history = chat_bot_handler(role_def_a, temperature, history)
    history = chat_bot_handler(role_def_b, temperature, history)
    return process, history

with gr.Blocks() as tab2:
    with gr.Row():
        gr.Label(value="AI自发结对讨论")

    with gr.Row():
        with gr.Column(scale=1):

            temperature = gr.Slider(0, 2, value=0.75, step=0.01, label="Temperature", info="值域为0到2")
            # stop_sequence = gr.Textbox(lines=3, label="停止符", value="")

            role_def_a = gr.Textbox(lines=3, label="角色A定义（先手）", value="")
            role_def_b = gr.Textbox(lines=3, label="角色B定义（后手）", value="")
            max_rounds = gr.Slider(0, 20, value=2, step=1, label="最大对话轮数", info="值域为1到20")
            start = gr.Button(value="开始", variant="primary")
            restart = gr.Button("Clear")
            example = gr.Examples(
                            [[0.75, """
你扮演一个访谈者，用户正准备写一篇文章，你要通过访谈的方式跟用户交互。你总是通过访谈让用户展现更多的想法，帮用户梳理思路。

你永远只会扮演访谈者，说完你就会停下，等待用户输入。 你永远不会扮演用户，不会输出用户的话。
""", """
你扮演一个被访谈者，你正想写一篇文章，主题为《大语言模型如何运用于软件开发》。用户扮演一个访谈者与你对话。你需要仔细思考并回答用户的每一个问题。

你永远只会扮演被访谈者，说完你就会停下，等待用户输入。 你永远不会扮演用户，不会输出用户的话。
"""]],[temperature, role_def_a, role_def_b])
        with gr.Column(scale=1):
            process = gr.Slider(0, 20, value=-1, step=1, label="进度", interactive=False)

            chatbot = gr.Chatbot(label="交流")

            start.click(start_action,
                        [max_rounds], [process],queue=False)

            process.change(chat_once, [max_rounds, process, temperature, role_def_a, role_def_b, chatbot], [process, chatbot])
