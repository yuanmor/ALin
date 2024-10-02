import os
import shutil
import argparse
import re

def fun1(src_path, pattern):
    count = 1
    found = False  # 标志是否找到匹配文件
    
    # 获取命令行当前工作目录，并在该目录下创建 'al' 文件夹
    current_dir = os.getcwd()  # 获取命令行的当前目录
    dst_path = os.path.join(current_dir, 'al')
    
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)  # 如果 'al' 文件夹不存在则创建
    
    try:
        # 编译正则表达式，忽略大小写
        regex = re.compile(pattern, re.IGNORECASE)
        
        for root, dirs, files in os.walk(src_path):
            for file in files:
                print(f"检测到文件: {file}")  # 打印每个文件名
                if regex.match(file):  # 使用正则表达式匹配文件名
                    found = True
                    src_file_path = os.path.join(root, file)
                    dst_file_path = os.path.join(dst_path, file)
                    
                    # 如果目标文件已存在，避免覆盖
                    while os.path.exists(dst_file_path):
                        count += 1
                        dst_file_path = os.path.join(dst_path, str(count) + '_' + file)
                    
                    shutil.copy2(src_file_path, dst_file_path)  # 将文件复制到目标文件夹
                    print(f"文件已复制到: {dst_file_path}")
                    
        if not found:
            print(f"未找到符合模式的文件: {pattern}")
    except PermissionError:
        print("权限错误: 请检查文件或文件夹权限")
    except FileNotFoundError:
        print("文件路径错误: 请检查输入的文件路径")
    except re.error:
        print("正则表达式错误: 请检查输入的正则表达式")
    except Exception as e:
        print(f"发生错误: {e}")

def main():
    parser = argparse.ArgumentParser(description="文件复制程序，支持文件名正则匹配")
    parser.add_argument("-f", "--move_file", required=True, help="需要复制的文件名模式（支持正则表达式）")
    parser.add_argument("-src", "--src_path", required=True, help="源文件夹路径 (自动探索子文件夹)")
    args = parser.parse_args()

    fun1(args.src_path, args.move_file)

if __name__ == "__main__":
    main()
