from pathlib import Path
from tkinter import filedialog, Tk
import time
from word_freq_txt2csv import TextReader

def main():
    Tk().withdraw()

    start_time = time.time()

    reader = TextReader()
    reader.execute(input_folder=Path(filedialog.askdirectory(title="选择文件夹")),
                   output_folder=Path(filedialog.askdirectory(title="选择输出文件夹")))

    end_time = time.time()
    time_consumption = end_time - start_time
    print(f"程序共运行了: {time_consumption:.2f} 秒")

if __name__ == "__main__":
    main()