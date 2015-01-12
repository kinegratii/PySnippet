#coding=utf8
"""
md文件合并脚本
"""

import os
import shutil
from datetime import datetime


class MDMergeProccessor(object):
    def __init__(self, src_dir, pre_mds, chapter_dirs_prex, appendix_mds, dst_dir, book_md):
        self.src_dir = src_dir
        self.pre_mds = pre_mds
        self.chapter_dirs_prex = chapter_dirs_prex
        self.appendix_mds = appendix_mds
        self.dst_dir = dst_dir
        # 基本路径
        self.base_path = os.path.dirname(__file__)
        # 书本目录
        self.book_path = os.path.join(self.base_path, self.src_dir)
        # 最后书本目录
        self.dst_book_dir = os.path.join(self.base_path, dst_dir)
        # 最后书本路径
        self.dst_book_path = os.path.join(self.base_path, dst_dir,book_md)
        

    def proccess(self):
        print('The task start...')
        if not os.path.exists(self.dst_book_dir):
            os.makedirs(self.dst_book_dir)
        self.dst_fp = open(self.dst_book_path, 'w')

        # 处理前言的md文件
        for md in self.pre_mds:
            md_path = os.path.join(self.book_path, md)
            self._add_to_dst_file(md_path)
                
        print('pre md file proccess success')
        # 处理每一章目录下的md文件
        chapter_dirs = os.listdir(self.book_path)
        print(chapter_dirs)
        for chapter_dir in chapter_dirs:
            if any([chapter_dir.startswith(prefix) for prefix in self.chapter_dirs_prex]):
                self._proccess_chapter(chapter_dir)
       # 处理附录的md文件 
        for md in self.appendix_mds:
            md_path = os.path.join(self.book_path, md)
            self._add_to_dst_file(md_path)

        self.dst_fp.close()
        
        print('[OK] The md file has been generated to %s' % self.dst_book_path)

    def _proccess_chapter(self, chapter_dir):
        print ('start proccess chapter %s' % chapter_dir)
        chapter_path = os.path.join(self.book_path, chapter_dir)
        files_names = os.listdir(chapter_path)
        for filename in files_names:
            if filename.endswith(r'.md'):
                # 将md内容追加到目标md文件
                self._add_to_dst_file(os.path.join(chapter_path, filename))
            else:
                # 复制文件到书本目录下
                self._copy_media(chapter_path, filename)
        

    def _add_to_dst_file(self, file_path):
        with open(file_path, 'r') as fp:
            content = fp.read()
            if content:
                self.dst_fp.write(os.linesep)
                self.dst_fp.write(content)
        
    def _copy_media(self, parent_path, file_name):
        src_path = os.path.join(parent_path, file_name)
        dst_path = os.path.join(self.dst_book_dir, file_name)
        if not os.path.exists(dst_path):
            shutil.copyfile(src_path,dst_path)  

def main():
    book_md_name = datetime.now().strftime('django_developement_notes_%Y%m%d.md')
    p = MDMergeProccessor(
        src_dir='book',
        pre_mds=['preface.md'],
        chapter_dirs_prex = ['01','02','03','04','05', '06'],
        appendix_mds = ['appendix.md',],
        dst_dir='build',
        book_md=book_md_name)
    p.proccess()

if __name__ == '__main__':
    main()
