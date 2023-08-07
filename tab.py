import gradio as gr

# import sys
# import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from tab_actions import start_action, send, chat_bot_handler


with gr.Blocks() as tab1:

    with gr.Row():
        with gr.Column(scale=1):
            temperature = gr.Slider(0, 2, value=0.75, step=0.01, label="Temperature", info="Choose between 0 and 2")
            # stop_sequence = gr.Textbox(lines=3, label="停止符", value="")

            role_def = gr.Textbox(lines=3, label="角色定义", value="")

            start = gr.Button(value="开始", variant="primary")
            restart = gr.Button("Clear")
            example = gr.Examples(
                            [[0.75, """
你扮演一个访谈者，用户正准备写一篇文章，你要通过访谈的方式跟用户交互。你总是通过访谈让用户展现更多的想法，帮用户梳理思路。

你永远只会扮演访谈者，说完你就会停下，等待用户输入。 你永远不会扮演用户，不会输出用户的话。
"""]],[temperature, role_def])
        with gr.Column(scale=1):

            chatbot = gr.Chatbot(label="交流")
            chat_box = gr.Textbox(label="我的回复")

            chat_box.submit(send,
                            [chat_box, chatbot],
                            [chat_box, chatbot], queue=False).then(
                chat_bot_handler, [role_def, temperature, chatbot], [chat_box, chatbot]
            )

            restart.click(lambda: None, None, chatbot, queue=False)
            start.click(start_action,
                        [role_def, temperature, chatbot],
                        [chat_box, chatbot], queue=False)
