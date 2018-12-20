// app.title = '极坐标系下的堆叠柱状图';
// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('grade'));
var option = {
    title: {
        text: '用户分级详情',
        left: 'center'
    },
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c}'
    },
    angleAxis: {
    },
    radiusAxis: {
        type: 'category',
        data: ['活跃', '流量', '目的', '分配'],
        z: 10
    },
    polar: {
        radius: '60%'
    },
    series: [
            {
                'type': 'bar',
                'data': [23, 0, 0, 0],
                'coordinateSystem': 'polar',
                'name': '非常活跃',
                'stack': 'a'
            }, {
                'type': 'bar',
                'data': [12, 0, 0, 0],
                'coordinateSystem': 'polar',
                'name': '活跃',
                'stack': 'a'
            },
            {
                'type': 'bar',
                'data': [9, 0, 0, 0],
                'coordinateSystem': 'polar',
                'name': '不活跃',
                'stack': 'a'
            },
            {
                'type': 'bar',
                'data': [0, 9, 0, 0],
                'coordinateSystem': 'polar',
                'name': '付费',
                'stack': 'a'
            }, {
                'type': 'bar',
                'data': [0, 30, 0, 0],
                'coordinateSystem': 'polar',
                'name': '免费',
                'stack': 'a'
            }, {
                'type': 'bar',
                'data': [0, 5, 0, 0],
                'coordinateSystem': 'polar',
                'name': '小流量',
                'stack': 'a'
            },
             {
                'type': 'bar',
                'data': [0, 0, 29, 0],
                'coordinateSystem': 'polar',
                'name': '学习型',
                'stack': 'a'
            },
            {
                'type': 'bar',
                'data': [0, 0, 15, 0],
                'coordinateSystem': 'polar',
                'name': '娱乐型',
                'stack': 'a'
            }, {
                'type': 'bar',
                'data': [0, 0, 0, 34],
                'coordinateSystem': 'polar',
                'name': '前期使用',
                'stack': 'a'
            }, {
                'type': 'bar',
                'data': [0, 0, 0, 10],
                'coordinateSystem': 'polar',
                'name': '均匀分配',
                'stack': 'a'
            }
    ],
    legend: {
        orient: 'vertical',
        x: 'left',
        show: true,
        data: ['非常活跃', '活跃', '不活跃', '付费', '免费', '小流量', '学习型', '娱乐型', '前期使用', '均匀分配']
    }
};
myChart.setOption(option);
window.onresize = chart.resize