# Yooc_AutoExam

[English Doc](./README.md) | [中文文档](./README-zh_CN.md)

A Python script which finishes the exam in [YOOC](https://www.yooc.me/) **without a question bank** automatically.

## Table of Contents

- [Requirements](#requirements)
- [Configuration](#configuration)
- [Usage](#usage)
- [Notes](#notes)
- [Customization](#customization)
- [License](#license)

## Requirements

- Python 3
- Required Python libraries:
  - `beautifulsoup4`
  - `pycryptodome`
  - `requests`
  - `urllib3`

You can install the required libraries using `pip`:

```bash
pip install -r requirements.txt
```

## Configuration

The configuration file `config.json` contains your credentials and settings for the automated exam. You can manually gather the necessary information and insert it into the configuration file.

```json
{
    "user_token": "",
    "sessionid": "",

    "examId": "",

    "time": 5,
    "accuracy": 100
}
```

Parameters in `config.json`:

- **user_token**: The token for user authentication.
- **sessionid**: The session ID for user session management.
- **examId**: The ID of the exam to be taken.
- **time**: The expected exam duration, in minutes.
- **accuracy**: The expected accuracy level for the answers (as a percentage, e.g., 80 for 80%).

### How to find the required values:

#### `user_token` and `sessionid`:

1. Log in to [yooc.me](https://yooc.me/mobile/dashboard) in your web browser.
2. Open your browser's **Developer Tools** (usually by pressing `F12` or `Ctrl+Shift+I`).
3. Navigate to the **Network** tab and look for **Cookies**.
4. You will find the `user_token` and `sessionid` stored in the list.
5. Copy their values and paste them into the `config.json` file.

#### `examId`:

1. Go to the **Exam Details** page in your browser.
2. Open your **Developer Tools** again and navigate to the **Network** tab.
3. Look for the request whose URL starts with `https://exambackend.yooc.me/api/exam/list/get`.
4. Click on that request, and in the **Response** section, the response will contain the `examId` of the exam.
5. Copy the `examId` value and paste it into the `config.json` file.

Make sure all the values are correctly copied into the `config.json` file for the script to function properly.

## Usage

1. Ensure your `config.json` file is properly configured with your credentials and preferences.

2. Run the script with:

   ```bash
   python yooc_exam.py
   ```

   This will start the automated exam.

3. Waiting for the script test. Generally speaking, the waiting duration is roughly equal to the expected test duration.

## Notes

- This script is **for educational purposes only**. I am not responsible for any consequences that may arise from the use of this script. Please ensure you comply with all relevant laws, terms of service, and ethical guidelines when using this script.
- The accuracy level for the answers is based on the desired percentage. The script will attempt to modify the answers to achieve this accuracy.
- The actual exam duration will incorporate a small amount of noise to simulate human behavior.

## Customization

The following operations are optional.

### Customize Wrong Answer Generation

The `to_wrong.py` module is used to generate wrong answers for **fill-in-the-blank** (completion) questions. It takes the correct answer as input and returns a wrong answer.

Default Behavior:

> The `to_wrong` function, by default, turns the answer into a period (`"."`) if the answer is a string. For non-string answers (like lists), it recursively applies the `to_wrong()` function to each item in the list.
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

You can modify the `to_wrong()` function by applying more complex logic for different types of answers in the specific exam.

### Adjusting Noise in the Script

The script will incorporate noise in the test duration. This noise is based on the `noise` parameters in `yooc_exam.py`.

```python
noise = 0.1  # noise of sleep time
```

Its default value is `0.1`, which means there is a 10% discrepancy between the actual duration and the expected duration. You can adjust the `noise` variable in the script to make the random delay smaller or larger, depending on your needs.

## License

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](./LICENSE) file for more details.
