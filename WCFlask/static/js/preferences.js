// app.title = '极坐标系下的堆叠柱状图';
// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('preferences'));

var option = {
    title: {
        text: '行为偏好详情',
        left: 'center',
    },
    angleAxis: {
        type: 'category',
        data: ['休息', '饮食', '活动', 'POI'],
        z: 10
    },
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c}'
    },
    radiusAxis: {
    },
    polar: {
        radius: '60%'
    },
    series: [{
        type: 'bar',
        data: [11, 0, 0, 0],
        coordinateSystem: 'polar',
        name: '早睡早起',
        stack: 'a'
    }, {
        type: 'bar',
        data: [29, 0, 0, 0],
        coordinateSystem: 'polar',
        name: '熬夜晚起',
        stack: 'a'
    }, {
        type: 'bar',
        data: [31, 0, 0, 0],
        coordinateSystem: 'polar',
        name: '午休',
        stack: 'a'
    }, {
        type: 'bar',
        data: [13, 0, 0, 0],
        coordinateSystem: 'polar',
        name: '不午休',
        stack: 'a'
    }, {
        type: 'bar',
        data: [0, 32, 0, 0],
        coordinateSystem: 'polar',
        name: '食堂',
        stack: 'a'
    }, {
        type: 'bar',
        data: [0, 10, 0, 0],
        coordinateSystem: 'polar',
        name: '外带外卖',
        stack: 'a'
    }, {
        type: 'bar',
        data: [0, 30, 0, 0],
        coordinateSystem: 'polar',
        name: '高峰用餐',
        stack: 'a'
    }, {
        type: 'bar',
        data: [0, 11, 0, 0],
        coordinateSystem: 'polar',
        name: '低峰用餐',
        stack: 'a'
    }, {
        type: 'bar',
        data: [0, 0, 29, 0],
        coordinateSystem: 'polar',
        name: '勤奋好学',
        stack: 'a'
    }, {
        type: 'bar',
        data: [0, 0, 15, 0],
        coordinateSystem: 'polar',
        name: '社团活跃',
        stack: 'a'
    }, {
        type: 'bar',
        data: [0, 0, 0, 39],
        coordinateSystem: 'polar',
        name: '图书馆',
        stack: 'a'
    }, {
        type: 'bar',
        data: [0, 0, 0, 40],
        coordinateSystem: 'polar',
        name: 'ST2',
        stack: 'a'
    }, {
        type: 'bar',
        data: [0, 0, 0, 10],
        coordinateSystem: 'polar',
        name: '28#',
        stack: 'a'
    }
    ],
    legend: {
        orient: 'vertical',
        x: 'right',
        show: true,
        data: ['早睡早起', '熬夜晚起', '午休', '不午休', '食堂', '外带外卖', '高峰用餐', '低峰用餐', '勤奋好学', '社团活跃', '图书馆', 'ST2', '28#']
    }
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);