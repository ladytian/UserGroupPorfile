// app.title = '环形图';
// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('POI'));

var option = {
    title: {
        text: 'POI预测详情',
        left: 'center',
    },
    tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
    },
    legend: {
        orient: 'vertical',
        x: 'left',
        left: 'right',
        data:['图书馆', 'ST2-1', 'ST1-2', '28A-210', '6-306', '5-102', '3-201', '6-108', 'S6-4', 'S7-2']
    },
    series: [
        {
            name:'POI预测',
            type:'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: false,
            label: {
                normal: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    show: true,
                    textStyle: {
                        fontSize: '30',
                        fontWeight: 'bold'
                    }
                }
            },
            labelLine: {
                normal: {
                    show: false
                }
            },
            data:[
                {value:35, name:'图书馆'},
                {value:17, name:'ST2-1'},
                {value:19, name:'ST1-2'},
                {value:40, name:'28A-210'},
                {value:41, name:'6-306'},
                {value:44, name:'5-102'},
                {value:43, name:'3-201'},
                {value:44, name:'6-108'},
                {value:24, name:'S6-4'},
                {value:20, name:'S7-2'}
            ]
        }
    ]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);