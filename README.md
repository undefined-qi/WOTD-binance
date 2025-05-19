# WOTD-binance
A simple Python CLI helper to guess Binance Word of the Day. 帮助更快猜出币安每日一词。
用gpt猜得太慢了，我就自己写了一个
- ✅ 支持灰色字母过滤（不可出现的字母）
- 🟨 支持黄色字母筛选（存在但位置未知）
- 🟩 支持绿色字母精准定位（如 4e 表示第 4 位是 e）
- 🔁 多轮交互式输入，动态缩小候选单词
- 📚 使用 NLTK 官方词库（已本地缓存）
 ## 🚀 Getting Started / 快速开始

### 1. 安装依赖

```bash
pip install nltk
