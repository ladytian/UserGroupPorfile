# -*- coding:UTF-8 -*-

import json

def get_wc_data():
    sourcedata = [
                    {
                    'name': '本科生',
                    'value': 44,
                    'textStyle': {
                        'normal': {
                            'color': 'black'
                        },
                        'emphasis': {
                            'color': 'red'
                        }
                    }
                    },
                    {
                        'name': '男生',
                        'value': 24
                    },
                    {
                        'name': '女生',
                        'value': 20
                    },
                    {
                        'name': '非常活跃',
                        'value': 23
                    },
                    {
                         'name': '活跃',
                        'value': 12
                    },
                    {
                        'name': '不活跃',
                        'value': 9
                    },
                    {
                        'name': '付费',
                        'value': 9
                    },
                    {
                        'name': '免费',
                        'value': 30
                    },
                    {
                        'name': '小流量',
                        'value': 5
                    },
                    {
                        'name': '勤奋好学',
                        'value': 29
                    },
                    {
                        'name': '娱乐型',
                        'value': 15
                    },
                    {
                        'name': '前期使用',
                        'value': 34
                    },
                    {
                        'name': '均匀分配',
                        'value': 10
                    },
                    {
                        'name': '早睡早起',
                        'value': 11
                    },
                    {
                        'name': '熬夜晚起',
                        'value': 29
                    },
                    {
                        'name': '午休',
                        'value': 31
                    },
                    {
                        'name': '不午休',
                        'value': 13
                    },
                    {
                        'name': '食堂',
                        'value': 32
                    },
                    {
                        'name': '外带外卖',
                        'value': 10
                    },
                    {
                        'name': '高峰用餐',
                        'value': 30
                    },
                    {
                        'name': '低峰用餐',
                        'value': 11
                    },
                    {
                        'name': '社团活动',
                        'value': 5
                    }
                ]
    return json.dumps(sourcedata)


# def get_basic_data():
#     sourcedata = {
#                     'array1': ['本科生-男','本科生-女','研究生-男','研究生-女','23-101','23-102','26-201','26-202','26-203','26-204'], 
#                     'array2': [
#                         {'value':30, 'name':'本科生-男'},
#                         {'value':14, 'name':'本科生-女'}
#                     ],
#                     'array3': [
#                         {'value':4, 'name':'23-101'},
#                         {'value':4, 'name':'23-102'},
#                         {'value':4, 'name':'26-201'},
#                         {'value':4, 'name':'26-202'},
#                         {'value':4, 'name':'26-203'},
#                         {'value':4, 'name':'26-204'}
#                     ]
#                 }
#     return json.dumps(sourcedata)


# def get_grade_data():
#     sourcedata = {
#                     'array1': ['非常活跃', '活跃', '不活跃', '付费', '免费', '小流量', '学习型', '娱乐型', '前期使用', '均匀分配'], 
#                     'array2': [{
#                         'type': 'bar',
#                         'data': [6, 0, 0, 0],
#                         'coordinateSystem': 'polar',
#                         'name': '非常活跃',
#                         'stack': 'a'
#                     }, {
#                         'type': 'bar',
#                         'data': [3, 0, 0, 0],
#                         'coordinateSystem': 'polar',
#                         'name': '活跃',
#                         'stack': 'a'
#                     },
#                     {
#                         'type': 'bar',
#                         'data': [1, 0, 0, 0],
#                         'coordinateSystem': 'polar',
#                         'name': '不活跃',
#                         'stack': 'a'
#                     },
#                     {
#                         'type': 'bar',
#                         'data': [0, 1, 0, 0],
#                         'coordinateSystem': 'polar',
#                         'name': '付费',
#                         'stack': 'a'
#                     }, {
#                         'type': 'bar',
#                         'data': [0, 5, 0, 0],
#                         'coordinateSystem': 'polar',
#                         'name': '免费',
#                         'stack': 'a'
#                     }, {
#                         'type': 'bar',
#                         'data': [0, 4, 0, 0],
#                         'coordinateSystem': 'polar',
#                         'name': '小流量',
#                         'stack': 'a'
#                     },
#                      {
#                         'type': 'bar',
#                         'data': [0, 0, 5, 0],
#                         'coordinateSystem': 'polar',
#                         'name': '学习型',
#                         'stack': 'a'
#                     },
#                     {
#                         'type': 'bar',
#                         'data': [0, 0, 5, 0],
#                         'coordinateSystem': 'polar',
#                         'name': '娱乐型',
#                         'stack': 'a'
#                     }, {
#                         'type': 'bar',
#                         'data': [0, 0, 0, 8],
#                         'coordinateSystem': 'polar',
#                         'name': '前期使用',
#                         'stack': 'a'
#                     }, {
#                         'type': 'bar',
#                         'data': [0, 0, 0, 2],
#                         'coordinateSystem': 'polar',
#                         'name': '均匀分配',
#                         'stack': 'a'
#                     }
#                     ]
#                 }
#     return json.dumps(sourcedata)