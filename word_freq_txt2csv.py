# -*- coding: utf-8 -*-
import pandas as pd
import re
from pathlib import Path
from snownlp import SnowNLP as sn
from textblob import TextBlob as tb

class TextReader:
    def __init__(self):
        self.file_path = None
    def txt_reader(self):
        '''
        读取文本
        '''
        with open(self.file_path, "r", encoding="gb18030") as f:
            text = f.read()
        return text

    def chinese_text_selector(self):
        '''
        提取文本中的中文
        '''
        text = self.txt_reader()
        chinese_text = re.findall(r'[\u4e00-\u9fa5]+', text)
        chinese_string = " ".join(chinese_text)
        return chinese_string

    def english_text_selector(self):
        '''
        提取文本中的英文
        '''
        text = self.txt_reader()
        english_text = re.findall(r'[a-zA-Z]+', text)
        english_string = " ".join(english_text)
        return english_string

    def word_analysis(self):
        '''
        分析中文词频以及英文词频
        '''
        chinese_buffer = sn(self.chinese_text_selector())
        chinese_words_list = chinese_buffer.words
        chinese_word_freq = pd.Series(chinese_words_list).value_counts().reset_index()
        chinese_word_freq.columns = ['Chinese Word', 'Frequency']

        english_buffer = tb(self.english_text_selector())
        english_words_list = english_buffer.words
        english_word_freq = pd.Series(english_words_list).value_counts().reset_index()
        english_word_freq.columns = ['English Word', 'Frequency']

        return chinese_word_freq, english_word_freq

    def save_to_csv(self, file_path, chinese_word_freq, english_word_freq, output_folder):
        '''
        将统计结果保存为csv文件
        '''
        file_name = file_path.stem
        combined_data = pd.concat([chinese_word_freq, english_word_freq], axis=1)

        output_csv_path = output_folder / f"{file_name}_word_frequency.csv"
        combined_data.to_csv(output_csv_path, index=False, encoding="utf-8-sig")

    def execute(self, input_folder: Path, output_folder: Path):
        '''
        执行层，需要提供input_folder（需要统计词频的文件所在的文件夹）和output_folder（希望结果输出到的文件夹）分别的路径
        '''
        if not input_folder or not output_folder:
            print("没有提供文件夹")
            return

        for file in input_folder.glob("*.txt"):
            self.file_path = file
            print(f"正在解析处理: {file.name}")
            chinese_word_freq, english_word_freq = self.word_analysis()
            self.save_to_csv(file, chinese_word_freq, english_word_freq, output_folder)