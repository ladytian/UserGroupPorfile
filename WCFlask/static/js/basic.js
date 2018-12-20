// app.title = '嵌套环形图';
// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('basic'));
var option = {
    title: {
        text: '基础属性详情',
        left: 'center',
    },
    tooltip: {
        trigger: 'item',
        // formatter: '{a} <br/>{b}: {c} ({d}%)'
    },
    legend: {
        orient: 'vertical',
        x: 'left',
        data: ['本科生-男','本科生-女','研究生-男','研究生-女','S6-409','S6-411', 'S6-413', 'S6-414', 'S6-415', 'S6-416', 'S7-202', 'S7-206', 'S7-208', 'S7-215', 'S7-218']
    },
    series: [
        {
            name:'角色-性别',
            type:'pie',
            selectedMode: 'single',
            radius: [0, '40%'],

            label: {
                normal: {
                    position: 'inner'
                }
            },
            labelLine: {
                normal: {
                    show: false
                }
            },
            data: [
                {'value':24, 'name':'本科生-男'},
                {'value':20, 'name':'本科生-女'}
            ]
        },
        {
            name:'宿舍',
            type:'pie',
            radius: ['55%', '70%'],
            label: {
                normal: {
                    // formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
                    show: false,
                    backgroundColor: '#eee',
                    borderColor: '#aaa',
                    borderWidth: 1,
                    borderRadius: 4,
                    shadowBlur:3,
                    shadowOffsetX: 2,
                    shadowOffsetY: 2,
                    shadowColor: '#999',
                    padding: [0, 7],
                    rich: {
                        a: {
                            color: '#999',
                            lineHeight: 22,
                            align: 'center'
                        },
                        // abg: {
                        //     backgroundColor: '#333',
                        //     width: '100%',
                        //     align: 'right',
                        //     height: 22,
                        //     borderRadius: [4, 4, 0, 0]
                        // },
                        hr: {
                            borderColor: '#aaa',
                            width: '100%',
                            borderWidth: 0.5,
                            height: 0
                        },
                        b: {
                            fontSize: 16,
                            lineHeight: 33
                        },
                        per: {
                            color: '#eee',
                            backgroundColor: '#334455',
                            padding: [2, 4],
                            borderRadius: 2
                        }
                    }
                }
            },
            data: [
                {'value':4, 'name':'S6-409'},
                {'value':4, 'name':'S6-411'},
                {'value':4, 'name':'S6-413'},
                {'value':4, 'name':'S6-414'},
                {'value':4, 'name':'S6-415'},
                {'value':4, 'name':'S6-416'},
                {'value':4, 'name':'S7-202'},
                {'value':4, 'name':'S7-206'},
                {'value':4, 'name':'S7-208'},
                {'value':4, 'name':'S7-215'},
                {'value':4, 'name':'S7-218'},
            ]
        }
    ]
};       
myChart.setOption(option);
window.onresize = chart.resize