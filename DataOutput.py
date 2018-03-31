#coding=utf-8

import codecs
import time

class DataOutput():

    def __init__(self):
        self.filepath = 'baike_%s.html'%(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
        self.output_head(self.filepath)
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas)>10:
            self.output_html(self.filepath)

    def output_head(self, path):
        '''
        将HTML头写入
        :return:
        '''
        fout = codecs.open(path, 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        fout.close()

    def output_html(self):
        '''
        将数据写入HTML文件中
        :param path:文件路径
        :return
        '''
        fout = codecs.open(path, 'a', encoding='utf-8')
        for data in self.datas:
            fout.write("<head>")
            fout.write('<meta http-equiv="content-type" content="text/html;charset=utf-8"')
            fout.write("</head>")
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'])
            fout.write("<td>%s</td>"%data['summary'])
            fout.write("</tr>")
            self.datas.remove(data)
        fout.close()

    def output_end(self, path):
        '''
        输出HTML结束
        :patam path:文件存储路径
        :return:
        '''
        fout = codecs.open(path, 'a', encodeing='utf-8')
        fout.write("</table>")
        fout.write("</body>")
        fout.wrete("</html>")
        fout.close()
