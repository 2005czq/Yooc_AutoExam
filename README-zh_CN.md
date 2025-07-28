# Yooc_AutoExam

[English Doc](./README.md) | [中文文档](./README-zh_CN.md)

一款用于在 [易班优课](https://www.yooc.me/) 上自动完成考试的 Python 脚本，并且**无需题库**。

## 目录

- [要求](#要求)
- [配置](#配置)
- [使用方法](#使用方法)
- [注意事项](#注意事项)
- [定制化](/#定制化)
- [开源许可](#开源许可)

## 要求

- Python 3
- 所需的 Python 库：
  - `beautifulsoup4`
  - `pycryptodome`
  - `requests`
  - `urllib3`

你可以使用 `pip` 安装所需的库：

```bash
pip install -r requirements.txt
```

## 配置

配置文件 `config.json` 包含了你的凭证和自动考试的设置。你需要手动收集必要的信息并填入配置文件中。

```json
{
    "user_token": "",
    "sessionid": "",

    "examId": "",

    "time": 5,
    "accuracy": 100
}
```

`config.json` 文件中的参数：

- **user_token**：用户认证的令牌。
- **sessionid**：用于用户会话管理的会话 ID。
- **examId**：要参与的考试的 ID。
- **time**：预期的考试时长，单位为分钟。
- **accuracy**：预期的答题准确度（百分比，例如 80 表示 80%）。

### 如何获取所需的值：

#### `user_token` 和 `sessionid`：

1. 在浏览器中登录 [yooc.me](https://yooc.me/mobile/dashboard)。
2. 打开浏览器的 **开发者工具**（通常按 `F12` 或 `Ctrl+Shift+I`）。
3. 进入 **网络**（Network）标签，并查找 **Cookies**。
4. 在列表中找到 `user_token` 和 `sessionid`。
5. 复制它们的值并粘贴到 `config.json` 文件中。

#### `examId`：

1. 在浏览器中打开 **考试详情** 页面。
2. 再次打开 **开发者工具** 并进入 **网络** 标签。
3. 查找 URL 以 `https://exambackend.yooc.me/api/exam/list/get` 开头的请求。
4. 点击该请求，在 **响应** 部分会包含考试的 `examId`。
5. 复制 `examId` 值并粘贴到 `config.json` 文件中。

确保所有值都正确复制到 `config.json` 文件中，脚本才能正常运行。

## 使用方法

1. 确保 `config.json` 文件已正确配置了你的凭证和偏好设置。

2. 运行脚本：

   ```bash
   python yooc_exam.py
   ```

   这将启动自动化考试。

3. 等待脚本考试结束。一般而言，等待时长大致与预期考试时长相等。

## 注意事项

- 本脚本仅限于 **学习用途**。本人不对使用该脚本可能引发的任何后果负责。在使用脚本时，请确保遵守道德及所有相关法律、服务条款。
- 答题的准确度基于所期望的百分比。脚本会尝试调整答案以达到该准确度。
- 实际考试时长将会加入少量噪音以模拟人类的行为。

## 定制化

以下操作为可选操作。

### 定制错误答案生成

`to_wrong.py` 模块用于生成 **填空题** 的错误答案。它接收正确答案作为输入并返回错误答案。

默认行为：

> 如果答案是字符串类型，`to_wrong` 函数默认会将答案转化为一个句点（"."）。如果答案是非字符串类型（例如列表），则会递归地对列表中的每个项应用 `to_wrong()` 函数。
>
> ```python
> def to_wrong(answer):
>     """
>     Customize the wrong answer based on the correct one.
>     This function is triggered for fill-in-the-blank questions.
>     """
>     if isinstance(answer, str):
>         return '.'
>     else:
>         return [to_wrong(item) for item in answer]
> ```

为了对特定考试中的不同类型的答案应用更复杂的逻辑，你可以通过修改 `to_wrong()` 函数来自定义错误答案的生成方式。

### 调整脚本中的噪声

脚本会在考试用时中加入噪声。此噪声基于 `yooc_exam.py` 中的 `noise` 参数的。

```python
noise = 0.1  # 延迟时间的噪声
```

默认值为 `0.1`，表示实际时长与预期时长之间有 10% 的偏差。你可以根据需要调整 `noise` 变量，来增大或减小随机噪声。

## 开源许可

本项目采用 **GNU General Public License v3.0**。详细内容请参阅 [LICENSE](./LICENSE) 文件。
