var chart = echarts.init(document.getElementById('wordcloud'));
var sourcedata_wc = [];
$.get('http://127.0.0.1:5000/getdata/',function(data){
    sourcedata_wc = JSON.parse(data);
    var option = {
        title: {
            text: '用户群体词云图',
            left: 'center',
        },
        tooltip: {},
        series: [ {
            type: 'wordCloud',
            gridSize: 2,
            sizeRange: [20, 90],
            rotationRange: [-90, 90],
            shape: 'circle',
            width: 600,
            height: 900,
            drawOutOfBound: false,
            textStyle: {
                normal: {
                    color: function () {
                        return 'rgb(' + [
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160)
                        ].join(',') + ')';
                    }
                },
                emphasis: {
                    shadowBlur: 10,
                    shadowColor: '#333'
                }
            },

            data: window.sourcedata_wc
        } ]
    };
    chart.setOption(option);
    window.onresize = chart.resize;
}
)