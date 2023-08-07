# 定义第一个标签页的输入和输出
import random

from logic.llm_driver import build_chat


def send(user_message, history):
    if (len(history) == 0):
        return "", history
    else:
        history[-1][1] = user_message
        return "", history


def start_action(start_message, temperature, history):
    return chat_bot_handler(start_message, temperature, history)

def chat_bot_handler(system_message, temperature, history):
    # 定义一个空字符串，用来拼接每一轮对话
    normal_chat = build_chat(temperature=temperature)
    message_string_history = [system_message]
    # 遍历 history 列表中的每一个元素
    for item in history:
        # 取出当前元素中的问题和回答
        question, answer = item

        # 将问题和回答拼接成一个字符串，并添加到结果字符串中
        message_string_history += [question, answer]
    messages = transform_to_messages(message_string_history)

    message = normal_chat(messages)

    return "", history + [[message, None]]

def transform_to_messages(input_strings):
    output_strings = []
    system = input_strings[0]
    output_strings.append({"role": "system", "content": system})

    roles = ["user", "assistant"]

    for index, string in enumerate(input_strings[1:]):
        role = roles[index % 2]
        translated_string = {"role": role, "content": string}
        output_strings.append(translated_string)

    return output_strings


def post_history(history, parsed_response):
    history[-1][1] = parsed_response.line
