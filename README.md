# Yooc_AutoExam

A Python script which finishes the exam in [YOOC](https://www.yooc.me/) without a question bank automatically.

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

The configuration file `config.json` file contains your credentials and settings for the automated exam process. You can manually gather the necessary information and insert it into the configuration file.

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
- **examId**: The ID of the exam you want to participate in.
- **time**: The expected exam duration, in minutes.
- **accuracy**: The expected accuracy level for the answers (as a percentage, e.g., 80 for 80%).

How to find required values:

- `user_token` and `sessionid`:
   After logging in to [yooc.me](https://yooc.me/mobile/dashboard), open your browser's developer tools (usually `F12` or `Ctrl+Shift+I`). Navigate to the **Network** tab, and look for **Cookies**. You will find `user_token` and `sessionid` in the list. Copy their values and paste them into the `config.json` file.
- `examId`:
   Go to the **Exam Details** page. If you're using a browser's developer tools, inspect the **Network** tab while the page loads, and look for the API request that retrieves the exam data. The request URL or response will contain the `examId`. Alternatively, the `examId` can sometimes be found directly in the page's URL.

Make sure all the values are correctly copied into the `config.json` file for the script to function properly.

## Usage

1. Ensure your `config.json` file is properly configured with your credentials and preferences.

2. Run the script with:

   ```bash
   python exam_script.py
   ```

This will start the automated exam process. If you need to pass specific parameters or configure the script further, refer to the configuration section for more details.

## Notes

- This script is **for educational purposes only**. I am not responsible for any consequences that may arise from the use of this script. Please ensure you comply with all relevant laws, terms of service, and ethical guidelines when using this script.
- The accuracy level for the answers is based on the desired percentage. The script will attempt to modify the answers to achieve this accuracy.
- The duration of the exam is randomized to mimic human-like behavior.

## Customization

The following operations are optional.

### Customize Wrong Answer Generation

The `to_wrong.py` module is used to generate wrong answers for **fill-in-the-blank** (completion) questions. It takes the correct answer as input and returns a wrong answer.

Default Behavior:

> The `to_wrong` function, by default, turns the answer into a period (`"."`) if the answer is a string. For non-string answers (like lists), it recursively applies the `to_wrong()` function to each item in the list.
>
> ```python
> def to_wrong(answer):
>        """
>        Customize the wrong answer based on the correct one.
>        This function is triggered for fill-in-the-blank questions.
>        """
>        if isinstance(answer, str):
>            return '.'
>        else:
>            return [to_wrong(item) for item in answer]
>    ```

You can modify the `to_wrong()` function by applying more complex logic for different types of answers in the specific exam.

### Adjusting noise in the Script

The script simulates human-like duration in the exam. This delay is randomized based on the `noise` factor in `yooc_exam.py`.

```python
noise = 0.1  # noise of sleep time
```

Its default value is `0.1`, which means there is a 10% discrepancy between the actual duration and the expected duration. You can adjust the `noise` variable in the script to make the random delay smaller or larger, depending on your needs.

## License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for more details.

You are free to use, modify, and distribute this software, provided that the original copyright notice and this permission notice are included in all copies or substantial portions of the software. The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement.