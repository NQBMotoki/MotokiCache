# 项目简介
本项目为小组项目的题一，即统计books.zip内的文本文件中的中文及英文的词频，并将统计结果保存到csv文件中。源代码为[word_freq_txt2csv.py](word_freq_txt2csv.py)

## 目录
- [安装](#安装)
- [项目架构](#项目架构)
- [使用说明](#使用说明)
- [功能列表](#功能列表)
- [许可协议](#许可协议)

## 安装
1. 本项目的Python环境版本为3.12.4，建议使用Anaconda。
2. 安装依赖包：
- pandas
- snownlp
- textblob

## 项目架构
/txt_analyzer
│
├── output/
│   └── None
├── books/
│   └── (Should be filled with txt files)
├── word_freq_txt2csv.py
├── README.md
├── LICENSE
└── demonstration.py

## 使用说明
1. 将需要分析的 txt 文件放入 books 文件夹中。
2. 创建一个 output 文件夹，用于存放输出结果。
3. 创建 input_folder 与 output_folder ，使用filedialog.askdirectory()方法分别选择输入和输出文件夹。
4. 创建一个 TextReader 实例，并调用 execute(input_folder, output_folder)方法，参数为上面步骤中选择的文件夹路径。
5. 等待后可打开 output 文件夹查看分析结果。

**参考示范代码：[demonstration.py](demonstration.py)**

## 功能列表
- txt_reader()：读取文本
- chinese_text_selector()：提取文本中的中文
- english_text_selector()：提取文本中的英文
- word_analysis()：分析中文词频以及英文词频
- save_to_csv()：将统计结果保存为csv文件
- execute()：执行项目的主功能

## 许可协议
本项目采用 MIT 许可证进行授权。您可以自由地使用、修改和分发该项目的代码，但需保留原始版权声明及许可文本。  
详细许可条款请见 [LICENSE](LICENSE) 文件。
